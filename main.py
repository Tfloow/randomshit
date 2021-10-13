f = open("test.txt", "a")
f.write("test \n")
f.close()
print(open("test.txt", "r").read())
x = 1
a = 0.0134


def delete(file):
    d = open(file, "w")
    d.write("")
    d.close()


def angle(function):
    tangent = []
    for x in range(51):
        derivated = 2*a*x
        print(derivated)
        app = str(str(derivated) + "(x-" + str(x/2) + ")")
        tangent.append(app)
    print(tangent)


def speed(data):


angle(a*x**2)
print(open("billeDataset2.txt", "r").readlines()[3])
