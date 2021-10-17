import numpy


def delete(file):
    d = open(file, "w")
    d.write("")
    d.close()


def angle(x1, x2):
    tangent = []
    for x in range(x1, x2):
        derivated =70/2601 * x -70/51
        d = 35/2601*x**2-70/51*x+40 - derivated*x
        angleLow = numpy.arctan(numpy.absolute(derivated))*180/numpy.pi
        angleUp = 90 - angleLow
        app = str(str(x)+ str(" ") + str(derivated) + "(x)+" + str(d)+ " upper angle: "+ str(angleUp) + " lower angle :" + str(angleLow)+str("\n"))
        tangent.append(app)
        powDer = pow(derivated, 2)
        powDer1 = powDer+1
        powRac = pow(powDer1, 3)
        powRac = pow(powRac, 1/2)
        l=None
        ktop = 70/2601
        k = ktop/powRac
    print(numpy.array(tangent))
    pretty = "example: "
    """for f in range(x1, x2):
        pretty+= tangent[f]
    open("modified data.txt", "a").write(pretty)
    """
    return angleLow, k

def Sacceleration(h,e, Sspeed, r):
    conAngle =angle(73,74)[0]*numpy.pi/180
    print(conAngle)
    k = angle(73,74)[1]
    print(k)
    g = 9.81
    Sacceleration = 5*h*(-e*Sspeed**2*k-g*numpy.cos(conAngle)*e*Sspeed+h*g*numpy.sin(conAngle))/2*r**2+5*h**2
    print(Sacceleration)

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

#delete("modified data.txt")
#angle()
#print(open("billeDataset2.txt", "r").readlines()[3])
#speed(20)

Sacceleration(0.00795, 0.1,10, 0.008)
