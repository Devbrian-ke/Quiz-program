
#  Ultimate Python Quiz
 
A fun, interactive command-line quiz application that tests your Python knowledge — built entirely with core Python, no external dependencies required.
 
---
 
##  Overview
 
**Ultimate Python Quiz** is a terminal-based multiple-choice quiz game designed to help beginners and intermediate learners test their Python programming knowledge. Questions are presented one at a time, and the app tracks your score and gives motivational feedback at the end.
 
---
 
##  Features
 
-  Multiple-choice questions (A/B/C/D format)
-  Instant right/wrong feedback after each answer
-  Final score summary with performance message
-  Dynamic feedback — from beginner encouragement to "Python master" status
-  Easily extendable — add as many questions as you like
- Zero dependencies — uses only built-in Python
---
 
## Requirements
 
- Python **3.6+**
No third-party libraries needed. The quiz runs entirely on Python's standard library.
 
---
 
## Installation
 
### 1. Clone or Download the Project
 
```bash
git clone https://github.com/your-username/python-quiz.git
cd python-quiz
```
 
Or simply download the `quiz_program.py` file directly.
 
### 2. Verify Python is Installed
 
```bash
python --version
```
 
If Python is not installed, download it from [python.org](https://www.python.org/downloads/).
 
---
 
##  Usage
 
Run the quiz from your terminal:
 
```bash
python quiz_program.py
```
 
### Example Session:
 
```
Welcome to the Ultimate Python Quiz!
--------------------------------------
 
1. What is the output of print(2 ** 3)?
A. 6
B. 8
C. 9
D. 5
Your answer (A/B/C/D): B
 Correct!
 
...
 
 You got 4 out of 5 correct!
 Not bad! Keep sharpening your skills.
```
 
---
 
##  Project Structure
 
```
python-quiz/
│
└── quiz_program.py   # Main quiz application
```
 
---
 
##  How It Works
 
The quiz is powered by two core components:
 
| Component | Description |
|-----------|-------------|
| `quiz_questions` | A list of dictionaries, each holding a question, options, and correct answer |
| `run_quiz()` | Iterates through questions, captures input, checks answers, and tracks score |
 
### Score Feedback Logic
 
| Score | Message |
|-------|---------|
| All correct | You're a Python master! |
| 50% or above |  Not bad! Keep sharpening your skills. |
| Below 50% |  Keep learning. You're on the path! |
 
---
 
## ➕ Adding More Questions
 
To add your own questions, extend the `quiz_questions` list in `quiz_program.py` following this structure:
 
```python
{
    "question": "6. What data type is the result of 10 / 2 in Python 3?",
    "options": ["A. int", "B. float", "C. str", "D. bool"],
    "answer": "B"
}
```
 
Each dictionary must include:
- `"question"` — the question text
- `"options"` — a list of four answer choices (A–D)
- `"answer"` — the correct option letter (`"A"`, `"B"`, `"C"`, or `"D"`)
---
 
##  Contributing
 
Contributions are welcome! Fork the repo, add more questions or features (like a timer or difficulty levels), and submit a pull request.
 
---
 
## License
 
This project is open source and available under the [MIT License](LICENSE).
 
---
 
## Author
 
**Brian** — [@Devbrian-ke](https://github.com/Devbrian-ke)
