import os
import cv2
import numpy as np
import pandas as pd

total = 0
dict = {'Classification': [], 'Mean R': [], 'Mean G': [], 'Mean B': [],}
mean_array = []
def get_data_set(image_path):
    if 'healthy' in image_path:
        dict['Classification'].append('healthy')
    else:
        dict['Classification'].append('sick')
        
    global total
    image = cv2.imread(image_path)
    
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    mean_rgb = image_rgb.mean(axis=(0,1))
    
    mean_array.append(mean_rgb)
    dict['Mean R'].append(mean_rgb[0])
    dict['Mean G'].append(mean_rgb[1])
    dict['Mean B'].append(mean_rgb[2])
    total += mean_rgb

# Specify the directory path
def load(folder_path):
    global total
    # Get a list of all files in the folder
    file_paths = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file_name))]

    # Print the list of file paths
    for file_path in file_paths:
        get_data_set(file_path)

def get_mean_array():
    return mean_array
def get_total_rgb():
    return total
def get_dict():
    return dict