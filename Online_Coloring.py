# coding=utf-8
import PIL.Image
from tkColorChooser import askcolor
import PIL.ImageTk
from PIL import *
from Tkinter import *
import tkFileDialog
from tkColorChooser import askcolor
from PIL import ImageTk
global pix
global xSize
global ySize
def convertToBinaryRGB(rgbValue):
    r, g, b, f = rgbValue
    average = (r + g + b + f) / 4
    if average > 200:
        return 255, 255, 255, 255
    return 0, 0, 0, 0


def addToScreen(Img):
    render = ImageTk.PhotoImage(Img)
    img = Label(root, image=render)
    img.image = render
    img.place(x=150, y=50)
    img.bind("<Button-1>")

def makeNum(rgbValues):
    if len(rgbValues) == 4:
        r, g, b, f = rgbValues
        average = (r + g + b + f) / 4
        if average == 255:
            return 1  # means white
        return 0  # means black
    else:
        r, g, b = rgbValues
    average = (r + g + b) / 3
    if average == 255:
        return 1  # means white
    return 0  # means black

def openFile():


    file_path_string = tkFileDialog.askopenfilename()
    # drawingImage=Image.open(file_path_string)
    fp = open(file_path_string, "rb")
    global drawingImage
    drawingImage = PIL.Image.open(fp)
    global pix
    global xSize
    global ySize
    pix = drawingImage.load()
    xSize, ySize = drawingImage.size  # Get the width and hight of the image for iterating over
    print xSize, ySize
    for i in range(xSize):
        for j in range(ySize):
            pix[i, j] = convertToBinaryRGB(pix[i, j])

    for i in range(xSize):
        for j in range(ySize):
         pix[i][j]





def saveImage():
    pass
def getColor():
    pass
root = Tk()

root.title("Painting Project")
root.geometry("600x400")

menu_bar = Menu(root)  # Create main menu bar
file_menu = Menu(menu_bar, tearoff=0)  # Create the submenu (tearoff is if menu can pop out)
file_menu.add_command(label="Add Image!", command=openFile)  # Add commands to submenu
file_menu.add_command(label="Save Image!", command=saveImage)
file_menu.add_command(label="End!", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)  # Add the "File" drop down sub-menu in the main menu bar
root.config(menu=menu_bar)
pickColor = Button(root, text='Pick Color', command=getColor)
pickColor.grid(row=0, column=0)

root.mainloop()

