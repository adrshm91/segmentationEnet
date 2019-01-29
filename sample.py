import cv2
import numpy as np

img_path = "C:\\Users\\z003zxuz\\Documents\\Research_Project\\code\\segmentation\\data\\aachen_000000_000019.png"

img = cv2.imread(img_path, -1)

img_mean_channels = np.mean(img, axis=0)
img_mean_channels = np.mean(img_mean_channels, axis=0)

mean_channels += img_mean_channels