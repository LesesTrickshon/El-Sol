# EL SOL
## KI-basierender Solarpannle Schadendetector
[Version in English 🇮🇳 🇳🇿](README.md)

---
## Inhaltsverzeichnis
- [Information](#Informationen)
- [Installation](#Installation)
- [Nutzung](#Nutzung)
- [Beitragen](#Beitragen)
- [Lizenz](#Lizenz)
---
## Information
El Sol ist ein Python 3.10 script der durch ein Wärmebild herausinden kann, ob bestimmte Sonnenkollektoren richtig funktionieren. Das Projekt wird von [@LT (MainDev)](https://github.com/LesesTrickshon) und [NOT ON GITHUB YET (SideDev)](https://github.com/LesesTrickshon/el-sol) gebaut.
### Funktionalität
El Sol nutz diese Bibilotheken:
- Tensorflow
- Keras from Tensorflow
- Numpy
- cv2
- os
- Matplot
- PyGame (I will have to see later.)

#### *Wie findet das Programm heraus, welche Pannles kaputt sind?*
Die KI ist eine abgeänderte Version einer MNIST-KI, welche herausfinden kann welche Zahl der User gezeichnet hat. Diese KI arbeitet mit einer viel **höheren** Bilderqualität und drei Color-Channels als die MNIST-KI welche 28x28 Schwarz-Weiß-Bilder nutzt.
