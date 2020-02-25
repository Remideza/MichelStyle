# MichelStyle
MichelStyle is an implementation of theme images interpolation for [Fast Style Transfer for Arbitrary Styles](https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/tf2_arbitrary_image_stylization.ipynb)

The goal of it is to generate a video from a static image using Style Tranfer
### An example with the first clip made with it, Otaniemi
[![](http://img.youtube.com/vi/IYK83KiojzA/0.jpg)](http://www.youtube.com/watch?v=IYK83KiojzA "Otaniemi - Bend the Future")

# How it works
You first set the image that you want to create a video with as cover.jpg, then you set the themes you want to use by putting the 256x256 images in the param dir, you then name the images with the number of hundredth of a second you want for transision
For example, in the included repo, you start with image 0 transition into the second image at 1 second then onto the third at 2 seconds and ends at 2.5 seconds on the last image
![Here](https://i.ibb.co/kgQGKww/ex.jpg)


## Parameters
As i didn't do any graphic interface or command line parameters, the editable parameters are all on top of the script in capslock

|                |Function                         
|----------------|-------------------------------|
|FPS            |Sets the FPS of the final video  
|MAXBATCH|Numbers of generated frames saved in ram before saving to disk 
|VIDEOCOMBINE|Generate or not the video once the frame generation is done
|AUDIOCOMBINE|If you put an audio.mp3 in the folder, it automaticly combine the audio with the video at the end of the generation


## Thricky things
Since i originally didn't plan to release it, the program is quite in a development state, there is a few things to know about it
It generates frames in the temp directory, saving them as jpg images, which mean you can delete part of the frames in the temp dir to regenate them with different themes images, it can save a lot of time instead of redoing the whole video
If you want to do another video with others images, you have to delete the whole content of the temp folder
## Help finding theme images
While trying to find themes for the clip, i made a theme image tester that is included in the themetest directory, this will generate single frames for each theme image you wanna test to show you how it's going to look like on the final video