# SmartIM

reset Input Method to default keyboard-layout when exit insert mode, and restore Input Method after enter insert mode again.

inspire by [smartim](https://github.com/ybian/smartim)

## Installation

### Package Control

The easiest way to install SmartIM is with [Package Control](http://wbond.net/sublime_packages/package_control)

- Bring up the Command Palette (<kbd>cmd+shift+p</kbd> on OS X, <kbd>ctrl+shift+p</kbd> on Linux/Windows)
- Select "Package Control: Install Package" (it'll take a few seconds)
- Select "SmartIM" when the list appears

Package Control will automatically keep SmartIM up to date with the latest version.

### Manually

1. cd `~/Library/Application\ Support/Sublime\ Text\ 3/Packages`
2. `git clone https://github.com/icymind/SmartIM`

## Config

If your keyboard layout isn't `com.apple.keylayout.US`, you need to tell SmartIM by setting it in SmartIM.sublime-settings:
Click "Preferences - Package Settings - SmartIM - Settings - User", then add the following line to the file:

```json
{
	"keyboard_layout": "your_default_keyboard_id"
}
```

Replace `your_default_keyboard_id` with the ID string of your input method (which can be get via `./im-select`)

### issue

if you got "permission deny" issue, please fix it by:
`chmod +x ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/SmartIM/im-select`
test
