import os;
from PIL import Image;
from itertools import product;
from sys import argv as args

def tile(dir_in, dir_out, dx):
	dx = int(dx)
	for image in os.listdir(dir_in):
		name, ext = os.path.splitext(image);
		img = Image.open(os.path.join(dir_in, image));
		img_w, img_h = img.size;
		grid = product(range(0, img_h-img_h%dx, dx), range(0, img_w-img_w%dx, dx));
		for ix, jx in grid:
			box = (jx, ix, jx+dx, ix+dx);
			out = os.path.join(dir_out, f'{name}_{ix}_{jx}{ext}');
			img.crop(box).save(out);

#input, output, tile size	
tile(args[1],args[2],args[3])
