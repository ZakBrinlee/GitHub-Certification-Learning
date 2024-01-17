# [Learning Git and GitHub - course](https://www.linkedin.com/learning/paths/prepare-for-the-github-foundations-certification)
Started: January 16th, 2023
Completed: January 17th, 2023

## Notes
- I have been using Git and GitHub since 2016. This will be fun and informative
- Version control is an essential skill for developers to master, and Git is by far the most popular version control system on the web. In this fast-paced course, author Ray Villalobos shows you how to install Git and use the fundamental commands you need to work with Git projects: moving files, managing logs, and working with branches.

## Links
- [Git](https://git-scm.com/)
- [Git Cheat-Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Markdown Cheat-sheet](https://www.markdownguide.org/cheat-sheet/)
- [Markdown Basic Syntax](https://www.markdownguide.org/basic-syntax/)
- [Markdown Extended Syntax - Advanced](https://www.markdownguide.org/extended-syntax/)

## Working With Git
- Version control
- Easily collaboration of code
- Two types of Version Control Architecutre
-- Centralized 
--- Single storage location for code
--- Tracking and Retrieval are all happening on the same server
--- Apache SubVersioN (popular software for centralized version)
-- Distributed
--- Clone (copy) of the source code
--- Source code (on server) is considered the "working copy"
--- Push/Pull code from the source code
- What is Git?
-- Version Control
-- Time Machine
-- Check points (commits)
-- Multiverse (branches)
-- Synchronize (merging)
- Rebasing
-- Allows you to take the changes from one branch and apply them onto another
-- This is the time machine part of Git as it lets you rewrite the commit history

## Working with GitHub
### What is GitHub?
- Cloud Repository
- Collaborative Environment
- Project Management
- Must know how to
-- Set up remote
-- Push
--- How to push files to the remote repository
-- Fetch/Pull

### Using Markdown
- General info, use Markdown Cheatsheet until you are familiar
- Check links section for basic syntax and cheatsheet

### Markdown Additions
- This is extended syntax for additional features in markdown
- New to me
-- Footnotes `[^1]` -> reference lower in doc with `[^1]: footnote here`

## GitHub Repos and Projects
### Repo Essential Files
- README.md
  - Purpose of repo
  - Homepage
  - `root`, `docs` or `.github`
  - Table of Contents
  - [Awesome README Examples](https://github.com/matiassingers/awesome-readme)
- LICENSE (optional)
  - Informs developers of how they are legally allowed to use the software
  - Open Source - free to use by anyone
  - Helper sites to create the correct license for your project
  - Common file exts: `.md`, `.txt`, `rst`
  - Must be in the `root` folder
- CODE_OF_CONDUCT.MD
  - Adopt a code of conduct to define community standards, signal a welcoming and inclusive project, and outline procedures for handling abuse.
- SECURITY.md
  - How you specify your security support
  - How to report vulnerabilities
- CONTRIBUTING.md
  - How to contribute
  - Issues sidebar
- SUPPORT.md
  - How to get support for the project
- CODEOWNERS
  - Who is responsible for each part of the project
  - Must have permissions
  - Automatic notifications
  - Branch by branch modifiable

### CODEOWNERS
- Allows the project to have parts of the project assigned to code owners
- Code owners are automatically requested for review when someone opens a pull request that modifies code that they own
- If a file has a code owner, you can see who the code owner is before you open a pull request.
- [GitHub CODEOWNERS Doc](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)

### Syncing GitHub
- `fetch` vs `pull`
-- `fetch` will sync the connection between remote and local
-- `pull` will sync and copy the changes from a remote repo into the local files/working directy
- Releases
-- Specific version of your application
-- `vX.X.X` -> `v<main-release.sub-release.minor-release|bug-fix>`


### Repository Insights
- Pulse
-- Overview of the repository including # of Pull Requests, Open Pull requests, etc
- Contributors
-- Graphs with information regarding additions, deletions, contributors, etc
- Community
--
- Community Standards
-- How the project compares to GitHub's community standards
- Traffic
-- Vistors, Clones, referring sites, popular content, etc
- Commits
-- Shows commits over time
- Code Frequency
-- Graphs of actions to code on the repo
- Depency Graph
-- What dependencies the project has and if any are out of date
- Network
-- Graph of people making pull requests/changes to code. 
- Forks
-- List of forks from the repo

### GitHub Shortcut Features
- `?` immediately opens a helper
-- If in repo, will open command pallete
-- If in main GH, will open Shortcut window
- `CMD+k` opens command pallete
- `CMD+.` opens a lightweight editor in github.dev


## GitHub Social and Publishing
### GitHub Discussions
- A place to discuss topics not neccessarily related to the code. 
-  Use discussions to ask and answer questions, share information, make announcements, and conduct or participate in a conversation about a project on GitHub.
- [GitHub Discussions](https://docs.github.com/en/discussions)
- Awesome place to get feedback from users using features
-- Polls
-- Q&A
-- Much more

### GitHub Notifications
- Types of notifications
- Great view/settings in the Notification panel on GitHub
- Configurable in Profile Settings

### GitHub gists
- Share code, notes, and snippets.
- [GitHub all gists](https://gist.github.com/discover)
-- Great place to find small code snippets for things like regex, apis, formulas etc

### GitHub wikis
- You can host documentation for your repository in a wiki, so that others can use and contribute to your project.
- [GitHub Wikis about doc](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis)
- Allows different pages for separating documention

### GitHub Pages
- Ability to host static website for free
- Use your own custom domains or default `github.io`
- [GitHub Pages docs](https://pages.github.com/)
