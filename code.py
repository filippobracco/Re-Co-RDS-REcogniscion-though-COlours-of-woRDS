
# coding: utf-8

# In[ ]:

from IPython import display
from ipywidgets import widgets
from pynq.pmods import Grove_Color
from pynq.pl import Overlay
import time
import threading

Overlay("pmod.bit").download()

def valore_letto(R, G, B):
    if (R>G)and(R>B):
        return 'R'
    elif (B>G)and(B>R):
        return 'B'
    elif(G>R)and(G>B):
        return 'G'

def colorsToHex(red, green, blue):
    color = (int(red) << 16) | (int(green) << 8) | int(blue)
    return "#%0.6X"%color


def rescaleColor(colors, saturations):

    for i in range(len(colors)):
        minVal = saturations[i][0]
        maxVal = saturations[i][1]
        color = colors[i]
        
        delta = maxVal - minVal
        color = max(color, minVal)
        color = min(color, maxVal)
        colors[i] = int((color - minVal)*(255 / delta))
    return colors

ok = False
execution = True 
valore = 'N'
lista = ['I']
risultato = []
word = []

def start(button):
    global ok
    ok = True

def stop(button):
    global execution
    execution = False 
    print('The word is: '+ ''.join(word), flush=True)

def program():

    square = widgets.Button(disabled = True)
    square.width = "300px"
    square.height = "300px"
    square.text_size = "200px"
    square.margin = "5px 0px 0px 110px"
    display.display(square)

    
    startButton = widgets.Button(description = "START", width="300px")
    startButton.margin = "5px 0px 0px 110px"
    startButton.on_click(start)
    display.display(startButton)
    
    stopButton = widgets.Button(description = "STOP", width="300px")
    stopButton.margin = "5px 0px 0px 110px"
    stopButton.on_click(stop)
    display.display(stopButton)
    
    grove_color = Grove_Color(1, 1)
    
    inizio = False

    while execution:
        red, green, blue, clear = grove_color.read()
        redN = int((red / clear)*255)
        greenN = int((green / clear)*255)
        blueN = int((blue / clear)*255)
        
        
        colors = [redN, greenN, blueN]
        saturations = [(34, 155), (71,147), (29, 117)]
        redN, greenN, blueN = rescaleColor(colors, saturations)
        
        
        square.background_color = colorsToHex(redN, greenN, blueN)
        time.sleep(0.1)
        
        if ok:
            valore = valore_letto(redN, greenN, blueN)
            if valore != lista[-1] and valore != None:
                lista.append(valore)
                
            if len(lista) == 12:
                if inizio:
                    lista.pop(1)
                else:
                    inizio = True
                
                for i in range(11):
                    if lista[i] == 'G':
                        risultato.append(int(1))
                    elif lista[i] == 'B':
                        risultato.append(int(0))
                lista.clear()
                lista.append('I')
                cod = int(0)
                for i in range(5):
                    cod = cod + int(risultato[i]*(2**(4-i)))
                if cod < 26:
                    word.append(lettera)
                    print(chr(cod + 65), flush=True)
                    square.description = lettera
                    audio_source = display.Audio(filename="./Alfabeto/" + lettera +".m4a", autoplay = True)
                    display.display(audio_source)
                else:
                    print('Invalid letter!', flush=True)
                    square.description = lettera
                    audio_source = display.Audio(filename="./Alfabeto/ERROR.m4a", autoplay = True)
                    display.display(audio_source)
     

                risultato.clear()
                
thread = threading.Thread(target = program)
thread.start()


# In[ ]:



