# 🐍 Interactive Personal Data Collector

A simple **Python beginner project** that collects basic information from the user and displays the entered data along with its **data type** and **memory address**.

## 🔗 Live Demo

👉 **Run the project online:**
https://onlinegdb.com/B2Z3w1t7v

## 📌 GitHub Repository

👉 **GitHub:**
https://github.com/JAYRAJSINH2703/My-project

---

## 📖 About the Project

The **Interactive Personal Data Collector** is a Python program designed to demonstrate basic Python concepts through an interactive program.

The program asks the user to enter:

* Name
* Age
* Height
* Favourite Number

After collecting the information, it displays the entered values, their Python data types, and their memory addresses.

It also approximately calculates the user's birth year based on the entered age.

---

## ✨ Features

* 👤 Takes the user's name as input
* 🎂 Takes the user's age
* 📏 Takes height in meters
* 🔢 Takes a favourite number
* 🧩 Displays the data type of each value
* 💾 Displays the memory address using Python's `id()` function
* 📅 Calculates an approximate birth year
* 🖥️ Provides an interactive console-based experience

---

## 🛠️ Technologies Used

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| Python     | Programming Language               |
| `input()`  | Taking user input                  |
| `int()`    | Converting input to integer        |
| `float()`  | Converting input to decimal number |
| `type()`   | Checking data type                 |
| `id()`     | Getting object's memory identity   |

---

## 📂 Project Structure

```text
My-project/
│
├── My_Project.py
│
└── README.md
```

---

## 💻 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/JAYRAJSINH2703/My-project.git
```

### 2. Open the project

```bash
cd My-project
```

### 3. Run the Python file

```bash
python My_Project.py
```

---

## 🧑‍💻 Example

```text
Welcome to the Interactive Personal Data collector !

Please Enter Your Name : Jayraj
Please Enter Your Age : 18
Please Enter You Height in meters : 1.75
Please Enter Your Favourite Number : 7

Thank You ! Here is the information that we collect from you

Name : Jayraj <class 'str'>
Age : 18 <class 'int'>
Height : 1.75 <class 'float'>
Favourite Number : 7 <class 'int'>

Your Birth Year is Approximately: 2008 (Based On Your Age)

Thank You For Using Personal Data Collector
```

---

## 📚 Python Concepts Demonstrated

### 1. Variables

The program stores user information in variables such as:

```python
Name
Age
Height
Fav
```

### 2. User Input

The `input()` function is used to take information from the user.

```python
Name = input("Please Enter Your Name :")
```

### 3. Type Casting

The program converts input into integer and floating-point values.

```python
Age = int(input("Please Enter Your Age :"))
Height = float(input("Please Enter You Height in meters :"))
```

### 4. Data Types

The `type()` function displays the data type of a variable.

```python
type(Name)
type(Age)
type(Height)
```

### 5. Memory Identity

The `id()` function displays the identity associated with an object.

```python
id(Name)
id(Age)
```

### 6. Basic Calculation

The program calculates an approximate birth year using:

```python
age = 2026 - Age
```

---

## 🎯 Learning Objectives

This project helps beginners understand:

* Python variables
* User input
* Type casting
* String, integer and float data types
* The `type()` function
* The `id()` function
* Basic arithmetic operations
* Console output using `print()`

---

## 👨‍💻 Author

**Jayrajsinh**

GitHub:
https://github.com/JAYRAJSINH2703

---

## 📄 License

This project is created for **educational and learning purposes**.
