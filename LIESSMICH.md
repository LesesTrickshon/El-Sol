<div align="center">
  <h1>El Sol</h1>
  <h3>KI-basierender Solarpannle Schadendetector</h3>
</div>

- [Version in English 🇮🇳 🇳🇿](README.md)
- Version op de goede oude leuke Nederlandse taal (Heb ik nog niet geschrijft)
<div align="center">
  <img src="https://github.com/LesesTrickshon/El-Sol/blob/main/Logos/logo-nobg.png?raw=true" width="40%" alt="El Sol logo" />
</div>

---
## Inhaltsverzeichnis
- [Information](#Informationen)
- [Installation](#Installation)
- [Nutzung](#Nutzung)
- [Beitragen](#Beitragen)
- [Lizenz](#Lizenz)
---
## Information
El Sol ist ein Python 3.10 script der durch ein Wärmebild herausinden kann, ob bestimmte Sonnenkollektoren richtig funktionieren. Das Projekt wird von [Leaf Tide🍃](https://github.com/LesesTrickshon) und [Lennard6](https://github.com/lennard6) gebaut.
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
