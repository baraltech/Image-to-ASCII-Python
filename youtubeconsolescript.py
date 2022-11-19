import pywhatkit

imagefilepath = str(input("Enter the path of the image to convert: "))
savefilepath = str(input("Enter the path of the file to save the text in: "))
try:
    pywhatkit.image_to_ascii_art(imagefilepath, savefilepath)
except:
    print("Error")