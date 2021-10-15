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
    r = []
    place = int(place)
    for i in range(2):
        f = open(data, "r")
        r.append(float(f.readlines()[place + i][:10]))
        f.close()
    result =
    print(r)
    print(r)
    print(result)

angle(a*x**2)
print(open("billeDataset2.txt", "r").readlines()[3])
speed("billeDataset2.txt", 20)
