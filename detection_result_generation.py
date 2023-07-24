import os
import numpy as np
import pandas as pd
import nrrd
import nibabel as nib

data_folder = "/home/tianyu/Desktop/data_base/final_data/mask2"

files = os.listdir(data_folder)
files_sorted = sorted(files)

result = []
for i, file in enumerate(files_sorted):

    print(i)

    if i == 24:
        result.append([124, 0, 0, 0, 0, 0, 0, 0])
        continue

    img = nib.load(os.path.join(data_folder, file))
    data = img.get_fdata()

    coordZ, coordX, coordY = np.where(data == 1)

    x_length = coordX.max() - coordX.min()
    y_length = coordY.max() - coordY.min()
    z_length = coordZ.max() - coordZ.min()
    center_x = coordX.min() + x_length / 2
    center_y = coordY.min() + y_length / 2
    center_z = coordZ.min() + z_length / 2

    result.append([100+i, center_x, center_y, center_z, x_length, y_length, z_length, 0.7])

# 转化为DataFrame并保存为csv文件
df = pd.DataFrame(result, columns=['public_id', 'coordX', 'coordY', 'coordZ', 'x_length', 'y_length', 'z_length', 'probability'])
df.to_csv("output3.csv", index=False)