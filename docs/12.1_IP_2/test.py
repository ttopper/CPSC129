# http://stackoverflow.com/questions/12798885/python-image-library-convert-pixels-to-2d-list

#from PIL import Image
##image = Image.open("3blks1.png")
##image.show()
##image.size
##dir(image)
##image.histogram()
##pix = image.load()
##pix[0,0] --> (211, 211, 211, 255) RGBA
##
##
##image = im.convert("L")
##pix = image.load() # pix is a pixel map access object
##pix[0,0]
##for i in range(10):
##	for j in range(10):
##		print pix[i,j],
##	print
##im_copy = im.copy()
##im.save('new.png') # im.save(outfile,format,options)

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

im = Image.open("Moon.jpg") # Open the file and returns an image object.
im = im.convert("L") # Convert to a greyscale image.
pix = im.load() # Load the image pixel map for easy access

# Create new images to hold horizontal and vertical edge strength values.
# la for Laplacian
la = Image.new("L", im.size) 
lapix = la.load()

working = []
for x in range(im.size[1]):
    working.append(im.size[1] * [0])
    
minval = 0
maxval = 0
for x in range(1, im.size[0]-1): # Q: Why does this start at 1 and not 0?
    for y in range(1, im.size[1]-1): # Q: Why does this go to im.size[1]-1 and not im.size[1]?
        val = -pix[x-1, y-1] - pix[x, y-1]  - pix[x+1, y-1] \
                     - pix[x-1, y] + 8 * pix[x, y] - pix[x+1,y] \
                      -pix[x-1, y+1] - pix[x, y+1]  - pix[x+1, y+1]
        if val < minval: minval = val
        if val > maxval: maxval = val
        working[x][y] = val
print 'working: min =', minval, 'max =', maxval
for x in range(im.size[0]):
    for y in range(im.size[1]):
        lapix[x,y] = (working[x][y]-minval)*255/(maxval-minval)
##la.save('Moon_la_scaled.png')

##im = Image.open("Moon_Laplacian_Scaled.png") # Open the file and returns an image object.
##im = im.convert("L") # Convert to a greyscale image.
##pix = im.load() # Load the image pixel map for easy access
##
##lamin = lapix[0,0]
##lamax = lapix[0,0]
##for x in range(1, im.size[0]-1): # Q: Why does this start at 1 and not 0?
##    for y in range(1, im.size[1]-1): # Q: Why does this go to im.size[1]-1 and not im.size[1]?
##        if lapix[x,y] < lamin:
##            lamin = lapix[x,y]
##        if lapix[x,y] > lamax:
##            lamax = lapix[x,y]
##
##print 'min =', lamin, 'max =', lamax

# ====================================================================
##im = Image.open("Moon.jpg") # Open the file and returns an image object.
##im = im.convert("L") # Convert to a greyscale image.
##pix = im.load() # Load the image pixel map for easy access
##
##la = Image.open("Moon_Laplacian_Scaled.png") # Open the file and returns an image object.
##la = la.convert("L") # Convert to a greyscale image.
##lapix = la.load() # Load the image pixel map for easy access
##
##sharp = Image.new("L", im.size) 
##sharppix = sharp.load()
##
##working = []
##for x in range(im.size[1]):
##    working.append(im.size[1] * [0])
##minval = 0
##maxval = 0
##for x in range(1, im.size[0]-1):
##    for y in range(1, im.size[1]-1):
##        val = pix[x,y] + lapix[x,y]
##        if val < minval: minval = val
##        if val > maxval: maxval = val
##        working[x][y] = val
##print 'min =', minval, 'max =', maxval
##minv = 0
##maxv = 0
##for x in range(im.size[0]):
##    for y in range(im.size[1]):
##        sharppix[x,y] = (working[x][y]-minval)*255/(maxval-minval)
##        if sharppix[x,y] < minv: minv = sharppix[x,y]
##        if sharppix[x,y] > maxv: maxv = sharppix[x,y]
##print 'min =', minv, 'max =', maxv
##sharp.save('sharp.png')
##sharphist = sharp.histogram()
##imhist = im.histogram()
##print sum(imhist), sum(sharphist)
##
##### Compare to the original
####tot = 0
####for x in range(im.size[0]):
####    for y in range(im.size[1]):
####        tot += sharppix[x,y]-pix[x,y]
####print 'Total difference =', tot
##
##print 'Done.'
##
##def equalize(input_image, model_image):
##    ''' Returns eq_image a version of input_image whose pixel values have been
##        equalized so its histogram will match model_image's histogram.
##        
##        Leaves input_image and model_image unchanged.
##        
##        See http://en.wikipedia.org/wiki/Histogram_matching for background.
##
##        Outline:
##        1. Build histograms of the grey level values in each image.
##        2. Build cumulative distributions (CDFs) of the grey level values in
##           each image from the histograms.
##        3. Use the CDFs to build a pixel value lookup table (LUT).
##        4. Loop through the input image and use the LUT to assign
##           new equalized pixel values.
##    '''
##    # 1. Get the grey level histograms for each image.
##    input_histogram = input_image.histogram()
##    model_histogram = model_image.histogram()
##    # print input_histogram, '\n', model_histogram # DEBUG
##    # Minimal error checking to avoid annoying failures.
##    if len(input_histogram) != len(model_histogram):
##        print 'Error: Histograms do not have same length!'
##        return
##    if len(input_histogram) != 256 or len(model_histogram) != 256:
##        print 'Error: Histograms do not use full 0-255 range of values!'
##        return
##
##    # 2. Build the Cumulative Distribution Functions (cdf's) for each image
##    # TODO: s/b a separate function.
##    input_cdf = input_histogram[:]
##    for i in range(1, len(input_cdf)):
##        input_cdf[i] = input_cdf[i] + input_cdf[i-1]
##    model_cdf = model_histogram[:]
##    for i in range(1, len(model_cdf)):
##        model_cdf[i] = model_cdf[i] + model_cdf[i-1]
##    # print input_cdf, '\n', model_cdf # DEBUG
##
##    # 3. Build a lookup table (lut) that will let us look up a pixel value in
##    # input_image to see what it should become in the equalized image.
##    lut = 256*[0]  
##    # The rule is to assign each lut entry the index (grey level) of
##    # the first entry in model_cdf that is greater than or equal to
##    # input_cdf's entry.
##    grey_level = 0
##    for input_cdf_index in range(len(input_histogram)):
##        while model_cdf[grey_level] < input_cdf[input_cdf_index]:
##            grey_level += 1
##        lut[input_cdf_index] = grey_level
##    # print lut # DEBUG
##    
##    # 4. Create the equalized image, eq_image, by looping through input_image
##    # using the lut to assign pixel values for eq_image.
##    eq_image = Image.new("L", input_image.size) 
##    eq_pix = eq_image.load()
##    input_pix = input_image.load()
##    for x in range(im.size[0]):
##        for y in range(im.size[1]):
##            eq_pix[x,y] = lut[input_pix[x,y]]
##            
##    return eq_image
##    
##
##eq = equalize(sharp, im)
##eq.save('eq.png')
