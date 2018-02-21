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

rm1 = RM(1, 4)
rm1.add_matrix_to_right()
rm1.rm_mult_matrix(rm1)
rm1.rm_dual()
# rm1.print_matrix()
# rm1.rm_dual()
# rm1.print_matrix()

# rm2 = RM(1, 4)
# rm1.rm_mult_matrix(rm1)
# rm1.rm_dual()
# rm1.rm_mult_matrix(rm1)
rm1.print_matrix()
