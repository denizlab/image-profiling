import numpy as np
import pandas as pd
import h5py

from preprocessing import extract_feature

def main():
    pipeline('images')

# Image profiling pipeline
def pipeline(iteration_choice, max_data):
    image_array = iteration_choice(max_data = max_data)
    df = extract_feature(image_array)
    return df

# Load OAI/NYU data
def loader_h5py(image_file):
    try:
        image = np.array(h5py.File(image_file, 'r')['data'][:]).astype('float32')
        image = np.asarray(image)
        return image
    except: 
        print('illegal file', image_file)
        return None

# Loading iteration for OAI
def iteration_OAI(max_data = 100):
    images_dir = '/gpfs/data/denizlab/Users/bz1030/data/OAI_2020/'
    OAI_csv = '/gpfs/data/denizlab/Users/bz1030/data/OAI_2020/train.csv'
    OAI_data = pd.read_csv(sup_contents)
    image_array = []
    for index in range(max_data):
        image_path = get_OAI_path(images_dir, OAI_data, index)
        image = loader_h5py(image_path)
        if image is not None:
            image_array.append(image)
    return image_array 

# Get OAI image path from csv
# From Bofei's code (data.py)
def get_OAI_path(images_dir, OAI_data, index):
    row = OAI_data.loc[index]
    month = row['Visit']
    pid = row['ID']
    target = int(row['KLG'])
    side = int(row['SIDE'])
    if side == 1:
        fname = '{}_{}_RIGHT_KNEE.hdf5'.format(pid,month)
    elif side == 2:
        fname = '{}_{}_LEFT_KNEE.hdf5'.format(pid, month)
    image_path = os.path.join(images_dir, month, fname)
    return image_path

# Loading iteration for NYU
def iteration_NYU(max_data = 100):
    NYU_csv = '/gpfs/data/denizlab/Users/jt3545/bofei_test/i17-Data-Process-Infer/nyu_data_unsup_noTKR.csv'
    NYU_data = pd.read_csv(unsup_contents)
    image_array = []
    for index in range(max_data):
        image_path = get_NYU_path(NYU_data, index)
        image = loader_h5py(image_path)
        if image is not None:
            image_array.append(image)
    return image_array 

# Get NYU image path from csv
# From Bofei's code (data.py)
def get_NYU_path(NYU_data, index):
    row = NYU_data.loc[index]
    image_path = row['file_path']
    return image_path

if __name__ == '__main__':
    main()
