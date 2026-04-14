---
title: Manage Your Dotfiles
description:
created: 2026-04-14
modified: 2026-04-14
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

There are many [tools](https://github.com/webpro/awesome-dotfiles?tab=readme-ov-file#tools) for managing your dotfiles - user-specific configuration files

[dotfiles-manager · GitHub Topics · GitHub](https://github.com/topics/dotfiles-manager)

To name a few:

1. [GNU Stow](https://www.gnu.org/software/stow/)
2. [Dotbot](https://github.com/anishathalye/dotbot)
3. [yadm](https://yadm.io/)
4. [chezmoi](https://www.chezmoi.io/)

# What I was trying to do

These tools are additional dependencies that need to be installed prior to setting up your dotfiles. They are fairly heavyweight, so I prefer to avoid external dependencies in favor of a simpler, self-contained setup. As a bonus, there is one less thing that needs to be done when setting up new systems.

Since all the dotfiles resides in $home by default, I just `git init` in my $home folder, ignore all files by default and keep a whitelist of dotfiles I want to backup in .gitignore.

```git
*    # ignores everything
!.*  # un-ignores all dotfiles
.ssh # ignores the .ssh file or folder
```

Tracking the home folder directly into a public git repository is [a bad practice](https://askubuntu.com/questions/1316229/is-it-bad-practice-to-git-init-in-the-home-directory-to-keep-track-of-dot-files).

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

# A Better Approach: Git Bare repository

Looking around the Internet, I have found a few solutions over the years, but I settled on a very simple system several years ago which has served me very well in the time since.

Recently, I came across [this thread in HackerNews](https://news.ycombinator.com/item?id=11070797) and it literally blew my mind. In this post, I would like to share this very elegant solution that avoids the need for any symlinking.

This method does not use symlinks.

> Pro-Tip: stop using billion of useless third-party tools and just use bare git repo to manage dotfiles without messing with **symlinks** and other bs.

The technique consists in storing a **Git bare repository** in a “_side_” folder (like `$HOME/.cfg` or `$HOME/.myconfig`) using a specially crafted alias so that commands are run against that repository and instead of the usual `.git` local folder, which would interfere with any other Git repositories around.

The normal way of doing this would be to do a `git init` in your `$HOME`, but that would totally mess up git commands if you have other repositories in your `$HOME` (also, you probably don’t want your entire `$HOME` in a git repo). So, instead, we will create a dummy folder and initialize a **bare** repository (essentially a git repo with **no** working directory) in there. All git commands will be run with our dummy as the git directory, but `$HOME` as the work directory.

The `--bare` flag creates a repository that doesn’t have a working directory, making it impossible to edit files and commit changes in that repository.

---

```text
mkdir $HOME/.dotfiles
git init --bare "$HOME/.dotfiles"
echo "alias dotfiles='/usr/local/bin/git --git-dir=\$HOME/.dotfiles/ --work-tree=\$HOME'" >> ~/.zshrc
source ~/.zshrc
dotfiles config --local status.showUntrackedFiles no
dotfiles remote add origin <git-repo-url-of-your-dotfiles: e.g., git@github.com:huaminghuangtw/dotfiles.git>
dotfiles status
cd $HOME
dotfiles add .gitconfig
dotfiles commit -m "Add .gitconfig"
dotfiles add .zshrc
dotfiles commit -m "Add .zshrc"
dotfiles push
```

No extra tooling, no symlinks, no manually copy. Files are tracked on a version control system, you can use different branches for different computers,

Keep configuration files in a separate directory

With the use of a `bare` repository, there is no `.git` directory in your `$HOME` directory; so it does not introduce any surprises while working with `git`.

---

# Setting Up a New Machine

Also, you can replicate you configuration easily on new machines. All that is required is cloning your dotfiles followed by copying or linking files. Keeping the entire home directory under version complicates installation.

To set up a new machine to use your version controlled config files, all you need to do is to clone the repository on your new machine telling git that it is a bare repository:

then to clone the git repository onto a new system (after git is set up), you’d run `git clone --bare {URL} $HOME/.dotfiles.git`, then you can `git --git-dir={…} --work-tree=$HOME checkout` so your dotfiles go into the correct places. Then you can reload your OS/shell/etc. as needed so the new configuration files are loaded and you should be good to go. you’ll also need to set `showUntrackedFiles` to false again.

```text
git clone --bare <git-repo-url-of-your-dotfiles: e.g., git@github.com:huaminghuangtw/dotfiles.git> $HOME/.dotfiles
echo "alias dotfiles='/usr/local/bin/git --git-dir=\$HOME/.dotfiles/ --work-tree=\$HOME'" >> ~/.zshrc
source ~/.zshrc
!!! Move your existing dotfiles to `~/.dotfiles.backup`. If you don’t need your old dotfiles anymore, you can safely delete the `~/.dotfiles.backup` directory. !!!
dotfiles checkout 
dotfiles config --local status.showUntrackedFiles no
```

* The step above might fail with a message like:

```text
1error: The following untracked working tree files would be overwritten by checkout:
2    .bashrc
3    .gitignore
4Please move or remove them before you can switch branches.
5Aborting
```

***

This is because your `$HOME` folder might already have some stock configuration files which would be overwritten by Git. The solution is simple: back up the files if you care about them, remove them if you don’t care. I provide you with a possible rough shortcut to move all the offending files automatically to a backup folder:

```text
1mkdir -p .config-backup && \
2config checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | \
3xargs -I{} mv {} .config-backup/{}
```

* Re-run the check out if you had problems:

```text
1config checkout
```

Or:

```text
git clone --separate-git-dir=$HOME/.dotfiles <git-repo-url-of-your-dotfiles: e.g., git@github.com:huaminghuangtw/dotfiles.git> $HOME/dotfiles-tmp
rm -r dotfiles-tmp
```

---

This is how I manage my [dotfiles](https://github.com/huaminghuangtw/dotfiles).

Looking around the Internet, many individuals have open sourced their dotfiles for others to see. A quick GitHub search returns tens of thousands of results.

There are many great dotfiles repos out there, each containing their own inspiration and gems. One way to go through them is to [search GitHub for "dotfiles"](https://github.com/search?q=dotfiles&type=Repositories).

---

[TL; DR](https://github.com/Siilwyn/my-dotfiles/tree/master/.my-dotfiles)

---

Make others’ lives easier

If you have a way to easily share your dotfiles amongst other developers, you’re only going to make it easier _for yourself_ to pull in someone else’s `super-awesome-executable` that will make your own workflow amazing.
