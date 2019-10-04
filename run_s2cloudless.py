import rsgislib
import rsgislib.imageutils
import rsgislib.rastergis
import numpy
from rios import applier
from rios import cuiprogress
from s2cloudless_img import S2PixelCloudDetector

def run_s2cloudless(input_img, out_prob_img, out_cloud_msk, gdalformat):
    """
Function which runs the S2Cloudless methods in 256 x 256 pixel blocks 
across an image.

:param input_img: input sentinel-2 image with all 13 bands.
:param output_img: the output image cloud mask
:param gdalformat: the GDAL image file format of the output image file.

"""
    s2_pxl_cloud_detect = S2PixelCloudDetector(all_bands=True)

    infiles = applier.FilenameAssociations()
    infiles.s2image = input_img
    outfiles = applier.FilenameAssociations()
    outfiles.out_prob_img = out_prob_img
    outfiles.out_cloud_msk = out_cloud_msk
    otherargs = applier.OtherInputs()
    otherargs.s2_pxl_cloud_detect = s2_pxl_cloud_detect
    aControls = applier.ApplierControls()
    aControls.progress = cuiprogress.CUIProgressBar()
    aControls.drivername = gdalformat
    aControls.omitPyramids = True
    aControls.calcStats = False

    def _applyS2Cloudless(info, inputs, outputs, otherargs):
        """
        This is an internal rios function
        """
        # Current shape is: [13 x n x m]
        # Image data needs to be in shape [1 x n x m x 13]
        s2img_reshp = numpy.expand_dims(numpy.stack([inputs.s2image[0], inputs.s2image[1], inputs.s2image[2], inputs.s2image[3], inputs.s2image[4], inputs.s2image[5], inputs.s2image[6], inputs.s2image[7], inputs.s2image[8], inputs.s2image[9], inputs.s2image[10], inputs.s2image[11], inputs.s2image[12]], axis=2), axis=0)
        s2img_reshp_toa = s2img_reshp/10000.0
        outputs.out_prob_img = otherargs.s2_pxl_cloud_detect.get_cloud_probability_maps(s2img_reshp_toa)
        outputs.out_cloud_msk = otherargs.s2_pxl_cloud_detect.get_mask_from_prob(outputs.out_prob_img)

    applier.apply(_applyS2Cloudless, infiles, outfiles, otherargs, controls=aControls)


run_s2cloudless('./S2A_MSIL1C_20190826T113321_N0208_R080_T30UVD_20190826T150540_stack_img.kea', 'S2A_MSIL1C_20190826T113321_N0208_R080_T30UVD_20190826T150540_cloud_prob.kea', 'S2A_MSIL1C_20190826T113321_N0208_R080_T30UVD_20190826T150540_cloud_msk.kea', 'KEA')
rsgislib.imageutils.popImageStats('S2A_MSIL1C_20190826T113321_N0208_R080_T30UVD_20190826T150540_cloud_prob.kea', usenodataval=True, nodataval=0, calcpyramids=True)
rsgislib.rastergis.populateStats(clumps='S2A_MSIL1C_20190826T113321_N0208_R080_T30UVD_20190826T150540_cloud_msk.kea', addclrtab=True, calcpyramids=True, ignorezero=True)
"""
run_s2cloudless('./S2B_MSIL1C_20190917T112119_N0208_R037_T30UVD_20190917T132014_stack_img.kea', 'S2B_MSIL1C_20190917T112119_N0208_R037_T30UVD_20190917T132014_cloud_prob.kea', 'S2B_MSIL1C_20190917T112119_N0208_R037_T30UVD_20190917T132014_cloud_msk.kea', 'KEA')
rsgislib.imageutils.popImageStats('S2B_MSIL1C_20190917T112119_N0208_R037_T30UVD_20190917T132014_cloud_prob.kea', usenodataval=True, nodataval=0, calcpyramids=True)
rsgislib.rastergis.populateStats(clumps='S2B_MSIL1C_20190917T112119_N0208_R037_T30UVD_20190917T132014_cloud_msk.kea', addclrtab=True, calcpyramids=True, ignorezero=True)

run_s2cloudless('./S2B_MSIL1C_20190920T113319_N0208_R080_T30UVD_20190920T132811_stack_img.kea', 'S2B_MSIL1C_20190920T113319_N0208_R080_T30UVD_20190920T132811_cloud_prob.kea', 'S2B_MSIL1C_20190920T113319_N0208_R080_T30UVD_20190920T132811_cloud_msk.kea', 'KEA')
rsgislib.imageutils.popImageStats('S2B_MSIL1C_20190920T113319_N0208_R080_T30UVD_20190920T132811_cloud_prob.kea', usenodataval=True, nodataval=0, calcpyramids=True)
rsgislib.rastergis.populateStats(clumps='S2B_MSIL1C_20190920T113319_N0208_R080_T30UVD_20190920T132811_cloud_msk.kea', addclrtab=True, calcpyramids=True, ignorezero=True)
"""
