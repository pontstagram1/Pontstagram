from PIL import Image
import ImageFilter
import time
im = Image.open("lena.bmp")



def contraste(im,valR=1.0,valG=1.0,valB=1.0):
    imtmp=Image.new(im.mode ,im.size)
    pixels = list(im.getdata())
    if im.mode=="RGB":
        pixels = [ (int(min(max(128+(pixel[0]-128)*valR,0),255)),int(min(max(128+(pixel[1]-128)*valG,0),255)),int(min(max(128+(pixel[2]-128)*valB,0),255))) for pixel in pixels]
    else:
        pixels = [ int(min(max(128+(pixel-128)*valR,0),255)) for pixel in pixels]
            
    imtmp.putdata(pixels)
    return imtmp

contraste(im,7,2,0.6).show()
Image.blend(contraste(im,7,2,0.6), im.filter(ImageFilter.CONTOUR), 0.2).filter(ImageFilter.SMOOTH_MORE).show()

            
    

