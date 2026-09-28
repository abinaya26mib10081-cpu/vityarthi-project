# 🎲 Terminal Bingo Game (Python)

A command-line interface (CLI) Bingo game built in Python where a player competes against the computer. The game uses a classic 5x5 card setup with numbers ranging from 1 to 25, automatically marking off drawn numbers and tracking completed lines (horizontal, vertical, and diagonal) to spell **B-I-N-G-O**.

---

## ✨ Features

- **Player vs. Computer AI:** Play turn-by-turn against an automated computer player.
- **5x5 Grid Board:** Numbers from 1 to 25 are randomly distributed on both player and computer cards.
- **Automatic Line Detection:** Automatically detects horizontal, vertical, and diagonal lines.
- **B-I-N-G-O Progress Tracker:** Track your letter completion in real-time after every turn.

---

## 🛠️ Prerequisites & Installation

Before running the game, ensure you have **Python**, **Pip**, and **Git** installed on your system.

### 1. Install Git
- **Windows:**
  1. Download the installer from the [Official Git Website](https://git-scm.com/download/win).
  2. Run the executable and keep default options selected.
  3. Verify installation by running in Command Prompt:
     ```cmd
     git --version
     ```
- **macOS:** Install via Terminal: `xcode-select --install`
- **Linux (Ubuntu/Debian):** Install via Terminal: `sudo apt update && sudo apt install git`

### 2. Install Python & Pip
- **Windows:**
  1. Download Python 3.x installer from [python.org](https://www.python.org/downloads/).
  2. **Crucial:** Check the box **"Add python.exe to PATH"** during setup.
  3. Verify installation in Command Prompt:
     ```cmd
     python --version
     pip --version
     ```
- **macOS / Linux:** Python 3 often comes pre-installed. Verify or install via package manager:
  ```bash
  python3 --version
  pip3 --version
  ```

---

## 🚀 How to Clone and Run

Follow these steps to clone the project from GitHub and run it in Command Prompt (`cmd`):

### Step 1: Open Command Prompt
Press `Win + R`, type `cmd`, and press **Enter**.

### Step 2: Clone the Repository
Navigate to the directory where you want to save the project (e.g., Desktop) and run:
```cmd
cd Desktop
git clone https://github.com/abinaya26mib10081-cpu/vityarthi-project.git
```

### Step 3: Navigate into the Project Folder
```cmd
cd vityarthi-project
```

### Step 4: Run the Game
Execute the Python script by entering:
```cmd
python "ABINAYA 26MIB10081.py"
```
*(Note: If you are using `python3` on Linux/macOS, use `python3 "ABINAYA 26MIB10081.py"` instead.)*

---

## 🎮 How to Play

1. **Start the Game:** Upon launching, both your card and the computer's card will be displayed.
2. **Your Turn:**
   - Enter a number between **1 and 25** that hasn't been called yet.
   - The selected number will be marked with an `X` on **both** your card and the computer's card.
3. **Computer's Turn:**
   - The computer will randomly pick an available number, which will also be marked on both cards.
4. **Winning Condition:**
   - Completing a horizontal row, vertical column, or diagonal line awards one letter of **B-I-N-G-O**.
   - The first player to complete **5 lines** (spelling out full **B-I-N-G-O**) wins the game!

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.