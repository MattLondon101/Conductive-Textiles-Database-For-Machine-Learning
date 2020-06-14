import os
from natsort import natsorted,ns
import cv2 as cv
from PIL import Image
import numpy as np
from sklearn.utils import shuffle

# train_ims4=[]
test_ims4=[]
src='C:/Users/matth/Documents/Jobs/TangibleMediaMIT/knits/Seyedin/test_ims/4'
for fileName in natsorted(os.listdir(src),alg=ns.PATH):
    filePath=os.path.join(src,fileName)
    if os.path.isfile(filePath):
        im=cv.imread(filePath,0)
        # train_ims4.append(im)
        test_ims4.append(im)

# binarize b&w (0&1)
# train_im4=[]
test_im4=[]
# for i in train_ims4:
for i in test_ims4:
    j=np.where(i>105,1,0)
    # train_im4.append(j)
    test_im4.append(j)
    

tr0=train_im0
tr1=train_im1
tr2=train_im2
tr3=train_im3
tr4=train_im4

te0=test_im0
te1=test_im1
te2=test_im2
te3=test_im3
te4=test_im4


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

trs=np.concatenate([tr0,tr1,tr2,tr3,tr4])
trls=np.concatenate([trl0,trl1,trl2,trl3,trl4])
tes=np.concatenate([te0,te1,te2,te3,te4])
tels=np.concatenate([tel0,tel1,tel2,tel3,tel4])

trim,trla=shuffle(trs,trls,random_state=0)
testim,testlab=shuffle(tes,tels,random_state=0)




