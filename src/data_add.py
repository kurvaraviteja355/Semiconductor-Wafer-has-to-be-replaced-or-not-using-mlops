import os
from glob import glob

data_dirs = ["wafer-dataset-main/Training_Batch_Files", "wafer-dataset-main/Prediction_Batch_files"]

for data in data_dirs:
    files = glob(data + r"/*.csv")
    for file in files:
        os.system(f"dvc add {file}")

print("\n #### all files added to dvc ####")
