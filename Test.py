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

rm1 = RM(1, 3)
rm2 = RM(1, 1)
rm1.add_matrix_to_right(1)
rm2.copy_RM(rm1)
rm2.print()
rm1.rm_dual()
rm1.print()
rm1.conjunction(rm2)
rm1.print()
