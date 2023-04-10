# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:51:03 2023

@author: arobinson
"""

from pulp import *

# Create a LP problem
prob = LpProblem("SimpleLPProblem", LpMaximize)

# Define decision variables
x = LpVariable('x', lowBound=0)  # Variable x, lower bound 0
y = LpVariable('y', lowBound=0)  # Variable y, lower bound 0

# Define the objective function
prob += 2 * x + 3 * y  # Maximize 2x + 3y

# Define the constraints
prob += 3 * x + y <= 4  # Constraint: 3x + y <= 4
prob += x + 2 * y <= 5  # Constraint: x + 2y <= 5

# Solve the LP problem
prob.solve()

# Print the status of the solution
print("Status:", LpStatus[prob.status])

# Print the optimal solution values
print("Optimal Solution:")
print("x =", value(x))
print("y =", value(y))
print("Objective value =", value(prob.objective))
