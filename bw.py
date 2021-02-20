import numpy as np
from PIL import Image
from PIL import ImageFilter
from imageio import imwrite
from scipy import ndimage

urlimg = 'Kopia 7_2'

i = Image.open(urlimg + '.jpg')
i = i.convert("L")
# i = i.filter(ImageFilter.SHARPEN)
# i = i.filter(ImageFilter.GaussianBlur(radius=1))
# i = i.filter(ImageFilter.MinFilter(size=3))

i = np.array(i)


def _purify_piece(lx, ly, img):
	x0 = lx
	y0 = ly
	xend = x0+40
	yend = y0+40	

	sub = img[x0:xend,y0:yend]
	mm = sub.mean()*1.1
	sub[sub>mm*0.85] = 255
	sub[sub<mm*0.80] = 0
	img[x0:xend,y0:yend] = sub
	return img


def purify(img):
	width = img.shape[1]
	height = img.shape[0]
	print(width)
	print(height)

	for k in range(0, height, 40):
		for l in range(0, width, 40):
			_purify_piece(k, l, i)


purify(i)

imwrite(urlimg+"out.jpg", i)
