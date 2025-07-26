---
title: VS Code CLI and URL Schemes
description: A quick reference for the most useful Visual Studio Code command-line interface (CLI) options and URL schemes.
created: 2025-07-20T07:55:03
modified: 2025-07-26T14:24:21
draft: false
tags:
  - Today-I-Learned/cli
  - Today-I-Learned/url-schemes
  - Today-I-Learned/vs-code
sources:
  - https://code.visualstudio.com/docs/configure/command-line
---

Visual Studio Code has a powerful [command-line interface (CLI)](https://code.visualstudio.com/docs/configure/command-line) that lets you control how you launch the editor through command-line options (switches).

## Opening Files and Folders

* **Open a file**: `code <file_path>`. You can list multiple files separated by spaces. If a file doesn't exist, it will be created. When opening multiple files, VS Code opens them all as tabs in a single window instance.
* **Open a folder**: `code <folder_path>`. You can specify multiple folders separated by spaces to create a [Multi-root Workspace](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces) that includes each folder and allows you to manage multiple project “roots” simultaneously.

## Common CLI Options

### Go to File Location [^1]

Open a file at a specific line and optional column.

```bash
code -g, --goto path/to/file:line[:column]
```

### New Window

Open a fresh session of VS Code instead of restoring the previous session.

```bash
code -n, --new-window [path/to/folder-or-file]
```

You can also use `-r` or `--reuse-window` to force opening a file or folder in the last active window.

### Wait for Close

Wait for the opened file to be closed before returning to the command line. This is useful for things like editing a Git commit message.

```bash
code -w, --wait path/to/file
```

### Use a Specific Profile

Specify the directory for user data, which is useful for managing separate profiles or running as a different user.

```bash
code --user-data-dir "/path/to/custom/profile"
```

### Disable Extensions

Open VS Code with all installed extensions temporarily disabled.

```bash
code --disable-extensions
```

### Verbose Logging

Enables verbose logging, which is helpful for diagnosing issues.

```bash
code --verbose
```

### Show Help

Displays all available CLI options.

```bash
code --help
```

Alternatively, you can view the manual page:

```bash
man code
```

## Further Reading

For a complete list of options, see the official documentation:

* [Core CLI Options](https://code.visualstudio.com/docs/configure/command-line#_core-cli-options)
* [Advanced CLI Options](https://code.visualstudio.com/docs/configure/command-line#_advanced-cli-options)

## URL Schemes

You can also use `vscode://` URL schemes to open folders and files.

### Open a Folder

```url
vscode://file/{full path to folder}/
```

### Open a File

```url
vscode://file/{full path to file}
```

### Open a File to a Specific Line and Column

```url
vscode://file/{full path to file}:line:column
```

[^1]: The column number for character position is optional.
