# 🔐 SCT_CS_3 – Password Strength Checker
Task 03 – Evaluate Password Strength Using Multiple Security Criteria
Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters

This project implements a Password Strength Checker that analyzes a user's password based on widely accepted security standards. The tool evaluates the password structure and provides:

A strength rating (VERY WEAK → STRONG)

A detailed score breakdown

Helpful feedback

Suggestions to create a stronger password

It uses Python’s re (regular expressions) to check for character patterns and complexity.

🚀 Features

Evaluates password based on:

Length

Lowercase letters

Uppercase letters

Numbers

Special characters

Detection of common weak patterns

Returns:

A numerical score

Overall strength level

Color-coded indicator

Detailed feedback

Recommendations

Allows repeated checking until the user enters "quit"

🧠 Scoring System
Criteria	Points
Length (12+)	+3
Length (8–11)	+2
Length (6–7)	+1
Contains lowercase letters	+1
Contains uppercase letters	+1
Contains numbers	+1
Contains special characters	+2
Contains common patterns (e.g., “123”, “password”)	−1
🏷️ Strength Levels
Score	Strength	Indicator
7–8	STRONG	🟢
5–6	MODERATE	🟡
3–4	WEAK	🟠
0–2	VERY WEAK	🔴
📂 Project Structure
SCT_CS_3/
│── password_checker.py
│── README.md


🖥️ Example Output
Enter a password to check: SecurePass123!

PASSWORD STRENGTH: 🟢 STRONG
Score: 8/8

Detailed Feedback:
✓ Excellent length (12+ characters)
✓ Contains lowercase letters
✓ Contains uppercase letters
✓ Contains numbers
✓ Contains special characters

✓ Great job! Your password is strong.

🛠️ Requirements

Works with standard Python installation:

python3 password_checker.py


No additional libraries needed beyond Python's built-in re module.

🤝 Contributing

Pull requests and enhancements are welcome!


If you want, I can also generate:

📌 A logo/banner for the project
📌 A GUI version of the password checker (Tkinter)
📌 A web version using HTML/CSS/JS
