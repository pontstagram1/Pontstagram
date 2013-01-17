from PIL import Image
import ImageFilter
import time
import random
im = Image.open("tour.jpg")
p = im.load()

#////////////////////////  FONCTIONS ANNEXES  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def contraste(im,valR=1.0,valG=1.0,valB=1.0):
    imtmp=Image.new(im.mode ,im.size)
    pixels = list(im.getdata())
    if im.mode=="RGB":
        pixels = [ (int(min(max(128+(pixel[0]-128)*valR,0),255)),int(min(max(128+(pixel[1]-128)*valG,0),255)),int(min(max(128+(pixel[2]-128)*valB,0),255))) for pixel in pixels]
    else:
        pixels = [ int(min(max(128+(pixel-128)*valR,0),255)) for pixel in pixels]    
    imtmp.putdata(pixels)
    return imtmp

def luminosite(im,val):
    imtmp=Image.new(im.mode ,im.size)
    pixels = list(im.getdata())
    if im.mode=="RGB":
        pixels = [ (int(min(max(pixel[0]+val,0),255)),int(min(max(pixel[1]+val,0),255)),int(min(max(pixel[2]+val,0),255))) for pixel in pixels]
    else:
        pixels = [ int(min(max(pixel+val,0),255)) for pixel in pixels]    
    imtmp.putdata(pixels)
    return imtmp

def sepia(im):
    imtmp=Image.new("RGB" ,im.size)
    pixels = list(im.getdata())
    if im.mode=="RGB":
        pixels = [ (int(min(max((pixel[0] * .393) + (pixel[1] *.769) + (pixel[2]  * .189),0),255)),
                        int(min(max((pixel[0] * .349) + (pixel[1] *.686) + (pixel[2]  * .168),0),255)),
                        int(min(max((pixel[0] * .272) + (pixel[1] *.534) + (pixel[2]  * .131),0),255))) for pixel in pixels]
    else:
        pixels = [ (int(min(max((pixel * .393) + (pixel *.769) + (pixel  * .189),0),255)),
                        int(min(max((pixel * .349) + (pixel *.686) + (pixel  * .168),0),255)),
                        int(min(max((pixel * .272) + (pixel *.534) + (pixel  * .131),0),255))) for pixel in pixels]
    imtmp.putdata(pixels)
    return imtmp

def bruit(im,var):
    imtmp=Image.new(im.mode ,im.size)
    pixels = list(im.getdata())
    if im.mode=="RGB":
        pixels = [ (int(min(max(pixel[0]*random.normalvariate(1,var),0),255)),int(min(max(pixel[1]*random.normalvariate(1,var),0),255)),int(min(max(pixel[2]*random.normalvariate(1,var),0),255))) for pixel in pixels]
    else:
        pixels = [ int(min(max(pixel*random.normalvariate(1,var),0),255)) for pixel in pixels]    
    imtmp.putdata(pixels)
    return imtmp

#////////////////////////  LISTE DE FILTRES  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



def test1(im):
    imtmp = Image.blend(contraste(im,1,1.5,2), im.filter(ImageFilter.SMOOTH), 0.2).filter(ImageFilter.SMOOTH_MORE)
    return imtmp

def filtre_vieux(im):
    imtmp = sepia(luminosite(bruit(contraste(im,0.3,0.3,0.3),0.15).filter(ImageFilter.SMOOTH_MORE),20))
    return imtmp




#////////////////////////  TESTS  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

filtre_vieux(im).show()
    


            
    

