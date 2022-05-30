from turtle import width
from PIL import Image

im1 = Image.open('image-collage/fantasy1.jpg')
im2 = Image.open('image-collage/human2.jpg')

#画像の大きさをそろえる
(width,height) = (im1.width,im1.height)
im2 = im2.resize((width,height))

threshold = 80
mask = im2.point(lambda p: p > threshold and 255).convert('1')

im = Image.composite(im1, im2, mask)

im.save('maked-image/collage2.jpg')