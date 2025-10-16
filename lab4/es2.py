"""
Implement a class Chain that represents a broken line (also called polygonal
chain, "spezzata" in Italian) on a cartesian plane.
The broken line is represented as an ordered list of points (passed as a parameter 
to the __init__ method; the order of the appearance of the points in the list indicates 
the order in which the points are connected). The list is memorized as the only attribute 
(private) of the class.

Implement the following methods:
    - delete_point which deletes the last point of the broken line and returns the deleted point;
    - add_point which adds a new point at the end of the broken line and returns the added point;
    - dist_extremes which determines and returns (as a float) the Euclidean distance between the first and last point of the broken line;
    - __len__ which determines and returns (converted to int) the length of the broken line as the sum of the segments that make it up.

Points are instances of the Point class seen during lectures.

Add to class Point a new method distance that returns the euclidean distance (as a float) 
between the point and another passed as a parameter.
"""

import math

class Point:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

    def whoareyou(self):
        return self.x, self.y
    
    def __str__(self):
        return "Point" + str(self.whoareyou())
    
    def distance(self, point):
        return math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)

class Chain:
    def __init__(self, points: list):
        self.__points = points

    def delete_point(self):
        return (self.__points.pop(len(self.__points) - 1))
    
    def add_point(self, new_point):
        self.__points.append(new_point)

        return new_point
    
    def dist_extremes(self):
        return self.__points[0].distance(self.__points[len(self.__points) - 1])
    
    def __len__(self):
        list_distances = []
        for i in range(len(self.__points) - 1):
            list_distances.append(self.__points[i].distance(self.__points[i + 1]))

        _sum = sum(list_distances)

        return int(_sum) 

print(Chain([Point(0,0), Point(0,3), Point(4,0)]).dist_extremes())