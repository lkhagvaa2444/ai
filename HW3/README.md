markdown
Copy code
# Linear Programming Problem Solver

## Overview

This project solves a linear programming problem using the `scipy.optimize.linprog` function from the SciPy library. The objective is to maximize the function \(3x + 2y + 5z\) subject to the given constraints.

## Problem Details

**Objective Function:**
\[ \text{Maximize } 3x + 2y + 5z \]

**Constraints:**
1. \( x + y \leq 10 \)
2. \( 2x + z \leq 9 \)
3. \( y + 2z \leq 11 \)
4. \( x \geq 0, y \geq 0, z \geq 0 \)

## Result

The optimal value and solution found by the solver are:

Optimal value: 29.0
Optimal solution: x=2.0, y=8.0, z=0.5