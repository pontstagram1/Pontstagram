from PIL import Image
import ImageFilter
import time
import random
from math import exp,pi,sqrt



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

def flou_pixel(pixel,pixel2,x,y,w,h,a,b,c):
    if (x>0) and (x<w-1) and (y>0) and (y<h-1):
        if im.mode =="RGB":
            pixel2[x,y]=(int(a*pixel[x,y][0]+(b*0.25)*(pixel[x-1,y][0]+pixel[x+1,y][0]+pixel[x,y-1][0]+pixel[x,y+1][0])+(c*0.25)*(pixel[x-1,y-1][0]+pixel[x-1,y+1][0]+pixel[x+1,y-1][0]+pixel[x+1,y+1][0])),
                        int(a*pixel[x,y][1]+(b*0.25)*(pixel[x-1,y][1]+pixel[x+1,y][1]+pixel[x,y-1][1]+pixel[x,y+1][1])+(c*0.25)*(pixel[x-1,y-1][1]+pixel[x-1,y+1][1]+pixel[x+1,y-1][1]+pixel[x+1,y+1][1])),
                        int(a*pixel[x,y][2]+(b*0.25)*(pixel[x-1,y][2]+pixel[x+1,y][2]+pixel[x,y-1][2]+pixel[x,y+1][2])+(c*0.25)*(pixel[x-1,y-1][2]+pixel[x-1,y+1][2]+pixel[x+1,y-1][2]+pixel[x+1,y+1][2])))
        else :
            pixel2[x,y]=a*pixel[x,y]+(b/4)*(pixel[x-1,y]+pixel[x+1,y]+pixel[x,y-1]+pixel[x,y+1])+(c/4)*(pixel[x-1,y-1]+pixel[x-1,y+1]+pixel[x+1,y-1]+pixel[x+1,y+1])

def flou(im,sigma):
    pixel = im.load()
    imtmp=Image.new("RGB" ,im.size)
    pixel2 = imtmp.load()
    W,H = im.size
    a= 1
    b= exp(-1/float(2*sigma))
    c=  exp(-1/float(sigma))
    norm = a+b+c
    a=a/norm
    b=b/norm
    c=c/norm
    for x in range(W):
        for y in range(H):
            flou_pixel(pixel,pixel2,x,y,W,H,a,b,c)
    return imtmp

def flou2(im,sigma):
    pixel = im.load()
    imtmp=Image.new("RGB" ,im.size)
    pixel2 = imtmp.load()
    W,H = im.size
    t=min(W,H)/3
    a=1
    b= exp(-1/(2*sigma))
    c=  exp(-2/(2*sigma))
    for x in range(W):
        for y in range(H):
            if ((x-W/2)*(x-W/2)+(y-H/2)*(y-H/2)>t*t):
                flou_pixel(pixel,pixel2,x,y,W,H,a,b,c)
            else:
                pixel2[x,y]=pixel[x,y]
    return imtmp           
    
    

        

#////////////////////////  LISTE DE FILTRES  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



def test1(im):
    imtmp = Image.blend(contraste(im,1,1.5,2), im.filter(ImageFilter.SMOOTH), 0.2).filter(ImageFilter.SMOOTH_MORE)
    return imtmp

def test2(im):
    imtmp = Image.blend(contraste(im,2,1.5,0.7), im.filter(ImageFilter.SMOOTH), 0.2).filter(ImageFilter.SMOOTH_MORE)
    return imtmp

def filtre_vieux(im):
    imtmp = sepia(luminosite(bruit(contraste(im,0.3,0.3,0.3).filter(ImageFilter.SMOOTH_MORE),0.15),20))
    return imtmp

def filtre_vieux_opt(im):
    imtmp=Image.new("RGB" ,im.size)
    pixels = list(im.getdata())
    pixelstmp=list()
    if im.mode=="RGB":
        for pixel in pixels:            
            p0=((128+(pixel[0]-128)*0.3)*random.normalvariate(1,0.15)+20)
            p1=((128+(pixel[1]-128)*0.3)*random.normalvariate(1,0.15)+20)
            p2=((128+(pixel[2]-128)*0.3)*random.normalvariate(1,0.15)+20)
            pixelstmp.append( (int(min(max(p0 * .393 + p1 *.769+ p2 * .189,0),255)),
                        int(min(max(p0 * .349 + p1*.686 + p2* .168,0),255)),
                        int(min(max(p0* .272 + p1*.534 + p2* .131,0),255))))
    else:
        for pixel in pixels:
            p0=((128+(pixel-128)*0.3)*random.normalvariate(1,0.15)+20)
            pixelstmp.append((int(min(max(p0 * (.393 +.769+.189),0),255)),
                        int(min(max(p0 * (.349 +.686 + .168),0),255)),
                        int(min(max(p0* (.272 +.534 + .131),0),255))))
    imtmp.putdata(pixelstmp)
    return imtmp.filter(ImageFilter.SMOOTH_MORE)

def filtre_vieux_opt2(im):
    imtmp=im.copy()
    pixel =imtmp.load()
    X,Y = imtmp.size
    if im.mode=="RGB":
        for x in range(X):
            for y in range(Y):
                p0=((128+(pixel[x,y][0]-128)*0.3)*random.normalvariate(1,0.15)+20)
                p1=((128+(pixel[x,y][1]-128)*0.3)*random.normalvariate(1,0.15)+20)
                p2=((128+(pixel[x,y][2]-128)*0.3)*random.normalvariate(1,0.15)+20)
                pixel[x,y]=( (int(min(max(p0 * .393 + p1 *.769+ p2 * .189,0),255)),
                            int(min(max(p0 * .349 + p1*.686 + p2* .168,0),255)),
                            int(min(max(p0* .272 + p1*.534 + p2* .131,0),255))))
    else:
        for pixel in pixels:
            p0=((128+(pixel-128)*0.3)*random.normalvariate(1,0.15)+20)
            pixelstmp.append((int(min(max(p0 * (.393 +.769+.189),0),255)),
                        int(min(max(p0 * (.349 +.686 + .168),0),255)),
                        int(min(max(p0* (.272 +.534 + .131),0),255))))
    return imtmp.filter(ImageFilter.SMOOTH_MORE)
    




#////////////////////////  TESTS  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#im = Image.open("paysage.jpg")
#flou(im,5).show()



            
    

