# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:14:36 2023

@author: arobinson
"""

import unittest
from pulp import *

class TestLPProblem(unittest.TestCase):

    def test_lp_problem(self):
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

        # Assert the status of the solution is optimal
        self.assertEqual(prob.status, LpStatusOptimal)

        # Assert the optimal solution value
        self.assertAlmostEqual(value(prob.objective), 36, places=2)

if __name__ == '__main__':
    unittest.main()