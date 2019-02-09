from imageIO import *
from imenh_lib import *
from scipy import misc
import matplotlib.pyplot as plt
import PIL
import warnings
import time
from metric import psnr

warnings.simplefilter("ignore") # suppress warnings

def callAlphaMean(inputname, alpha, outputname, type):
    outpath = 'output/alphaMean/'
    if(type == "GRAY"):
        img = imread_gray('input/' + inputname)
        start_time = time.time()
        img = enh_alphaTMean(img,alpha,n=5)
        end_time = time.time()
        imwrite_gray(outpath + outputname, img)
    elif(type == "COLOUR"):
        imgR, imgG, imgB = imread_colour('input/' + inputname)
        start_time = time.time()
        imgR = enh_alphaTMean(imgR,alpha,n=5)
        imgG = enh_alphaTMean(imgG,alpha,n=5)
        imgB = enh_alphaTMean(imgB,alpha,n=5)
        end_time = time.time()
        imwrite_colour(outpath + outputname, imgR, imgG,imgB)
    
    print('Completed: ', outputname,'in', round(end_time-start_time, 2),'seconds')

def callTruncMedian(inputname, outputname, type):
    outpath = 'output/truncatedMedian/'
    if(type == "GRAY"):
        img = imread_gray('input/' + inputname)
        start_time = time.time()
        img = enh_truncMedian(img,n=5)
        end_time = time.time()
        imwrite_gray(outpath + outputname, img)
    elif(type == "COLOUR"):
        imgR, imgG, imgB = imread_colour('input/' + inputname)
        start_time = time.time()
        imgR = enh_truncMedian(imgR,n=5)
        imgG = enh_truncMedian(imgG,n=5)
        imgB = enh_truncMedian(imgB,n=5)
        end_time = time.time()
        imwrite_colour(outpath + outputname, imgR, imgG,imgB)
    
    print('Completed: ', outputname,'in', round(end_time-start_time, 2),'seconds')

def callHybridMedian(inputname, outputname, type):
    
    outpath = 'output/hybridMedian/'
    if(type == "GRAY"):
        img = imread_gray('input/' + inputname)
        start_time = time.time()
        img = enh_hybridMedian(img,n=5)
        end_time = time.time()
        imwrite_gray(outpath + outputname, img)
    elif(type == "COLOUR"):
        imgR, imgG, imgB = imread_colour('input/' + inputname)
        start_time = time.time()
        imgR = enh_hybridMedian(imgR,n=5)
        imgG = enh_hybridMedian(imgG,n=5)
        imgB = enh_hybridMedian(imgB,n=5)
        end_time = time.time()
        imwrite_colour(outpath + outputname, imgR, imgG,imgB)
    print('Completed: ', outputname,'in', round(end_time-start_time, 2),'seconds')


# Compute with alpha value 0.2
callAlphaMean('noise_1.jpg', 0.2, 'alpha2_output_1.jpg', "GRAY")
callAlphaMean('noise_2.jpg', 0.2, 'alpha2_output_2.jpg', "GRAY")
callAlphaMean('noise_3.jpg', 0.2, 'alpha2_output_3.jpg', "COLOUR")
callAlphaMean('noise_4.jpg', 0.2, 'alpha2_output_4.jpg', "GRAY")
callAlphaMean('gaussian_noise.png', 0.2, 'alpha2_gaussian_output.png', "COLOUR")
callAlphaMean('lowlight_noise.png', 0.2, 'alpha2_lowlight_output.png', "GRAY")
callAlphaMean('uniform_noise.png', 0.2, 'alpha2_uniform_output.png', "COLOUR")

# Quantititative metric for alpha

# original_gaussian.png

# original_lowlight.png
# original_speckle.png

# Compute with alpha value 0.4
callAlphaMean('noise_1.jpg', 0.4, 'alpha4_output_1.jpg', "GRAY")
callAlphaMean('noise_2.jpg', 0.4, 'alpha4_output_2.jpg', "GRAY")
callAlphaMean('noise_3.jpg', 0.4, 'alpha4_output_3.jpg', "COLOUR")
callAlphaMean('noise_4.jpg', 0.4, 'alpha4_output_4.jpg', "GRAY")
callAlphaMean('gaussian_noise.png', 0.4, 'alpha4_gaussian_output.png', "COLOUR")
callAlphaMean('lowlight_noise.png', 0.4, 'alpha4_lowlight_output.png', "GRAY")
callAlphaMean('uniform_noise.png', 0.4, 'alpha4_uniform_output.png', "COLOUR")

# Compute truncated median "mode" filtering
callTruncMedian('noise_1.jpg', 'mode_output_1.jpg', "GRAY")
callTruncMedian('noise_2.jpg', 'mode_output_2.jpg', "GRAY")
callTruncMedian('noise_3.jpg', 'mode_output_3.jpg', "COLOUR")
callTruncMedian('noise_4.jpg', 'mode_output_4.jpg', "GRAY")
callTruncMedian('gaussian_noise.png', 'mode_gaussian_output.png', "COLOUR")
callTruncMedian('lowlight_noise.png', 'mode_lowlight_output.png', "GRAY")
callTruncMedian('uniform_noise.png', 'mode_uniform_output.png', "COLOUR")

# Compute hybrid median filtering
callHybridMedian('noise_1.jpg', 'hybrid_output_1.jpg', "GRAY")
callHybridMedian('noise_2.jpg', 'hybrid_output_2.jpg', "GRAY")
callHybridMedian('noise_3.jpg', 'hybrid_output_3.jpg', "COLOUR")
callHybridMedian('noise_4.jpg', 'hybrid_output_4.jpg', "GRAY")
callHybridMedian('gaussian_noise.png', 'hybrid_gaussian_output.png', "COLOUR")
callHybridMedian('lowlight_noise.png', 'hybrid_lowlight_output.png', "GRAY")
callHybridMedian('uniform_noise.png', 'hybrid_uniform_output.png', "COLOUR")