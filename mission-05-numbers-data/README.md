# Mission 5 — Numbers and data

## 1. Task / objective
The goal of Mission 5 was to demystify how electronic computers represent and manipulate quantitative data and text. This required performing manual step-by-step mathematical conversions between decimal, binary, and hexadecimal number systems, verifying calculations using the Python interactive shell, engineering an interactive CLI conversion tool (`number_converter.py`), and analyzing text encoding standards (ASCII vs. UTF-8).

## 2. Work completed

### Task 5.1 — Convert numbers by hand

#### 1. Decimal to Binary Conversions (Repeated Division by 2)

- **Convert Decimal 13 to Binary**:
  - $13 \div 2 = 6$ remainder **1** (Least Significant Bit)
  - $6 \div 2 = 3$ remainder **0**
  - $3 \div 2 = 1$ remainder **1**
  - $1 \div 2 = 0$ remainder **1** (Most Significant Bit)
  - Reading remainders from bottom to top: **$1101_2$**

- **Convert Decimal 25 to Binary**:
  - $25 \div 2 = 12$ remainder **1** (LSB)
  - $12 \div 2 = 6$ remainder **0**
  - $6 \div 2 = 3$ remainder **0**
  - $3 \div 2 = 1$ remainder **1**
  - $1 \div 2 = 0$ remainder **1** (MSB)
  - Reading remainders from bottom to top: **$11001_2$**

- **Convert Decimal 42 to Binary**:
  - $42 \div 2 = 21$ remainder **0** (LSB)
  - $21 \div 2 = 10$ remainder **1**
  - $10 \div 2 = 5$ remainder **0**
  - $5 \div 2 = 2$ remainder **1**
  - $2 \div 2 = 1$ remainder **0**
  - $1 \div 2 = 0$ remainder **1** (MSB)
  - Reading remainders from bottom to top: **$101010_2$**

---

#### 2. Binary to Decimal Conversions (Positional Value Expansion)

- **Convert Binary 1010 to Decimal**:
  $$\begin{aligned}
  1010_2 &= (1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0) \\
         &= (1 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1) \\
         &= 8 + 0 + 2 + 0 = \mathbf{10_{10}}
  \end{aligned}$$

- **Convert Binary 1101 to Decimal**:
  $$\begin{aligned}
  1101_2 &= (1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) \\
         &= (1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1) \\
         &= 8 + 4 + 0 + 1 = \mathbf{13_{10}}
  \end{aligned}$$

---

#### 3. Hexadecimal Conversions

- **Convert Hexadecimal A to Decimal**:
  - In hexadecimal, single digits span $0-9$ and $A-F$, where $A=10, B=11, C=12, D=13, E=14, F=15$.
  - Therefore, $\mathbf{A_{16} = 10_{10}}$.

- **Convert Hexadecimal 1F to Decimal**:
  $$\begin{aligned}
  1F_{16} &= (1 \times 16^1) + (15 \times 16^0) \\
          &= 16 + 15 = \mathbf{31_{10}}
  \end{aligned}$$

- **Convert Binary 1111 to Hexadecimal**:
  - A group of 4 binary bits (a nibble) maps directly to one hexadecimal digit:
  - $1111_2 = (1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 15_{10} = \mathbf{F_{16}}$.

---

### Task 5.2 — Verify using Python
I validated each manual calculation inside an interactive Python 3 shell session using Python's built-in numeric functions:

| Conversion Tested | Python Expression Executed | Evaluated Result | Verification Status |
| :--- | :--- | :--- | :---: |
| Decimal 13 $\rightarrow$ Binary | `bin(13)` | `'0b1101'` | Verified ($1101$) |
| Decimal 25 $\rightarrow$ Binary | `bin(25)` | `'0b11001'` | Verified ($11001$) |
| Decimal 42 $\rightarrow$ Binary | `bin(42)` | `'0b101010'` | Verified ($101010$) |
| Binary 1010 $\rightarrow$ Decimal | `int("1010", 2)` | `10` | Verified ($10$) |
| Binary 1101 $\rightarrow$ Decimal | `int("1101", 2)` | `13` | Verified ($13$) |
| Hexadecimal A $\rightarrow$ Decimal | `int("A", 16)` | `10` | Verified ($10$) |
| Hexadecimal 1F $\rightarrow$ Decimal | `int("1F", 16)` | `31` | Verified ($31$) |
| Binary 1111 $\rightarrow$ Hexadecimal | `hex(0b1111)` | `'0xf'` | Verified ($F$) |

All Python runtime evaluations matched the manual mathematical calculations with 100% accuracy.

---

### Task 5.3 — Build a small number converter
I engineered `number_converter.py` inside the `mission-05-numbers-data/` folder. The program features input validation (`str.isdigit()`), formats outputs across decimal, binary, hexadecimal, and octal bases, and computes minimum storage bit length.

#### Verification Test Runs:

| Input Decimal Value | Binary Output (`bin()`) | Hexadecimal Output (`hex()`) | Octal Output (`oct()`) | Minimum Bits |
| :---: | :--- | :--- | :--- | :---: |
| **`13`** | `0b1101` (`1101`) | `0xd` (`D`) | `0o15` (`15`) | 4 bits |
| **`25`** | `0b11001` (`11001`) | `0x19` (`19`) | `0o31` (`31`) | 5 bits |
| **`255`** | `0b11111111` (`11111111`) | `0xff` (`FF`) | `0o377` (`377`) | 8 bits |
| **`1024`** | `0b10000000000` | `0x400` (`400`) | `0o2000` | 11 bits |

#### Operational analysis of conversion functions:
- **`bin(n)`**: Accepts an integer argument and returns its binary equivalent as a string prefixed with `0b`. The prefix explicitly distinguishes base-2 notation from decimal values.
- **`hex(n)`**: Converts an integer to lowercase hexadecimal format prefixed with `0x`, condensing every 4 bits into a single character ($0-9, a-f$).
- **`int(string, base)`**: Parses an arbitrary-base string representation into its base-10 numerical integer value.

---

### Task 5.4 — How is text stored?

- **ASCII decimal values for 'A' and 'a':**
  - Uppercase **'A'** corresponds to decimal code **`65`** (Binary: `01000001`).
  - Lowercase **'a'** corresponds to decimal code **`97`** (Binary: `01100001`).
  - *Verified in Python using*: `ord('A')` $\rightarrow$ `65`, `ord('a')` $\rightarrow$ `97`.
  - Notice the difference between 'A' and 'a' is exactly $32$ ($2^5$), meaning toggling a single bit flips character case!

- **Why is a standardized character encoding required to store text?**  
  Computers possess no inherent concept of letters, punctuation, or alphabets; transistors only store charge levels representing binary numbers (`0` and `1`). A character encoding standard defines an agreed-upon mapping dictionary between abstract visual glyphs and concrete integer values. Without an agreed standard, a file written on one operating system would decode into random garbled text (mojibake) on another.

- **Examples of characters beyond basic ASCII:**  
  Standard 7-bit ASCII is restricted to 128 characters ($0-127$), designed exclusively for English. Contemporary characters such as the Indian Rupee symbol (**`₹`**), the sacred Devanagari syllable (**`ॐ`**), or modern emojis (**`🚀`**) cannot be encoded in 7-bit ASCII. These characters require **UTF-8**, a variable-length Unicode encoding that utilizes between 1 and 4 bytes per character to represent every human writing system.

---

## 3. Commands / tools used
- `python3 -i` (Python interactive REPL for manual verification)
- `python3 mission-05-numbers-data/number_converter.py` (tested with test vectors)
- `ord()` and `chr()` built-in Python string introspection functions.

## 4. My understanding
Binary is the native language of computing hardware because digital logic gates are constructed from silicon MOSFET transistors, which operate as binary switches (voltage high = 1, voltage low = 0).

Hexadecimal is indispensable because raw binary strings quickly become unreadable to humans (e.g., `1111111111110000`). Because $2^4 = 16$, exactly 4 binary bits map to a single hex digit. Thus, an 8-bit byte is represented by two hex digits, and 24-bit RGB colors or 32-bit memory addresses become clean and legible.

## 5. Difficulties faced
When accepting user input, if a user entered negative values, floating point numbers (e.g. `13.5`), or pressed enter without typing anything, `int()` crashed the script with an unhandled `ValueError`.

## 6. How I resolved them
I implemented sanitization logic using `str.strip()` and guarded conversion with `str.isdigit()`, which cleanly checks that the input consists purely of valid base-10 digits before parsing, printing a descriptive error message if invalid input is supplied.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`
- `mission-05-numbers-data/README.md`

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
- Branch: `main`
