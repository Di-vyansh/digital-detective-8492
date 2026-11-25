# Mission 3 — Understand the operating system

## 1. Task / objective
The goal of Mission 3 was to analyze the operating system running on my machine (macOS). This involved investigating system identity, active user privileges, disk storage utilization, process lifecycle management, Process IDs (PIDs), Unix filesystem paths (absolute versus relative), file security permissions (`rwx`), and summarizing the foundational responsibilities of modern operating systems.

## 2. Work completed

### Task 3.1 — Explore your operating system

| Operating System Metric | What it reveals about the system | Actual Observation on my Machine (Privacy-Safe) |
| :--- | :--- | :--- |
| **Operating System & Kernel** | The platform name, release version, and underlying kernel architecture. | macOS Darwin Kernel Version 27.2.0 (ARM64 Apple Silicon) |
| **Active User Account** | The username of the currently authenticated shell session. | `divyansh` (audited using `whoami`) |
| **Primary Disk Storage Space** | Total, used, and available capacity on the root storage partition. | Root partition (`/`) reports over 100 GB available under APFS container architecture (`df -h /`). |
| **Active Process Supervision** | The collection of programs currently scheduled by the OS. | Monitored running user and daemon processes using `ps -ef` and `top`. |

---

### Task 3.2 — Understand processes
A **process** is an active, running instance of a computer program that has been loaded into memory with its own dedicated memory address space, execution state, and system resources.

- **Process ID (PID)**:
  - Every process is assigned a unique numerical integer identifier known as a **PID** (Process ID) by the operating system kernel when created.
  - The operating system uses PIDs to track, schedule CPU time for, assign memory to, and enforce security policies on every running application.
  - When inspecting processes via `ps -ef | head -n 10`, each row reveals:
    - `UID`: User ID owning the process.
    - `PID`: Process ID.
    - `PPID`: Parent Process ID (the process that spawned it).
    - `TIME`: Cumulative CPU execution time consumed.
    - `CMD`: Binary path and arguments being executed.
- **Why is PID tracking critical?**  
  If a background program freezes or enters an infinite loop, administrators can terminate only that specific runaway process using its unique PID (e.g. `kill -9 <PID>`) without destabilizing the rest of the operating system.

---

### Task 3.3 — Understand paths and permissions

#### Absolute vs Relative Paths

- **Absolute Path**:
  - The complete, unambiguous location of a file or directory starting from the root of the file system (`/`).
  - It remains valid regardless of the shell's current working directory.
  - *Example from my machine*:  
    `/Users/divyansh/Desktop/digital-detective-8492/mission-03-operating-system/README.md`
- **Relative Path**:
  - A location specified in relation to the shell's current working directory.
  - Uses `.` to denote the current directory and `..` to reference the parent directory.
  - *Example from the repository root*:  
    `./mission-03-operating-system/README.md`

#### File Permissions
Unix-based systems enforce access control on files and directories using a 10-character notation divided into four distinct components:

| Permission String | File Type | Owner Permissions (`u`) | Group Permissions (`g`) | Others Permissions (`o`) | Meaning |
| :---: | :---: | :---: | :---: | :---: | :--- |
| `-rw-r--r--` | File (`-`) | `rw-` (Read + Write) | `r--` (Read only) | `r--` (Read only) | Standard documentation or source code file. |
| `drwxr-xr-x` | Directory (`d`) | `rwx` (Read + Write + Execute) | `r-x` (Read + Execute) | `r-x` (Read + Execute) | Standard directory permitting traversal. |

- **`r` (Read)**: Permits viewing or opening the file contents (or listing directory contents).
- **`w` (Write)**: Permits modifying, editing, or truncating file contents (or creating/deleting files inside a directory).
- **`x` (Execute)**: Permits executing the file as a compiled binary or shell script (or entering/traversing a directory).
- **Modifying Permissions**: Controlled via the `chmod` command (e.g. `chmod 755 script.sh` or `chmod +x hello.py`).

---

### Task 3.4 — Explain operating-system responsibilities
The operating system serves as the foundational software layer mediating between physical hardware and application software. Its five core responsibilities are:

1. **Process Management & Scheduling**: Allocates CPU clock cycles fairly across competing threads, handling context switching, process prioritization, creation, and termination.
2. **Memory Management**: Coordinates virtual and physical RAM, allocating isolated address spaces to individual applications and preventing memory corruption or unauthorized cross-process snooping.
3. **File System Management**: Organizes binary blocks on physical SSDs into logical files and directories, tracking metadata, timestamps, fragmentation, and access permissions.
4. **Device & I/O Abstraction**: Provides standardized device drivers so applications can interact with displays, audio controllers, keyboards, and network cards through consistent software APIs without needing custom hardware-level code.
5. **Security & Protection**: Enforces user authentication, process isolation, access control lists (ACLs), and firewall boundaries to safeguard sensitive system data from unauthorized access or malware.

---

## 3. Commands / tools used
- `uname -v`, `whoami`
- `df -h /` (inspected available storage)
- `ps -ef | head -n 10` (audited running processes and PIDs)
- `ls -l` (inspected Unix file permission strings)

## 4. My understanding
The operating system acts as the master conductor of the computer. Without an OS, every software application would need to incorporate its own low-level hardware drivers for every manufacturer's SSD, graphics chip, and Wi-Fi card.

Understanding permissions (`rwx`) clarifies how Unix-based operating systems like macOS enforce security at the file-system level, preventing ordinary applications or network services from overwriting critical kernel binaries.

## 5. Difficulties faced
Distinguishing between how the kernel interprets the execute (`x`) permission on a regular file (allowing program execution) versus on a directory (allowing the user to `cd` into and traverse the directory) was initially confusing.

## 6. How I resolved them
I tested this directly in the terminal: removing the `x` permission from a test directory caused `cd` to return a `Permission denied` error even though the directory had read (`r`) permissions, proving that directory entry requires execute permission.

## 7. Evidence / files
- `mission-03-operating-system/README.md`
- Documentation tables auditing system metrics, process structures, path types, and permission models.

## 8. Commit details
- Commit message: `Document operating system and file management`
- Branch: `main`
