#https://github.com/ONETAPL3G3ND
class Test(dict):
    def __init__(self, **kwargs):
        print("innit")
        super().__init__(kwargs)

    def __setitem__(self, key, value):
        print(f"setitem: {value}")
        super().__setitem__(key, value * 3)

if __name__ == '__main__':
    t = Test(One=1, Two=2)
    t["five"] = 5
    print(t)
