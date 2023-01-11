from PIL import ImageGrab
import numpy as nm
import pytesseract
import pyautogui
import cv2
from pynput.keyboard import Key, Listener
dict = {
    'la mer du Nord': [305, 535],
    'Marseille': [456, 960],
    'Nantes': [218, 737],
    'le Massif central': [375, 865],
    'la Garonne': [265, 900],
    'locéan Atlantique': [115, 828],
    'océan Atlantique': [115, 828],
    'les Vosges': [515, 700],
    'Lyon': [439, 824],
    'la Loire': [288, 745],
    'Paris': [325, 648],
    'Strasbourg': [544, 664],
    'Montpellier': [399, 947],
    'le Rhin': [542, 683],
    'Nice': [530, 936],
    'la Corse': [590, 1028],
    'Bordeaux': [230, 871],
    'la mer Méditerranée': [465, 1010],
    'le Jura': [475, 790],
    'les Alpes': [487, 870],
    'la Seine': [395, 684],
    'Toulouse': [286, 927],
    'la Saéne': [445, 797],
    'la Manche': [159, 573],
    'le Rhéne': [433, 918],
    'les Pyrénées': [320, 985],
}
pyautogui.doubleClick(420, 800)


def imToString():
    pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
    while (True):
        cap = ImageGrab.grab(bbox=(200, 457, 566, 504))
        captureString = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')
        print(f'Detected: {captureString}', end="")
        if any(ext in captureString for ext in dict.keys()):
            print("Match Found, Clicking Option")
            index = dict.get(captureString.strip())
            print(index)
            pyautogui.click(index[0], index[1])
            # imToString() # Uncomment to make recursive
            break
        else:
            print("No Match")
            break


def on_press(key):
    print()
    if (key.char == 'e'):
        imToString()
    else:
        quit()

def on_release(key):
    if key == Key.esc:
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
