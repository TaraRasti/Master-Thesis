#!/usr/bin/env python
# coding: utf-8

# In[84]:


from PIL import Image
from matplotlib import image
from matplotlib import pyplot
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp
import imageio


# In[90]:


L = []
for i in range(len(os.listdir('/Users/taraapple/Downloads/ALZHEIMER/demented/'))):
    L.append(os.listdir('/Users/taraapple/Downloads/ALZHEIMER/demented/')[i])


# In[92]:


L[22]


# In[93]:


L = np.delete(L, 22, axis=None)
L


# In[94]:


len(L)


# In[95]:


path = []
for i in range(150):
    path.append('/Users/taraapple/Downloads/ALZHEIMER/demented/' +  L[i])


# In[96]:


path


# In[97]:


len(path)


# In[98]:


for i in range(len(path)):
    from matplotlib import image
    filepath = path[i] + '/150' + path[i][46:60] + '.png'
    image  = image.imread(filepath)
    if len(image.shape) > 2 and image.shape[2] == 4:
        img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    file_path =  '/Users/taraapple/Downloads/A/demented/150' + path[i][46:60]
    plt.imsave(file_path, img, format='jpg', cmap = 'gray')


# In[99]:


from PIL import Image
from matplotlib import image
from matplotlib import pyplot
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp
image = image.imread('/Users/taraapple/Downloads/A/demented/150sub-OAS30853')
print(image.dtype)
print(image.shape)
pyplot.imshow(image)
pyplot.show()

