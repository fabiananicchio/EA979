import pptk
import numpy as np
import plyfile
	
data = plyfile.PlyData.read('germany.ply')['vertex']

xyz = np.c_[data['x'], data['y'], data['z']]          # Eixos
rgb = np.c_[data['red'], data['green'], data['blue']] # RGB
n = np.c_[data['nx'], data['ny'], data['nz']]         # Normais


def printmodel():
	v = pptk.viewer(xyz)
	v.set(point_size=0.005)
	v.attributes(rgb / 255., 0.5 * (1 + n))
	return

# extractedData = rgb[:,[2]]  # gets x axis

# matrix = 1*[1*[256]]
# print(matrix)
# rgb[:,[2]][0] = matrix
# print(rgb[:,[2]])

P = np.array([[1, 2, 3],
		   [4, 5, 6],
		   [7, 8, 9],
		   [10, 11, 12]])

y=1
for y in range(10):
	if y ==0:
		y=1
	for x in range(len(rgb)): 
		if x == 0:
			x=1
		w = y * 200000
# primeira camada - vermelho
		if (x < w):
			rgb[x,0] = 255
			rgb[x,1] = 0
			rgb[x,2] = 0
# segunda camada - laranja
		if (x < (w-200000)):
			rgb[x,0] = 250
			rgb[x,1] = 170
			rgb[x,2] = 0
# terceira camada - preto
		if (x < (w-400000)):
			rgb[x,0] = 0
			rgb[x,1] = 0
			rgb[x,2] = 0			
		x+=1
	printmodel()	
	print("fase "+ str(y))

