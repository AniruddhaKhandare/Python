# ➕ add

A simple Python package for performing basic addition operations. Designed for learning, testing, or using as a utility in larger Python applications.

![License](https://img.shields.io/github/license/AniruddhaKhandare/add)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![Build](https://img.shields.io/github/actions/workflow/status/AniruddhaKhandare/add/python-app.yml)

---

## ✨ Features

- Add two numbers
- Command-line interface (CLI) support
- Lightweight with no external dependencies

---

## 📦 Installation

Clone the repository and install the package:

bash
git clone https://github.com/AniruddhaKhandare/add.git
cd add
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install .



🧪 Usage
As a Python Module
python
Copy
Edit
from add import add_numbers

result = add_numbers(3, 5)
print(result)  # Output: 8
From the Command Line
bash
Copy
Edit
python -m add 3 5
# Output: 8
🧪 Running Tests
bash
Copy
Edit
pytest tests/
🗂 Project Structure
bash
Copy
Edit
add/
├── add/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_add.py
├── setup.py
└── README.md
🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.


