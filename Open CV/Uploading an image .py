#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install opencv-python


# In[1]:


import cv2


# In[2]:


img1=cv2.imread("C://Users//Raman Angra//Desktop//Open CV//duckk.png")


# In[3]:


img1
#Because it is in the from of an 3d array(b,g,r)


# In[4]:


img2= cv2.resize(img1,(1280,700))
cv2.imshow("Coloured Image",img2)
cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()

