import PIL.Image
import PIL.ImageTk
import webbrowser
import random
import keyboard
import time
import tkinter as tk
from tkinter import Frame
from tkinter import Text
from tkinter import Label
#----------------------------------------------------------------------
possiblevals = [-1,0,1]
callback = None
singularx = 0
singulary = 0
#image = str(input("image name: \n\t> " ))
image = "wheel.jpg"
len,height = PIL.Image.open(image).size
coords = []
names = [[None] * 4, [None] * 4, [None] * 4, [None] * 4]
coordslist = []
#----------------------------------------------------------------------
#----------------------------------------------------------------------
## Crop Function
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = PIL.Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)

## Crops Individual Images
def cropdata(len, height):

    amountupx = int(len/4)
    amountdowny = int(height/4)
    for ycounter in range(0,4):
        for xcounter in range(0,4):
            if xcounter == 3 and ycounter == 3 :
                coords = []


                coords.append(0)
                coords.append(0)
                coords.append(amountupx)
                coords.append(amountdowny)

                crop('White-Square.jpg', coords, 'croppedwhite.jpg')
                names[3][3] = 'croppedwhite.jpg'

            coords = []
            x = xcounter * amountupx
            y = ycounter * amountdowny


            stringname = "cropped" + str(xcounter) + "_" + str(ycounter) + ".jpg"
            names[xcounter][ycounter] = (stringname)
            coords.append(x)
            coords.append(y)
            coords.append(x+amountupx)
            coords.append(y+amountdowny)
            print(coords)

            crop(image, coords, stringname)

## Recreates Image Using Array
def ImageReset():
    for ycounter in range(0,4):
        for xcounter in range(0,4):
            x = xcounter * amountupx
            y = ycounter * amountdowny
            blockname = names[xcounter][ycounter]
            new_image.paste(PIL.Image.open(blockname), (x,y))

    new_image.save('Image_1.jpg')
    label.img = PIL.ImageTk.PhotoImage(PIL.Image.open('Image_1.jpg'))
    label.config(image=label.img)


## Verifies and Simplifies Coords Givin By Clicks
def coordverification(coordslistvar):
    global coordslist
    for i in coordslistvar :
        for x in range(0,16) :
            if x < i < x+1 :
                coordslistvar[coordslistvar.index(i)] = x
    if (coordslist[0] - coordslist[2] == 1 or coordslist[0] - coordslist[2] == 1) and (coordslist[1] - coordslist[3] == 1 or coordslist[1] - coordslist[3] == -1) :
        pass
    else :
        print(whitex, whitey)
        if coordslist[0] - whitex in possiblevals or coordslist[1] - whitey in possiblevals :
            if coordslist[0] - coordslist[2] == 1 :
                print('left')
                swapleft()
            if coordslist[0] - coordslist[2] == -1 :
                print('right')
                swapright()
            if coordslist[1] - coordslist[3] == 1 :
                swapup()
                print('up')
            if coordslist[1] - coordslist[3] == -1 :
                print('down')
                swapdown()
    print(coordslist)
    coordslist = []
#----------------------------------------------------------------------
## Detects Events
def callbackbegin(event):
    global coordslist
    frame.focus_set()
    eventx1 = event.x /(len / 4)
    eventy1 = event.y / (height / 4)
    coordslist.append(eventx1)
    coordslist.append(eventy1)

def callbackend(event):
    global coordslist

    frame.focus_set()
    eventx2 =  event.x /(len / 4)
    eventy2 = event.y / (height / 4)
    coordslist.append(eventx2)
    coordslist.append(eventy2)
    coordverification(coordslist)

def key(event):
    if repr(event.char()) == 'q' :
        quit()

#----------------------------------------------------------------------
## Movement Controls on array
def swapright():
    global whitex
    global whitey
    if whitex != 0 :
        names[whitex][whitey] = names[whitex - 1][whitey]
        names[whitex - 1][whitey] = 'croppedwhite.jpg'
        whitex -= 1
        ImageReset()
def swapleft():
    global whitex
    global whitey
    if whitex != 3 :
        names[whitex][whitey] = names[whitex + 1][whitey]
        names[whitex + 1][whitey] = 'croppedwhite.jpg'
        whitex += 1
        ImageReset()
def swapup():
    global whitex
    global whitey
    if whitey != 3 :
        names[whitex][whitey] = names[whitex][whitey + 1]
        names[whitex][whitey + 1] = 'croppedwhite.jpg'
        whitey += 1
        ImageReset()
def swapdown():
    global whitex
    global whitey
    if whitey != 0 :
        names[whitex][whitey] = names[whitex][whitey - 1]
        names[whitex][whitey - 1] = 'croppedwhite.jpg'
        whitey -= 1
        ImageReset()

#----------------------------------------------------------------------

window = tk.Tk()

frame = Frame(window, width= len , height= height)
window.title("Sixteen_Game")


window.configure(background='white')

label = tk.Label(window)
label.bind("<Button-1>", callbackbegin)
label.bind("<ButtonRelease-1>", callbackend)
label.pack()



#----------------------------------------------------------------------



#----------------------------------------------------------------------

cropdata(len, height)

names[3][3] = 'croppedwhite.jpg'
random.shuffle(names)
for i in names :
    random.shuffle(i)
new_image = PIL.Image.new('RGB', (len, height))

amountupx = int(len/4)
amountdowny = int(height/4)
for ycounter in range(0,4):
    for xcounter in range(0,4):
        x = xcounter * amountupx
        y = ycounter * amountdowny
        blockname = names[xcounter][ycounter]
        new_image.paste(PIL.Image.open(blockname), (x,y))

new_image.save('Image_1.jpg')

label.img = PIL.ImageTk.PhotoImage(PIL.Image.open('Image_1.jpg'))
label.config(image=label.img)


for x in range(0,4) :
    for y in range(0,4) :
        if names[x][y] == 'croppedwhite.jpg' :
            whitex = x
            whitey = y
#----------------------------------------------------------------------


#----------------------------------------------------------------------


#Start the GUI
window.mainloop()




#----------------------------------------------------------------------


#----------------------------------------------------------------------










#s
