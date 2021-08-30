#https://python.plainenglish.io/automatically-resize-all-your-images-with-python-36f5b6dfc275
import argparse
import cv2
import os

def resizeImg(image, width=None, height=None):
  dim=None
  (h,w) = image.shape[:2]
  if width is None and height is None:
    return image
  
  elif width is not None and height is not None:
    dim = (width, height)
  
  elif width is None:
    r = height/float(h)
    dim = (int(w*r), height)
  else:
    r = width / float(w)
    dim = (width, int(h*r))
  resized = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
  return resized


def main():
  DS = os.path.sep
  imgDir = os.getcwd()
  parser = argparse.ArgumentParser(description='...')
  parser.add_argument('--x', default=0, type=int, help="Width")
  parser.add_argument('--y', default=0, type=int, help="Height (0 = automatic)")
  parser.add_argument('--normalize', default=0, type=int, help="Normalize (0 = automatic)")
  parser.add_argument('img_path', nargs='?', default="in/1.jpg")
  args = parser.parse_args()  
  xx = args.x
  yy = args.y
  print("x,y=",xx,yy)
  #normalize = args.normalize
  #img_path = args.img_path
  #res_path = args.img_path.rsplit(".", -1)[0]+"_"+str(x)+".jpg"
  #print("curdir=",os.path.curdir)
  #print ("getcwdu=",os.getcwdu())
  #dir_path = os.path.dirname(os.path.realpath(__file__))
  print("imgDir=",imgDir)
  
  folder           = imgDir+DS+"in"+DS
  newResizedFolder = imgDir+DS+"out"+DS
  if not os.path.exists(folder):
    os.makedirs(folder)
  if not os.path.exists(newResizedFolder):
    os.makedirs(newResizedFolder)
  for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename))
    if img is not None:
      x = xx or 2048
      newImage = resizeImg(img,x)
      zoomImage = resizeImg(img,600)
      newImgPath = newResizedFolder + filename.rsplit(".", -1)[0]+"_"+str(x)+".jpg"
      print(filename,newImage.shape,newImgPath)	
      cv2.imwrite(newImgPath, newImage)
      cv2.imshow("newImage", zoomImage)
      cv2.waitKey(333)
  cv2.waitKey(1000)
  cv2.destroyAllWindows()
	
	
if __name__ == "__main__":
  main()



#Different interpolation methods are used. 
#Preferable interpolation methods are 
#cv.INTER_AREA for shrinking 
#cv.INTER_CUBIC (slow) & 
#cv.INTER_LINEAR for zooming. 
#By default, the interpolation method cv.INTER_LINEAR is used for all resizing purposes.
