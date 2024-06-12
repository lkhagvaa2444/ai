from scipy.optimize import linprog

# Coefficients of the objective function
c = [-3, -2, -5]  # Negate for maximization

# Coefficients of the inequality constraints
A = [
    [1, 1, 0],
    [2, 0, 1],
    [0, 1, 2]
]

# Right-hand side of the inequality constraints
b = [10, 9, 11]

# Bounds for the variables
x_bounds = (0, None)
y_bounds = (0, None)
z_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds, z_bounds], method='highs')

# Print the results
print(f"Optimal value: {-result.fun}")
print(f"Optimal solution: x={result.x[0]}, y={result.x[1]}, z={result.x[2]}")
