import math


# from Charts import *


def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)


# from scipy.stats import t

# CONST
pi = 3.14159265
Yc = 17.3 * (10 ** -6)


class Calculation:
    def __init__(self, n0, i, s1, n1, s2, n2):
        self.s0 = None

        if n0 == n1:
            raise 'n0 = n1'
        if n1 == n2:
            raise 'n1 = n2'
        if n2 == n0:
            raise 'n0 = n2'

        if n0 < n1:
            if n0 < n2:
                self.s0 = (s1 / (pow(1 + i, n1 - n0))) + s2 / (pow(1 + i, n2 - n1))
            else:
                self.s0 = (s1 / (pow(1 + i, n0 - n1))) + s2 * (pow(1 + i, n0 - n2))
        else:
            if n0 < n2:
                self.s0 = s1 * (pow(1 + i, n0 - n1)) + s2 / (pow(1 + i, n2 - n0))
            else:
                self.n0 = s1 * pow(1 + i, n0 - n1) + s2 * pow(1 + i, n0 - n2)


if __name__ == "__main__":
    n0 = 1
    i = 2
    s1 = 3
    n1 = 4
    s2 = 5
    n2 = 6
    calculation = Calculation(n0, i, s1, n1, s2, n2)
    print(calculation.s0)
    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
