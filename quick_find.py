class QuickFindUF:
    def __init__(self, n) -> None:
        self.id = [i for i in range(n)]
    
    def connected(self, p, q):
        return self.id[p] == self.id[q]
    
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid
    
    def show_list(self):
        return self.id

uf = QuickFindUF(10)
all_list = uf.show_list()
print(all_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

not_connected = uf.connected(0, 4)
print(not_connected)  # False

uf.union(0, 4)  # Connect ids 0 and 4

connected = uf.connected(0, 4)
print(connected)  # True

connected = uf.union(4, 5)
connected = uf.union(7, 9)
connected = uf.union(6, 7)

# Testing
# uf.union(4, 3)
# uf.union(3, 8)
# uf.union(6, 5)
# uf.union(9, 4)
# uf.union(2, 1)
# uf.union(5, 0)
# uf.union(7, 2)
# uf.union(6, 1)
# print(uf.connected(8, 9))
# print(uf.connected(0, 7))

all_list = uf.show_list()
print(all_list)  # Returns all changed ids
