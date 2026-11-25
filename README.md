# Traffic-Violation
# 🚦 Traffic Violation Penalty Calculator

## 📌 Project Overview

The **Traffic Violation Penalty Calculator** is a Python-based application designed to calculate traffic violation penalties based on vehicle categories, offence types, and repeat-offence status.

The system processes multiple traffic violations, calculates individual fines, determines the total penalty, and identifies possible driving licence disqualification conditions based on predefined rules.

## 🎯 Objectives

- Identify different vehicle categories.
- Process multiple traffic violations.
- Calculate penalties based on offence types.
- Apply additional penalties for repeat offences.
- Calculate the total traffic penalty.
- Assign violation points.
- Identify possible disqualification conditions.
- Generate a detailed penalty report.

## 🚗 Vehicle Categories

The system supports three vehicle categories:

1. Two Wheeler
2. Car
3. Commercial Vehicle

## ⚖️ Traffic Violation Fine Rules

The project uses the following sample fine structure:

| Offence | Two Wheeler | Car | Commercial |
|---|---:|---:|---:|
| Overspeeding | ₹1,000 | ₹1,500 | ₹2,000 |
| Signal Jumping | ₹1,000 | ₹1,000 | ₹1,500 |
| No Helmet | ₹500 | ₹0 | ₹0 |
| No Seatbelt | ₹0 | ₹500 | ₹500 |
| Drunk Driving | ₹5,000 | ₹5,000 | ₹10,000 |
| Dangerous Driving | ₹5,000 | ₹5,000 | ₹10,000 |

**Note:** These amounts are illustrative academic values and do not represent official government traffic fines.

## 🚀 Features

1. Vehicle category selection.
2. Multiple violation processing.
3. Different offence identification.
4. Repeat-offence detection.
5. Automatic penalty calculation.
6. Total fine calculation.
7. Violation point calculation.
8. Disqualification condition checking.
9. Detailed penalty report generation.

## 🔁 Repeat-Offence Calculation

The system applies the following sample rule:

- First offence: Normal fine.
- Repeat offence: Double the normal fine.

Example:

```text
Normal Fine = ₹1,000

Repeat Offence Fine = ₹1,000 × 2

Final Fine = ₹2,000
```

## 🚫 Disqualification Conditions

The system checks the following sample conditions:

- Serious offences such as drunk driving.
- Dangerous driving.
- Total violation points reaching 10 or more.

If any condition is satisfied, the program displays:

**DISQUALIFICATION REVIEW REQUIRED**

This is an educational simulation, not an actual licence suspension decision.

## 💻 Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

## 🐍 Python Concepts Used

- Variables and Data Types
- Dictionaries
- Lists
- Conditional Statements
- For Loops
- While Loops
- Functions
- Arithmetic Operators
- User Input and Output

## 📁 Project Structure

```text
Traffic-Violation-Penalty-Calculator/
│
├── traffic_violation.py
├── README.md
├── problem_statement.txt
├── objectives.txt
├── assumptions.txt
├── algorithm.txt
├── pseudocode.txt
├── flowchart.png
├── test_cases.txt
│
└── output_screenshots/
    ├── output1.png
    ├── output2.png
    └── output3.png
```

## ▶️ How to Run the Project

**Step 1:** Install Python 3.

**Step 2:** Download or clone the project repository.

**Step 3:** Open the project folder in Visual Studio Code.

**Step 4:** Open the terminal.

**Step 5:** Run the following command:

```bash
python traffic_violation.py
```

**Step 6:** Select the vehicle category.

**Step 7:** Enter the number of violations.

**Step 8:** Select the offence types and specify whether each offence is repeated.

**Step 9:** View the final penalty report.

## 🧪 Test Cases

| Test Case | Input / Condition | Expected Result |
|---|---|---|
| TC01 | Car + Overspeeding | Fine ₹1,500 |
| TC02 | Two-wheeler + No Helmet | Fine ₹500 |
| TC03 | Car + No Seatbelt | Fine ₹500 |
| TC04 | Car + Repeat Overspeeding | Fine ₹3,000 |
| TC05 | Two-wheeler + Drunk Driving | Fine ₹5,000 and review required |
| TC06 | Dangerous Driving | Disqualification review required |
| TC07 | Total points reach 10 | Disqualification review required |
| TC08 | Multiple violations | Combined penalty calculated |

## 📊 Expected Output

The program displays:

- Selected vehicle category.
- Number of traffic violations.
- Offence details.
- Repeat-offence status.
- Individual penalty amounts.
- Violation points.
- Total penalty amount.
- Disqualification review status.

## 📝 Conclusion

The Traffic Violation Penalty Calculator provides a simple and systematic method for calculating traffic penalties using Python.

It processes multiple traffic violations based on vehicle categories, offence types, and repeat-offence conditions.

The system also calculates total penalties and identifies possible disqualification conditions using predefined rules.

This project demonstrates the practical application of fundamental Python programming concepts in traffic penalty management.

---

**Project Name:** Traffic Violation Penalty Calculator

**Subject:** Python Activity-Based Learning 
name : sree hasini
section:5

**Programming Language:** Python 3

**Project Type:** Case Study
