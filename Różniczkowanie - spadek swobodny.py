import numpy as np
import matplotlib.pyplot as plt

global g
g = 9.81

class Rozniczkowanie:

    def spadek(self, dt):

        t = np.arange(0, 1000, dt)
        s = (0.5 * g * t ** 2) / 1E3

        x1 = []
        krok = 0

        for i in range(0, len(t)):
            x1.append(krok + g * t[i] * dt)
            krok = krok + g * t[i] * dt

        x = []

        for i in x1:
            x.append(i / 1E3)

        plt.plot(t, x, lw=2, label='numerycznie')
        plt.plot(t, s, lw=2, label='analitycznie')
        plt.xlabel("t [s]")
        plt.ylabel("s [km]")
        plt.legend(loc=2)
        plt.savefig('spad.pdf')
        plt.show()


# Bez append
    def spadek2(self, dt):

        t = np.arange(0, 1000, dt)
        s = (0.5 * g * t ** 2) / 1E3

        x = np.zeros(len(t))
        v = np.zeros(len(t))

#z definicji pochodnej
        for i in range(1, len(t)):
            v[i] = v[i - 1] + g * dt
            x[i] = x[i - 1] + v[i - 1] * dt

        x1 = []

        for i in x:
            x1.append(i / 1E3)

        plt.plot(t, x1, lw=2, label='numerycznie')
        plt.plot(t, s, lw=2, label='analitycznie')
        plt.xlabel("t [s]")
        plt.ylabel("s [km]")
        plt.legend(loc=2)
        plt.savefig('spad2.pdf')
        plt.show()

Rozniczkowanie().spadek(10)
Rozniczkowanie().spadek2(10)