import sublime
import sublime_plugin
import subprocess
import os

def get_setting(key, default):
	settings = sublime.load_settings('SmartIM.sublime-settings')
	return settings.get(key, default)

class SmartimCommand(sublime_plugin.EventListener):
	def __init__(self):
		self.BINPATH = os.path.join(os.path.dirname(__file__), "im-select")
		self.LAYOUT = get_setting("keyboard_layout", "com.apple.keylayout.US")
		self.IMEs = {}
		self.PreviousModes = {}

	def on_new_async(self, view):
		# print('SmartIM in new Buffer')
		self.LAYOUT = get_setting("keyboard_layout", "com.apple.keylayout.US")

		id = view.id()
		self.IMEs[id] = self.LAYOUT
		self.PreviousModes[id] = None
		view.settings().clear_on_change('command_mode')
		view.settings().add_on_change('command_mode', lambda: self.callback(view))

	def on_load_async(self, view):
		# print('SmartIM in load file')
		self.LAYOUT = get_setting("keyboard_layout", "com.apple.keylayout.US")

		id = view.id()
		self.IMEs[id] = self.LAYOUT
		self.PreviousModes[id] = None
		view.settings().clear_on_change('command_mode')
		view.settings().add_on_change('command_mode', lambda: self.callback(view))

	def on_close(self, view):
		# print('on close')
		id = view.id()
		if id in self.IMEs: del self.IMEs[id]
		if id in self.PreviousModes: del self.PreviousModes[id]
		view.settings().clear_on_change('command_mode')


	def callback(self, view):
		currentMode = view.settings().get('command_mode')
		id = view.id()
		
		if (currentMode == self.PreviousModes[id]): return

		# print('callback been called')
		self.PreviousModes[id] = currentMode

		# print("current id: %d" % id)
		# print(self.PreviousModes)
		# print(self.IMEs)

		if (currentMode == True):
			self.IMEs[id] = subprocess.check_output([self.BINPATH]).decode('utf-8').strip()
			subprocess.call([self.BINPATH, self.LAYOUT])
			return

		view.show_popup('<p style="font-size: 0.5em">' + self.IMEs[id].split('.')[-1] + '</p>', sublime.HIDE_ON_MOUSE_MOVE)
		sublime.set_timeout_async(lambda: view.hide_popup(), 1000)
		
		if (self.IMEs[id] == None or self.IMEs[id] == self.LAYOUT):
			return
		subprocess.call([self.BINPATH, self.IMEs[id]])
