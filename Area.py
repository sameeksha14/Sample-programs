import numpy as np
from PIL import Image
width=5
height=4
array = np.zeros([height,width,3],dtype = np.uint8)
#maje an image out of this array
img = Image.fromarray(array)
img.save('test.png')
array1 = np.zeros([500,300,3],dtype = np.uint8)
array1[:,:100] = [255,128,0] #orange color
array1[:,100:] = [0,0,255] #blue color
img1 = Image.fromarray(array1)
img1.save('test1.png')
image = Image.open('test1.png')
rgb_im = image.convert('RGB')
r,g,b = rgb_im.getpixel((1,1))
r,g,b = rgb_im.getpixel((150,1))
print(r,g,b)
#para = "I will become rich someday"
#print(list(para))