from sys import argv

class Fish():
    def __init__(self, f_name, l_name="fish"):
        self.f_name = f_name
        self.l_name = l_name

    def swim(self):
        print("{0} {1} swims".format(self.f_name, self.l_name))

class Trout(Fish):
    pass

class Salmon(Fish):
    def __init__(self, f_name, l_name="Fish"):
        self.l_name = l_name
        self.f_name = f_name

if __name__ == "__main__":
    t = Trout(argv[1])
    t.swim()
    s = Salmon(argv[1])
    s.swim()
