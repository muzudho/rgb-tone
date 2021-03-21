import cv2
import numpy as np
from PIL import Image
from datetime import datetime

images = []

# 描画する画像を作る,128を変えると色を変えれます 0黒→255白
#width = 300
#height = 300
#canvas = np.full((height, width, 3), 128, dtype=np.uint8)
#new_img = Image.fromarray(canvas)
# images.append(new_img)

# `im_arr1` - 大きな配列
im_arr1 = cv2.imread("./shared/cos-curve.png")
print(f"im_arr1={im_arr1}")
cv2.imshow('Title', im_arr1)
cv2.waitKey(0)
cv2.destroyAllWindows()
images.append(Image.fromarray(im_arr1))

# Vivid
im_arr1 = cv2.imread("./shared/vivid-tone(cos-curve-exagger1of4).png")
images.append(Image.fromarray(im_arr1))

# Strong saturation
im_arr1 = cv2.imread("./shared/bright-tone(cos-curve-8of10-add-2of10).png")
images.append(Image.fromarray(im_arr1))

im_arr1 = cv2.imread("./shared/strong-tone(cos-curve-8of10).png")
images.append(Image.fromarray(im_arr1))

im_arr1 = cv2.imread("./shared/deep-tone(cos-curve-6of10).png")
images.append(Image.fromarray(im_arr1))

# Soft saturation
im_arr1 = cv2.imread("./shared/light-tone(cos-curve-3of10+7of10).png")
images.append(Image.fromarray(im_arr1))

im_arr1 = cv2.imread("./shared/soft-tone(cos-curve-4of10+4of10).png")
images.append(Image.fromarray(im_arr1))

im_arr1 = cv2.imread("./shared/dull-tone(cos-curve-5of10+2of10).png")
images.append(Image.fromarray(im_arr1))

im_arr1 = cv2.imread("./shared/dark-tone(cos-curve-4of10).png")
images.append(Image.fromarray(im_arr1))

# Pale saturation
im_arr1 = cv2.imread("./shared/pale-tone(cos-curve-2of10+8of10).png")
images.append(Image.fromarray(im_arr1))

im_arr1 = cv2.imread("./shared/light-grayish-tone(cos-curve-3of10+6of10).png")
images.append(Image.fromarray(im_arr1))

im_arr1 = cv2.imread("./shared/grayish-tone(cos-curve-3of10+3of10).png")
images.append(Image.fromarray(im_arr1))

im_arr1 = cv2.imread("./shared/dark-grayish-tone(cos-curve-2of10-2of10).png")
images.append(Image.fromarray(im_arr1))


# cv2.imshow('canvas',canvas)
# cv2.imwrite('form.jpg',canvas)
date = datetime.now().strftime("%Y%m%d_%H%M%S")
path = f"output/out-{date}.gif"
fps = 1
duration_time = int(1000.0 / fps)
images[0].save(path,
               save_all=True,
               append_images=images[1:],
               optimize=False,
               duration=duration_time,
               loop=0)
