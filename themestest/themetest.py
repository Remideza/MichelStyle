import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import tensorflow_hub as hub
import cv2
import PIL
import os
import pickle

def tensor_to_image(tensor):
  tensor = tensor*255
  tensor = np.array(tensor, dtype=np.uint8)
  if np.ndim(tensor)>3:
    assert tensor.shape[0] == 1
    tensor = tensor[0]
  return PIL.Image.fromarray(tensor)

generatedtable = []
filenametable = []
themetable = []

for filename in os.listdir('./themes'):
	themetable.append(filename[:-4])
	lol = cv2.imread('./themes/' + filename, cv2.IMREAD_COLOR)
	cv2.imwrite('./themes/' + filename, cv2.resize(lol, (256,256)))

for filename in os.listdir('./generated'):
	
	generatedtable.append(filename[:-4])

todot = []

for t in themetable:
	if t not in generatedtable:
		todot.append(t)


todo = len(todot)
print(str(todo) + " themes to generate")
hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
path = os.getcwd()


content_image = plt.imread('cover.jpg')
content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.

for c in todot:
	print("")
	style_image = plt.imread('./themes/' + c + '.jpg')
	
	style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.
	outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
	
	stylized = tensor_to_image(outputs[0])
	
	stylized.save('./generated/' + c +".jpg")
	todo = todo - 1
	print("remaining " + str(todo))



