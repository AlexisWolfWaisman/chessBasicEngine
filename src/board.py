from string import ascii_lowercase as abc
from itertools import product as prodCartesiano
global edgeLong
global board
global X_axis
global Y_axis
edgeLong = 8
board = list(prodCartesiano(range(1,edgeLong+1),range(1,edgeLong+1)))


replaceAll = lambda list,value: [value for x in list]
matrixFormBoard = [list(range(1,edgeLong+1)) for x in range(1,edgeLong+1)]
matrixFormBoard = [replaceAll(element," ") for element in matrixFormBoard ]

# coordinates
X_axis = list(abc[:edgeLong])
Y_axis = list(range(1,edgeLong+1))

