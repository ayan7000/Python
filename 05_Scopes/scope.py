
x =99

def f1():
    x=88
    def f2():
        print(x)
    return f2
f1()

myresult = f1()
myresult()


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g =  chaicoder(3)
print(f)
print(g)
