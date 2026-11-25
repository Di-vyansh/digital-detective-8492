# Mission 1 — Know your computer

## 1. Task / objective
The goal of Mission 1 was to investigate the fundamental architecture of modern computer systems. This involved tracing an everyday computing scenario through the classic **IPOS** (Input, Processing, Output, Storage) model, cataloging physical hardware peripherals alongside system software on my personal computer, and analyzing three distinct automated embedded computer systems found in contemporary daily life.

## 2. Work completed

### Task 1.1 — Trace one activity using IPOS
**Activity chosen**: Streaming a high-definition video lecture on YouTube and capturing an annotated screenshot note.

| Stage | What happens in this activity? | Physical Hardware / System Component |
| :--- | :--- | :--- |
| **Input** | I search for the lecture topic using the keyboard and click the video player controls using the trackpad. I trigger a screen capture key combination (`Cmd + Shift + 4`). | Apple Magic Keyboard, Force Touch Trackpad |
| **Processing** | The Central Processing Unit (CPU) schedules network decoding threads. The graphics processing hardware (GPU / Video Decoder) decompresses incoming AV1/H.264 stream frames. System memory (RAM) maintains active frame buffers, while macOS CoreGraphics captures the designated pixel boundary. | Apple Silicon SoC (M-series CPU & GPU cores), Unified System Memory (RAM) |
| **Output** | High-resolution visual video frames are rendered across the screen at 60 Hz. Digital audio samples are decoded and converted into sound waves. A visual thumbnail preview of the captured frame appears on the desktop. | Liquid Retina Display, Integrated Stereo Speaker Array |
| **Storage** | The web browser caches incoming video segments temporarily in high-speed flash storage. The finalized screenshot PNG file is written persistently to the APFS file system on the local solid-state drive. | Internal NVMe Solid-State Drive (SSD) running APFS |

#### How the activity moves from input to output and storage:
1. Physical user interactions (key presses and trackpad gestures) generate hardware interrupt requests that the operating system converts into software events.
2. The browser process receives these input events, transmits network socket packets across Wi-Fi, and receives compressed video bitstreams.
3. The CPU and hardware media decoders decompress the audiovisual stream in RAM, continuously dispatching pixel matrices to the GPU and audio buffers to the audio controller.
4. The user-initiated screenshot command instructs the graphics server to freeze the framebuffer buffer, encode the raster image into a PNG container, and commit the byte stream to persistent SSD storage.

---

### Task 1.2 — Identify hardware and software
Below is a categorized audit of physical components and software applications actively utilized on my development machine:

| Category | Item Name | Primary Function / Role in Workflow |
| :--- | :--- | :--- |
| **Hardware (Input)** | Built-in Force Touch Trackpad | Translates multi-touch physical gestures, taps, and pressure into precise UI pointer coordinates. |
| **Hardware (Input)** | Integrated Magic Keyboard | Scans mechanical key matrices to produce ASCII and modifier keycode interrupt signals. |
| **Hardware (Processing)** | Apple Silicon M-series Processor | Heterogeneous System-on-Chip (SoC) executing user threads, arithmetic logic, and vectorized matrix computations. |
| **Hardware (Output)** | Built-in Liquid Retina Display | High-density LED backlit matrix providing visual raster output for operating system and application graphical interfaces. |
| **Hardware (Output)** | Built-in Stereo Audio Drivers | Converts digital pulse-code modulation (PCM) audio streams into analog acoustic vibrations. |
| **Hardware (Storage)** | Internal NVMe Solid-State Drive | Non-volatile NAND flash storage hosting the operating system kernel, system binaries, and user files. |
| **Hardware (Storage)** | Unified System RAM (Memory) | High-throughput, low-latency volatile memory storing actively executed instructions and program data structures. |
| **Software (Operating System)** | macOS Darwin Kernel (v27.2.0) | Manages hardware abstractions, virtual memory subsystems, preemptive multitasking, and file access security. |
| **Software (Application)** | Visual Studio Code | Integrated Development Environment (IDE) providing syntax highlighting, debugger integration, and code editing. |
| **Software (Application)** | Unix Terminal (Zsh Shell) | Command-line interface interpreter allowing direct interaction with the underlying Unix system utilities. |
| **Software (Toolchain)** | Python 3 Interpreter (v3.14.7) | High-level language bytecode compiler and virtual runtime executing Python scripts. |
| **Software (VCS)** | Git Version Control System | Distributed source-code revision tracker maintaining change histories and project snapshots. |

---

### Task 1.3 — Computer systems around you
Computers are no longer confined to traditional desktop or laptop form factors; dedicated microcontrollers and embedded computing platforms govern modern infrastructure. Here are three distinct real-world computer systems:

#### 1. Electronic Toll Collection System (FASTag / RFID Highway Toll)
- **Input**: High-frequency RFID antenna mounted on the toll gantry detects and reads the unique electronic identifier embedded on the vehicle's windshield tag as it approaches.
- **Processing**: An embedded lane controller system validates the tag ID against an encrypted whitelist, queries a cloud transaction server via cellular WAN to verify the wallet balance, and deducts the appropriate toll fare.
- **Output**: A visual signal light turns green, an overhead LED digital sign displays the transaction confirmation, and a motorized boom barrier swings open to allow passage.
- **Storage**: The transaction record (tag ID, timestamp, lane ID, deducted amount) is stored in a local SQLite database log and synchronized with the national banking clearinghouse.

#### 2. Advanced Multi-Sensor Smartwatch (e.g., Apple Watch)
- **Input**: Photoplethysmography (PPG) optical sensors emit green LED light through the skin to measure capillary blood volume changes, while a 3-axis accelerometer tracks wrist motion.
- **Processing**: An ultra-low-power ARM Cortex-based System-on-Chip processes raw optical reflection signals using algorithmic signal filters and fast Fourier transforms (FFT) to calculate continuous heart rate and step metrics.
- **Output**: An ultra-bright OLED display renders real-time biometric metrics, animated fitness rings, and sends haptic vibrations through a linear resonant actuator to the user's wrist.
- **Storage**: Embedded flash memory maintains rolling 7-day health metrics, workout logs, and sleep architecture telemetry before wireless synchronization to mobile storage.

#### 3. Smart Commercial Building Thermostat (e.g., Nest Learning Thermostat)
- **Input**: Solid-state thermistors detect ambient room temperature, digital capacitive sensors assess relative humidity, and passive infrared (PIR) sensors monitor room occupancy.
- **Processing**: A dual-core embedded microprocessor evaluates current ambient readings against learned user schedules, thermal inertia models, and weather forecasts to determine optimal heating/cooling cycles.
- **Output**: Solid-state relays trigger 24V AC signals to energize HVAC compressors or fan blowers, while a circular color LCD informs room occupants of target temperatures.
- **Storage**: Non-volatile EEPROM memory stores user temperature preferences, Wi-Fi configuration credentials, and historical runtime logs.

---

## 3. Commands / tools used
- `uname -a` — Inspected kernel architecture and hardware platform identification.
- `sysctl -n machdep.cpu.brand_string` — Audited CPU hardware specifications.
- Text editors & markdown preview tools to structure technical documentation.

## 4. My understanding
Exploring the IPOS paradigm reinforces the principle that every digital device—regardless of whether it is a multi-core laptop or an embedded toll booth sensor—fundamentally adheres to the same architectural cycle: gathering input from sensors or human peripherals, computing decisions through arithmetic logic units, rendering outputs to users or actuators, and committing state to persistent storage.

Recognizing the boundary between hardware (the physical silicon circuits that carry electrical charges) and software (the abstract encoded instructions directing those charges) clarifies why operating systems are necessary to bridge the gap safely and efficiently.

## 5. Difficulties faced
When analyzing embedded systems, it was challenging at first to distinguish between temporary volatile working buffers (like microcontroller registers) and persistent non-volatile storage in resource-constrained IoT devices.

## 6. How I resolved them
I researched microcontroller architectural datasheets (specifically how flash memory and EEPROM retain configuration data even when the device is completely powered down), allowing me to accurately document the storage phase across embedded systems.

## 7. Evidence / files
- `mission-01-computer-basics/README.md`
- Documentation tables verifying IPOS mapping, hardware/software classifications, and embedded system workflows.

## 8. Commit details
- Commit message: `Complete computer basics and IPOS mission`
- Branch: `main`
