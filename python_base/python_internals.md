# ⚙️ Python Internals: Source Code to Execution

This document explains what happens behind the scenes when you run a Python script, focusing on the compilation process, the **.pyc** file, and the **Python Virtual Machine (PVM)**.

---

## 🚀 The Execution Flow

Python is often called an "interpreted" language, but it actually goes through a compilation step before executing. The process follows these four stages:

1. **Source Code (`.py`)**: The human-readable code you write.
2. **Compiler**: Python's internal compiler checks for syntax errors.
3. **Bytecode (`.pyc`)**: An intermediate, platform-independent code.
4. **PVM (Python Virtual Machine)**: The engine that actually runs the code.

---

## 📦 1. The .pyc File (Bytecode)

When you run or import a script, Python compiles it into **Bytecode**.

- **Storage**: These files are stored in the `__pycache__` directory.
- **Purpose**: Bytecode is a low-level set of instructions. It is faster for a machine to read than raw text.
- **Efficiency**: Python saves these files so that if the source code hasn't changed, it can skip the compilation step next time, making the program start faster.

> **Note:** `.pyc` files are **platform-independent**. You can move a `.pyc` file from Windows to Linux, and it will work as long as the Python version is the same.

---

## 🧠 2. The PVM (Python Virtual Machine)

The **PVM** is the heart of the Python system. It is not a physical machine but a software engine (an interpreter).

### How it works:

1. It loads the **Bytecode** instructions.
2. It loops through each instruction and translates it into **Machine Code** (binary) that your computer's CPU can understand.
3. It executes the logic and handles memory management (Garbage Collection).

## 🛠️ Summary Table

| Component       | File Extension | Role                                              |
| :-------------- | :------------- | :------------------------------------------------ |
| **Source Code** | `.py`          | Written by the programmer; easy to read and edit. |
| **Bytecode**    | `.pyc`         | Low-level instructions stored in `__pycache__`.   |
| **PVM**         | _(Software)_   | The runtime engine that executes the bytecode.    |

"Interpreted" means the code is executed by an intermediate program (the Interpreter/PVM) rather than being turned into a standalone machine-code file (.exe). This allows for features like platform independence and faster development cycles.
