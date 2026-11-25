#!/usr/bin/env python3
# Mission 5 - Multi-Base Number Converter
# Student: Divyansh Pal (USN: 2402608492)
# Campus: S-VYASA University

import sys

def convert_number(input_val=None):
    print("=" * 50)
    print("   Digital Detective — Number System Converter   ")
    print("=" * 50)
    
    if input_val is None:
        raw = input("Enter a positive decimal integer: ").strip()
    else:
        raw = str(input_val).strip()
        print(f"Input received: {raw}")

    # Validate input: must be non-empty and consist only of digits
    if not raw.isdigit():
        print("\n[Error] Invalid input. Please enter a valid positive whole number (digits 0-9 only).")
        return False
        
    num = int(raw)
    
    # Base conversions using Python built-in primitives
    bin_str = bin(num)
    hex_str = hex(num)
    oct_str = oct(num)
    
    # Formatted representations
    clean_bin = bin_str[2:]
    clean_hex = hex_str[2:].upper()
    clean_oct = oct_str[2:]
    bit_count = num.bit_length() if num > 0 else 1
    
    print("\n--- Conversion Results ---")
    print(f"Decimal (Base 10)     : {num}")
    print(f"Binary (Base 2)        : {bin_str}  (Raw: {clean_bin})")
    print(f"Hexadecimal (Base 16)  : {hex_str}  (Raw: {clean_hex})")
    print(f"Octal (Base 8)         : {oct_str}  (Raw: {clean_oct})")
    print(f"Minimum Bits Required  : {bit_count} bit(s)")
    print("-" * 50)
    return True

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    convert_number(arg)
