#!/usr/bin/env python
# coding: utf-8

# # K-means algorithm

import numpy as np
import matplotlib.pyplot as plt

import color

def importImage(imdir):
    
    im_array = plt.imread(imdir)
    im_array = (im_array * 255).astype(np.int64)
    im_array = im_array[:,:,:3]

    height = np.shape(im_array)[0]
    width = np.shape(im_array)[1]
    
    channels = np.shape(im_array)[2]
    
    return im_array, width, height, channels

im_dirs = ["./triangles.png", "./spaceship.png"]

for i in range(2):
    
    image, width, height, channels = importImage(im_dirs[i])
    im_data = np.reshape(image, (height*width, 3))
    
    clusters, means = color.kmeans(5, 10, im_data)
    dominantColor = color.getDominant(clusters, means) 
    
    im_clusters = np.reshape(clusters, (height, width, 3))
    block = np.ones((100,160,3), dtype=np.uint8)*dominantColor
    
    f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize = (7,10))
    ax1.imshow(image, aspect = "equal")
    ax2.imshow(im_clusters, aspect = "equal")
    ax3.imshow(block)
    plt.savefig(im_dirs[i]+"+clusts+dom.png", bbox_inches="tight")
