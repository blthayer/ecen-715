"""Module for homework 3, problem 3.

NOTE: This module depends on Gurobi being installed and on the path. The
path to the license is set in the GUROBI_LICENSE path.
"""
# Pyomo recommends the following import, but I suspect it's only
# necessary when using Python2.
from __future__ import division
# Import pyomo model components.
from pyomo.environ import ConcreteModel, Var, Objective, Constraint, \
    SolverFactory
import os

# Define path to Gurobi license.
GUROBI_LICENSE = os.path.join('C:/', 'gurobi810', 'gurobi.lic')


def solve(d):
    """Helper method to create the model for this problem, with varying
    levels of demand.

    :param d: demand in MW.

    :returns model: initialized pyomo model.
    """
    # Initialize concrete model.
    model = ConcreteModel()
    # We'll have variables g1 and g2
    model.g = Var([1, 2])
    model.obj = Objective(expr=25*model.g[1] + 35*model.g[2])
    model.constraint1 = Constraint(expr=model.g[1] + model.g[2] == d)
    model.constraint2 = Constraint(rule=gen1_constraint)
    model.constraint3 = Constraint(rule=gen2_constraint)
    # Alternatively to specifying a rule which returns a 3 element
    # tuple, the generator constraints can be added individually.
    # model.constraint4 = Constraint(expr=model.g[2] >= 20)
    # model.constraint5 = Constraint(expr=model.g[2] <= 100)
    return model


def gen1_constraint(model):
    """Constraint for generator 1.
    10 <= g1 <= 50.
    """
    return 10, model.g[1], 50


def gen2_constraint(model):
    """Constraint for generator 2.
    20 <= g2 <= 100.
    """
    return 20, model.g[2], 100


def print_model_generation(model):
    """Helper to print results."""
    print('g1 = {} MW'.format(model.g[1].value))
    print('g2 = {} MW'.format(model.g[2].value))


if __name__ == '__main__':
    # Gurobi must have the license path stored in the following
    # environment variable:
    os.environ['GRB_LICENSE_FILE'] = GUROBI_LICENSE
    # Initialize Gurobi solver.
    opt = SolverFactory('gurobi')
    # 50MW demand case.
    print('*' * 80)
    print('d = 50')
    m1 = solve(50)
    r1 = opt.solve(m1)  # ,tee=True
    print('Results:')
    print_model_generation(m1)
    # m1.display()
    # m1.pprint()
    # m1.g.pprint()
    # 100MW demand case.
    print('*' * 80)
    print('d = 100')
    m2 = solve(100)
    r2 = opt.solve(m2)
    print('Results:')
    print_model_generation(m2)
    # m2.g.pprint()
    pass
