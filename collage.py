from PIL import Image

im1 = Image.open('image-collage/easter.jpg')
im2 = Image.open('image-collage/boy.jpg')

threshold = 240
mask = im2.point(lambda p: p > threshold and 255).convert('1')

im = Image.composite(im1, im2, mask)

im.save('maked-image/collage.jpg')