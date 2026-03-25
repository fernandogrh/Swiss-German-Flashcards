![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Handling-purple?logo=pandas)
![CSV](https://img.shields.io/badge/CSV-File%20Storage-orange)
![OOP](https://img.shields.io/badge/OOP-Object%20Oriented%20Design-red)

![Project](https://img.shields.io/badge/Project-Personal%20Portfolio-success)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

# 🐍 Swiss German Flashcards 🇨🇭

### A simple but powerful flashcard app built with Python to learn Swiss German vocabulary.
### Focused on clean logic, persistence, and user-friendly learning flow.

## 🚀 About the Project

This project is a **desktop flashcard application** built with Python and Tkinter. It helps users learn Swiss German words by flipping cards, tracking progress, and saving learned words automatically.

The goal wasn’t just to “make it work”, but to build something that shows:

- clean structure

- real-world data handling

- thoughtful UX decisions

- scalable logic

## 🧠 How It Works

- Each flashcard shows a Swiss German word

- After 3 seconds, the card flips to reveal the English translation

- You decide if you know the word:

    - ❌ Skip → word stays in rotation

    - ✅ Known → word is removed and saved

- Your progress is tracked live

- Learned words are saved so progress persists between sessions

Once all words are learned, the app clearly tells you 🎉

## ✨ Features

- 🖼️ Flashcard-style UI (front & back)

- ⏱️ Timed card flipping

- 📊 Progress counter (learned / total)

- 💾 Persistent learning using CSV files

- 🔁 Randomized card selection

- 🧠 Smart completion handling when no cards remain

## 🛠️ Tech & Concepts Used

This project intentionally showcases **core Python development skills**:

### Python Concepts

- Functions & modular logic

- Global state handling

- List & dictionary operations

- Defensive programming (if not to_learn)

- Randomized selection

### Libraries & Tools

- Tkinter

    - Canvas, Buttons, Labels
    
    - Image handling (PhotoImage)
    
    - Timers (after, after_cancel)

- Pandas

  - Reading CSV files

  - Writing updated learning progress

  - Converting data to dictionaries

- CSV-based persistence

  - Automatically creates and updates progress files

  - No manual setup required

## ▶️ How to Run

  git clone https://github.com/fernandogrh/Swiss-German-Flashcards.git
  cd Swiss-German-Flashcards
  pip install -r requirements.txt
  python main.py

> ⚠️ Make sure the 'data/' and 'images/' folders are present.

## 👤 Author

Built by **Fernando Ramirez**