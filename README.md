# Conductive-Textiles-Database-For-Machine-Learning

* Database of conductive and non-conductive knit patterns for use in machine learning.

* Sequential CNN for training and testing

This repository contains 40 train and 20 test images for each knit type (see Index below)
Black and White (0 and 1) images are in train_ims and test_ims directories.

```
Index for Knit Types:
0 = plain
1 = co-knit
2 = conductive_stitch_co-knit
3 = plain_non_conductive_stitch
4 = co-knit_alternate
```

The remaining directories comprise the original images (first 5 directories) scripts for preparing the data for training. File dataPrepareImgs.py creates greyscale copies and augmentations of original images. File array_label.py converts greyscale to black and white, then to arrays with a corresponding label array. Data was trained with the sequential CNN in sequentialCNN.py.The original images were taken from [Seyedin 2018](https://www.sciencedirect.com/science/article/abs/pii/S2352940718300180). 

The first training run achieved:
```
val_accuracy: 0.9700
Test loss: 0.451622017621994
Test accuracy: 0.9700000286102295
```

The ultimate goal of this repository is to develop an accurate model to aid in development of conductive textiles.

