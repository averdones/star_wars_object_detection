# Star Wars Object Detection
This repository contains the dataset and some of the configuration files to train an object detector of R2-D2 and BB-8 from Star Wars, 
using [Tensorflow's object detection API](https://github.com/tensorflow/models/tree/master/research/object_detection).

The final model has been fine-tuned using one of the [models pre-trained](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)
on the [COCO dataset](http://mscoco.org/) as a starting point (*transfer learning*).

## Some results
![result_1](https://github.com/averdones/star_wars_object_detection/blob/master/results/result_1.gif "Result 1")

![result_2](https://github.com/averdones/star_wars_object_detection/blob/master/results/result_2.gif "Result 2")

The outcome seems acceptable considering the small size and low variability of the dataset used.

## Trying the dataset
In order to try the dataset, you first need to follow the [installation instructions](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md) on the Tensorflow page. 
Then, you can train your own model following analogous commands as in the [pet detector](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_pets.md).
