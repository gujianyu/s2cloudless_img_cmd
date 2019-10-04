import rsgislib
import rsgislib.imageutils

import glob
import os.path

def stack_sen2(img_path, tmp_dir, output_img):
	rsgis_utils = rsgislib.RSGISPyUtils()
	b01_img = ''
	b02_img = ''
	b03_img = ''
	b04_img = ''
	b05_img = ''
	b06_img = ''
	b07_img = ''
	b08_img = ''
	b8A_img = ''
	b09_img = ''
	b10_img = ''
	b11_img = ''
	b12_img = ''
	
	imgs = glob.glob(os.path.join(img_path, '*.jp2'))
	for img in imgs:
		#print(img)
		img_basename = os.path.basename(img)
		img_x_res, img_y_res = rsgis_utils.getImageRes(img)
		print("{}: ({}, {})".format(img_basename, img_x_res, img_y_res))
		
		if 'B01' in img_basename:
			b01_img = img
		elif 'B02' in img_basename:
			b02_img = img
		elif 'B03' in img_basename:
			b03_img = img
		elif 'B04' in img_basename:
			b04_img = img
		elif 'B05' in img_basename:
			b05_img = img
		elif 'B06' in img_basename:
			b06_img = img
		elif 'B07' in img_basename:
			b07_img = img
		elif 'B08' in img_basename:
			b08_img = img
		elif 'B8A' in img_basename:
			b8A_img = img
		elif 'B09' in img_basename:
			b09_img = img
		elif 'B10' in img_basename:
			b10_img = img
		elif 'B11' in img_basename:
			b11_img = img
		elif 'B12' in img_basename:
			b12_img = img
	
	# Resample B01:
	b01_resample_img = os.path.join(tmp_dir, "{}_resample.kea".format(os.path.splitext(os.path.basename(b01_img))[0]))
	rsgislib.imageutils.resampleImage2Match(b02_img, b01_img, b01_resample_img, 'KEA', 'nearestneighbour', datatype=None, noDataVal=None, multicore=False)
	
	# Resample B05:
	b05_resample_img = os.path.join(tmp_dir, "{}_resample.kea".format(os.path.splitext(os.path.basename(b05_img))[0]))
	rsgislib.imageutils.resampleImage2Match(b02_img, b05_img, b05_resample_img, 'KEA', 'nearestneighbour', datatype=None, noDataVal=None, multicore=False)
	
	# Resample B06:
	b06_resample_img = os.path.join(tmp_dir, "{}_resample.kea".format(os.path.splitext(os.path.basename(b06_img))[0]))
	rsgislib.imageutils.resampleImage2Match(b02_img, b06_img, b06_resample_img, 'KEA', 'nearestneighbour', datatype=None, noDataVal=None, multicore=False)
	
	# Resample B07:
	b07_resample_img = os.path.join(tmp_dir, "{}_resample.kea".format(os.path.splitext(os.path.basename(b07_img))[0]))
	rsgislib.imageutils.resampleImage2Match(b02_img, b07_img, b07_resample_img, 'KEA', 'nearestneighbour', datatype=None, noDataVal=None, multicore=False)
		
	# Resample B8A:
	b8A_resample_img = os.path.join(tmp_dir, "{}_resample.kea".format(os.path.splitext(os.path.basename(b8A_img))[0]))
	rsgislib.imageutils.resampleImage2Match(b02_img, b8A_img, b8A_resample_img, 'KEA', 'nearestneighbour', datatype=None, noDataVal=None, multicore=False)
	
	# Resample B09:
	b09_resample_img = os.path.join(tmp_dir, "{}_resample.kea".format(os.path.splitext(os.path.basename(b09_img))[0]))
	rsgislib.imageutils.resampleImage2Match(b02_img, b09_img, b09_resample_img, 'KEA', 'nearestneighbour', datatype=None, noDataVal=None, multicore=False)
	
	# Resample B10:
	b10_resample_img = os.path.join(tmp_dir, "{}_resample.kea".format(os.path.splitext(os.path.basename(b10_img))[0]))
	rsgislib.imageutils.resampleImage2Match(b02_img, b10_img, b10_resample_img, 'KEA', 'nearestneighbour', datatype=None, noDataVal=None, multicore=False)
	
	# Resample B11:
	b11_resample_img = os.path.join(tmp_dir, "{}_resample.kea".format(os.path.splitext(os.path.basename(b11_img))[0]))
	rsgislib.imageutils.resampleImage2Match(b02_img, b11_img, b11_resample_img, 'KEA', 'nearestneighbour', datatype=None, noDataVal=None, multicore=False)
	
	# Resample B12:
	b12_resample_img = os.path.join(tmp_dir, "{}_resample.kea".format(os.path.splitext(os.path.basename(b12_img))[0]))
	rsgislib.imageutils.resampleImage2Match(b02_img, b12_img, b12_resample_img, 'KEA', 'nearestneighbour', datatype=None, noDataVal=None, multicore=False)
		
	sen2_band_imgs = [b01_resample_img, b02_img, b03_img, b04_img, b05_resample_img, b06_resample_img, b07_resample_img, b08_img, b8A_resample_img, b09_resample_img, b10_resample_img, b11_resample_img, b12_resample_img]
	sen2_band_names = ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B8A', 'B09', 'B10', 'B11', 'B12']
	rsgislib.imageutils.stackImageBands(sen2_band_imgs, sen2_band_names, output_img, 0.0, 0.0, 'KEA', rsgislib.TYPE_16UINT)
	
	rsgislib.imageutils.popImageStats(output_img, usenodataval=True, nodataval=0, calcpyramids=True)


stack_sen2('/Users/pete/Development/s2cloudless_img_cmd/S2A_MSIL1C_20190826T113321_N0208_R080_T30UVD_20190826T150540.SAFE/GRANULE/L1C_T30UVD_A021813_20190826T113320/IMG_DATA', './tmp', 'S2A_MSIL1C_20190826T113321_N0208_R080_T30UVD_20190826T150540_stack_img.kea')

stack_sen2('/Users/pete/Development/s2cloudless_img_cmd/S2B_MSIL1C_20190917T112119_N0208_R037_T30UVD_20190917T132014.SAFE/GRANULE/L1C_T30UVD_A013219_20190917T112504/IMG_DATA', './tmp', 'S2B_MSIL1C_20190917T112119_N0208_R037_T30UVD_20190917T132014_stack_img.kea')

#stack_sen2('/Users/pete/Development/s2cloudless_img_cmd/S2B_MSIL1C_20190920T113319_N0208_R080_T30UVD_20190920T132811.SAFE/GRANULE/L1C_T30UVD_A013262_20190920T113318/IMG_DATA', './tmp', 'S2B_MSIL1C_20190920T113319_N0208_R080_T30UVD_20190920T132811_stack_img.kea')


