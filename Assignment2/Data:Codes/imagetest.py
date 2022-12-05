from PIL import Image
file_path =  "/Users/hyunjaekim/Desktop/CS361-A2/n02113799_204.jpg" 
# open method used to open different extension image file
im = Image.open(file_path) 
  
# This method will show image in any image viewer 
im.show()
