from PIL import Image, ImageDraw, ImageFont
import math
import os
import sys
import pandas as pd

inputFolder = sys.argv[1]
dataFile = sys.argv[2]
outputFolder = sys.argv[3]
fontSize = int(sys.argv[4])

files = os.listdir(inputFolder)
files.sort()

df = pd.read_csv(dataFile, header=None)

tags = df.iloc[:, 0]

for file, tag in zip(files, tags):

    image = Image.open(inputFolder+file) 
      
    #right = 100
    #left = 100
    #top = 100
      
    width, height = image.size 
      
    bottom = math.ceil(0.1 * height)
    #new_width = width + right + left 
    #new_height = height + top + bottom 
    new_height = height + bottom 
      
    result = Image.new(image.mode, (width, new_height), (255, 255, 255)) 
      
    result.paste(image) 
    I1 = ImageDraw.Draw(result)
    myFont = ImageFont.truetype('FreeMono.ttf', fontSize)
    
    I1.text((10, height+10), tag, font=myFont, fill=(255, 0, 0))
      
    result.save(f"{outputFolder}{file}") 
