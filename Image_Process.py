from scipy import misc
import numpy as np
import matplotlib.pyplot as plt


#return the weighted average of a pixel(i.e convert from RGB to Greyscale )
def Weighted_Average(pixel):
	return(0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2])

rgb_image = misc.imread('bird_small.png')
#print('The image Dimensions are :: '+ str(len(rgb_image)) +'  ' + str(len(rgb_image[0])) +' '+ str(len(rgb_image[0][0])))

#print('Changing image from RGB to Gray-Scale ')

#find the dimensions of the Image
dimen_one = len(rgb_image)
dimen_two = len(rgb_image[0])
grey_image = np.zeros((dimen_one, dimen_two))

fp = open('ex7.txt', 'w')

#print(str(dimen_one) + ' '+ str(dimen_two))
for i in range(dimen_one):
	x = ''
	for j in range(dimen_two):
		grey_image[i][j] = Weighted_Average(rgb_image[i][j])
		x += str(grey_image[i][j])+ ' '
	fp.write(x+'\n')
fp.close()


