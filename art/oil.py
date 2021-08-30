import cv2
img = cv2.imread('1.jpg')
res = cv2.xphoto.oilPainting(img, 7, 1)
cv2.imwrite("1oil.jpg", res)

ret = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
cv2.imwrite("1wet.jpg", ret)

dst_gray, dst_color  = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 
cv2.imwrite("1dst_gray.jpg", dst_gray)
cv2.imwrite("1dst_color.jpg", dst_color)

dst_gray2, dst_color2  = cv2.pencilSketch(img, sigma_s=20, sigma_r=0.1, shade_factor=0.1) 
cv2.imwrite("1dst_gray.jpg", dst_gray)
cv2.imwrite("1dst_color.jpg", dst_color)
cv2.imwrite("2dst_gray.jpg", dst_gray2)
cv2.imwrite("2dst_color.jpg", dst_color2)




cv2.imshow("res", res)
cv2.waitKey(0)


cv2.imshow("ret", ret)
cv2.waitKey(0)

cv2.imshow("dst_gray", dst_gray)
cv2.waitKey(0)

cv2.imshow("dst_color", dst_color)
cv2.waitKey(0)

cv2.imshow("dst_gray2", dst_gray2)
cv2.waitKey(0)

cv2.imshow("dst_color2", dst_color2)
cv2.waitKey(0)

cv2.destroyAllWindows()
