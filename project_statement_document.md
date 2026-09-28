# Project Statement: Terminal-Based BINGO Game

## 1. Problem Statement

Traditional BINGO games rely heavily on physical equipment—such as physical cards, paper markers, and mechanical caller cages—or require multi-player human presence. Replicating this experience in modern software often leads to over-engineered applications that require high-performance graphics engines, continuous internet connectivity, complex user authentication systems, or heavy Graphical User Interfaces (GUIs).

There is a distinct need for a lightweight, self-contained, terminal-based software solution that provides an interactive, turn-based BINGO experience against an automated computer opponent. The system must eliminate physical setup requirements, automate card generation and line evaluation, handle user input errors gracefully, and run efficiently within a Command-Line Interface (CLI) environment.

---

## 2. Scope of the Project

### 2.1 In-Scope
* **Terminal-Based Core Engine**: A modular Python application designed for execution within standard command-line interfaces.
* **Automated Matrix Generation**: Generation of independent $5 \times 5$ grid layouts containing randomized permutations of integers from $1$ to $25$ for both human and computer participants.
* **Dual-Board Tracking**: Simultaneous state updating across both player boards whenever a number is called by either participant.
* **Automated Opponent Logic**: Turn-based computer selection engine that filters out previously called numbers and picks dynamically from remaining valid candidates.
* **Input Validation & Exception Guarding**: Comprehensive handling of CLI inputs to reject non-integers, numbers outside the $1–25$ range, and duplicate selections without crashing the program.
* **Multi-Directional Pattern Recognition**: Dynamic scanning algorithms to evaluate horizontal rows, vertical columns, and primary/secondary diagonals.
* **Automated Win Resolution**: Game-loop termination and victory declaration upon registering $\ge 5$ completed lines for either participant.

### 2.2 Out-of-Scope
* Graphical User Interfaces (GUIs) using desktop frameworks (e.g., Tkinter, PyQt) or web frontends.
* Networked multi-player functionality over TCP/IP sockets or web protocols.
* Persistent database storage for player profiles, game history, or high scores.

---

## 3. Target Users

* **Casual CLI Gamers**: Users looking for a quick, zero-dependency, text-based game for offline entertainment directly in their terminal.
* **Programming Students & Educators**: Learners studying foundational computer science principles, such as multidimensional array manipulation, matrix traversal algorithms, modular program structures, and game loop state management.
* **Academic Assessors & Reviewers**: Code reviewers evaluating procedural programming concepts, control flow logic, and terminal UI design in Python.

---

## 4. High-Level Features

* **Dynamic $5 \times 5$ Grid Initialization**: Automatically generates distinct, non-repeating number layouts ($1$ to $25$) for the player and computer at the start of each session.
* **Shared Call Propagation**: Automatically marks selected numbers on both cards simultaneously, accurately reflecting traditional BINGO caller dynamics.
* **Smart Opponent Engine**: Computer turn generation that evaluates remaining uncalled numbers to guarantee valid choices every round.
* **Robust CLI Guarding**: Continuous input verification that displays clear feedback on invalid entries and prompts retry attempts without skipping turns.
* **Real-Time Matrix Renderer**: Clean ASCII grid output displaying remaining numbers and replacing called positions with distinct `" X "` flags.
* **Comprehensive Line Counting**: Algorithmic evaluation of 5 rows, 5 columns, and 2 diagonals to calculate total line completions after every turn.
* **Progressive B-I-N-G-O Progress Tracking**: Dynamic string output illustrating B-I-N-G-O letter progression as lines are completed.
* **Graceful Termination Engine**: Immediate declaration of victory and session shutdown as soon as 5 lines are completed by either participant.