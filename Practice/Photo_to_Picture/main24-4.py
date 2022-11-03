import numpy as np
import cv2 

ff=np.fromfile(r'Practice\Photo_to_Picture\cake.jpg', np.uint8 )
img =cv2.imdecode(ff, 1)
img =cv2.resize(img, dsize=(0,0), fx=0.5,fy=0.5, interpolation=cv2.INTER_LINEAR)
cartoon_img = cv2.stylization(img, sigma_s=100, sigma_r=0.1)

cv2.imshow('cartoon view', cartoon_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
