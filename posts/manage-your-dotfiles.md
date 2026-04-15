---
title: How I Manage Dotfiles
description:
created: 2026-04-14
modified: 2026-04-15
draft: true
featured: false
canonicalPath: 2026/4/14/manage-your-dotfiles
tags:
  - /Today-I-Learned/
sources: []
---

Today I learned

plain-text hidden files, commonly referred to as dotfiles, that are stored in the user’s home directory.

According to [Wikipedia](https://en.wikipedia.org/wiki/Hidden_file_and_hidden_directory#:~:text=Commonly%2C%20user%2Dspecific%20application%20configuration%20information%20is%20stored%20in%20the%20user%27s%20home%20directory%20as%20a%20dotfile.):

> User-specific application configuration information is stored in the user’s home directory as a dotfile.

Look at [dotfiles.org](http://dotfiles.org/), a nifty little site that’s designed to help share your own dotfiles:

> Face it: you’re proud of that 204-line .bashrc, and you should be! You’ve fine-tuned your prompt, carefully planned your aliases, and written some pretty time-saving functions over the years.

---

IMO, dotfiles are one of the most important tools you’ll use as a programmer.

Most likely, as a developer, you will keep using and improving your dotfiles for your entire career. Your dotfiles will most likely be the _longest project you ever work on_. For this reason, it is worthwhile to organize your dotfiles project in a disciplined manner for maintainability and extensibility.

Take the time to sit down and really personalize and tweak their shell

For developers who spend any amount of time in the terminal, tweaking and optimizing settings for command-line programs can be an extremely worthwhile investment. Something as easy as light shell customization can result in a significant increase in productivity.

---

# What I was trying to do

 Over the years, I always manage my dotfiles individually using [GitHub Gists](http://gist.github.com/), which distribute in different gists. I have always want to find a way to centralize them to make my life easier. Looking around the Internet, I have found a few solutions.

## Use A Dotfile Manager

There are many [tools](https://github.com/webpro/awesome-dotfiles?tab=readme-ov-file#tools) for managing your dotfiles - user-specific configuration files

[dotfiles-manager · GitHub Topics · GitHub](https://github.com/topics/dotfiles-manager)

To name a few:

1. [GNU Stow](https://www.gnu.org/software/stow/)
2. [Dotbot](https://github.com/anishathalye/dotbot)
3. [yadm](https://yadm.io/)
4. [chezmoi](https://www.chezmoi.io/)

These tools are additional dependencies that need to be installed prior to setting up your dotfiles. They are fairly heavyweight, so I prefer to avoid external dependencies in favor of a simpler, self-contained setup. As a bonus, there is one less thing that needs to be done when setting up new systems.

## Track $HOME Directory with Git

Since all the dotfiles resides in $home by default, I can just `git init` in my $home folder, ignore all files by default and keep a whitelist of dotfiles I want to backup in .gitignore.

```git
*    # ignores everything
!.*  # un-ignores all dotfiles
.ssh # ignores the .ssh file or folder
```

However, tracking the home folder directly into a public git repository is [a bad practice](https://askubuntu.com/questions/1316229/is-it-bad-practice-to-git-init-in-the-home-directory-to-keep-track-of-dot-files).

1. Using this approach to backup dotfiles is dangerous as you mean reveal/leak your credentials (e.g., `.ssh`) on the Internet. Be careful what you push to a public repository on GitHub, e.g. .ssh, .gnupg, etc.

	Also consider that your repository will contain private information in areas you don’t expect, even if you exclude things like your SSH keys. Sharing this repository publicly is probably not a good idea.

2. While git tracking your dotfiles is a great idea, having a git repo at home level makes it easy to accidentally run commands to that repo when you actually mean to run it in a more specific directory repository.

	For example:

	```bash
	mkdir ~/Projects/my-awesome-web-app
	cd ~/Projects/my-awesome-web-app
	npm init # initializes node projects, creates package.json
	git add package.json # would not fail, since it’s actually inside a git repo
	git commit -m "starts work" # actually commits to the home repo, not locally
	```

	Note also that if you have other git working trees in your home directory, you’ll want the parent directories of those to be excluded from this repository so git doesn’t start thinking they are sub-repositories or something.

	I don’t like to have the home directory git repository, simply because you run into weirdness with sub-directories of home also being git repos.

# A Better Way to Manage Dotfiles: Git Bare repository

My next idea was to symlink dotfiles to a single directory and manage that folder with git. But this also felt unnecessarily complex. What a headache! Surely there would be a simpler way to do this, right?

But taken to its extreme where the entire root filesystem is trackable, this approach is not ideal. These are my requirements:

* Any file on the machine can be added to the dotfiles repo
* The dotfiles repo doesn’t interfere with any other git repos

Recently, I came across [this thread in HackerNews](https://news.ycombinator.com/item?id=11070797) and it literally blew my mind.

This method uses a [git bare repository](http://www.saintsjd.com/2011/01/what-is-a-bare-git-repository/), and aliasing git commands to send them to that repo. Simple setup process? Check. Version control in git? Check. Easy installation on different machine? Check. Awesome!

In this post, I would like to share this very elegant solution that avoids the need for any symlinking.

## What is Git bare repository

creates only a folder for git control files, which normally reside inside the .git folder within the repository.

? Bare repos _only_ include commits (and some metadata). There’s nothing in process, uncommitted, or staged on a bare repo, like you might have in a working copy.

---

A **bare Git repository** is a repository that does not contain a “working tree” (the actual editable project files). Instead, it contains only the versioning data and administrative files typically found within a standard `.git` folder.

Key Characteristics

* **No Working Directory:** You cannot directly edit, add, or commit files within a bare repository because the source code files are not checked out on disk.
* **Structure:** While a standard repo keeps its data in a hidden `.git` folder, a bare repo places those contents (like `hooks`, `info`, `objects`, and `refs`) directly in the project root.
* **Naming Convention:** By convention, bare repository folder names end with a `.git` suffix (e.g., `project-name.git`) to signal that it is not for local development.

Primary Uses

* **Central Sharing Point:** They serve as the “hub” for team collaboration. Platforms like **GitHub** and **GitLab** use bare repositories on their servers because they only need to store history and receive pushes, not provide an editing environment.
* **Safe Remote Targets:** Git generally forbids pushing to a non-bare repository to prevent the working tree and history from becoming out of sync. Bare repos are safe for `git push` operations because there is no working tree to disrupt.
* **Dotfile Management:** Some developers use them to manage system configuration files (dotfiles) across different machines without moving the actual files into a subfolder.

Common Commands

* **Create a new bare repo:**
		`git init --bare <repo-name>.git`
* **Clone an existing repo as bare:**
		`git clone --bare <source-url>`
* **Convert an existing repo to bare:**
		Move the `.git` folder to a new location and update its configuration using **Git’s configuration documentation**.

---

[Reddit - Trying to understand bare repos](https://www.reddit.com/r/git/comments/6ncejs/comment/dk8ixyq)

Non-bare repos have a structure like this:

```text
project/
    .git/
        <gitfiles>
    user-file1
    user-file2
    …
```

The user works in the `project` folder, and the `.git` folder in there has all the revisions, branch pointers, etc., which I’ve labeled `<gitfiles>`, i.e. all of git’s junk for this particular repo.

Bare repos are like this:

```text
project.git/
    <gitfiles>
```

There is no `.git` folder, and the `.git` name has moved up as an extension onto the project name (just a convention, not guaranteed to be set up like this everywhere). Because bare repos can’t have a user, there’s no reason to cordon off the git files into their own directory, and they can all just be out in the main project folder, and the `.git` extension is like a simple signifier of this; the project folder itself is the folder full of the git junk for this repo.

Bare repos are just repos that can’t have a user or working space in them. They’re just meant to be put somewhere so users can push to them and fetch/pull from them. They are basically just the `.git` folder from a regular, non-bare repo.

---

[What is a bare git repository? \| Jon Saints](https://www.saintsjd.com/2011/01/what-is-a-bare-git-repository/)

> Well, a working repository created with `git init` is for… **working**. It is where you will actually edit, add and delete files and `git commit` to save your changes. If you are starting a project in a folder on your dev machine where you will add, edit and delete files of your project, use “git init”. Note: if you `git clone` a repository you will be given a **working** repository with the .git folder and copies of the working files for editing.
>
> A bare repository created with `git init --bare` is for… **sharing**. If you are collaborating with a team of developers, and need a place to share changes to a repo, then you will want to create a bare repository in centralized place where all users can push their changes (often the easy choice is github.com). Because git is a distributed version control system, no one will directly edit files in the shared centralized repository. Instead developers will clone the shared bare repo, make changes locally in their working copies of the repo, then push back to the shared bare repo to make their changes available to other users.
>
> Because no one ever makes edits directly to files in the shared bare repo, a working tree is not needed. In fact the working tree would just get in way and cause conflicts as users push code to the repository. This is why bare repositories exist and have no working tree.

## Setup

The technique consists in storing a **Git bare repository** in a “_side_” folder (like `$HOME/.cfg` or `$HOME/.dotfiles`)

The normal way of doing this would be to do a `git init` in your `$HOME`, but that would totally mess up git commands if you have other repositories in your `$HOME` (also, you probably don’t want your entire `$HOME` in a git repo). So, instead, we will create a dotfiles repo with the `--bare` parameter. The `--bare` flag creates a repository that doesn’t have a working directory. All git commands will be run with our dummy as the git directory, but `$HOME` as the work directory.

```text
cd $HOME
mkdir .dotfiles
git init --bare .dotfiles
```

1. Add alias setting to shell configuration file. I use zsh so it’s `.zshrc`. For bash, it’d be `.bashrc`. We will use this alias `dotfiles` to interact with the dotfiles repos instead of the usual `git`.
2. Reload the shell setting.

```text
echo "alias dotfiles='$(which git) --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'" >> $HOME/.zshrc
source ~/.zshrc
```

With `git-worktree`, and you can use it with any repo to create a working tree in another directory.

Now you can use the full power of git directly in your home directory by using the new `dotfiles` command (rather than `git`).

Maybe you were brave and typed config status already. This will list the content of your whole home directory as “untracked files”. This is not what we want. We can prevent untracked files from showing up when we call `dotfiles status`:

```text
dotfiles config --local status.showUntrackedFiles no
```

How to ignore files in a bare git repo?

In a bare git repository, you cannot use a working tree, so you can’t simply create or edit a `.gitignore` file as usual. Instead, you should use the core.excludesFile configuration to specify a global ignore file for your dotfiles setup.

1. Create a global ignore file (e.g., ~/.gitignore):

```text
.DS_Store
```

1. Tell your bare repo to use this file for ignores:

```text
dotfiles config --local core.excludesFile ~/.gitignore
```

Now, your bare repo will respect the ignore rules in `~/.gitignore`.

## Basic usage

Now git status will only check what’s being tracked. You can also play around with other commands as you wish:

```text
dotfiles status
dotfiles log
dotfiles diff
```

Optionally, you can use git remote repo if you want to manage the files online.

```text
dotfiles remote add origin git@github.com:username/repo.git
```

Verify with `dotfiles remote -v`

Now, you can add some files, either local, in your home directory, or anywhere on the system, and commit them to the repo.

```text
dotfiles add ~/.gitconfig
dotfiles commit -m "Add .gitconfig"
dotfiles add ~/.zshrc
dotfiles commit -m "Add .zshrc"
dotfiles add /etc/udev/rules.d/my-udev.rules
dotfiles commit -m "Add udev rules"
```

```text
dotfiles push
```

No extra third-party tooling, no symlinks, no manually copy. Files are tracked on a version control system, you can use different branches for different computers,

Keep configuration files in a separate directory

With the use of a `bare` repository, there is no `.git` directory in your `$HOME` directory; so it does not introduce any surprises while working with `git`.

Using git bare repositories, there is no more moving files into an initialized git repository and then creating symlinks. Now, I just add, commit and then push. Done.

## Additional Features

First, I wholly depend on tig for quickly seeing the state or history of a git repo, so to invoke tig on the dotfiles repo we use this:

alias dtig=‘GIT_DIR=/home/mx/.dotfiles GIT_WORK_TREE=/ tig’

Second, because of the huge spread of where files are, I found myself always needing to list which files are explicitly tracked, using `dotfiles ls-files`. It’s really helpful to be able to quickly see where that config file was that you need to edit again.

## Setting Up a New Machine

Also, you can replicate you configuration easily on new machines. All that is required is cloning your dotfiles followed by copying or linking files. Keeping the entire home directory under version complicates installation.

To set up a new machine to use your version controlled config files, all you need to do is to clone the repository on your new machine telling git that it is a bare repository:

First, create alias to ensure that the git bare repository works without problem and reload the shell setting to use that alias.

```text
echo "alias dotfiles='$(which git) --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'" >> $HOME/.zshrc
source ~/.zshrc
```

Clone the remote repo.

```text
git clone --bare git@github.com:username/repo.git $HOME/.dotfiles
```

Git will store all the repo metadata but not check out any version of the contents of the repo in that directory.

Check if it works fine.

```text
dotfiles checkout
dotfiles config --local status.showUntrackedFiles no
```

If you already have configuration files with identical names, checkout will fail with a message like:

```text
error: The following untracked working tree files would be overwritten by checkout:
    .zshrc
    .gitignore
Please move or remove them before you can switch branches.
Aborting
```

This is because your `$HOME` folder might already have some stock configuration files which would be overwritten by Git.

The solution is simple: back up the files (move them to e.g. `~/.dotfiles.backup`) if you care about them, or delete them if you don’t care.

Then, re-run the check out if you had problems:

```text
config checkout
```

Finally, prevent untracked files from showing up on `dotfiles status` as we previously did.

```text
dotfiles config --local status.showUntrackedFiles no
```

---

That’s it!

This is how I manage my [dotfiles](https://github.com/huaminghuangtw/dotfiles).

Looking around the Internet, many individuals have open sourced their dotfiles for others to see. A quick GitHub search returns tens of thousands of results.

There are many great dotfiles repos out there, each containing their own inspiration and gems. One way to go through them is to [search GitHub for "dotfiles"](https://github.com/search?q=dotfiles&type=Repositories).

---

[TL; DR](https://github.com/Siilwyn/my-dotfiles/tree/master/.my-dotfiles)

---

Make others’ lives easier

If you have a way to easily share your dotfiles amongst other developers, you’re only going to make it easier _for yourself_ to pull in someone else’s `super-awesome-executable` that will make your own workflow amazing.
