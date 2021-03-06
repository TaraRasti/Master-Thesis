# -*- coding: utf-8 -*-
"""nifti.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FOFjdSBLxKwXdGiqTW6go4_T0VbV6x8_
"""

from google.colab import drive
drive.mount('/content/drive')

import os
import numpy as np
import nibabel as nib
import imageio
import matplotlib
from nibabel.viewers import OrthoSlicer3D
from matplotlib import pylab as plt

L = os.listdir('/content/drive/MyDrive/new-oasis/normal')
path ='/content/drive/MyDrive/new-oasis/normal/'

A = []
for i in range(len(L)):
  niifilepath = path + L[i]
  img = nib.load(niifilepath) 
  A.append(img.shape)   
  print(niifilepath, img.shape)

L = os.listdir('/content/drive/MyDrive/new-oasis/normal')
path ='/content/drive/MyDrive/new-oasis/normal/'
import numpy as np
A = []
for i in range(len(L)):
  niifilepath = path + L[i]
  img = nib.load(niifilepath) 
  A.append(img.shape)   
  print(niifilepath[40:52], img.shape)

L = os.listdir('/content/drive/MyDrive/new-oasis/normal')
path ='/content/drive/MyDrive/new-oasis/normal/'
import numpy as np
B = []
for i in range(len(L)):
  niifilepath = path + L[i]
  img = nib.load(niifilepath) 
  if img.shape == (176, 256, 256):
    B.append(niifilepath)

for i in range(len(B)):
  niifilepath = B[i]
  img = nib.load(niifilepath)
  def read_niifile(niifilepath): #read niifile file
    img = nib.load(niifilepath) #download niifile file (actually extract the file)
    img_fdata = img.get_fdata() #Get niifile data
    return img_fdata

  s = '{}' + niifilepath[40:52] + '.png'

  def save_fig(niifilepath,savepath): #Save as picture
    fdata = read_niifile(niifilepath) #Call the above function to get data
    (x,y,z) = fdata.shape #Get data shape information: (length, width, dimension-number of slices, fourth dimension)

    for k in range(z):
      silce = fdata[:,:,k] #Three positions represent three slices with different angles
      imageio.imwrite(os.path.join(savepath, s.format(k)),silce) #Save the slice information as png format
 
  savepath='/content/drive/MyDrive/' + niifilepath[40:52]
  save_fig(niifilepath,savepath)

L = os.listdir('/content/drive/MyDrive/new-oasis/normal')
path ='/content/drive/MyDrive/new-oasis/normal/'
import numpy as np
B = []
for i in range(len(L)):
  niifilepath = path + L[i]
  img = nib.load(niifilepath) 
  if img.shape != (176, 256, 256):
    B.append(niifilepath) 
    print(niifilepath, img.shape)

for i in range(26):
  niifilepath = B[i+134]
  img = nib.load(niifilepath)
  def read_niifile(niifilepath): #read niifile file
    img = nib.load(niifilepath) #download niifile file (actually extract the file)
    img_fdata = img.get_fdata() #Get niifile data
    return img_fdata

  s = '{}' + niifilepath[40:52] + '.png'

  def save_fig(niifilepath,savepath): #Save as picture
    fdata = read_niifile(niifilepath) #Call the above function to get data
    (x,y,z) = fdata.shape #Get data shape information: (length, width, dimension-number of slices, fourth dimension)

    for j in range(y):
      silce = fdata[:,j,:] #Three positions represent three slices with different angles
      imageio.imwrite(os.path.join(savepath, s.format(j)),silce) #Save the slice information as png format
 
  savepath='/content/drive/MyDrive/' + niifilepath[40:52]
  save_fig(niifilepath,savepath)

for i in range(12):
  niifilepath = B[i+160]
  img = nib.load(niifilepath)
  def read_niifile(niifilepath): #read niifile file
    img = nib.load(niifilepath) #download niifile file (actually extract the file)
    img_fdata = img.get_fdata() #Get niifile data
    return img_fdata

  s = '{}' + niifilepath[40:52] + '.png'

  def save_fig(niifilepath,savepath): #Save as picture
    fdata = read_niifile(niifilepath) #Call the above function to get data
    (x,y,z) = fdata.shape #Get data shape information: (length, width, dimension-number of slices, fourth dimension)

    for k in range(z):
      silce = fdata[:,:,k] #Three positions represent three slices with different angles
      imageio.imwrite(os.path.join(savepath, s.format(k)),silce) #Save the slice information as png format
 
  savepath='/content/drive/MyDrive/' + niifilepath[40:52]
  save_fig(niifilepath,savepath)

niifilepath = "/content/drive/MyDrive/new-oasis/normal/sub-OAS30253_ses-d1288_T1w.nii.gz"
img = nib.load(niifilepath)
def read_niifile(niifilepath): #read niifile file
  img = nib.load(niifilepath) #download niifile file (actually extract the file)
  img_fdata = img.get_fdata() #Get niifile data
  return img_fdata

s = '{}' + niifilepath[40:52] + '.png'

def save_fig(niifilepath,savepath): #Save as picture
  fdata = read_niifile(niifilepath) #Call the above function to get data
  (x,y,z) = fdata.shape #Get data shape information: (length, width, dimension-number of slices, fourth dimension)

  for k in range(z):
    silce = fdata[:,:,k] #Three positions represent three slices with different angles
    imageio.imwrite(os.path.join(savepath, s.format(k)),silce) #Save the slice information as png format
 
savepath='/content/drive/MyDrive/' + niifilepath[40:52]
save_fig(niifilepath,savepath)