import sublime
import sublime_plugin
import subprocess
import os

def get_setting(key, default = None):
	settings = sublime.load_settings('SmartIM.sublime-settings')
	return settings.get(key, default)

class SmartimCommand(sublime_plugin.EventListener):
	IME = None
	PreviousMode = True
	BINPATH = os.path.join(os.path.dirname(__file__), "im-select")
	LAYOUT = None


	def on_activated_async(self, view):
		SmartimCommand.LAYOUT = get_setting("keyboard_layout", "com.apple.keylayout.US")
		view.settings().clear_on_change('command_mode')
		view.settings().add_on_change('command_mode', lambda: self.callback(view))

	def callback(self, view):
		currentMode = view.settings().get('command_mode')
		if (currentMode == SmartimCommand.PreviousMode): return

		SmartimCommand.PreviousMode = currentMode


		if (currentMode == True):
			SmartimCommand.IME = subprocess.check_output([SmartimCommand.BINPATH]).decode('utf-8').strip()
			subprocess.call([SmartimCommand.BINPATH, SmartimCommand.LAYOUT])
			return

		if (SmartimCommand.IME == None or SmartimCommand.IME == SmartimCommand.LAYOUT):
			return
		subprocess.call([SmartimCommand.BINPATH, SmartimCommand.IME])
