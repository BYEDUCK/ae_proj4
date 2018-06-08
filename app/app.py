import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.arange(-12, 12, 0.1)
    x1 = np.power(np.subtract(x, 6), 2)
    x2 = np.power(x, 2)

    plt.figure(1)
    plt.plot(x1, x2, 'b-')
    plt.xlabel('(x-6)^2')
    plt.ylabel('x^2')
    plt.grid(True)
    plt.axis([-30, 60, -30, 100])
    plt.show()
