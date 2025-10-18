import numpy as np

img = np.random.randint(0,256,(100,100))

bright = np.clip(img * 2,0,255)

flipped = img.T

print("original shape: ",img.shape)
print("flipped shape: ",flipped.shape)
print("max brightness value: ",bright.max())