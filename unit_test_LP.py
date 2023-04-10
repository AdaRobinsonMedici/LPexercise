# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:53:00 2023

@author: arobinson
"""

import unittest
from pulp import *

class TestLPProblem(unittest.TestCase):

    def test_lp_problem(self):
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

        # Assert the status of the solution is optimal
        self.assertEqual(prob.status, LpStatusOptimal)

        # Assert the optimal solution values
        self.assertAlmostEqual(value(x), 1.0, places=2)
        self.assertAlmostEqual(value(y), 1.5, places=2)
        self.assertAlmostEqual(value(prob.objective), 6.0, places=2)

if __name__ == '__main__':
    unittest.main()
