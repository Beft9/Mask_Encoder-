import tensorflow as tf
from PIL import Image
import numpy as np


#FOLDER = r"path_to_your_image_source"    # FOLDER = r"C:/..../Training_Masks/"
#pil_image = Image.open(FOLDER+"image_name.png")

#encoded_data = Mask_encoder(pil_image)

def Mask_encoder(pil_image):
    
    size = pil_image.size
    image_array = np.asarray(pil_image)
    
    encoded_data = ""
    i = 0
    while(i < size[1]):
        j = 0
        while(j < size[0]):
            if(image_array[i][j] != 0):
                encoded_data += str(size[0]*i+j)
                print(str(size[0]*i+j))
                counter = 1
                while(True):
                    j += 1;
                    if(j >= size[0]):
                        j = 0
                        i += 1
                        if(i >= size[1]):
                            encoded_data += " "+str(counter)+" " 
                            break
                    if(image_array[i][j] == 0):
                        encoded_data += " "+str(counter)+" "
                        break
                    else:
                        counter += 1;
            j += 1
        i += 1

    return str(encoded_data[:-1])

