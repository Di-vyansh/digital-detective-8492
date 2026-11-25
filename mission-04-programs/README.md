# Mission 4 — How programs run

## 1. Task / objective
The goal of Mission 4 was to explore the execution mechanics of software programs. This required writing and running a standalone Python program (`hello.py`) from the command line, observing its standard output stream, and conducting an in-depth comparative analysis contrasting compiled programming languages against interpreted programming languages.

## 2. Work completed

### Task 4.1 — Create and run a Python program
- Created the source code file `hello.py` inside the `mission-04-programs/` directory.
- Implemented a clean, modular Python script:
  ```python
  # Mission 4 - Hello World Script
  # Student: Divyansh Pal (USN: 2402608492)
  # Campus: S-VYASA University

  def main():
      print("Hello from Python! System exploration in progress.")

  if __name__ == "__main__":
      main()
  ```
- Executed the program directly from the repository root via terminal:
  ```bash
  python3 mission-04-programs/hello.py
  ```
- **Observed Terminal Output**:
  ```
  Hello from Python! System exploration in progress.
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Comparison Dimension | Compiled Languages (e.g., C, C++, Rust, Go) | Interpreted Languages (e.g., Python, Ruby, JavaScript) |
| :--- | :--- | :--- |
| **Translation Phase** | Translates the entire high-level source code into native machine code (binary zeros and ones) ahead of time before any execution occurs. | Reads, parses, and translates source code instructions on the fly line-by-line (or into intermediate bytecode) during runtime. |
| **Output Artifact** | Produces a standalone, executable machine-code binary file (e.g. `.exe` on Windows or ELF/Mach-O binary on Linux/macOS). | Does not generate a standalone native binary; requires the runtime interpreter application (e.g., `python3`) to be present on the target host. |
| **Execution Speed** | **Fastest execution speed**: The CPU executes native machine instructions directly on the physical silicon without intermediary translation overhead. | **Slower execution speed**: The interpreter must continuously interpret and evaluate bytecode instructions inside a software virtual machine at runtime. |
| **Portability** | **Platform-dependent binaries**: A binary compiled on macOS (Apple Silicon arm64) will not run on Windows (x86_64) without recompilation for the target architecture. | **Highly portable source code**: The exact same `.py` source file executes unchanged across macOS, Windows, and Linux, as long as a platform-compatible Python runtime is installed. |
| **Error Discovery** | Syntax and type errors are detected entirely during the build/compilation phase before the program can ever run. | Syntax errors or runtime exceptions (like accessing undefined variables) may only be encountered when execution reaches that specific branch of code. |
| **Typical Use Cases** | Operating systems kernels, video game engines, embedded flight systems, device drivers, and high-frequency trading engines. | Data science, machine learning scripting, web backend development, automated system administration, and rapid prototyping. |

#### Difference between compiler and interpreter (in my own words):
Think of a **compiler** like a professional translator who takes an entire book written in Spanish, translates the complete text into English ahead of time, and publishes a finished English book. Once published, anyone who speaks English can read it at full reading speed without the translator ever needing to be in the room.

An **interpreter**, by contrast, is like a live simultaneous speech interpreter sitting beside you at a conference. As each speaker utters a sentence in Spanish, the interpreter translates that single sentence into English into your ear in real time. It allows you to immediately start listening without waiting for the entire speech to conclude, but the overall presentation moves at a slower pace because translation happens continuously as words are spoken.

---

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py` (executed the script)
- Python 3.14.7 runtime
- Nano / code editor for script authoring.

## 4. My understanding
Understanding the contrast between compilers and interpreters clarifies why different programming languages are selected for different engineering tasks. When maximum hardware performance and microsecond latency are paramount, compiled languages like C++ or Rust are chosen because they map directly to native processor instructions.

Conversely, for applications emphasizing developer velocity, readability, and platform independence, interpreted languages like Python excel because developers can immediately test and iterate on code without lengthy compilation builds.

## 5. Difficulties faced
Ensuring the Python execution command correctly referenced the file path whether run from the project root directory or from inside the `mission-04-programs/` folder.

## 6. How I resolved them
I tested invoking the script using both relative paths:
- From root: `python3 mission-04-programs/hello.py`
- From directory: `cd mission-04-programs && python3 hello.py`
Documenting both methods in the root README guarantees smooth execution for any evaluator.

## 7. Evidence / files
- `mission-04-programs/hello.py`
- `mission-04-programs/README.md`

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Branch: `main`
