import cv2
import numpy as np

im1 = cv2.imread('image/asi.jpg')
im2 = cv2.imread('image/ita.jpg')

im_v = cv2.vconcat([im1, im1])
cv2.imwrite('asia^2.jpg', im_v)

def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)
im_v_resize = vconcat_resize_min([im1, im2, im1])
cv2.imwrite('itasia.jpg', im_v_resize)
