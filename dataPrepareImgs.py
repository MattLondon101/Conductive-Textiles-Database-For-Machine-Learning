from __future__ import print_function
from keras.preprocessing.image import ImageDataGenerator
import numpy as np 
import os
import glob
import skimage.io as io
import skimage.transform as trans

def adjustData(img,flag_multi_class,num_class):
    img = img / 255  
    return (img)


def trainGenerator(batch_size,train_path,image_folder,aug_dict,image_color_mode = "grayscale",
                    mask_color_mode = "grayscale",image_save_prefix  = "image",
                    flag_multi_class = False,num_class = 1,save_to_dir = None,target_size = (100,100),seed = 1):
    #if you want to visualize the results of generator, set save_to_dir = "your path"
    image_datagen = ImageDataGenerator(**aug_dict)
    image_generator = image_datagen.flow_from_directory(
        train_path,
        classes = [image_folder],
        class_mode = None,
        color_mode = image_color_mode,
        target_size = target_size,
        batch_size = batch_size,
        save_to_dir = save_to_dir,
        save_prefix  = image_save_prefix,
        seed = seed)
    train_generator = image_generator
    for (img) in train_generator:
        img = adjustData(img,flag_multi_class,num_class)
        yield (img)

# Orig Values
data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')
"""
data_gen_args = dict(rotation_range=.4,
                    width_shift_range=0.06,
                    height_shift_range=0.06,
                    shear_range=0.7,
                    zoom_range=0.06,
                    horizontal_flip=True,
                    fill_mode='nearest')
"""
#myGenerator = trainGenerator(1,'C:/Users/matth/Documents/Jobs/TangibleMediaMIT/knits/Seyedin_2018/','0_plain',data_gen_args,save_to_dir = 'C:/Users/matth/Documents/Jobs/TangibleMediaMIT/knits/Seyedin_2018/train_ims_orig/0')
#myGenerator = trainGenerator(1,'C:/Users/matth/Documents/Jobs/TangibleMediaMIT/knits/Seyedin_2018/','1_coknit',data_gen_args,save_to_dir = 'C:/Users/matth/Documents/Jobs/TangibleMediaMIT/knits/Seyedin_2018/train_ims_orig/1')
#myGenerator = trainGenerator(1,'C:/Users/matth/Documents/Jobs/TangibleMediaMIT/knits/Seyedin_2018/','2_conductive_stitch_coknit',data_gen_args,save_to_dir = 'C:/Users/matth/Documents/Jobs/TangibleMediaMIT/knits/Seyedin_2018/train_ims_orig/2')
#myGenerator = trainGenerator(1,'C:/Users/matth/Documents/Jobs/TangibleMediaMIT/knits/Seyedin_2018/','3_plain_non_conductive_stitch',data_gen_args,save_to_dir = 'C:/Users/matth/Documents/Jobs/TangibleMediaMIT/knits/Seyedin_2018/train_ims_orig/3')
myGenerator = trainGenerator(1,'C:/Users/matth/Documents/Jobs/TangibleMediaMIT/knits/Seyedin_2018/','4_coknit_alternate',data_gen_args,save_to_dir = 'C:/Users/matth/Documents/Jobs/TangibleMediaMIT/knits/Seyedin_2018/train_ims_orig/4')


num_batch = 39
for i,batch in enumerate(myGenerator):
    if(i >= num_batch):
        break

