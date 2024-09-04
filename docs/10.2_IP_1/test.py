# http://stackoverflow.com/questions/12798885/python-image-library-convert-pixels-to-2d-list

from PIL import Image
##image = Image.open("3blks1.png")
##image.show()
##image.size
##dir(image)
##image.histogram()
##pix = image.load()
###pix[0,0] --> (211, 211, 211, 255) RGBA
##
##
##image = image.convert("L")
##pix = image.load() # pix is a pixel map access object
##pix[0,0]
##for i in range(10):
##	for j in range(10):
##		print(pix[i,j], end = ' ')
##	print()
##im_copy = image.copy()
##image.save('new.png') # im.save(outfile,format,options)

##im = Image.open("faces1.png")
##pix = im.load()
##
##print(im.size) # im.size is a tuple giving the size of image (cols,rows)
##
##for x in range(im.size[0]):
##    for y in range(im.size[1]):
##        #pix[x,y] = (pix[x,y][0]//2,pix[x,y][1]//2,pix[x,y][2]//2,pix[x,y][3]//2)
##        pix[x,y] = tuple(num//2 for num in pix[x,y])
##im.save("dkfaces.png")
##
##print('Done.')

# load returns an access object that's attached to the image; to modify 
# the image, just assign to the object
# http://www.gossamer-threads.com/lists/python/python/671395

##from PIL import Image
##
##im = Image.open("Bikesgray.png") # Opens the file and returns an image object.
##im = im.convert("L") # Convert to a greyscale image.
##
### Now we need a way to access the image pixel values.
### PIL provides "pixel map access objects":
##pix = im.load() # pix is a "pixel map access object" for the image named im.
### It gives us direct access to the pixel values,
### similar to the way u.cells gave us access
### to the cell values in a life universe.
### For a grey scale image the values in pix will range from
### 0 for black, to 255 for white.
##
##print im.size # a tuple giving the image dimensions
### pix coordinate system is [x, y],
### with [0, 0] in the upper left corner of the image,
### x measuring across the image, and y down the image.
##for x in range(10):
##	for y in range(10):
##		print pix[x,y],
##	print
##print im.size # Tuple giving size of image (cols,rows)
##
####for x in range(im.size[0]):
####	for y in range(im.size[1]):
####		pix[x,y] = pix[x,y]*3/2
##		
###im.save("brtpenguins.png")
##
##print 'Done.'
##for x in range(10):
##	for y in range(10):
##		print pix[x,y], # coordinates are [x,y] with [0.0] in upper left corner
##	print
#image.show()
##new = Image.new("L", image.size)
##newpix = new.load()
##for x in range(image.size[0]):
##    for y in range(image.size[1]):
##        if pix[x,y] >= 200:
##            newpix[x,y] = 255
##        else:
##            newpix[x,y] = 0
##new.save('newer.png') # im.save(outfile,format,options)

##dx = Image.new("L", image.size)
##dxpix = dx.load()
##dy = Image.new("L", image.size)
##dypix = dy.load()
##import math
##mag = Image.new("L", im.size)
##magpix = mag.load()
##print im.size
##for x in range(1, im.size[0]-1):
##    for y in range(1, im.size[1]-1):
##        #print x,y,':',
##        #local_avg = max((pix[x-1,y-1]+pix[x-1,y]+pix[x-1,y+1]+pix[x,y-1]+pix[x,y]+pix[x,y+1]+pix[x+1,y-1]+pix[x+1,y]+pix[x+1,y+1])/9, 1)
##        dx = pix[x+1,y-1] + pix[x+1,y] + pix[x+1,y+1] - pix[x-1,y-1] - pix[x-1,y] - pix[x-1,y+1]
##        dy = pix[x+1,y+1] + pix[x,y+1] + pix[x-1,y+1] - pix[x+1,y-1] - pix[x,y-1] - pix[x-1,y-1]
##        #magpix[x,y] = int(math.sqrt((dx/3)**2+(dy/3)**2)/local_avg*255)
##        magpix[x,y] = int(math.sqrt((dx/3)**2+(dy/3)**2))
##mag.save('mag.png')
from PIL import Image

im = Image.open("Bikesgray.png") # Open the file and returns an image object.
im = im.convert("L") # Convert to a greyscale image.
pix = im.load() # Load the image pixel map for easy access

# Create new images to hold horizontal and vertical edge strength values.
# dx for horizontal edge strengths.
dx = Image.new("L", im.size) # On creation dx is filled with 0s.
dxpix = dx.load()
# dy for vertical edge strengths.
dy = Image.new("L", im.size)
dypix = dy.load()

for x in range(1, im.size[0]-1): # Q: Why does this start at 1 and not 0?
    for y in range(1, im.size[1]-1): # Q: Why does this go to im.size[1]-1 and not im.size[1]?
        dxpix[x,y] = pix[x+1, y-1]+ pix[x+1, y]  + pix[x+1, y+1] \
                     - pix[x-1, y] - pix[x-1, y-1] - pix[x-1,y+1]
        dypix[x,y] = pix[x-1, y+1]+ pix[x, y+1]  + pix[x+1, y+1] \
                     - pix[x-1, y-1] - pix[x, y-1] - pix[x+1,y-1]

dx.save('dx.png')
dy.save('dy.png')

print('Done.')
