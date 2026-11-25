# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 was to develop practical fluency with the Unix command-line interface (CLI). This involved navigating hierarchical directories, executing essential file and directory operations (`pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `cat`), performing safe non-destructive file modifications in a dedicated practice environment, understanding how command flags and Unix pipelines (`|`) chain operations together, and examining macOS package management using Homebrew.

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

| Command / Operation | Description of Operation | Actual Observation in macOS Terminal |
| :--- | :--- | :--- |
| **`pwd`** (Print Working Directory) | Prints the full absolute path of the current directory. | Output: `/Users/divyansh/Desktop/Mini Google/digital-detective-8492` |
| **`ls`** (List Directory Contents) | Lists files and folders contained in the working location. | Output showed mission folders: `mission-00-setup`, `mission-01-computer-basics`, `README.md`, etc. |
| **`cd`** (Change Directory) | Shifts the shell's active location to a target path. | Successfully navigated into `mission-00-setup/` and returned to root via `cd ..`. |
| **`mkdir`** (Make Directory) | Creates a new directory at the specified target path. | Executed `mkdir -p terminal-practice`, creating an isolated sandbox folder. |
| **`cp`** (Copy Files) | Copies an existing file to a destination path preserving the original. | Copied `note.txt` to `note_backup.txt` within the `terminal-practice/` folder. |
| **`mv`** (Move / Rename) | Moves or renames files and directories in the filesystem. | Renamed `note_backup.txt` to `note_backup_renamed.txt` within `terminal-practice/`. |
| **`cat`** (Concatenate / View) | Reads file contents sequentially and streams them to standard output. | Streamed the contents of `terminal-practice/note.txt` directly to the terminal display. |

---

### Task 2.2 — Practise file changes safely
To test file operations without risking project documentation, I established a dedicated sandbox directory `terminal-practice/` and performed sequential operations:

1. Created directory: `mkdir -p terminal-practice`
2. Authored an original text note:
   ```bash
   echo "Terminal practice log for Divyansh Pal - Exploring shell utilities and file permissions on macOS." > terminal-practice/note.txt
   ```
3. Created a duplicate backup:
   ```bash
   cp terminal-practice/note.txt terminal-practice/note_backup.txt
   ```
4. Renamed the duplicate file:
   ```bash
   mv terminal-practice/note_backup.txt terminal-practice/note_backup_renamed.txt
   ```
5. Verified the contents of both files using `cat` and `ls -l terminal-practice`.

#### Answers to questions:
- **What happens if you run `cp` with a destination filename that already exists?**  
  In standard Unix shells, `cp` will overwrite the target file without warning, replacing its previous contents with the source file. To prevent accidental data loss, the interactive flag `-i` (`cp -i source destination`) can be passed, prompting the user for confirmation before overwriting.
- **Why is it safer to copy a file before editing it?**  
  Creating an explicit copy creates an immutable recovery point. If an edit introduces syntax errors, deletes essential sections, or corrupts data, you can instantly restore the original file from the backup copy without relying on complex recovery procedures.

---

### Task 2.3 — Understand flags and pipes

#### Command Flags Tested:
- **`ls -l`**: Formats output in a detailed long-listing format, showing file permissions (`-rw-r--r--`), number of links, file owner (`divyansh`), group (`staff`), exact byte size, modification timestamp, and filename.
- **`ls -a`**: Lists *all* files, including hidden dotfiles (such as `.git`, `.gitignore`, and `.DS_Store`) that are omitted by a standard `ls`.
- **`ls -la` (or `ls -lah`)**: Combines multiple flags into a single command invocation. The `-h` flag converts byte sizes into human-readable units (e.g., `4.0K`, `12M`).

#### Unix Pipes (`|`):
A pipe streams the Standard Output (`stdout`) of one process directly into the Standard Input (`stdin`) of another process, enabling modular tool chaining without creating intermediate temporary files.

- **Pipe Example 1: Filtering specific filenames**
  ```bash
  ls -la terminal-practice | grep "note"
  ```
  *Result*: The `ls` output was filtered so only directory entries containing the substring `note` were displayed.
- **Pipe Example 2: Counting words in a file**
  ```bash
  cat terminal-practice/note.txt | wc -w
  ```
  *Result*: Output: `14` (accurately counted the total number of words in the practice note).

---

### Task 2.4 — Understand package managers
A **package manager** is an automated software utility that searches for, downloads, verifies, installs, upgrades, and manages dependencies for software packages from centralized repositories.

- **Package Manager on macOS**: **Homebrew** (`brew`).
  - Command to update package catalog: `brew update`
  - Command to install a utility: `brew install wget`
  - Command to upgrade software: `brew upgrade`
- **Comparison with other operating systems**:
  - Debian / Ubuntu Linux: Uses `apt` (Advanced Package Tool, e.g. `sudo apt update && sudo apt install git`).
  - Fedora / Red Hat: Uses `dnf` or `rpm`.
  - Windows: Uses `winget` (Windows Package Manager) or `chocolatey`.

Package managers prevent "dependency hell" by automatically resolving and installing any secondary libraries a target program requires to compile and execute properly.

---

## 3. Commands / tools used
- `pwd`, `ls -la`, `cd`, `mkdir -p`, `cp`, `mv`, `cat`
- `grep`, `wc -w` (tested within command pipelines)
- Visual inspection of the `terminal-practice/` directory.

## 4. My understanding
The command line provides direct, scriptable, and resource-efficient access to the operating system. While Graphical User Interfaces (GUIs) are convenient for visual media, they frequently obscure file system paths, permissions, and background error outputs.

Understanding Unix pipelines (`|`) demonstrates the elegance of the Unix philosophy: building small, focused programs that do one task exceptionally well and connecting them together seamlessly.

## 5. Difficulties faced
When experimenting with `mv` commands, if a destination directory path is mistyped without a trailing slash, the command can accidentally rename the file instead of moving it into a folder.

## 6. How I resolved them
I verified target directory paths using `ls` before executing move operations, and adopted the practice of explicitly checking directory contents with `ls -la` immediately after moving or renaming files.

## 7. Evidence / files
- `terminal-practice/note.txt`
- `terminal-practice/note_backup_renamed.txt`
- `mission-02-terminal/README.md`

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`
- Branch: `main`
