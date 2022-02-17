class BTreeNode:

    def __init__(self):
        self.data = []
        self.children = []
        self.leaf = False
        self.n = 0



class Globals:
    root = None
    np = None
    current_pointer = None
    haskey = set()

    @staticmethod
    def init():
        i = None
        Globals.np = BTreeNode()
        Globals.np.data = [0 for _ in range(5)]
        Globals.np.children = [None for _ in range(6)]
        Globals.np.leaf = True
        Globals.np.n = 0
        for i in range(0, 6):
            Globals.np.children[i] = None
        return Globals.np

    @staticmethod
    def lookup(p, target):
        Globals.help(p, target)
        return Globals.haskey.__contains__(target)

    @staticmethod
    def help(p, target):
        i = None
        i = 0
        while i < p.n:
            if p.leaf is False:
                Globals.help(p.children[i], target)

            Globals.haskey.add(p.data[i])
            i += 1

        if p.leaf is False:
            Globals.help(p.children[i], target)

    @staticmethod
    def display(p, target):
        print("")
        i = 0
        while i < p.n:
            if p.leaf is False:
                Globals.display(p.children[i], target)
            print(p.data[i], end="")
            i += 1

        if p.leaf is False:
            Globals.display(p.children[i], target)
        print("")

    @staticmethod
    def sort(p, n):
        i = None
        j = None
        temp = None
        for i in range(0, n):
            for j in range(i, n + 1):
                if p[i] > p[j]:
                    temp = p[i]
                    p[i] = p[j]
                    p[j] = temp
    @staticmethod
    def insert(a):
        i = None
        temp = None
        Globals.current_pointer = Globals.root
        if Globals.current_pointer is None:
            Globals.root = Globals.init()
            Globals.current_pointer = Globals.root
        else:
            if Globals.current_pointer.leaf is True and Globals.current_pointer.n == 5:
                temp = Globals.split_child(Globals.current_pointer, -1)
                Globals.current_pointer = Globals.root
                i = 0
                while i < (Globals.current_pointer.n):
                    if (a > Globals.current_pointer.data[i]) and (a < Globals.current_pointer.data[i + 1]):
                        i += 1
                        break
                    elif a < Globals.current_pointer.data[0]:
                        break
                    else:
                        i += 1
                        continue

                Globals.current_pointer = Globals.current_pointer.children[i]
            else:
                while Globals.current_pointer.leaf == False:
                    i = 0
                    while i < (Globals.current_pointer.n):
                        if i + 1 < 5 and (a > Globals.current_pointer.data[i]) and (a < Globals.current_pointer.data[i + 1]):
                            i += 1
                            break
                        elif a < Globals.current_pointer.data[0]:
                            break
                        else:
                            i += 1
                            continue

                    if (Globals.current_pointer.children[i]).n == 5:

                        temp = Globals.split_child(Globals.current_pointer, i)
                        Globals.current_pointer.data[Globals.current_pointer.n] = temp
                        Globals.current_pointer.n += 1
                        continue
                    else:
                        Globals.current_pointer = Globals.current_pointer.children[i]
        Globals.current_pointer.data[Globals.current_pointer.n] = a
        Globals.sort(Globals.current_pointer.data, Globals.current_pointer.n)
        Globals.current_pointer.n += 1

    @staticmethod
    def split_child(current_pointer, i):
        j = None
        mid = None
        np1 = None
        np3 = None
        y = None
       # TreeNode np1, *np3, *y
        np3 = Globals.init()
        np3.leaf = True
        if i == -1:
            mid = current_pointer.data[2]
            current_pointer.data[2] = 0
            current_pointer.n -= 1
            np1 = Globals.init()
            np1.leaf = False
            current_pointer.leaf = True
            for j in range(3, 5):
                np3.data[j - 3] = current_pointer.data[j]
                np3.children[j - 3] = current_pointer.children[j]
                np3.n += 1
                current_pointer.data[j] = 0
                current_pointer.n -= 1
            for j in range(0, 6):
                current_pointer.children[j] = None
            np1.data[0] = mid
            np1.children[np1.n] = current_pointer
            np1.children[np1.n + 1] = np3
            np1.n += 1
            Globals.root = np1
        else:
            y = current_pointer.children[i]
            mid = y.data[2]
            y.data[2] = 0
            y.n -= 1
            for j in range(3, 5):
                np3.data[j - 3] = y.data[j]
                np3.n += 1
                y.data[j] = 0
                y.n -= 1


            current_pointer.children[i + 1] = y
            current_pointer.children[i + 1] = np3
        return mid

if __name__ == '__main__':
    c = Globals()
    for i in range(0, 20):
        c.insert(i)
#    c.insert(25)
 #   # c.insert(23)
    # c.insert(20)
    print("insert numbers from 0 - 19")

    if c.lookup(c.root, 2):
        print("2 is found")
    if c.lookup(c.root, 4):
        print("4 is found")
    if c.lookup(c.root, 8):
        print("8 is found")
    if not c.lookup(c.root, 22):
        print("22 is not found")
    if not c.lookup(c.root, 23):
        print("32 is not found")
    if c.lookup(c.root, 13):
        print("12 is found")


