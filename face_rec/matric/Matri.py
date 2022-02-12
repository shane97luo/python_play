# This Python file uses the following encoding: utf-8

import numpy as np

class Matri:
    def __init__(self):
        pass

    def Eye(self, n):
        e = np.eye(n)
        e * e;

        m1 = np.array([
        [4, -1, 2, 1],
        [1, 1, 0, 3],
        [0, 3, 1, 4]
        ])

        m2 = np.array([
        [1, 2],
        [0, 1],
        [3, 0],
        [-1, 2]
        ])

        m_1 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ])

        m_2 = np.array([
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
        ])

        m3 = m_1*m_2
        m3_ = np.multiply(m_1, m_2)
        m4 = m_1 + m_2
        m5=np.matmul(m1, m2)
        print("\n============\n", m3)
        print("\n============\n", m4)
        print("\n============\n", m5)

        return
