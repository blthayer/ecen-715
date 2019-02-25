"""
Module for Homework 2, problem 2. Using a system of complex equations
to confirm my by-hand Thevenin equivalent method.
"""
import numpy as np

if __name__ == '__main__':
    v1 = 100
    v2 = 1j*100

    z1 = 6
    z2 = 1j*4
    z3 = 1j*-10
    z4 = 5

    A = np.array(
        [
            [-(z1 + z2),    0,      -z4],
            [1,             -1,     -1],
            [-(z1 + z2),    -z3,    0]]
    )

    b = np.array([
        [-v1 + v2],
        [0],
        [-v1]
    ])

    x = np.linalg.solve(A, b)

    print('currents:')
    print(x)

    i1 = x[0][0]
    i2 = x[1][0]
    i3 = x[2][0]

    print('Power generated by v1:')
    print(v1 * np.conj(i1))
    print('Power generated by v2:')
    print(v2 * -np.conj(i3))
    print('Power absorbed by z1:')
    print((v1 - (i1 * z2) - (i2 * z3)) * np.conj(i1))
    print('Power absorbed by z2:')
    print((v1 - (i1 * z1) - (i2 * z3)) * np.conj(i1))
    print('Power absorbed by z3:')
    print((v1 - (i1 * (z1 + z2))) * np.conj(i2))
    print('Power absorbed by z4:')
    print((v1 - (i1 * (z1 + z2)) - v2) * np.conj(i3))

    print('')
    print('Calculate i2 via Thevenin equivalents:')
    zth = ((z1 + z2) * z4) / (z1 + z2 + z4)
    i_temp = (v1 - v2) / (z1 + z2 + z4)
    vth = v1 - i_temp * (z1 + z2)
    i2_th = vth / (zth + z3)
    print(i2_th)