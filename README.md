# Sketch-To-Photo
A python and javascript application to convert a sketch to photo.
Javascript is used to create a graphical user interface to make a sketch.
Python along with Opencv Image Processing Library is used to convert the sketch to image.
The details about python code are as follows
OVERVIEW
•	First we will specify all the libraries used
•	Then we will link the Json data and simultaneously download the images
•	Then we will take one object at a time and hole fill it.
•	Then comparing with respective images is done.
•	Best comparison is resized and grabcut is performed thereafter.
•	Image is copied to the background.
•	Process is repeated till all objects are over.
•	Final processed image is saved.
LIBRARIES USED
•	Various libraries were used in doing this code like Opencv  , Numpy , glob , Json and google images download and PIL.
•	Opencv or Open Souce Computer Vision library was used for processing the image and it was the most most used libray in the code.
•	NumPy is an library for n dimentional  array used to represent the image in the form of an array.
•	Glob is used to traverse through all the objects inside a folder.
•	Json or Javascript Object  Notation Serializer was used to decode Json strings into Python Objects
•	Google images Download was used to download the sample images from google.
•	PIL  or Python Imaging Library was used to find out the size of the image.
JSON FILE WORK AND DOWNLOADING IMAGES
•	Opening the json file and append the background in a python list.
•	Download the image of the background and then resize and save it.
•	Append the background to python list
•	Download the images of the respective objects by linking through json data.
•	Append all the objects to the python list
HOLE FILLING
•	Hole filling of the object is required since by the help of this feature a better comparison of the image is takes place so we have the most similar image in the output with respect to the sketch created..
•	In this feature when we read the image we convert it in Greyscale and then thresh the image by using binary inversion.
•	Then we create a mask for the image and by using Floodfill function in opencv we fill the image.
•	The output of the hole filled image is shown below.
COMPARING IMAGES
•	By comparing the images we get the best match out of the downloaded images.
•	To do this we take the holefilled image of the object and traverse through the respective folder and find out the best match of the image.
•	To find this we calculate the good points in each image and find the similarity constant .
•	The image with the best similarity constant is stored.
RESIZE
•	For the convenience of our code we have used a resize command provided by opencv by the help of which are able to resize the image according to our requirement.
•	This command takes two arguments one image to be processed and the other the size that we want the image to become.
•	In this project we have used this command a number of times like when converting background to the size of sketch or converting the grabcut image to perfect size of the object in the sketch etc.
•	The output after resize is shown below.
GRABCUT
•	Grabcut is a very powerful tool by the help of which we extract the foreground of an image and delete the background.
•	By the help of this function we convert the background of an image to black and retrieve the foreground.
•	In our project we took the best comparable image and then did the Grabcut of that image.
•	For that we have to use a mask and specify the foreground and background model.
•	Then we have to specify a rectangle that around which object we have to Grabcut the Image.
•	There is a function in opencv for Grabcut  by the help of which we remove the background and store the output image.
•	The output after Grabcut is shown below.
COPY IMAGE TO BACKGROUND
•	Copying an image to the background is required with the extra portion removed  from it.
•	We traverse through the pixels of the image and copy only those pixels to the background which are not completely black i.e. their all pixel values are not zero.
•	For this we run two for loops and compare every tuple and print those which are not completely black.
•	At last we save the image.
•	The output after copying is shown below.


