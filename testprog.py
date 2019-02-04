from imageIO import *
from imenh_lib import *
from scipy import misc
import matplotlib.pyplot as plt
import PIL

img = imread_gray('noisy1.jpg')
imwrite_gray('newimage.jpg', img)