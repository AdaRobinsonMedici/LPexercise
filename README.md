# SimpleLPProblem

A Python implementation of a simple linear programming (LP) problem using the PuLP library. This implementation defines decision variables, an objective function, and constraints to solve a maximization problem. The LP problem is solved using the PuLP solver and the optimal solution values are tested using the unittest module.

## Functionality

The `TestLPProblem` class defines a test case for the `lp_problem` function, which solves a simple LP problem with two decision variables, an objective function, and constraints. The LP problem is formulated as a maximization problem and the optimal solution values are asserted using the unittest assertions.

## Usage

To use this implementation, simply import the `TestLPProblem` class from the `unittest` module and run it using the `unittest.main()` function. The `TestLPProblem` class contains a single test case `test_lp_problem` which solves the LP problem and asserts the optimal solution values.

## Requirements

This implementation requires the following libraries to be installed:

- PuLP: A linear programming library for Python. Install using `pip install pulp`.
- unittest: A built-in module in Python for writing and running tests. No installation is required as it comes with Python.

## License

This implementation is open-source and available under the Apache License 2.0. Feel free to use, modify, and distribute it as per the terms of the license.

## Credits

This implementation was created by `ADA ROBINSON` on Thu Apr 06 15:53:00 2023.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
