# EL SOL
### AI-driven Solar-Pannle health detector
[Version auf Deustch 🇩🇪 🇦🇹](LIESSMICH.md)

---
## Table of Contents
- [Information](#Information)
- [Installation](#Installation)
- [Usage](#Usage)
- [Contributing](#Contributing)
- [License](#License)
---
## Information
El Sol is a Python 3.10 script made to detect if a Solar Pannle is broken just by using thermal image data. The Project is by [Leaf Tide🍃](https://github.com/LesesTrickshon) and [Lennard6](https://github.com/lennard6).
### How it works
El Sol uses the these Liberarys:
- Tensorflow
- Keras from Tensorflow
- Numpy
- cv2
- os
- Matplot
- PyGame (I will have to see later.)

#### *How does it find out which pannle is broken which one isn't?*
The AI is a forked version of an MNIST-AI which is a AI that can determine which number the user drew. This AI is using a way **higher** resolution for the images and 3 color channles instead of the 28x28 and the singular black and white channle used by MNIST.
