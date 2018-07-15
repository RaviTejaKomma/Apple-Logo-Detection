# Logo-Classification
- Convolutional Neural Network to tell whether an image contains Apple logo or not.
- Click here for [demo](https://logo-classification-ravi.herokuapp.com/classify_logos/upload)

### Convolutional Neural Network
- Convolutional neural networks consist of several layers of small neuron collections that each look at small portions of an image.
- The results from all the collections in a layer are made to overlap to create a representation of the entire image.
- The layer below then repeats this process on the new image representation, allowing the system to learn about the makeup of the image.
- Deep convolutional neural networks were invented in the early 1980s. But it is only in the last couple of years that computers have begun to have the horsepower necessary for high-quality image recognition.

### Building CNN

#### Step 1: Importing the packages

We need five packages for building of convolution neural networks:
- Sequential
- Convolution2D
- MaxPooling2D
- Flatten
- Dense

Sequential:
  - This package is used to initialize the neural network. There are two ways of initializing a neural network:
	- Sequence of layers
	- Graph
  - Since convolution neural network is a sequence of layers, we initialize it using this package.

Convolution2D:
  - This is used to build the convolution layers. Images are generally represented in the 2D form and hence convolution 2D is used to build convolution layers.

MaxPooling2D:
  - This is used to add pooling layers.

Flatten:
  - It is used to convert all pooled feature maps created using convolution and max pooling into large feature vector which is the given as input to connected networks.

Dense:
  - This is used to add fully connected layers and artificial neural networks.

#### Step 2: Initializing Convolution Neural Network

To initialize CNN we have to create an object of the Sequential class:

![Image](images/1.jpg?raw=true "Title")
