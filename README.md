# CYBERLAB - Password Security Simulator

#### Video Demo: <Link do video>

## Description

CYBERLAB is a password security simulator built in Python.
The goal of this project is to demonstrate how password strength, entropy, hashing, and brute force attacks work in practice.

This program allows the user to:

1. Generate password hashes (SHA256, SHA1, MD5)
2. Analyze password strength using entropy
3. Simulate a realistic brute force attack
4. Estimate theoretical crack time based on entropy

The project was designed to show how password complexity increases exponentially, not linearly.

---

## Project Structure

The project is modular and separated into multiple files:

- 'project.py' -> Main program and menu interface
- 'hashing.py' -> Hash generation functions
- 'analyzer.py' -> Password entropy calculation and strength analysis
- 'brute_force.py' -> Brute force attack simulation
- 'estimator.py' -> Mathematical crack time estimation
- 'utils.py' -> Helper functions (formatting, reports, visualization)

This separation improves readability, maintainability, and organization.

---

## How It Works

### 1. Hash Generation

The program uses Python's 'hashlib' library to generate:
- SHA256
- SHA1
- MD5

This demonstrates how passwords are stored securely as hashes instead of plain text.

---

### 2. Password Entropy

Password entropy is calculated using the formula:

Entropy = Length * log₂(Character Set Size)

Where:
- Length = number of characters
- Character Set Size = number of possible characters used

Higher entropy means exponentially more possible combinations.

---

### 3. Brute Force Simulation

The brute force attack simulates an attacker trying all possible combinations until the password is found.

It:
- Generates combinations up to a defined length
- Hashes each attempt
- Compares it to the target hash
- Measures the time taken

This demonstrates how short passwords can be cracked quickly.

---

### 4. Crack Time Estimation

The program estimates how long it would take to crack a password using:

Total Combinations = 2^Entropy

Then divides this by an assumed guesses-per-second value to calculate time in:
- Seconds
- Minutes
- Hours
- Years (if necessary)

This shows the exponential growth of password security.

---

## Design Decisions

I chose to separate the program into multiple files to:

- Improve code organization
- Follow modular programming principles
- Make the system easier to extend in the future

I also implemented both a realistic brute force simulation and a theoretical estimator to compare practical and mathematical perspectives.

---

## What I Learned

While building this project, I learned:

- How hashing algorithms work
- The difference between hashing and encryption
- How entropy measures password strength
- Why password security grows exponentially
- How brute force attacks operate
- How to structure a multi-file Python project

---

## Limitations

- The brute force attack is limited to short passwords (for practical runtime reasons)
- The guesses-per-second value is an estimation
- This is a simulation, not a real hacking tool

---

## Conclusion

This project demonstrates the importance of strong passwords and how small increases in length or character complexity dramatically increase security.

It combines mathematical theory (entropy and exponential growth) with pratical simulation (brute force attack), providing a complete educational tool for understanding password security.
