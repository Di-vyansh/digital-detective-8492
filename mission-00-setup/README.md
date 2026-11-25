# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The primary objective of Mission 0 was to construct a disciplined, well-structured software repository for the Digital Detective investigation. This required confirming the local runtime environment (verifying Python 3 and Git installations), establishing the project workspace according to the required naming pattern (`digital-detective-` followed by the last four digits of my USN: `8492`), scaffolding the mission directory hierarchy, authoring the master root README with clean markdown links, and establishing remote tracking with GitHub.

## 2. Work completed
- Verified the local macOS terminal environment, confirming operational installations of Python 3 (`Python 3.14.7`) and Git (`git version 2.54.0`).
- Generated the primary project root repository folder named `digital-detective-8492`.
- Scaffolding the full suite of modular mission directories and documentation files:
  - `mission-00-setup/README.md`
  - `mission-01-computer-basics/README.md`
  - `mission-02-terminal/README.md`
  - `mission-03-operating-system/README.md`
  - `mission-04-programs/README.md`
  - `mission-05-numbers-data/README.md`
  - `mission-06-git-github/README.md`
  - `mission-07-networking/README.md`
  - `mission-08-final-report/README.md`
  - `evidence/`
- Authored the root `README.md` providing clear student identification, technical scope, and navigation index.
- Initialized local Git source control on the `main` branch and linked the remote repository: `https://github.com/Di-vyansh/digital-detective-8492`.

## 3. Commands / tools used
- `python3 --version` — Verified the installed Python runtime (`Python 3.14.7`).
- `git --version` — Confirmed the active Git build (`git version 2.54.0 (Apple Git-157)`).
- `mkdir -p` — Generated the mission folder structure recursively.
- `touch` — Created empty initial markdown files across all subdirectories.
- `git init -b main` — Initialized the local repository using `main` as the default branch.
- `git config user.name "Divyansh Pal"` — Configured commit author name.
- `git config user.email "Di-vyansh@users.noreply.github.com"` — Set associated GitHub author email.
- `git status` — Audited tracked and untracked files in the working directory.
- `git add .` — Staged initial repository files to the index.
- `git commit -m "Set up Digital Detective mission structure"` — Committed the baseline snapshot.

## 4. My understanding
Establishing an organized repository structure before writing code or documentation is fundamental to software engineering. Separating distinct phases of work into isolated subdirectories (`mission-00` through `mission-08`) prevents clutter, preserves logical separation of concerns, and simplifies future code review.

Furthermore, leveraging Git from the very first step ensures every modification is versioned, auditable, and easily restorable if an error occurs. A standardized `README.md` at both the root and within each module creates a navigable hierarchy for assessors and collaborators.

## 5. Difficulties faced
Initially, when authoring relative links inside the root `README.md`, testing the markdown preview revealed that relative link targets must use exact forward slashes and correct case-sensitive folder names (`./mission-01-computer-basics/README.md`) to resolve properly on Unix-based GitHub web interfaces.

## 6. How I resolved them
I audited all relative markdown link paths across the root `README.md`, tested each link using an in-editor markdown previewer, and verified that every link accurately routes to the corresponding mission documentation file without 404 broken path errors.

## 7. Evidence / files
- Root repository folder structure:
  ```
  digital-detective-8492/
  ├── README.md
  ├── evidence/
  ├── mission-00-setup/README.md
  ├── mission-01-computer-basics/README.md
  ├── mission-02-terminal/README.md
  ├── mission-03-operating-system/README.md
  ├── mission-04-programs/README.md
  ├── mission-05-numbers-data/README.md
  ├── mission-06-git-github/README.md
  ├── mission-07-networking/README.md
  └── mission-08-final-report/README.md
  ```
- Environment verification outputs:
  - Python runtime: `Python 3.14.7`
  - Git version: `git version 2.54.0 (Apple Git-157)`
  - Kernel: `Darwin 27.2.0 (macOS arm64)`

## 8. Commit details
- Commit message: `Set up Digital Detective mission structure`
- Branch: `main`
