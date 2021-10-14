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


def speed(data, place):
    t = []
    x = []
    y = []
    v = 0
    i = 2
    place = int(place)
    f = open(data, "r")
    r = float(f.readlines()[place + i][:10])
    f.close()
    f = open(data, "r")
    r2 = float(f.readlines()[place + 1][:10])
    print(r2)
    result = r2 - r
    print(r)
    print(result)

angle(a*x**2)
print(open("billeDataset2.txt", "r").readlines()[3])
speed("billeDataset2.txt", 20)
