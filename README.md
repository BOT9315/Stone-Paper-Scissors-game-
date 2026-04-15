# ✊ Stone Paper Scissors

A clean, modular command-line game built in Python where you battle the computer in the classic Stone Paper Scissors showdown. Tracks your score across multiple rounds until you decide to quit.

---

## 📁 Project Structure

```
stone-paper-scissors/
├── main.py       # Game loop, score tracking, and user menu
├── utils.py      # Orchestrates a single round
├── choice.py     # Handles user input and computer random choice
└── logic.py      # Determines Win / Lose / Draw outcome
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (no external libraries required)

### Run the Game

```bash
git clone https://github.com/BOT9315/Stone-Paper-Scissors-game-.git
cd Stone-Paper-Scissors-game-
python main.py
```

---

## 🎮 How to Play

1. Run `main.py`
2. Enter `1` to play a round or `2` to exit
3. Choose your move:
   - `1` → Stone
   - `2` → Paper
   - `3` → Scissors
4. The computer picks randomly — the result is shown instantly
5. Your score and the computer's score are updated after every round
6. Enter `2` at the main menu to see the final score and exit

---

## 🧠 Game Logic

| You       | Computer  | Result |
|-----------|-----------|--------|
| Stone     | Scissors  | ✅ Win  |
| Paper     | Stone     | ✅ Win  |
| Scissors  | Paper     | ✅ Win  |
| Any       | Same      | 🤝 Draw |
| Anything else | —    | ❌ Lose |

---

## 💡 Example Session

```
--- Welcome to Stone Paper Scissors Game ---
1. Enter 1 if you want to Play
2. Enter 2 if you want to Exit
Enter choice what you want to do: 1

1. Stone
2. Paper
3. Scissors
Enter number: 1

You chose: Stone
Computer chose: Scissors
Result: Win
Score -> You: 1  Computer: 0
```

---

## 🛠️ Code Overview

| File | Responsibility |
|------|---------------|
| `main.py` | Main game loop, score tracking, menu handling |
| `utils.py` | `run()` — ties together choice and logic for one round |
| `choice.py` | `user_choice()` for input, `computer_choice()` for random pick |
| `logic.py` | `check(user, comp)` — returns `"Win"`, `"Lose"`, or `"Draw"` |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**BOT9315**
- GitHub: [@BOT9315](https://github.com/BOT9315)
- Project: [Stone-Paper-Scissors-game-](https://github.com/BOT9315/Stone-Paper-Scissors-game-)
