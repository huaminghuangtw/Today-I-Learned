---
title: How to Minimize Distractions in VS Code
created: 2025-08-11
modified: 2026-06-30
sources:
  - https://stackoverflow.com/questions/40891692/how-to-disable-or-hide-scrollbar-minimap
  - https://stackoverflow.com/questions/50593516/colored-pixels-in-scrollbar-in-vs-code
---

Today I learned how to minimize distractions in VS Code.

# Use Zen Mode

* Activate Zen Mode with `Cmd+K Z`.
	* Or from the Command Palette → “View: Toggle Zen Mode”.
* Press `Cmd+K Z` again to exit Zen Mode.

# Hide UI Elements

* Hide the sidebar (`Cmd`+`B`).
* Hide the panel (`Cmd`+`J`).
* Hide the status bar (`Cmd`+`Shift`+`P` → “View: Toggle Status Bar Visibility”).
* Hide the [breadcrumbs](https://code.visualstudio.com/docs/getstarted/userinterface#_breadcrumbs) via `Cmd`+`Shift`+`P` → “View: Toggle Breadcrumbs”.
	* Alternatively, you can add this line to `settings.json`:

	```json
	"breadcrumbs.enabled": false
	```

* Hide the [minimap](https://code.visualstudio.com/docs/getstarted/userinterface#_minimap) via `Cmd+Shift+P` → “View: Toggle Minimap”.
	* Alternatively, you can add this line to `settings.json`:

	```json
	"editor.minimap.enabled": false
	```

* Hide the scroll bar:

	```json
	"editor.scrollbar.horizontal": "hidden",
	"editor.scrollbar.vertical": "hidden"
    ```

* Hide the [overview ruler](https://code.visualstudio.com/api/references/theme-color):

	```json
	"workbench.colorCustomizations": {
		"editor.hideCursorInOverviewRuler": true,
		"editorOverviewRuler.border": "#0000",
		"editorOverviewRuler.findMatchForeground": "#0000",
		"editorOverviewRuler.rangeHighlightForeground": "#0000",
		"editorOverviewRuler.selectionHighlightForeground": "#0000",
		"editorOverviewRuler.wordHighlightForeground": "#0000",
		"editorOverviewRuler.wordHighlightStrongForeground": "#0000",
		"editorOverviewRuler.wordHighlightTextForeground": "#0000",
		"editorOverviewRuler.modifiedForeground": "#0000",
		"editorOverviewRuler.addedForeground": "#0000",
		"editorOverviewRuler.deletedForeground": "#0000",
		"editorOverviewRuler.errorForeground": "#0000",
		"editorOverviewRuler.warningForeground": "#0000",
		"editorOverviewRuler.infoForeground": "#0000",
		"editorOverviewRuler.bracketMatchForeground": "#0000",
		"editorOverviewRuler.inlineChatInserted": "#0000",
		"editorOverviewRuler.inlineChatRemoved": "#0000",
		"editorOverviewRuler.commentDraftForeground": "#0000",
	},
	```
