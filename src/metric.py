# This code was borrowed from https://bitbucket.org/kuraiev/pymetrikz/src/9eee36e3cc6820eb2311a90129e254ce35820f2c/pymetrikz/metrikz.py?at=default&fileviewer=file-view-default
# I have not written any of this and am using it as a metric to compare noise reduced images with their originals
# Author: "Pedro Garcia Freitas <sawp@sawp.com.br>"
#Copyright: "Copyright (c) 2011-2014 Pedro Garcia"
# License: "GPLv2"

import numpy as __n

def psnr(reference, query, normal=255):
    """Computes the Peak Signal-to-Noise-Ratio (PSNR).

    value = psnr(reference, query, normalization=255)

    Parameters
    ----------
    reference: original image data.
    query    : modified image data to be compared.
    normal   : normalization value (255 for 8-bit image

    Return
    ----------
    value    : PSNR value
    """
    normalization = float(normal)
    msev = mse(reference, query)
    if msev != 0:
        value = 10.0 * __n.log10(normalization * normalization / msev)
    else:
        value = float("inf")
    return value

def mse(reference, query):
    """Computes the Mean Square Error (MSE) of two images.

    value = mse(reference, query)

    Parameters
    ----------
    reference: original image data.
    query    : modified image data to be compared.

    Return
    ----------
    value    : MSE value
    """
    (ref, que) = (reference.astype('double'), query.astype('double'))
    diff = ref - que
    square = (diff ** 2)
    mean = square.mean()
    return mean