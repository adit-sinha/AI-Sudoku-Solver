# Sudoku-Solver

This project is a full scale implementation of an automated Constraint Satisfacation solver for Sudoku. It uses the following principles for the implementation:
- Arc Consistency functions
- Backtracking search
- Data Plotting and File Handling

## Arc Consistency functions
These functions simplify the problem by reducing the domain of the variables before or while the solution is in progress. As per its wording, it ensures the data selected is consistent with the constraints established in the problem. 

## Backtracking search
Backtracking is an algorithm used to examine all possible configurations of a state space. In this case, we analyze the state space of the 9x9 sudoku and **backtrack** when a valid solution is not possible. It is the core algorithm for solving Sudoku since it is a constraint satisfaction problem (a problem where to assign values to a set of variables, we must abide by certain constraints).

## Data Plotting and File Handling<br>
The data for the sudoku is fetched from the array of sudoku provided and is plotted using the Constraint Satisfaction solver.
