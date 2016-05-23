# NeuralTalk

- The single python function to generate sentence from image.
- Forked from [NeuralTalk](https://github.com/karpathy/neuraltalk)
- An original [Readme.md](https://github.com/Thanabhat/neuraltalk/neuraltalk/Readme.md) is placed at neuraltalk/Readme.md

## Prerequisites
- [Caffe](http://caffe.berkeleyvision.org/) and [Caffe's python interface](http://caffe.berkeleyvision.org/installation.html#python) installed on your environment

## Setup
1. Install NeuralTalk using pip `sudo pip install git+https://github.com/Thanabhat/neuraltalk.git`
2. Download `VGG_ILSVRC_16_layers.caffemodel` from http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/ and place at `python_features/VGG_ILSVRC_16_layers.caffemodel`
3. Download `coco_cnn_lstm_v2.zip` from http://cs.stanford.edu/people/karpathy/neuraltalk/ , extract and place at `model/model_checkpoint_coco_visionlab43.stanford.edu_lstm_11.14.p`

## Example
Write this python code, place some `img.jpg`, run and get the sentence!
```python
from neuraltalk.caption_generator import CaptionGenerator

caption_generator = CaptionGenerator()
caption = caption_generator.get_caption('img.jpg')
print(caption)
```
