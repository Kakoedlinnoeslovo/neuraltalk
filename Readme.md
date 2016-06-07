# NeuralTalk

- Forked from [NeuralTalk](https://github.com/karpathy/neuraltalk)
- Add a single python function to generate sentence from image.
- An original [Readme.md](neuraltalk/Readme.md) is placed at neuraltalk/Readme.md

## Prerequisites
- [Caffe](http://caffe.berkeleyvision.org/) and [Caffe's python interface](http://caffe.berkeleyvision.org/installation.html#python) installed on your environment

## Setup
1. Install NeuralTalk using pip `sudo pip install git+https://github.com/Thanabhat/neuraltalk.git`
2. Download `VGG_ILSVRC_16_layers.caffemodel` from http://www.robots.ox.ac.uk/~vgg/research/very_deep/ and place at `python_features/VGG_ILSVRC_16_layers.caffemodel`
3. Download `coco_cnn_lstm_v2.zip` from http://cs.stanford.edu/people/karpathy/neuraltalk/ , extract and place at `model/model_checkpoint_coco_visionlab43.stanford.edu_lstm_11.14.p`

#### Setup option (script)
You may need to change the path '/usr/local/lib/python2.7/dist-packages/' to match your environment.
```
# install
sudo pip install git+https://github.com/Thanabhat/neuraltalk.git
sudo wget -O /usr/local/lib/python2.7/dist-packages/neuraltalk/python_features/VGG_ILSVRC_16_layers.caffemodel "http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_16_layers.caffemodel"
sudo wget -O /home/coco_cnn_lstm_v2.zip "http://cs.stanford.edu/people/karpathy/neuraltalk/coco_cnn_lstm_v2.zip" && sudo unzip /home/coco_cnn_lstm_v2.zip -d /usr/local/lib/python2.7/dist-packages/neuraltalk/model && sudo rm /home/coco_cnn_lstm_v2.zip
# test
sudo python -m neuraltalk.caption_generator
```

#### Setup option (docker)
https://hub.docker.com/r/thanabhat/docker-neuraltalk/

## Example
Write this python code, place some `img.jpg`, run and get the sentence!
```python
from neuraltalk.caption_generator import CaptionGenerator

caption_generator = CaptionGenerator()
caption = caption_generator.get_caption('img.jpg')
print(caption)
```
