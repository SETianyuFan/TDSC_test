import os
import numpy as np
import pandas as pd
import nrrd
import nibabel as nib


data_folder = "/home/tianyu/Desktop/data_base/final_data/mask2/DATA_118.nii.gz"

img = nib.load(data_folder)
data = img.get_fdata()

coordZ, coordY, coordX = np.where(data == 1)  # 获取所有mask点的坐标

print(coordY)