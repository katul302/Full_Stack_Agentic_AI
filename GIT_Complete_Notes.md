# 🧠 Git & GitHub — Complete Notes (Basic to Advanced)
### For Senior Engineers (13+ Years Experience)
*Covers: internals, workflows, branching strategies, CI/CD, team collaboration, troubleshooting*

---

## 📚 TABLE OF CONTENTS
1. [Git Internals — How Git Actually Works](#1-git-internals)
2. [Setup & Configuration](#2-setup--configuration)
3. [Core Commands — Daily Use](#3-core-commands)
4. [Branching & Merging](#4-branching--merging)
5. [Remote Repositories](#5-remote-repositories)
6. [Undoing Things — The Right Way](#6-undoing-things)
7. [Stashing & Cherry-picking](#7-stashing--cherry-picking)
8. [Rebasing — Deep Dive](#8-rebasing)
9. [Tags & Releases](#9-tags--releases)
10. [Git Workflows for Teams](#10-git-workflows-for-teams)
11. [GitHub Features](#11-github-features)
12. [Authentication Methods](#12-authentication-methods)
13. [Advanced Git](#13-advanced-git)
14. [Troubleshooting](#14-troubleshooting)
15. [Quick Reference Cheatsheet](#15-quick-reference-cheatsheet)

---

## 1. Git Internals — How Git Actually Works

### 🔍 Git is NOT a delta-based VCS — it's a **snapshot** system

Git stores a snapshot of your entire project every time you commit. If a file hasn't changed, Git stores a pointer to the previous identical file — not a copy.

### 🗂️ The Four Git Object Types

| Object | Description |
|--------|-------------|
| **blob** | Stores file content (no filename, no metadata) |
| **tree** | Stores directory structure (maps filenames → blobs/trees) |
| **commit** | Points to a tree + parent commit(s) + author/message |
| **tag** | Points to a commit with a label |

### 🔑 SHA-1 Hashing
Every object is identified by a 40-character SHA-1 hash of its content.
```bash
git cat-file -t 6f3818c   # shows type: commit/blob/tree/tag
git cat-file -p 6f3818c   # shows content of that object
```

### 📁 The `.git` Directory Structure
```
.git/
├── HEAD          # Points to current branch (e.g., ref: refs/heads/main)
├── config        # Repo-level git config
├── index         # Staging area (binary file)
├── objects/      # All blobs, trees, commits, tags
│   ├── pack/     # Packed objects (compressed)
│   └── info/
├── refs/
│   ├── heads/    # Local branches → commit SHAs
│   ├── remotes/  # Remote tracking branches
│   └── tags/     # Tags
└── logs/         # Reflog history
```

### 🌳 How a Commit is Stored
```
commit (SHA: abc123)
  └── tree (SHA: def456)   ← root directory snapshot
        ├── blob: README.md
        ├── blob: main.py
        └── tree: src/
              └── blob: app.py
```

### 🔄 The Three Trees (States of Git)
```
Working Directory  →  Staging Area (Index)  →  Repository (.git)
   (modified)           (git add)               (git commit)
```

### ⚡ Packfiles
Git periodically runs `git gc` to compress loose objects into packfiles using delta compression for efficiency.
```bash
git gc              # manually trigger garbage collection
git count-objects -v  # see how many loose objects exist
```

---

## 2. Setup & Configuration

### 🛠️ First-Time Global Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"   # VS Code as editor
git config --global init.defaultBranch main
git config --global pull.rebase false            # merge on pull (default)
git config --global core.autocrlf input          # macOS/Linux
git config --global core.autocrlf true           # Windows
```

### 📋 Config Levels (Priority: local > global > system)
```bash
git config --system   # /etc/gitconfig — all users on machine
git config --global   # ~/.gitconfig — current user
git config --local    # .git/config — current repo only
```

### 🔍 View & Edit Config
```bash
git config --list                        # show all config
git config --list --show-origin          # show config with file source
git config --global --edit               # open global config in editor
git config user.email                    # show specific value
git config --global --unset user.email   # remove a setting
```

### 🎨 Useful Aliases
```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.unstage "reset HEAD --"
git config --global alias.last "log -1 HEAD"
```

### 📝 .gitignore
```bash
# Create a global gitignore
git config --global core.excludesfile ~/.gitignore_global

# Common patterns
*.log
*.env
__pycache__/
.DS_Store
node_modules/
.venv/
dist/
build/
*.pyc
```

### 🔧 Initializing a Repo
```bash
git init                        # init in current directory
git init my-project             # init in new folder
git init --bare repo.git        # bare repo (for servers, no working tree)

# Connect to remote after init
git remote add origin git@github.com:user/repo.git
git branch -M main
git push -u origin main
```

---

## 3. Core Commands — Daily Use

### 📸 Staging & Committing
```bash
git status                        # show working tree status
git status -s                     # short format
git add file.py                   # stage a specific file
git add .                         # stage all changes
git add -p                        # interactively stage hunks (patch mode)
git add -u                        # stage only tracked files (no new files)

git commit -m "message"           # commit with inline message
git commit                        # open editor for message
git commit -am "message"          # stage tracked files + commit in one step
git commit --amend                # modify last commit (message or files)
git commit --amend --no-edit      # amend without changing message
```

### 📜 Viewing History
```bash
git log                           # full log
git log --oneline                 # compact one-line per commit
git log --oneline --graph --all   # visual branch graph
git log -n 5                      # last 5 commits
git log --author="Atul"           # filter by author
git log --since="2 weeks ago"     # filter by date
git log --grep="fix"              # filter by commit message
git log -- file.py                # commits that touched a file
git log -p file.py                # show diffs for a file
git log --stat                    # show file change stats
git shortlog -sn                  # commits per author
```

### 🔍 Diffing
```bash
git diff                          # unstaged changes vs last commit
git diff --staged                 # staged changes vs last commit
git diff HEAD                     # all changes vs last commit
git diff branch1..branch2         # diff between two branches
git diff abc123..def456           # diff between two commits
git diff HEAD~3 HEAD              # last 3 commits diff
git diff --name-only              # only show changed filenames
git diff --stat                   # summary of changes
```

### 🗑️ Removing & Moving Files
```bash
git rm file.py                    # remove file from repo and disk
git rm --cached file.py           # untrack file (keep on disk)
git mv old.py new.py              # rename/move file (tracked by git)
```

### 🔎 Searching
```bash
git grep "search_term"            # search in working directory
git grep "search_term" HEAD       # search in last commit
git grep -n "search_term"         # show line numbers
git log -S "function_name"        # find commits that added/removed string (pickaxe)
git log -G "regex_pattern"        # find commits matching regex in diff
```

### 📊 Blame
```bash
git blame file.py                 # show who changed each line
git blame -L 10,20 file.py        # blame specific line range
git blame -w file.py              # ignore whitespace changes
```

---

## 4. Branching & Merging

### 🌿 Branch Basics
```bash
git branch                        # list local branches
git branch -a                     # list all branches (local + remote)
git branch -v                     # list branches with last commit
git branch feature/login          # create new branch
git checkout feature/login        # switch to branch
git checkout -b feature/login     # create + switch in one step
git switch feature/login          # modern way to switch (Git 2.23+)
git switch -c feature/login       # modern way to create + switch
git branch -d feature/login       # delete branch (safe — merged only)
git branch -D feature/login       # force delete branch
git branch -m old-name new-name   # rename branch
```

### 🔀 Merging
```bash
git merge feature/login           # merge branch into current branch
git merge --no-ff feature/login   # always create merge commit (no fast-forward)
git merge --squash feature/login  # squash all commits into one (then commit manually)
git merge --abort                 # abort an in-progress merge
```

### ⚡ Fast-Forward vs No-Fast-Forward
```
Fast-Forward (linear history):
  main: A → B → C → D (feature commits applied directly)

No-Fast-Forward (preserves branch history):
  main: A → B → M (merge commit)
              ↗
  feature: C → D
```

### ⚔️ Resolving Merge Conflicts
```bash
# When conflict occurs:
git status                        # see conflicted files
# Edit files — look for conflict markers:
# <<<<<<< HEAD
# your changes
# =======
# their changes
# >>>>>>> feature/login

git add resolved-file.py          # mark as resolved
git commit                        # complete the merge

# Tools
git mergetool                     # open configured merge tool
git checkout --ours file.py       # keep your version
git checkout --theirs file.py     # keep their version
```

### 🌲 Branch Strategies
```
main          — production-ready code only
develop       — integration branch
feature/*     — new features (branch from develop)
release/*     — release preparation
hotfix/*      — urgent production fixes (branch from main)
```

### 🔍 Tracking Branches
```bash
git branch -u origin/main         # set upstream tracking
git branch -vv                    # show tracking info for all branches
git checkout --track origin/feature  # create local branch tracking remote
```

---

## 5. Remote Repositories

### 🌐 Managing Remotes
```bash
git remote -v                              # list remotes with URLs
git remote add origin git@github.com:user/repo.git   # add remote
git remote add upstream git@github.com:original/repo.git  # add upstream (for forks)
git remote remove origin                   # remove remote
git remote rename origin upstream          # rename remote
git remote set-url origin git@github.com:user/new-repo.git  # change URL
git remote show origin                     # detailed info about remote
```

### 📥 Fetching & Pulling
```bash
git fetch                          # download changes, don't merge
git fetch origin                   # fetch from specific remote
git fetch --all                    # fetch from all remotes
git fetch --prune                  # fetch + remove deleted remote branches

git pull                           # fetch + merge (default)
git pull origin main               # pull specific branch
git pull --rebase                  # fetch + rebase instead of merge
git pull --ff-only                 # only fast-forward, fail if not possible
```

### 📤 Pushing
```bash
git push                           # push current branch to tracked remote
git push origin main               # push to specific remote/branch
git push -u origin feature/login   # push + set upstream tracking
git push --all                     # push all branches
git push --tags                    # push all tags
git push origin --delete feature/login  # delete remote branch
git push --force                   # force push (DANGEROUS — rewrites history)
git push --force-with-lease        # safer force push (fails if remote has new commits)
```

### 🍴 Working with Forks
```bash
# Fork on GitHub, then:
git clone git@github.com:youruser/repo.git
git remote add upstream git@github.com:original/repo.git

# Sync fork with upstream
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### ⚠️ The Nested Clone Problem (Common Mistake)
```bash
# WRONG — running clone from INSIDE the repo:
cd ~/Documents/Full_Stack_Agentic_AI   # you're already IN the repo
git clone git@github.com:user/repo.git  # creates nested Full_Stack_Agentic_AI/

# CORRECT — run clone from PARENT directory:
cd ~/Documents
git clone git@github.com:user/repo.git  # creates ~/Documents/Full_Stack_Agentic_AI

# To update an existing local repo, use pull instead:
cd ~/Documents/Full_Stack_Agentic_AI
git pull                                # NOT git clone
```

---

## 6. Undoing Things — The Right Way

### 🧭 Decision Guide — Which Undo Command to Use?

| Situation | Command |
|-----------|---------|
| Unstage a file (keep changes) | `git restore --staged file.py` |
| Discard working dir changes | `git restore file.py` |
| Undo last commit (keep changes staged) | `git reset --soft HEAD~1` |
| Undo last commit (keep changes unstaged) | `git reset --mixed HEAD~1` |
| Undo last commit (discard all changes) | `git reset --hard HEAD~1` |
| Undo a pushed commit safely | `git revert <commit>` |
| Fix last commit message | `git commit --amend` |

### 🔄 git restore (Git 2.23+)
```bash
git restore file.py               # discard working dir changes
git restore --staged file.py      # unstage file (keep changes)
git restore --staged --worktree file.py  # unstage + discard changes
git restore --source HEAD~2 file.py      # restore file from 2 commits ago
```

### 🔁 git reset
```bash
git reset --soft HEAD~1           # undo commit, keep changes STAGED
git reset --mixed HEAD~1          # undo commit, keep changes UNSTAGED (default)
git reset --hard HEAD~1           # undo commit, DISCARD all changes ⚠️
git reset HEAD~3                  # go back 3 commits (mixed)
git reset abc123                  # reset to specific commit
git reset --hard origin/main      # reset local to match remote ⚠️
```

### ↩️ git revert (Safe for Shared History)
```bash
git revert HEAD                   # create new commit that undoes last commit
git revert abc123                 # revert a specific commit
git revert HEAD~3..HEAD           # revert last 3 commits
git revert --no-commit HEAD~3..HEAD  # revert without auto-committing
git revert -m 1 <merge-commit>    # revert a merge commit (keep parent 1)
```

> **Rule:** Use `reset` for local/unpushed commits. Use `revert` for pushed commits.

### 🧹 Cleaning Untracked Files
```bash
git clean -n                      # dry run — show what would be deleted
git clean -f                      # delete untracked files
git clean -fd                     # delete untracked files + directories
git clean -fX                     # delete only ignored files
git clean -fx                     # delete ignored + untracked files
```

### 🕰️ Reflog — Your Safety Net
```bash
git reflog                        # show all HEAD movements (even after reset)
git reflog show branch-name       # reflog for specific branch
git checkout HEAD@{3}             # go to state 3 moves ago
git reset --hard HEAD@{2}         # restore to 2 moves ago
# Reflog entries expire after 90 days by default
```

---

## 7. Stashing & Cherry-picking

### 📦 Git Stash
```bash
git stash                         # stash current changes (tracked files)
git stash push -m "WIP: login"    # stash with a description
git stash -u                      # stash including untracked files
git stash -a                      # stash including ignored files too

git stash list                    # list all stashes
git stash show                    # show summary of latest stash
git stash show -p                 # show full diff of latest stash
git stash show stash@{2}          # show specific stash

git stash pop                     # apply latest stash + remove from stash list
git stash apply                   # apply latest stash (keep in stash list)
git stash apply stash@{2}         # apply specific stash
git stash drop stash@{1}          # delete specific stash
git stash clear                   # delete ALL stashes ⚠️

git stash branch feature/wip      # create branch from stash + apply it
```

### 🍒 Cherry-picking
Cherry-pick applies a specific commit from one branch onto another.
```bash
git cherry-pick abc123            # apply commit abc123 to current branch
git cherry-pick abc123 def456     # apply multiple commits
git cherry-pick abc123..def456    # apply a range of commits
git cherry-pick --no-commit abc123  # apply changes without committing
git cherry-pick --abort           # abort in-progress cherry-pick
git cherry-pick --continue        # continue after resolving conflicts
git cherry-pick -x abc123         # append original commit SHA to message
```

### 🎯 When to Use Cherry-pick
```
✅ Backport a bug fix to an older release branch
✅ Apply a specific feature commit without merging the whole branch
✅ Recover a commit from a deleted branch
❌ Don't use for large sets of commits — use merge/rebase instead
```

### 💡 Stash Use Case Example
```bash
# You're on feature/login, need to quickly fix a bug on main
git stash push -m "WIP: login form validation"
git checkout main
git checkout -b hotfix/null-pointer
# ... fix bug, commit ...
git checkout feature/login
git stash pop
# Continue where you left off
```

---

## 8. Rebasing — Deep Dive

### 🔄 What is Rebase?
Rebase moves or replays commits from one branch onto another, creating a **linear history**.

```
Before rebase:
  main:    A → B → C
  feature:     ↘ D → E

After: git rebase main (from feature branch)
  main:    A → B → C
  feature:         ↘ D' → E'   (new commits, same changes)
```

### 🛠️ Basic Rebase
```bash
git checkout feature/login
git rebase main               # rebase feature onto main

git rebase --abort            # abort rebase in progress
git rebase --continue         # continue after resolving conflict
git rebase --skip             # skip current conflicting commit
```

### ✏️ Interactive Rebase — Rewrite History
```bash
git rebase -i HEAD~3          # interactively edit last 3 commits
git rebase -i abc123          # rebase from specific commit
```

**Interactive rebase commands:**
```
pick   abc123  commit message   → keep commit as-is
reword abc123  commit message   → keep commit, edit message
edit   abc123  commit message   → pause to amend commit
squash abc123  commit message   → merge into previous commit
fixup  abc123  commit message   → merge into previous (discard message)
drop   abc123  commit message   → delete this commit entirely
exec   command                  → run shell command
```

### 🗜️ Squashing Commits
```bash
# Squash last 3 commits into one
git rebase -i HEAD~3
# In editor: change 'pick' to 'squash' for commits 2 and 3
# Write combined commit message

# Alternative: squash merge
git checkout main
git merge --squash feature/login
git commit -m "Add login feature"
```

### ⚠️ Rebase Golden Rule
> **Never rebase commits that have been pushed to a shared remote branch.**
> Rebase rewrites commit SHAs — this breaks history for everyone else.

```bash
# Safe: rebase your local feature branch onto updated main
git fetch origin
git rebase origin/main

# DANGEROUS: rebasing a branch others are working on
git push --force-with-lease   # if you must force push after rebase
```

### 🆚 Merge vs Rebase

| | Merge | Rebase |
|--|-------|--------|
| History | Preserves branch history | Creates linear history |
| Merge commit | Yes (with --no-ff) | No |
| Safe for shared branches | ✅ Yes | ❌ No |
| Cleaner log | No | Yes |
| Use case | Team branches, main | Local feature cleanup |

---

## 9. Tags & Releases

### 🏷️ Tag Basics
Tags mark specific points in history — typically used for releases.

```bash
git tag                           # list all tags
git tag -l "v1.*"                 # list tags matching pattern
git tag v1.0.0                    # create lightweight tag (just a pointer)
git tag -a v1.0.0 -m "Release 1.0.0"  # create annotated tag (recommended)
git tag -a v1.0.0 abc123 -m "msg"     # tag a specific commit
git show v1.0.0                   # show tag details
git tag -d v1.0.0                 # delete local tag
```

### 📤 Pushing Tags
```bash
git push origin v1.0.0            # push a specific tag
git push origin --tags            # push all tags
git push origin --follow-tags     # push commits + annotated tags only
git push origin --delete v1.0.0   # delete remote tag
```

### 🆚 Lightweight vs Annotated Tags

| | Lightweight | Annotated |
|--|-------------|-----------|
| Stored as | Simple pointer to commit | Full git object |
| Has message | No | Yes |
| Has tagger info | No | Yes |
| Has date | No | Yes |
| Recommended for | Temporary/local | Releases |

### 📦 Semantic Versioning (SemVer)
```
v MAJOR . MINOR . PATCH
  v1     .  2    .  3

MAJOR — breaking changes
MINOR — new features (backward compatible)
PATCH — bug fixes (backward compatible)

Examples:
v1.0.0   — initial release
v1.1.0   — new feature added
v1.1.1   — bug fix
v2.0.0   — breaking API change
```

### 🚀 GitHub Releases
```bash
# Create a release on GitHub:
# 1. Push an annotated tag
git tag -a v1.0.0 -m "First stable release"
git push origin v1.0.0

# 2. Go to GitHub → Releases → Draft a new release
# 3. Select the tag, add release notes, attach binaries

# Using GitHub CLI:
gh release create v1.0.0 --title "v1.0.0" --notes "Release notes here"
gh release list
gh release view v1.0.0
```

### 🔍 Checking Out Tags
```bash
git checkout v1.0.0               # detached HEAD state — read only
git checkout -b release/v1.0.0 v1.0.0  # create branch from tag
```

---

## 10. Git Workflows for Teams

### 🌊 1. Git Flow (Vincent Driessen Model)
Best for: projects with scheduled releases
```
main        — production code (tagged releases)
develop     — integration branch
feature/*   — branch from develop, merge back to develop
release/*   — branch from develop, merge to main + develop
hotfix/*    — branch from main, merge to main + develop
```
```bash
# Feature workflow
git checkout develop
git checkout -b feature/user-auth
# ... work ...
git checkout develop
git merge --no-ff feature/user-auth
git branch -d feature/user-auth

# Release workflow
git checkout -b release/1.2.0 develop
# ... bump version, fix bugs ...
git checkout main && git merge --no-ff release/1.2.0
git tag -a v1.2.0 -m "Release 1.2.0"
git checkout develop && git merge --no-ff release/1.2.0
```

### 🚀 2. GitHub Flow (Simplified)
Best for: continuous deployment, web apps
```
main        — always deployable
feature/*   — branch from main, PR back to main
```
```bash
git checkout -b feature/add-search
# ... work, commit ...
git push -u origin feature/add-search
# Open Pull Request on GitHub
# Code review → merge → deploy
git branch -d feature/add-search
```

### 🦊 3. GitLab Flow
Best for: environment-based deployments
```
main        → staging → production
feature/*   → main (via MR)
```

### 🏢 4. Trunk-Based Development
Best for: large teams, CI/CD, feature flags
```
main (trunk) — everyone commits here frequently
feature/*    — very short-lived (< 1 day), or commit directly to main
```

### 📋 Pull Request / Merge Request Best Practices
```
✅ Keep PRs small and focused (< 400 lines changed)
✅ Write descriptive PR titles and descriptions
✅ Link to issue/ticket number
✅ Request specific reviewers
✅ Respond to review comments promptly
✅ Squash commits before merging for clean history
✅ Delete branch after merge
❌ Don't merge your own PRs without review
❌ Don't let PRs sit open for days
```

### 🔒 Branch Protection Rules (GitHub)
```
Settings → Branches → Add rule:
- Require pull request reviews before merging
- Require status checks to pass (CI)
- Require branches to be up to date
- Restrict who can push to matching branches
- Require signed commits
```

### 📝 Commit Message Convention (Conventional Commits)
```
<type>(<scope>): <short description>

Types:
feat     — new feature
fix      — bug fix
docs     — documentation only
style    — formatting, no logic change
refactor — code restructure, no feature/fix
test     — adding/updating tests
chore    — build process, dependencies
perf     — performance improvement
ci       — CI/CD changes

Examples:
feat(auth): add JWT token refresh
fix(api): handle null response from payment gateway
docs(readme): update installation steps
refactor(db): extract query builder to separate class
```

---

## 11. GitHub Features

### 🐙 GitHub Issues
```
- Track bugs, features, tasks
- Use labels: bug, enhancement, documentation, help wanted
- Assign to team members
- Link to PRs: "Closes #42" in PR description auto-closes issue on merge
- Use milestones to group issues for a release
```

### 🔄 GitHub Actions (CI/CD)
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

### 📋 GitHub Projects
```
- Kanban-style project boards
- Link issues and PRs to project cards
- Automate card movement with workflows
- Track progress across repositories
```

### 🔍 GitHub Code Search
```bash
# Search syntax on github.com:
repo:user/repo "search term"      # search in specific repo
language:python "def train"       # filter by language
path:src/ "import torch"          # search in specific path
is:open is:issue label:bug        # filter issues
```

### 🤖 GitHub Copilot & AI Features
```
- GitHub Copilot: AI pair programmer (code suggestions)
- Copilot Chat: ask questions about code
- Copilot for PRs: auto-generate PR descriptions
- GitHub Spark: AI-powered micro apps
```

### 🔐 GitHub Security Features
```
- Dependabot: automated dependency updates + security alerts
- Secret scanning: detects accidentally committed secrets
- Code scanning: static analysis with CodeQL
- Security advisories: private vulnerability reporting
- CODEOWNERS file: auto-assign reviewers by file path
```

### 📁 CODEOWNERS File
```bash
# .github/CODEOWNERS
# Format: pattern  @owner

*                   @default-team        # all files
*.py                @python-team
/docs/              @docs-team
/src/auth/          @security-team @lead-dev
```

### 🌐 GitHub Pages
```bash
# Deploy static site from repo
# Settings → Pages → Source: Deploy from branch
# Or use GitHub Actions for custom build

# Jekyll (default) or any static site generator
# URL: https://username.github.io/repo-name
```

### 📊 GitHub Insights
```
- Pulse: activity summary (PRs, issues, commits)
- Contributors: commit activity per contributor
- Traffic: views and clones of your repo
- Dependency graph: visualize dependencies
- Network graph: visualize fork relationships
```

---

## 12. Authentication Methods

### 🔑 1. SSH Keys (Recommended)
```bash
# Generate SSH key pair
ssh-keygen -t ed25519 -C "you@example.com"
# or for older systems:
ssh-keygen -t rsa -b 4096 -C "you@example.com"

# Start SSH agent and add key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key to clipboard (macOS)
pbcopy < ~/.ssh/id_ed25519.pub

# Add to GitHub: Settings → SSH and GPG keys → New SSH key

# Test connection
ssh -T git@github.com
# Expected: "Hi username! You've successfully authenticated..."

# Use SSH URL for cloning
git clone git@github.com:user/repo.git
```

### 🔐 2. Personal Access Tokens (HTTPS)
```bash
# GitHub → Settings → Developer settings → Personal access tokens
# Generate token with required scopes (repo, workflow, etc.)

# Use token as password when prompted, or embed in URL:
git clone https://TOKEN@github.com/user/repo.git

# Store credentials (so you don't type every time)
git config --global credential.helper store        # stores in plaintext
git config --global credential.helper cache        # caches in memory (15 min)
git config --global credential.helper osxkeychain  # macOS Keychain (recommended)
```

### 🔒 3. GPG Commit Signing
```bash
# Generate GPG key
gpg --full-generate-key

# List keys
gpg --list-secret-keys --keyid-format=long

# Configure git to use GPG key
git config --global user.signingkey YOUR_KEY_ID
git config --global commit.gpgsign true    # sign all commits automatically

# Sign a commit manually
git commit -S -m "signed commit"

# Verify signatures
git log --show-signature

# Export public key to add to GitHub
gpg --armor --export YOUR_KEY_ID
# GitHub → Settings → SSH and GPG keys → New GPG key
```

### 🏢 4. GitHub CLI Authentication
```bash
# Install GitHub CLI
brew install gh

# Authenticate
gh auth login
# Follow prompts: GitHub.com → HTTPS or SSH → browser or token

# Check auth status
gh auth status

# Refresh token
gh auth refresh
```

### 🔄 Switching Between SSH and HTTPS
```bash
# Check current remote URL
git remote -v

# Switch from HTTPS to SSH
git remote set-url origin git@github.com:user/repo.git

# Switch from SSH to HTTPS
git remote set-url origin https://github.com/user/repo.git
```

### 🗝️ Multiple SSH Keys (Multiple GitHub Accounts)
```bash
# ~/.ssh/config
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal

Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work

# Use in remote URL:
git remote add origin git@github-personal:user/repo.git
git remote add origin git@github-work:company/repo.git
```

---

## 13. Advanced Git

### 🔍 git bisect — Binary Search for Bugs
```bash
git bisect start
git bisect bad                    # current commit is bad
git bisect good v1.0.0            # last known good commit
# Git checks out middle commit — test it, then:
git bisect good                   # if this commit is good
git bisect bad                    # if this commit is bad
# Repeat until git finds the first bad commit
git bisect reset                  # end bisect session

# Automate with a test script
git bisect run python test.py     # runs script; exit 0=good, exit 1=bad
```

### 📦 Git Submodules
```bash
# Add a submodule
git submodule add git@github.com:user/lib.git libs/mylib
git commit -m "Add mylib submodule"

# Clone repo with submodules
git clone --recurse-submodules git@github.com:user/repo.git
# or after cloning:
git submodule update --init --recursive

# Update submodules to latest
git submodule update --remote

# Remove a submodule
git submodule deinit libs/mylib
git rm libs/mylib
rm -rf .git/modules/libs/mylib
```

### 🌲 Git Worktrees
Work on multiple branches simultaneously without stashing.
```bash
git worktree add ../hotfix-branch hotfix/critical-bug
git worktree list
git worktree remove ../hotfix-branch
```

### 🔧 git filter-repo (Rewrite History)
```bash
# Install: pip install git-filter-repo

# Remove a file from ALL history (e.g., accidentally committed secret)
git filter-repo --path secrets.env --invert-paths

# Rename a file throughout history
git filter-repo --path-rename old-name.py:new-name.py

# Remove sensitive string from all commits
git filter-repo --replace-text <(echo "password123==>REDACTED")
```

### 📊 git notes
```bash
git notes add -m "Code reviewed by team" abc123   # add note to commit
git notes show abc123                              # show notes
git push origin refs/notes/commits                 # push notes to remote
```

### 🔗 Useful Advanced Commands
```bash
# Find which branch contains a commit
git branch --contains abc123
git branch -r --contains abc123   # remote branches

# Show commits reachable from one branch but not another
git log main..feature             # commits in feature not in main
git log feature..main             # commits in main not in feature

# Show common ancestor of two branches
git merge-base main feature

# Archive repo as zip/tar
git archive --format=zip HEAD > repo.zip
git archive --format=tar.gz HEAD > repo.tar.gz

# Count commits
git rev-list --count HEAD
git rev-list --count main..feature

# Show file at specific commit
git show abc123:path/to/file.py

# Apply a patch file
git apply patch.diff
git am patch.patch                # apply mailbox-format patch (preserves author)
```

### 🏎️ Performance & Large Repos
```bash
git config --global core.preloadindex true    # parallel index operations
git config --global core.fscache true         # cache filesystem calls (Windows)
git config --global gc.auto 256               # run gc less frequently

# Shallow clone (faster, less history)
git clone --depth 1 git@github.com:user/repo.git
git clone --depth 10 --branch main git@github.com:user/repo.git

# Partial clone (skip large blobs)
git clone --filter=blob:none git@github.com:user/repo.git
```

---

## 14. Troubleshooting

### ❌ "Your branch is ahead of 'origin/main' by N commits"
```bash
git push                          # just push your commits
# or if you want to discard local commits:
git reset --hard origin/main
```

### ❌ "Your branch is behind 'origin/main'"
```bash
git pull                          # fetch + merge remote changes
git pull --rebase                 # fetch + rebase (cleaner history)
```

### ❌ "Merge conflict" during pull/merge
```bash
git status                        # see conflicted files
# Edit files, resolve conflict markers
git add resolved-file.py
git commit                        # or git rebase --continue
```

### ❌ "Detached HEAD state"
```bash
# You checked out a commit/tag directly, not a branch
git checkout main                 # go back to a branch
# or create a branch from current detached state:
git checkout -b new-branch-name
```

### ❌ Accidentally committed to wrong branch
```bash
# Move last commit to correct branch
git log --oneline -1              # note the commit SHA
git checkout correct-branch
git cherry-pick abc123            # apply commit here
git checkout wrong-branch
git reset --hard HEAD~1           # remove from wrong branch
```

### ❌ Accidentally committed a secret/password
```bash
# Remove from history (before pushing):
git reset --soft HEAD~1           # undo commit, keep changes staged
# Remove the secret from the file
git add .
git commit -m "Add feature without secret"

# If already pushed — use git filter-repo:
pip install git-filter-repo
git filter-repo --path secrets.env --invert-paths
git push --force-with-lease

# ALSO: immediately rotate/revoke the exposed secret!
```

### ❌ "Permission denied (publickey)"
```bash
# SSH key not added to agent or GitHub
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh -T git@github.com             # test connection
# If still failing: re-add public key to GitHub Settings
```

### ❌ "fatal: refusing to merge unrelated histories"
```bash
# Happens when two repos have no common ancestor
git pull origin main --allow-unrelated-histories
```

### ❌ Lost commits after reset --hard
```bash
git reflog                        # find the lost commit SHA
git checkout -b recovery-branch abc123  # recover it
# or:
git reset --hard abc123           # go back to that state
```

### ❌ Large file accidentally committed (repo too big)
```bash
# Find large files
git rev-list --objects --all | sort -k 2 > allfileshas.txt
git gc && git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -10

# Remove with filter-repo
git filter-repo --path large-file.zip --invert-paths
```

### ❌ "Updates were rejected because the tip of your current branch is behind"
```bash
# Option 1: Pull first, then push
git pull --rebase
git push

# Option 2: Force push (only if you're sure — rewrites remote history)
git push --force-with-lease
```

### ❌ Wrong commit message already pushed
```bash
git revert HEAD                   # safest: create a new "undo" commit
# or for minor typos in last commit (if only you use the branch):
git commit --amend -m "Correct message"
git push --force-with-lease
```

---

## 15. Quick Reference Cheatsheet

### 🚀 Setup
```bash
git init                          # initialize repo
git clone <url>                   # clone remote repo
git clone --depth 1 <url>         # shallow clone
```

### 📸 Daily Workflow
```bash
git status                        # check status
git add .                         # stage all
git add -p                        # stage interactively
git commit -m "message"           # commit
git commit --amend                # fix last commit
git push                          # push to remote
git pull                          # pull from remote
git pull --rebase                 # pull with rebase
```

### 🌿 Branching
```bash
git branch                        # list branches
git switch -c feature/name        # create + switch
git switch main                   # switch branch
git merge feature/name            # merge branch
git branch -d feature/name        # delete branch
git push origin --delete feature  # delete remote branch
```

### ↩️ Undoing
```bash
git restore file.py               # discard changes
git restore --staged file.py      # unstage
git reset --soft HEAD~1           # undo commit (keep staged)
git reset --hard HEAD~1           # undo commit (discard) ⚠️
git revert HEAD                   # safe undo (new commit)
git reflog                        # find lost commits
```

### 🔀 Remote
```bash
git remote -v                     # list remotes
git remote add origin <url>       # add remote
git fetch --prune                 # fetch + clean
git push -u origin branch         # push + track
git push --force-with-lease       # safe force push
```

### 🏷️ Tags
```bash
git tag -a v1.0.0 -m "msg"        # annotated tag
git push origin --tags            # push all tags
git tag -d v1.0.0                 # delete local tag
git push origin --delete v1.0.0   # delete remote tag
```

### 📦 Stash
```bash
git stash push -m "WIP"           # stash with name
git stash list                    # list stashes
git stash pop                     # apply + remove
git stash drop stash@{0}          # delete stash
```

### 🔍 Inspection
```bash
git log --oneline --graph --all   # visual log
git log --author="Name"           # filter by author
git diff --staged                 # staged changes
git blame file.py                 # who changed what
git bisect start                  # start bug hunt
git grep "pattern"                # search codebase
```

### 🍒 Cherry-pick & Rebase
```bash
git cherry-pick abc123            # apply specific commit
git rebase main                   # rebase onto main
git rebase -i HEAD~3              # interactive rebase
git rebase --abort                # abort rebase
```

### ⚙️ Config
```bash
git config --global user.name "Name"
git config --global user.email "email"
git config --global alias.lg "log --oneline --graph --all"
git config --list                 # show all config
```

### 🔑 SSH Quick Setup
```bash
ssh-keygen -t ed25519 -C "email"  # generate key
eval "$(ssh-agent -s)"            # start agent
ssh-add ~/.ssh/id_ed25519         # add key
ssh -T git@github.com             # test connection
```

### ⚠️ Common Mistakes to Avoid
```
❌ git clone inside an existing repo → creates nested folder
   ✅ Use: git pull (to update existing repo)

❌ git push --force on shared branches → breaks teammates
   ✅ Use: git push --force-with-lease

❌ git reset --hard on pushed commits → rewrites shared history
   ✅ Use: git revert (creates safe undo commit)

❌ Committing secrets/passwords → security risk
   ✅ Use: .gitignore + environment variables

❌ Working directly on main → risky
   ✅ Use: feature branches + pull requests
```

---
*End of Notes*
