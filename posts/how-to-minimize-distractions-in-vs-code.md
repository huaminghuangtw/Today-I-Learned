---
title: How to Minimize Distractions in VS Code
description:
created: 2025-08-11T15:29:01
modified: 2025-11-08T16:53:50
draft: false
featured: false
tags:
  - Today-I-Learned/vs-code
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

* Hide the sidebar (`Cmd+B`).
* Hide the panel (`Cmd+J`).
* Hide the status bar (`Cmd+Shift+P` → “View: Toggle Status Bar Visibility”).
* Hide the [breadcrumbs](https://code.visualstudio.com/docs/getstarted/userinterface#_breadcrumbs) via `Cmd+Shift+P` → “View: Toggle Breadcrumbs”.
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

* Hide the overview ruler:

	```json
	"editor.hideCursorInOverviewRuler": true
    ```
