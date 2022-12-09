#-*- coding: utf-8 -*-
#Importing Library
from PIL import Image
from sys import argv

# if you'd rather not use the command line, put the path to your file here
fileName = "dummy.txt" # path of your text file

# read file that user wants converted from command line. If file can't be read, assign 
# the file to a file in the directory
try:
    txt=open(argv[1], "rt",encoding='UTF-8')
except IndexError:
    print("No file entered. Using default file...")
    txt=open(fileName, "r")
except FileNotFoundError:
    print("Could not find file. Using default file...")
    txt=open(fileName, "r")   


# BG=Image.open("myfont/bg.png") #path of page(background)photo (I have used blank page)
BG=Image.open("myfont/7차퀴즈01.png") #path of page(background)photo (I have used blank page)
sheet_width=BG.width
gap, ht = 0, 0


# for each letter in the uploaded txt file, read the unicode value and replace it with
# the corresponding handwritten file in the "myfont" folder.
for i in txt.read().replace("\n",""):
        cases = Image.open("myfont/{}.png".format(str(ord(i))))
        BG.paste(cases, (gap, ht))
        size = cases.width
        height=cases.height
        gap+=size

        if sheet_width < gap or len(i)*115 >(sheet_width-gap):
            gap,ht=0,ht+140

# for i in range(0,txt.size[0]):
#     for j in range(0,txt.size[1]):
#         rgb = txt.getpixel((i,j))
#         rgb_a = round((rgb[0]+rgb[1]+rgb[2])/3) 
#         txt.putpixel((i,j),(rgb_a,rgb_a,rgb_a))


# print(gap)
# print(sheet_width)
BG.show()
# print(u"\u3131")