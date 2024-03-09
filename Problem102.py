f = open("p0102_triangles.txt", "r")
triangles = []
for x in f:
    axisVals = x.split(",")
    formatted = axisVals[5].split("\n")
    axisVals[5] = formatted[0]
    triangles.append(axisVals)
def strListToIntList(strLst):
    intLst = []
    for x in strLst:
        intLst.append(int(x))
    return intLst

intTriangles = []
for x in triangles:
    intTriangles.append(strListToIntList(x))

def areaOfTriangle(coordLst):
    x1 = coordLst[0]
    y1 = coordLst[1]
    x2 = coordLst[2]
    y2 = coordLst[3]
    x3 = coordLst[4]
    y3 = coordLst[5]

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))/2.0)

def isInside(coordList, point):
    A = areaOfTriangle(coordList)

    coordA1 = [point[0],point[1],coordList[2],coordList[3],coordList[4],coordList[5]]
    A1 = areaOfTriangle(coordA1)

    coordA2 = [coordList[0],coordList[1],point[0],point[1], coordList[4],coordList[5]]
    A2 = areaOfTriangle(coordA2)

    coordA3 = [coordList[0], coordList[1],coordList[2],coordList[3] , point[0], point[1]]
    A3 = areaOfTriangle(coordA3)

    if A == A1+A2+A3:
        return True
    else:
        return False

counter = 0
for x in intTriangles:
    if(isInside(x,[0,0])) == True:
        counter += 1

print(counter)