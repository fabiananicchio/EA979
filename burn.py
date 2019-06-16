import pptk
import numpy as np
import plyfile

data = plyfile.PlyData.read('vase.ply')['vertex']

xyz = np.c_[data['x'], data['y'], data['z']]          # Eixos
rgb = np.c_[data['red'], data['green'], data['blue']] # RGB
n = np.c_[data['nx'], data['ny'], data['nz']]         # Normais
params = [56 ,50 ,169 ,142 ,74 ,73 ,8 ,190 ,122 ,25 ,160 ,116 ,185 ,95, 96, 97, 98, 99, 100, 101, 102, 103, 104,20 ,143 ,37 ,68 ,147 ,71 ,61 ,154 ,32 ,25 ,16 ,17 ,80 ,11 ,181 ,61 ,181 ,147 ,97 ,120 ,31 ,136 ,50 ,43, 37, 95, 94, 44, 132, 90, 96, 148, 171, 71, 19, 33, 3, 56 ,50 ,169 ,142 ,74 ,73 ,8 ,190 ,122 ,25 ,160 ,116 ,185 ,20 ,143 ,37 ,68 ,147 ,71 ,61 ,154 ,32 ,25 ,16 ,17 ,80 ,11 ,181 ,61 ,181 ,147 ,97 ,120 ,31 ,136 ,50 ,43, 37, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 33, 3, 56 ,50 ,169 ,142 ,74 ,73 ,8 ,190 ,122 ,25 ,160 ,116 ,185 ,95, 96, 97, 98, 99, 100, 101, 102, 103, 104,20 ,143 ,37 ,68 ,147 ,71 ,61 ,154]

def printmodel():	
	v.attributes(rgb / 255., 0.5 * (1 + n))
	return

def burn(x, y):
	if x == 0:
		x=1
	w = y * 1500
# primeira camada - vermelho
	if (x < w):
		rgb[x,0] = 255
		#rgb[x,1] = 0
		#rgb[x,2] = 0
# segunda camada - laranja
	if (x < (w-700)):
		rgb[x,0] = 250
		rgb[x,1] = 170
		#rgb[x,2] = 0
# terceira camada - preto
	if (x < (w-1500)):
		rgb[x,0] = 0
		rgb[x,1] = 0
		rgb[x,2] = 0

def change(x, y):
	if (params[y] < params[y+1]) and (params[y] < params[y+2]):
		#rgb[x,0] = 50
		#rgb[x,1] -= 25
		rgb[x,2] += 25
	if (params[y] > params[y+1]) and (params[y] > params[y+2]):
		#rgb[x,0] = 50
		rgb[x,1] += 20
		#rgb[x,2] -= 45


v = pptk.viewer(xyz)
v.set(theta = 0.4)
v.set(phi = 180)
v.set(r = 1.5)

P = np.array([[1, 2, 3],
		   [4, 5, 6],
		   [7, 8, 9],
		   [10, 11, 12]])

for y in range(100):
	if y ==0:
		y=1
	for x in range(len(rgb)): 
		change(x, y)
		burn(x, y)
		x+=1
	printmodel()	
	print("fase "+ str(y) + " - " + str(params[y]))

