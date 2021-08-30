import cv2
img = cv2.imread('1.jpg')
res = cv2.xphoto.oilPainting(img, 7, 1)
cv2.imwrite("1oil.jpg", res)
cv2.imshow("res", res)
cv2.waitKey(0)

ret = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
cv2.imwrite("1wet.jpg", ret)
cv2.imshow("ret", ret)
cv2.waitKey(0)

cv2.destroyAllWindows()
