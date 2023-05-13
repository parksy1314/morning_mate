# -*- coding: utf-8 -*-

import tensorflow as tf
tf.compat.v1.disable_eager_execution()
import numpy as np
import os
import glob
import imageio.v2 as imageio
#import imread, imsave
import cv2
import argparse
from tensorflow.python.framework import ops

tf.compat.v1.disable_eager_execution()
graph = tf.compat.v1.get_default_graph()

parser = argparse.ArgumentParser()
parser.add_argument('--no_makeup', type=str, default=os.path.join('imgs', 'no_makeup', 'xfsy_0068.png'), help='path to the no_makeup image')
args = parser.parse_args()

def preprocess(img):
#    return (img / 255. - 0.5) * 2
    return ((img / 255.0) - 0.5) * 2.0

def deprocess(img):
#    return (img + 1.) / 2.0  
    return ((img + 1) / 2 * 255).astype(np.uint8)  

batch_size = 1
img_size = 256
no_makeup = cv2.resize(imageio.imread(args.no_makeup), (img_size, img_size))
X_img = np.expand_dims(preprocess(no_makeup), 0)
makeups = glob.glob(os.path.join('imgs', 'makeup', '*.*'))
result = np.ones((2 * img_size, (len(makeups) + 1) * img_size, 3))
result[img_size: 2 *  img_size, :img_size] = no_makeup / 255.

ops.reset_default_graph()
sess = tf.compat.v1.Session(graph=tf.compat.v1.get_default_graph())
sess.run(tf.compat.v1.global_variables_initializer())

saver = tf.compat.v1.train.import_meta_graph(os.path.join('models', 'model.meta'))
saver.restore(sess, tf.train.latest_checkpoint('models'))

graph = tf.compat.v1.get_default_graph()
X = graph.get_tensor_by_name('X:0')
Y = graph.get_tensor_by_name('Y:0')
Xs = graph.get_tensor_by_name('generator/xs:0')

for i in range(len(makeups)):
    makeup = cv2.resize(imageio.imread(makeups[i]), (img_size, img_size))
    Y_img = np.expand_dims(preprocess(makeup), 0)
    Xs_ = sess.run(Xs, feed_dict={X: X_img, Y: Y_img})
    Xs_ = deprocess(Xs_)
    result[:img_size, (i + 1) * img_size: (i + 2) * img_size] = makeup / 255.
    result[img_size: 2 * img_size, (i + 1) * img_size: (i + 2) * img_size] = Xs_[0]
    result = result.astype(np.uint8)
#imsave('result.jpg', result)
imageio.imwrite('result.jpg', result)
