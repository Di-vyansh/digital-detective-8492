# Digital Detective — Explore Your Computer • Build a Mini System Report

## Independent Learning & Computer Systems Assignment

### Student Information
- **Name**: Divyansh Pal
- **USN**: 2402608492 (USN ending: 8492)
- **Campus / Institution**: S-VYASA University
- **GitHub Username**: [Di-vyansh](https://github.com/Di-vyansh)
- **Repository Name**: digital-detective-8492
- **GitHub Repository URL**: [https://github.com/Di-vyansh/digital-detective-8492](https://github.com/Di-vyansh/digital-detective-8492)

---

### Project Overview
The **Digital Detective** project is a comprehensive practical investigation into the inner workings of modern computer architecture, operating systems, terminal environments, and networking fundamentals. Across 9 structured missions, I conducted hands-on investigations on my personal computer to inspect low-level hardware abstractions, file systems, process lifecycles, execution models, number representations, distributed version control workflows, and network protocols.

> **Development Workflow**: Following strict software engineering discipline, each mission was researched, documented in its dedicated folder, validated against actual system behavior, and committed incrementally into Git before moving to subsequent stages.

---

### Topics Explored
1. **Repository Setup**: Initializing the Unix development environment, verifying Python 3 and Git toolchains, structuring standardized documentation schemas, and linking to GitHub.
2. **Computer Fundamentals & IPOS Model**: Analyzing the Input, Processing, Output, and Storage cycle, categorizing hardware peripherals versus system software, and evaluating real-world embedded computer systems.
3. **Terminal Operations**: Navigating hierarchical Unix directory structures, executing atomic file manipulations (`pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `cat`), utilizing command arguments, constructing Unix pipelines (`|`), and inspecting package management architectures.
4. **Operating Systems Architecture**: Inspecting kernel telemetry, process scheduling, PID allocation, file system permissions (`rwxr-xr-x`), path resolutions (absolute vs. relative), and core OS subsystem responsibilities.
5. **How Programs Run**: Writing and executing Python scripts, analyzing the language execution pipeline, and contrasting compiled native binaries against bytecode-interpreted languages.
6. **Numbers and Data Representation**: Performing manual and algorithmic number system conversions (Decimal, Binary, Hexadecimal), developing a robust CLI conversion utility, and examining text encoding standards (ASCII vs. UTF-8).
7. **Git and GitHub Collaboration**: Managing working trees, staging indices, commit histories, branching strategies (`update-about`), opening and merging Pull Requests, and assembling a complete Git terminology glossary.
8. **Computer Networking & Protocols**: Deconstructing network topologies (LAN, MAN, WAN), packet-switched routing, DNS resolution mechanics, transport protocols (TCP vs UDP), and diagnosing live latency/routing with `ping` and `nslookup`.
9. **Final Verification & System Report**: Conducting an end-to-end quality assurance audit, validating program test cases, verifying documentation integrity, and ensuring clean repository standards.

---

### Mission Index

| Mission | Focus Area | Documentation Link | Status |
| :--- | :--- | :--- | :---: |
| **Mission 0** | Workspace setup, runtime verification & Git initialisation | [mission-00-setup/README.md](./mission-00-setup/README.md) | Completed |
| **Mission 1** | Computer fundamentals, IPOS pipeline & hardware analysis | [mission-01-computer-basics/README.md](./mission-01-computer-basics/README.md) | Completed |
| **Mission 2** | Unix shell navigation, pipelines & file manipulation | [mission-02-terminal/README.md](./mission-02-terminal/README.md) | Completed |
| **Mission 3** | OS architecture, process supervision & permissions | [mission-03-operating-system/README.md](./mission-03-operating-system/README.md) | Completed |
| **Mission 4** | Program execution, compilers vs. interpreters | [mission-04-programs/README.md](./mission-04-programs/README.md) | Completed |
| **Mission 5** | Number base systems, CLI converter & data encoding | [mission-05-numbers-data/README.md](./mission-05-numbers-data/README.md) | Completed |
| **Mission 6** | Distributed version control, branching & Pull Requests | [mission-06-git-github/README.md](./mission-06-git-github/README.md) | Completed |
| **Mission 7** | Network protocols, packet switching & DNS lifecycle | [mission-07-networking/README.md](./mission-07-networking/README.md) | Completed |
| **Mission 8** | Comprehensive audit, verification & final submission | [mission-08-final-report/README.md](./mission-08-final-report/README.md) | Completed |

---

### How to Run the Programs

#### 1. Hello World Program (Mission 4)
Execute the Python script from the repository root:
```bash
python3 mission-04-programs/hello.py
```
Expected Output:
```
Hello from Python! System exploration in progress.
```

#### 2. Number Base Converter (Mission 5)
Launch the interactive converter from the project root:
```bash
python3 mission-05-numbers-data/number_converter.py
```
Or enter the mission directory directly:
```bash
cd mission-05-numbers-data
python3 number_converter.py
```
The program accepts any positive base-10 integer (such as `13`, `25`, `42`, or `255`) and outputs verified representations in Binary, Hexadecimal, and Octal formats with clean formatting and bit-length metrics.
