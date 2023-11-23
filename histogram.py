import cv2
import numpy as np
from matplotlib import pyplot as plt


res = cv2.imread("resim/minyonlar.jpg")
cv2.imshow("Deneme", res)
B = res[:, :, 0]
G = res[:, :, 1]
R = res[:, :, 2]
T = 0.299 * R + 0.587 * G + 0.114 * B
a = np.zeros(256)
[w,h] =(T.shape)
for v in range(0,w):
    for u in range(0,h):
        i = res[v, u]
        a[i] =  a[i] +1
print(a)
plt.style.use("ggplot")
plt.hist(a)
plt.show()
