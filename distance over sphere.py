# Distance between coordinates over spehere

import math

# geocoordinates lat, lon with all angles measured from the x-axis
start = [90, 0]
end = [0, 0]

rearth = 6.3781 * 10**6  # radius of the earth (m)

# convert so the angle of the lat- coordinate is meausured from the y- axis
pointOne = [math.radians(start[0] - 90), math.radians(start[1])]
pointTwo = [math.radians(end[0] - 90), math.radians(end[1])]


def domath(posstart, posend):
    # convert the coordinates to vectors
    # asume the radius =1, the radius wont be relevant for calculating the angle between the vectors
    v1 = [math.sin(posstart[0]) * math.cos(posstart[1]), math.sin(posstart[0])
          * math.sin(posstart[1]),  math.cos(posstart[0])]

    v2 = [math.sin(posend[0]) * math.cos(posend[1]), math.sin(posend[0])
          * math.sin(posend[1]), math.cos(posend[0])]

    # calculate the length of the vectors
    absv1 = math.sqrt(math.pow(v1[0], 2) + math.pow(v1[2], 2) + math.pow(v1[2], 2))
    absv2 = math.sqrt(math.pow(v2[0], 2) + math.pow(v2[2], 2) + math.pow(v2[2], 2))

    # calculate the angle between the vectors according to yhe formula:
    # |v1|*|v2|*cos(a) = v1x*v2x + v1y*v2y + v1z*v2z
    a = math.acos(((v1[0] * v2[0]) + (v1[1] * v2[1]) + (v1[2] * v2[2])) / (absv1 * absv2))

    # calculate the distance over the sphere
    # part of the circumference(a/360) * whole circumference(2*r*pi)
    distance = (a / (2 * math.pi)) * (rearth * 2 * math.pi)  # now the radius is relewant

    return distance


distance = domath(pointOne, pointTwo)

print('Distance from: ' + str(start) + ' till: ' + str(end))
print(str(distance / 1000) + ' km')
