import pptk
import numpy as np
import plyfile
	
data = plyfile.PlyData.read('germany.ply')['vertex']

xyz = np.c_[data['x'], data['y'], data['z']]          # Eixos
rgb = np.c_[data['red'], data['green'], data['blue']] # RGB
n = np.c_[data['nx'], data['ny'], data['nz']]         # Normais
params = [4, 7, 4, 9, 6, 12, 18, 15, 3, 10, 11, 12, 13, 14, 3, 4, 5, 15, 14, 13]

def printmodel():
	
	v.set(point_size=0.005)
	v.attributes(rgb / 255., 0.5 * (1 + n))
	return

v = pptk.viewer(xyz)

P = np.array([[1, 2, 3],
		   [4, 5, 6],
		   [7, 8, 9],
		   [10, 11, 12]])

#y=1
for y in range(20):
	if y ==0:
		y=1
	for x in range(len(rgb)): 
		if x == 0:
			x=1
		w = params[y] * 100000
# primeira camada - vermelho
		if (x < w):
			rgb[x,0] = 255
			#rgb[x,1] = 0
			#rgb[x,2] = 0
# segunda camada - laranja
		if (x < (w-100000)):
			rgb[x,0] = 250
			rgb[x,1] = 170
			#rgb[x,2] = 0
# terceira camada - preto
		if (x < (w-200000)):
			rgb[x,0] = 0
			rgb[x,1] = 0
			rgb[x,2] = 0			
		x+=1
	printmodel()	
	print("fase "+ str(y) + " - " + str(params[y]))

