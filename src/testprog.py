from imageIO import *
from imenh_lib import *
from scipy import misc
import matplotlib.pyplot as plt
import PIL

def callAlphaMean(inputname, alpha, outputname):
    img = imread_gray('input/' + inputname)
    newimg = enh_alphaTMean(img,alpha,n=5)
    misc.imsave('output/alphaMean/' + outputname, newimg)
    print('Completed: ', outputname)

def callTruncMedian(inputname, outputname):
    img = imread_gray('input/' + inputname)
    newimg = enh_truncMedian(img,n=5)
    misc.imsave('output/truncatedMedian/' + outputname, newimg)
    print('Completed: ', outputname)

def callHybridMedian(inputname, outputname):
    img = imread_gray('input/' + inputname)
    newimg = enh_hybridMedian(img,n=5)
    misc.imsave('output/hybridMedian/' + outputname, newimg)
    print('Completed: ', outputname)

# Alpha Mean Filtering Noise Reduction
# Reading in images, modifying, and writing to files
############################################################
"""
callAlphaMean('noise_1.jpg', 0.2, 'alpha_output_1.jpg')
callAlphaMean('noise_2.jpg', 0.2, 'alpha_output_2.jpg')
callAlphaMean('noise_3.jpg', 0.2, 'alpha_output_3.jpg')
callAlphaMean('noise_4.jpg', 0.2, 'alpha_output_4.jpg')
callAlphaMean('ground_truth.png', 0.2, 'alpha_ground_truth_output.png')

callTruncMedian('noise_1.jpg', 'trunc_output_1.jpg')

callTruncMedian('noise_2.jpg', 'trunc_output_2.jpg')
callTruncMedian('noise_3.jpg', 'trunc_output_3.jpg')
callTruncMedian('noise_4.jpg', 'trunc_output_4.jpg')
callTruncMedian('ground_truth.png', 'trunc_ground_truth_output.png')
"""
callHybridMedian('noise_1.jpg', 'hybrid_output_1.jpg')
callHybridMedian('noise_2.jpg', 'hybrid_output_2.jpg')
callHybridMedian('noise_3.jpg', 'hybrid_output_3.jpg')
callHybridMedian('noise_4.jpg', 'hybrid_output_4.jpg')
callHybridMedian('ground_truth.png', 'hybrid_ground_truth_output.png')
#
# create_alpha_mean(0.2)
#img = imread_gray('noisy1.jpg')
#newimg = enh_alphaTMean(img,0.2,n=5)
#misc.imsave('outfile.jpg', newimg)