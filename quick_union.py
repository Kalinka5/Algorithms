class QuickUnionUF:
    def __init__(self, n) -> None:
        self.id = [i for i in range(n)]
    
    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j

    def show_list(self):
        return self.id


# Testing
uf = QuickUnionUF(10)
all_list = uf.show_list()
print(all_list) 

uf.union(4, 3)
uf.union(3, 8)
uf.union(6, 5)
uf.union(9, 4)
uf.union(2, 1)
uf.union(5, 0)
uf.union(7, 2)
uf.union(6, 1)
uf.union(7, 3)

all_list = uf.show_list()
print(all_list)
