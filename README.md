# 5-ALIVEE

Team Information
-
**Team Name:** 5-ALIVE

**Team ID:** 16

Problem Statement
-
**Problem Number:** 3

**Problem Title:** Space Mission Fuel Optimiser

Instructions to Run the Code
-
1) Ensure Python is installed (tested on Python 3.8+).

2) Save the main code file as main.py.

3) Place the waypoints.txt file in the same directory.

4) Open a terminal/command prompt in the project directory.

5) Run the following command:
*----> python main.py*

Dependencies
-
Before running the program, install the necessary packages (if not already installed):

*----> pip install -r requirements.txt*

Expected Input File: waypoints.txt
-
Text file containing 3D coordinates.

Format: Each line represents one waypoint with three float values (x, y, z) separated by spaces.

**Example waypoints.txt:**

**1.0 2.0 3.0**

**4.0 5.0 6.0**

**7.0 8.0 9.0**

Expected Output File: path.txt
-
Text file containing:

1) The sequence of **waypoint IDs** (1-based indexing),

2) Followed by the **total travel cost** (distance).

**Example path.txt after execution:**

**1 2 3 1 20.78**

*Meaning: Start at waypoint 1 → waypoint 2 → waypoint 3 → return to waypoint 1, total travel distance = 20.78 units.*

**Output & testcase data Snippets:**
![Screenshot 2025-04-26 102849](https://github.com/user-attachments/assets/3272c1e2-2c18-49ee-a8da-8764af209c3e)  ![Screenshot 2025-04-26 102830](https://github.com/user-attachments/assets/b6db616b-0180-4166-8291-bc4bf8127a54)


