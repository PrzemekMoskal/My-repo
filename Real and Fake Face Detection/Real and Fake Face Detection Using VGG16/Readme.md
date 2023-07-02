<h1>VGG16</h1>
<br>
A convolutional neural network is also known as a ConvNet, which is a kind of artificial neural network. A convolutional neural network has an input layer, an output layer, and various hidden layers. VGG16 is a type of CNN (Convolutional Neural Network) that is considered to be one of the best computer vision models to date. The creators of this model evaluated the networks and increased the depth using an architecture with very small (3 × 3) convolution filters, which showed a significant improvement on the prior-art configurations. They pushed the depth to 16–19 weight layers making it approx — 138 trainable parameters.

<h1>USAGE</h1>

VGG16 is object detection and classification algorithm which is able to classify 1000 images of 1000 different categories with 92.7% accuracy. It is one of the popular algorithms for image classification and is easy to use with transfer learning.

<h1>ARCHITECTURE</h1>
<ol>
<li>The 16 in VGG16 refers to 16 layers that have weights. In VGG16 there are thirteen convolutional layers, five Max Pooling layers, and three Dense layers which sum up to 21 layers but it has only sixteen weight layers i.e., learnable parameters layer.
</li>
<li>VGG16 takes input tensor size as 224, 244 with 3 RGB channel</li>
<li>Most unique thing about VGG16 is that instead of having a large number of hyper-parameters they focused on having convolution layers of 3x3 filter with stride 1 and always used the same padding and maxpool layer of 2x2 filter of stride 2.</li>
<li>The convolution and max pool layers are consistently arranged throughout the whole architecture</li>
<li>Conv-1 Layer has 64 number of filters, Conv-2 has 128 filters, Conv-3 has 256 filters, Conv 4 and Conv 5 has 512 filters.
Three Fully-Connected (FC) layers follow a stack of convolutional layers: the first two have 4096 channels each, the third performs 1000-way ILSVRC classification and thus contains 1000 channels (one for each class). The final layer is the soft-max layer.</li>
</ol>
<br>

<h1>CONFUSION MATRIX</h1>
![](https://github.com/kanishkakataria/Face-X/blob/master/Real%20and%20Fake%20Face%20Detection/Real%20and%20Fake%20Face%20Detection%20Using%20VGG16/confusion%20matrix.png)
<h1>ACCURACY MATRIX</h1>
<h2>LOSS CURVE</h1>