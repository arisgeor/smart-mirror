#!/usr/bin/env python

from mlx90614 import MLX90614

def get_temp():
    
    mlx90614 = MLX90614()
    print("Reading Temperature: ")

    try:
        obj_temp = mlx90614.get_obj_temp()
        print("Object temp is {:.2f}\n".format(obj_temp))
        return obj_temp
    except KeyboardInterrupt:
    	pass
