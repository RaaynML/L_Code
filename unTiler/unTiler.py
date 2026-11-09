import os
from PIL import Image
from sys import argv as args

def untile(dir_in, dir_out, dx, target_size=512):
	dx = int(dx)
	target_size = int(target_size)
	tiles_per_side = target_size // dx
	
	#Group files by base name
	files_by_base = {}
	for filename in os.listdir(dir_in):
		name, ext = os.path.splitext(filename)
		parts = name.rsplit('_', 2)
		if len(parts) == 3:
			base_name, ix_str, jx_str = parts
			try:
				ix, jx = int(ix_str), int(jx_str)
				if base_name not in files_by_base:
					files_by_base[base_name] = {}
				files_by_base[base_name][(ix, jx)] = (filename, ix, jx)
			except ValueError:
				continue
	
	for base_name, tiles in files_by_base.items():
		if not tiles:
			continue
		
		canvas = Image.new('RGB', (target_size, target_size))
		
		#source grid dim
		max_ix = max(ix for ix, jx in tiles.keys())
		max_jx = max(jx for ix, jx in tiles.keys())
		src_cols = max_jx // dx + 1
		src_rows = max_ix // dx + 1
		
		#Map source grid to linear sequence, then to 8x8 target grid
		for (ix, jx), (filename, _, _) in sorted(tiles.items()):
			tile_path = os.path.join(dir_in, filename)
			tile_img = Image.open(tile_path)
			
			if tile_img.mode != 'RGB':
				tile_img = tile_img.convert('RGB')
			
			#index in source grid
			src_idx = (ix // dx) * src_cols + (jx // dx)
			
			#Target position (8x8)
			target_grid_y = src_idx // tiles_per_side
			target_grid_x = src_idx % tiles_per_side
			
			#position in canvas
			paste_x = target_grid_x * dx
			paste_y = target_grid_y * dx
			
			canvas.paste(tile_img, (paste_x, paste_y))
			print(f"Pasted {filename} (src_idx={src_idx}) → grid({target_grid_x}, {target_grid_y}) at ({paste_x}, {paste_y})")
		
		out_path = os.path.join(dir_out, f'{base_name}.png')
		canvas.save(out_path)
		print(f"✓ Saved {out_path}\n")

if __name__ == "__main__":
	if len(args) < 4:
		print("Usage: python untile.py <input_dir> <output_dir> <tile_size> [target_size=512]")
		exit(1)
	
	target_size = int(args[4]) if len(args) > 4 else 512
	untile(args[1], args[2], args[3], target_size)
