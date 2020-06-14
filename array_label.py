import os
from natsort import natsorted,ns
import cv2 as cv
from PIL import Image
import numpy as np
from sklearn.utils import shuffle

# iterate dirs
train_ims=[]
# test_ims=[]
src='C:/Users/matth/Documents/Jobs/TangibleMediaMIT/knits/Seyedin/train_ims'
for fold in natsorted(os.listdir(src),alg=ns.PATH):
    fopath=os.path.join(src,fold)
    for fileName in natsorted(os.listdir(fopath),alg=ns.PATH):
        filePath=os.path.join(fopath,fileName)
        if os.path.isfile(filePath):
            im=cv.imread(filePath,0)
            train_ims.append(im)
            # test_ims.append(im)


# binarize b&w (0&1)
# train_im=[]
test_im=[]
# for i in train_ims:
for i in test_ims:
    j=np.where(i>105,1,0)
    # train_im.append(j)
    test_im.append(j)
    

trl0=[0]*40
trl1=[1]*40
trl2=[2]*40
trl3=[3]*40
trl4=[4]*40

tel0=[0]*20
tel1=[1]*20
tel2=[2]*20
tel3=[3]*20
tel4=[4]*20

trls=np.concatenate([trl0,trl1,trl2,trl3,trl4])
tels=np.concatenate([tel0,tel1,tel2,tel3,tel4])

trim,trla=shuffle(trs,trls,random_state=0)
testim,testlab=shuffle(tes,tels,random_state=0)
