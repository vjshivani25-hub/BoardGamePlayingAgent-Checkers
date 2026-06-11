# ♟️ Board Game Playing Agent – Checkers AI

## Artificial Intelligence Based Checkers Game


<img width="325" height="155" alt="banner" src="https://github.com/user-attachments/assets/4ac5293a-197c-4df9-9324-5466e8fda8f6" />

---

## 🎯 Project Overview

The **Checkers AI Agent** is an Artificial Intelligence project developed for the **Computational Foundations of Artificial Intelligence (CFAI)** course.

The system models Checkers as a state-space search problem and applies intelligent decision-making techniques to select optimal moves.

### ♟️ Game Pieces

| AI Player      | Human Player   |
| -------------- | -------------- |
| ⚫ Black Pieces | ⚪ White Pieces |

Example Board:

```text
  0 1 2 3 4 5 6 7

0 . ⚫ . ⚫ . ⚫ . ⚫
1 ⚫ . ⚫ . ⚫ . ⚫ .
2 . ⚫ . ⚫ . ⚫ . ⚫
3 . . . . . . . .
4 . . . . . . . .
5 ⚪ . ⚪ . ⚪ . ⚪ .
6 . ⚪ . ⚪ . ⚪ . ⚪
7 ⚪ . ⚪ . ⚪ . ⚪ .
```

---

## 🚀 Features

✅ Checkers Board Representation

✅ Move Generation

✅ Minimax Algorithm

✅ Alpha-Beta Pruning

✅ Heuristic Evaluation

✅ Explainable AI Decisions

---

## 🧠 AI Concepts Implemented

| Concept              | Status |
| -------------------- | ------ |
| State Representation | ✅      |
| Move Generation      | ✅      |
| Heuristic Evaluation | ✅      |
| Minimax Search       | ✅      |
| Alpha-Beta Pruning   | ✅      |
| Explainable AI       | ✅      |

---

## 📂 Project Structure

```text
BoardGamePlayingAgent-Checkers
│
├── main.py
├── README.md
├── requirements.txt
└── screenshots
```

---

## ⚙️ How It Works

```text
Board State
     │
     ▼
Generate Moves
     │
     ▼
Minimax Search
     │
     ▼
Alpha-Beta Pruning
     │
     ▼
Board Evaluation
     │
     ▼
Best Move Selected
```

---

## 📸 Screenshots

### Initial Board

<img width="225" height="225" alt="initial_board" src="https://github.com/user-attachments/assets/f05f4bc4-4244-44fc-a73b-6af5cd96da11" />


### AI Decision

<img width="335" height="151" alt="ai_move" src="https://github.com/user-attachments/assets/16a6f750-182b-47c3-9b5f-4498f1f18dab" />


### Board After Move

<img width="300" height="168" alt="final_board" src="https://github.com/user-attachments/assets/fe16b1ff-e833-445e-823a-70ea594f5c27" />


---

## ▶️ Run the Project

```bash
python main.py
```
---
## 📤 Sample Output

```text
Initial Board:

. A . A . A . A
A . A . A . A .
. A . A . A . A
. . . . . . . .
. . . . . . . .
H . H . H . H .
. H . H . H . H
H . H . H . H .

AI selected move: (2,1) -> (3,0)

Board After AI Move:

. A . A . A . A
A . A . A . A .
. . . A . A . A
A . . . . . . .
. . . . . . . .
H . H . H . H .
. H . H . H . H
H . H . H . H .

Evaluation Score: 0
```

### Output Explanation

* The game initializes an 8×8 Checkers board.
* The AI player (`A`) and Human player (`H`) pieces are placed in their standard starting positions.
* The Minimax algorithm with Alpha-Beta Pruning evaluates possible moves.
* The AI selects the best available move.
* The updated board state is displayed.
* The evaluation score represents the difference between AI and Human pieces.


---
## 💻  Requirements

- Python 3.8 or higher
- No external libraries required
---

## 📈 Future Enhancements

* ♚ King Piece Support
* 🎮 Human vs AI Mode
* 🖥️ Graphical User Interface
* 🤖 Reinforcement Learning Agent
* 📊 Advanced Evaluation Functions

---

---

## 👥 Team Members

| Name | Roll Number |
|--------|------------|
| MOSANGI VIJAYA LAKSHMI | 2520090201 |
| POTLABATHINI SHASHANTH | 2520090211 |
| SAI KRISHNA | 2520090156 |

---

---
## 👨‍💻 Course Information

**Course:** Computational Foundations of Artificial Intelligence (CFAI)

**Project:** Board Game Playing Agent – Checkers AI

**Academic Year:** 2025–2026

---

### ♟️ “Artificial Intelligence is best understood when it plays a game.” ♟️

                   🌟 Thank You 🌟
⭐ If you like this project, give it a star on GitHub ⭐
