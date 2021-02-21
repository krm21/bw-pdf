import os
import numpy as np
from PIL import Image
from imageio import imwrite

FILTER_SIZE = 40

def get_pic_list():
	extension_set = {".jpg", ".jpeg", ".png"}
	all_files = os.listdir()
	all_pics = []
	
	for file in all_files:
		if os.path.splitext(file)[1].lower() in extension_set:
			all_pics.append(file)

	return all_pics


def filter(lx, ly, img):
	x0 = lx
	y0 = ly
	xend = x0 + FILTER_SIZE
	yend = y0 + FILTER_SIZE	

	sub = img[x0:xend,y0:yend]
	mm = sub.mean()*1.1
	sub[sub>mm*0.85] = 255
	sub[sub<mm*0.80] = 0
	img[x0:xend,y0:yend] = sub
	return img


def iterate_filter(img):
	width = img.shape[1]
	height = img.shape[0]

	for k in range(0, height, FILTER_SIZE):
		for l in range(0, width, FILTER_SIZE):
			filter(k, l, img)


def process_image(img_filename):
	color_img = Image.open(img_filename)
	gray_img = color_img.convert("L")
	nparray_img = np.array(gray_img)

	iterate_filter(nparray_img)

	imwrite(os.path.splitext(img_filename)[0]+"_out.jpg", nparray_img)


def process_all_images():
	all_pics = get_pic_list()
	for picname in all_pics:
		if not os.path.splitext(picname)[0].endswith("_out"):
			process_image(picname)


if __name__ == "__main__":
	process_all_images()