# Re-Co-RDS-REcogniscion-though-COlours-of-woRDS
## Authors: Bracco Filppo, Di Vece Chiara, Gnocco Marina, Loizzo Federica Gabriella
Project started at Xilinx Pynq Hackathon
The source code *code.py* is can be played with Python 3, and *code_as_notbook_jupiter.ipynb* is a notebook Jupiter. Files in folder *Alfabeto* are essential for execution.

###Project Purpose
The purpose is to allow blind people to read through a color coding system. A photodiode is moved through a series of 'color bits' so it can be possible estract the information encodin. Green represents the value '1', Blu the value '0' and Red is put among each other Blu or red 'color bit', to allow to recognise the changing of color.
After recognition the letter is, in real time, shown on display and also played through a audio output. In case of invalid inseriment there will be an warning error.

###Necessary Libreries
To play the code the necessary libraries are:
* **display** from **IPython**
* **widgets** from **ipywidgets**
* **Grove_Color** from **pynq.pmods**
* **Overlay** from **pynq.pl**
* **time**
* **threading**


