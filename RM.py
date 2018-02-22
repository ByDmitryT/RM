import itertools


class RM:
    def __init__(self, r, m):
        if r > m or r < 1 or m < 1:
            raise Exception("r > m")
        self.r = r
        self.m = m
        self.n = 2 ** m
        self.generating_matrix = self.__create_generating_matrix__()
        self.k = len(self.generating_matrix)

    def __create_generating_matrix__(self):
        generating_matrix = [2 ** self.n - 1]
        count = self.n
        for m in range(self.m):
            count //= 2
            generating_matrix.append(int('0b' + 2**m * ('0'*count + '1'*count), 2))
        help_matrix = generating_matrix.copy()
        single_row = help_matrix.pop(0)
        for r in range(2, self.r + 1):
            for combo in itertools.combinations(help_matrix, r):
                help_row = single_row
                for row in combo:
                    help_row &= row
                generating_matrix.append(help_row)
        return generating_matrix

    def __bin__(self, number):
        return bin(number)[2:].zfill(self.n)

    def print(self):
        for row in self.generating_matrix:
            print(self.__bin__(row))
        # print('r =', self.r)
        # print('m =', self.m)
        print('n =', self.n)
        print('k =', self.k)

    def copy_RM(self, another_RM):
        self.k = another_RM.k
        self.n = another_RM.n
        self.m = another_RM.m
        self.r = another_RM.r
        self.generating_matrix = another_RM.generating_matrix.copy()

    def rm_mult_matrix(self, another_RM):
        if self.m != another_RM.m:
            raise Exception("columns are not equal")
        help_matrix = self.generating_matrix.copy()
        for row, another_row in itertools.product(help_matrix, another_RM.generating_matrix):
            new_row = row & another_row
            if new_row not in self.generating_matrix:
                self.generating_matrix.append(new_row)
        if self.r + another_RM.r < self.m:
            self.r += another_RM.r
        else:
            self.r = self.m
        self.k = len(self.generating_matrix)

    def rm_dual(self):
        positions_stepped_view = [-1] * self.n
        row_pos = 0
        while row_pos != self.k:
            remaining_rows = self.generating_matrix.copy()
            row = remaining_rows.pop(row_pos)
            column_in_row_pos = 0
            for column_in_row in self.__bin__(row):
                if column_in_row == '1':
                    if positions_stepped_view[column_in_row_pos] == -1:
                        for remaining_row in remaining_rows:
                            if self.__bin__(remaining_row)[column_in_row_pos] == '1':
                                self.generating_matrix[self.generating_matrix.index(remaining_row)] ^= row
                        positions_stepped_view[column_in_row_pos] = row_pos
                    break
                column_in_row_pos += 1
            row_pos += 1
        #
        # next step
        #
        #
        # kill null
        #
        while 0 in self.generating_matrix:
            self.generating_matrix.pop(self.generating_matrix.index(0))
        self.k = len(self.generating_matrix)
        #
        # next step
        #
        row_pos = 0
        single_matrix_pos = -1
        helper_matrix = []
        while row_pos != self.n - self.k:
            helper_row = ''
            single_matrix_pos = positions_stepped_view.index(-1, single_matrix_pos + 1)
            pos_in_positions = 0
            for position_stepped_view in positions_stepped_view:
                if position_stepped_view == -1:
                    if pos_in_positions == single_matrix_pos:
                        helper_row += '1'
                    else:
                        helper_row += '0'
                else:
                    helper_row += self.__bin__(self.generating_matrix[position_stepped_view])[single_matrix_pos]
                pos_in_positions += 1
            helper_matrix.append(int('0b' + helper_row, 2))
            row_pos += 1
        self.generating_matrix = helper_matrix
        self.r = self.m - self.r - 1
        self.k = len(self.generating_matrix)

    def add_matrix_to_right(self, number_of_columns):
        new_matrix = ''
        for i in range(number_of_columns):
            new_matrix += '0' * i + '1' + '0' * (self.k - i - 1)
        for i in range(number_of_columns):
            for j in range(self.k):
                self.generating_matrix[j] = int(self.__bin__(self.generating_matrix[j]) + new_matrix[i * self.k + j], 2)
            self.n += 1

    def conjunction(self, another_RM):
        self.generating_matrix += another_RM.generating_matrix
        self.k += another_RM.k
        self.rm_dual()
