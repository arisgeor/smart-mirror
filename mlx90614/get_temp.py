#!/usr/bin/env python

from mlx90614 import MLX90614

def get_temp():
    '''
    Function that calculates body temperature based
    on readings of Skin temperature, according to the paper
    "Correction of human forehead temperature variations 
    measured by non-contact infrared thermometer"
    doi: 10.1109/jsen.2021.3058958
    '''
    mlx90614 = MLX90614()
    print("Reading Body Temperature: ")

    try:
        obj_temp = mlx90614.get_obj_temp()
        amb_temp = mlx90614.get_amb_temp()
        body_temp = ((((obj_temp**4) - (amb_temp**4))/0.98)+(amb_temp**4))**(0.25)+2.3
        print("Body temperature is {:.2f}\n".format(body_temp))
        return body_temp

#        skin_temp2 = (((amb_temp**4) - (1-0.98)*((obj_temp)**4))/0.98)**(0.25)+2.3
#        print("Skin temp2 is {:.2f}\n".format(skin_temp2))
    except KeyboardInterrupt:
        pass

