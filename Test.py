import itertools
from RM import *

# b = 7
# a = 6
# a = [-1]*4
# print(a)
# print(bin(a ^ b)[2:].zfill(3)[2])

# b = [False]*(4-1)
# print(b)
# print(int(b, 2))

# a = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
# pos = a.index(1)
# print(a.index(1, pos + 1))
# pos = a.index(1, pos + 1)
# print(a.index(1, pos + 1))

for i in range(16):
    rm1 = RM(1, 4)
    rm1.add_matrix_to_right(1)
    rm1.kick_column(i)
    rm1.mult_rm_matrix(rm1)
    rm2 = RM()
    rm2.copy(rm1)
    # rm2.print()
    rm1.dual()
    # rm1.print()
    rm1.conjunction(rm2)
    rm1.print()
