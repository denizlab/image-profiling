import os
import numpy as np
import pandas as pd

from PIL import Image

# Image profiling pipeline
def pipeline(images_dir):
    image_array = iteration(images_dir)
    df = extract_feature(image_array)
    return df

# Loading function
def loader_test(image_file):
    try:
        image = Image.open(image_file)
        image = np.asarray(image)
        return image
    except: 
        print('illegal file', image_file)
        return None

# Iteration loop
# In:  directory name
# Out: array of numpy
def iteration(images_dir):
    image_array = []
    for image_file in sorted(os.listdir(images_dir)):
        image = loader_test(os.path.join(images_dir, image_file))
        if image is not None:
            image_array.append(image)
    return image_array 

# Features definition
# W, H, channel, Mean, Max, Min, Variance
# In:  numpy array of an image
# Out: features in a dictionary
def get_features(image):
    #q = np.quantile(image.reshape(-1), [0.25, 0.5, 0.75])
    channel = 1 if len(image.shape) <=2 else image.shape[2] # Verify channel
    features =  {'width' : image.shape[0], 
                 'height' : image.shape[1], 
                 'channel': channel, 
                 'mean' : image.mean(), 
                 'max' : image.max(), 
                 'min' : image.min(), 
                 'variance' : image.var(),
                 #'25% quantile' : q[0], 
                 #'median' : q[1], 
                 #'75% quantile' : q[2]
                 }
    return features

# Feature extraction
def extract_feature(image_array):
    df = pd.DataFrame(get_features(image_array[0]), index = [0])
    for i in range(len(image_array) - 1):
        features = get_features(image_array[i + 1])
        df = df.append(features, ignore_index = True)
    return df

# Profiling
def profiling(df, profile_name):
    import pandas_profiling
    profile = df.profile_report()
    profile.to_file(prefile_name, '.html')

# Save image
def Write_image(array, image_name):
    image = Image.fromarray(array)
    image.save(image_name, '.jpeg')
