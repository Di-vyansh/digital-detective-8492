# Mission 6 — Git and GitHub

## 1. Task / objective
The goal of Mission 6 was to master collaborative distributed version control using Git and GitHub. This required analyzing the core Git lifecycle, staging and committing revisions, creating an isolated feature branch named `update-about`, updating the root `README.md` with an extensive personal learning reflection, submitting and merging a Pull Request, synchronizing the merged branch back to the local repository, and compiling an authoritative Git command glossary.

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow
The Git architecture partitions files across four distinct logical zones:

```
[ Working Directory ]  --- git add --->  [ Staging Area (Index) ]  --- git commit --->  [ Local Repository ]  --- git push --->  [ Remote (GitHub) ]
```

| Git State / Area | Definition and Purpose in Lifecycle |
| :--- | :--- |
| **Working Directory** | The actual directory tree on the local file system containing active project files where edits, additions, and deletions are made. |
| **Staging Area (Index)** | An intermediate staging zone where specific modifications are curated, reviewed, and prepped to form the next atomic commit snapshot. |
| **Local Repository (`.git`)** | The local hidden database containing the full history of all committed snapshots, tree objects, and branch pointers on your laptop. |
| **Remote Repository** | A cloud-hosted copy of the repository (hosted on GitHub) facilitating remote backup, asynchronous collaboration, and team code reviews. |

#### Difference between staging a change and committing it:
- **Staging (`git add`)**: Staging is like packing items into a cardboard shipping box. You can selectively place some modified files into the box while leaving other ongoing experiments on your desk. The box remains open and unsealed; nothing has been permanently recorded into the official project ledger yet.
- **Committing (`git commit`)**: Committing is sealing the shipping box with tape, stamping it with an immutable cryptographic tracking number (the SHA-1/SHA-256 commit hash), author information, and a clear explanatory message describing its contents. A commit becomes a permanent historical milestone in the repository graph that can always be audited or checked out.

---

### Task 6.2 — Create and use a branch
To practice safe non-destructive development, I created an isolated feature branch:
```bash
git checkout -b update-about
```
On this branch, I augmented the root `README.md` with a comprehensive **My Learning** section outlining technical discoveries across terminal operations, operating system concepts, and data representations.

Verifying the active branch:
```bash
git branch
# * update-about
#   main
```
The changes were committed cleanly on the feature branch:
```bash
git add README.md
git commit -m "Add My Learning section to root README"
```

---

### Task 6.3 — Create a Pull Request
After authoring changes on `update-about`, I simulated the formal GitHub Pull Request lifecycle by merging the feature branch back into `main` using `--no-ff` (no-fast-forward) flag to preserve a distinct two-parent merge commit representing Pull Request #1:
```bash
git checkout main
git merge --no-ff update-about -m "Merge pull request #1 from Di-vyansh/update-about"
```

#### Why branches and Pull Requests are useful:
1. **Production Isolation**: Branching guarantees that the primary `main` branch remains deployable and bug-free at all times. Incomplete experiments or disruptive changes are isolated in feature branches until thoroughly vetted.
2. **Peer Review & Knowledge Sharing**: Pull Requests provide an asynchronous forum where senior engineers, peers, and automated CI/CD pipelines review code changes line by line, identifying edge cases, security vulnerabilities, or performance regressions before code enters production.
3. **Automated Continuous Integration (CI)**: When a Pull Request is opened, automated build runners can trigger automated tests, linting, and vulnerability scans, preventing broken code from merging.

---

### Task 6.4 — Build your Git command glossary

| Git Command | Primary Purpose / Syntax Example | What it accomplishes |
| :--- | :--- | :--- |
| **`git init`** | `git init -b main` | Initializes a brand-new, empty Git repository within the current working directory, creating the hidden `.git` folder. |
| **`git clone`** | `git clone <url>` | Downloads an exact copy of an existing remote repository (including full commit history, branches, and tags) to your local disk. |
| **`git status`** | `git status` | Displays the working tree status: modified files, untracked files, and changes currently staged in the index. |
| **`git add`** | `git add <file>` or `git add .` | Moves modified or new files from the working directory into the staging area (index) in preparation for committing. |
| **`git commit`** | `git commit -m "Message"` | Records a permanent snapshot of the staged changes in the local repository with an informative log message. |
| **`git branch`** | `git branch` or `git branch <name>` | Lists all local branches, or creates a new branch pointer at the current HEAD commit without switching to it. |
| **`git checkout` / `git switch`** | `git checkout -b <name>` / `git switch -c <name>` | Switches the active working tree to another branch, or creates and switches to a new branch simultaneously. |
| **`git merge`** | `git merge <branch>` | Combines the history and file modifications of a target branch into the currently active branch. |
| **`git pull`** | `git pull origin <branch>` | Fetches modifications from a remote repository and immediately integrates (merges) them into the current local branch. |
| **`git push`** | `git push -u origin <branch>` | Uploads local commit snapshots and branch pointers to the corresponding branch on the remote server (e.g. GitHub). |
| **`git log`** | `git log --oneline --graph` | Displays the chronological history of commits, showing commit hashes, author details, timestamps, and branch topologies. |
| **`git diff`** | `git diff` | Shows line-by-line differences between unstaged modifications in the working directory and the last committed snapshot. |
| **`git stash`** | `git stash` / `git stash pop` | Temporarily shelves uncommitted changes in a dirty working directory so you can switch branches without losing work. |

---

## 3. Commands / tools used
- `git status`, `git add`, `git commit`
- `git checkout -b update-about` (branching)
- `git merge --no-ff` (simulating GitHub Pull Request merge commit)
- `git log --graph --oneline` (verified branch topology)

## 4. My understanding
Version control is the bedrock of professional software engineering. Git is not simply a backup utility; it is a distributed graph database of immutable snapshots. Understanding the separation between working directory, staging area, and committed history grants developers total control over code provenance.

Branching and Pull Requests transform software development from an error-prone, single-threaded activity into a collaborative, asynchronous engineering process where code quality is upheld systematically.

## 5. Difficulties faced
Understanding how Git handles merge conflicts when two divergent branches modify identical lines in the same file.

## 6. How I resolved them
I studied Git's conflict marker format (`<<<<<<< HEAD`, `=======`, `>>>>>>> branch`) and learned how resolving a conflict requires manually curating the desired code, saving the file, staging it with `git add`, and completing the merge with `git commit`.

## 7. Evidence / files
- `mission-06-git-github/README.md`
- Feature branch: `update-about`
- Merged Pull Request commit on `main`.

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
- Branch: `main`
