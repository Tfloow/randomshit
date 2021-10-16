import numpy


def delete(file):
    d = open(file, "w")
    d.write("")
    d.close()


def angle():
    tangent = []
    for x in range(105):
        derivated = 2 * 35/2601 * x -70/51
        d = 35/2601*x**2-70/51*x+40 - derivated*x
        angleLow = numpy.arctan(numpy.absolute(derivated))*180/numpy.pi
        angleUp = 90 - angleLow
        app = str(str(x)+ str(" ") + str(derivated) + "(x)+" + str(d)+ " upper angle: "+ str(angleUp) + " lower angle :" + str(angleLow)+str("\n"))
        tangent.append(app)
    print(numpy.array(tangent))
    pretty = "example: "
    for f in range(105):
        pretty+= tangent[f]
    open("modified data.txt", "w").write(pretty)


def speed(place):
    t = []
    x = []
    y = []
    v = 0
    i = 2
    r = []
    resultx = []
    resulty = []
    place = int(place)
    for k in range(3604):  # 3605
        tempx = []
        tempy = []
        for i in range(2):
            f = open("xbille.txt", "r")
            tempx.append(float(f.readlines()[2 + k + i][:16]))
            f.close()
        resultx.append(tempx[0] - tempx[1] / 0.016554757367439336)
        for i in range(2):
            f = open("ybille.txt", "r")
            tempy.append(float(f.readlines()[2 + k + i][:16]))
            f.close()
        resulty.append(tempy[0] - tempy[1] / 0.016554757367439336)
    print(numpy.array(resultx))
    print(numpy.array(resulty))

delete("modified data.txt")
angle()
print(open("billeDataset2.txt", "r").readlines()[3])
speed(20)
