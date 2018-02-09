import itertools


class RM:
    def __init__(self, r, m):
        if r > m or r < 1 or m < 1:
            raise Exception
        self.r = r
        self.m = m
        self.n = 2 ** m
        self.G = self.__createG__()
        self.k = len(self.G)

    def __createG__(self):
        G = [[1]*self.n]
        count = self.n
        for m in range(self.m):
            count //= 2
            G.append(2**m * ([0]*count + [1]*count))
        help_matrix = G.copy()
        help_matrix.pop(0)
        for r in range(2, self.r + 1):
            for combo in itertools.combinations(help_matrix, r):
                help_row = [1]*self.n
                for row in combo:
                    help_row = list(map(lambda x, y: x*y, help_row, row))
                G.append(help_row)
        return G

    def print_matrix(self):
        count = 1
        for row in self.G:
            print(row, count)
            count += 1

    def copy_RM(self, another_RM):
        self.k = another_RM.k
        self.n = another_RM.n
        self.m = another_RM.m
        self.r = another_RM.r
        self.G = another_RM.G.copy()

    def mult_matrix(self, another_RM):
        pass

# def gen(k, n):
#     c = []
#     i = 2 ** n - 1
#     while i != -1:
#         b = bin(i)[2:]
#         b = '0'*(n - len(b)) + b
#         c.append([int(z) for z in b])
#         i -= 1
#     for y in itertools.combinations(c, k):
#         yield y

