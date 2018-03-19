import itertools
from RM import *

# r, m = 2, 6
# add_col = 3
#
# for i in range(2**m + 3):
#     rm1 = RM(r, m)
#     rm1.add_matrix_to_right(add_col)
#     rm1.kick_column(i)
#     rm1.mult_rm_matrix(rm1)
#     rm2 = RM()
#     rm2.copy(rm1)
#     # rm2.print()
#     rm1.dual()
#     # rm1.print()
#     rm1.conjunction(rm2)
#     rm1.print()

rm1 = RM(1, 6)
rm1.add_matrix_to_right(4)
rm1.mult_rm_matrix(rm1)
rm1.print()