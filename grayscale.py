import cv2 #opencv is a real time optimized computer vision library.
import matplotlib.image as image#image module in matplotlib library in python is used for working on images.
image=cv2.imread('img.jpg') #accesing the image
cv2.imshow("Original",image)
cv2.waitKey(0) #waitkey() function of opencv allows user to display a window for given millisec or until any key is pressed.

gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#converting the img into grayscale img

cv2.imshow('Grayscale',gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows() #destroyallwindows() function allows user to destroy all windows at any time.

#img=image.imread('img.jpg')
print(gray_img.shape)#getting pixels of image in a matrix format.
print("img as array",gray_img)

