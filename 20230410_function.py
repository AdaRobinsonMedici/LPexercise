from pulp import *

if i='A' then
sum (j, F(j,'A')*xj(j)) <=4;
elseif i='B' then
sum (j, F(j,'B')*xj(j)) <=8;
else if i='C' then 
sum (j, F(j,'C')*xj(j)) <=6;


# Define the sets
Chemicals = ['P1', 'P2', 'P3']
Feedstock = ['A', 'B', 'C']
MaxSupply = {'A': 4, 'B': 8, 'C': 6}

# Define the parameters
F = {(chemical, feedstock): value for (chemical, feedstock), value in
     {'P1': {'A': 2, 'B': 1, 'C': 0}, 'P2': {'A': 0, 'B': 0, 'C': 3}, 'P3': {'A': 0, 'B': 2, 'C': 1}}.items()}
Profit = {'P1': 3, 'P2': 4, 'P3': 6}

# Create the LP problem
prob = LpProblem("Maximize Profit", LpMaximize)

# Define the decision variables
x = LpVariable.dicts("x", Chemicals, lowBound=0, cat='Continuous')

# Define the objective function
prob += lpSum([Profit[j] * x[j] for j in Chemicals])

# Define the constraints
for i in Feedstock:
    prob += lpSum([F[j, i] * x[j] for j in Chemicals]) <= MaxSupply[i]

# Solve the LP problem
prob.solve()
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

