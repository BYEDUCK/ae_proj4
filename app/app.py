import matplotlib.pyplot as plt
import numpy as np
from platypus import NSGAII, Problem, Real, nondominated
from scipy.optimize import minimize

if __name__ == '__main__':
    x_space = np.linspace(-12, 12, 100)
    x1 = np.power(np.subtract(x_space, 6), 2)
    x2 = np.power(x_space, 2)

    x1_prym = []
    x2_prym = []

    for alfa in np.arange(0, 1, 0.1):
        result = minimize(
            lambda x: alfa * (x[0] ** 2) + (1 - alfa) * ((x[0] - 6) ** 2),
            np.array([0]),
            method='SLSQP',
            bounds=[(-12, 12,)]
        )
        x1_prym.append((result.x[0] - 6) ** 2)
        x2_prym.append(result.x[0] ** 2)

    problem = Problem(1, 2)
    problem.types[:] = Real(-12, 12)
    nondominated_solutions = []


    def shaffer(x):
        return [x[0] ** 2, (x[0] - a - 1) ** 2]


    problem.function = shaffer

    for a in np.arange(0, 1, 0.1):
        algorithm = NSGAII(problem)
        algorithm.run(300)
        nondominated_solutions.append(nondominated(algorithm.result))

    for solutions in nondominated_solutions:
        print('---------')
        for solution in solutions:
            print(solution.objectives)
        print('---------')
    
    plt.figure(1)
    plt.plot(x1, x2, 'b-', x1_prym, x2_prym, 'r*')
    plt.axis([-5, 50, -5, 50])
    plt.xlabel('(x-6)^2')
    plt.ylabel('x^2')
    plt.grid(True)
    plt.show()
