print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.keys import KC, make_key
envkb = KMKKeyboard()
envkb.col_pins = (board.GP10, board.GP9, board.GP8, board.GP7, board.GP6, board.GP5, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27)
envkb.row_pins = (board.GP11, board.GP12, board.GP13, board.GP14, board.GP15)
rollover_cols_every_rows = 4
envkb.diode_orientation = DiodeOrientation.COLUMNS
envkb.debug_enabled = False

layers = Layers()
envkb.modules = [layers]

#Simple thing to enable LED on pi once this script is executed
import digitalio
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False #make sure this is false by default

def capslockled(*args, **kwargs):
    led.value = not led.value #not current value so it acts like a toggle

KC.CAPS.before_press_handler(capslockled) 
#when capslock is pressed run caspslockled function

nokey = KC.NO
envkb.keymap = [
    [
    #Layer 0
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, nokey, KC.BSPC,
        KC.TAB, nokey, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLASH,
        KC.CAPS, nokey, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.NUHS, KC.ENT, 
        KC.LSFT, KC.NONUS_BSLASH, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, nokey, KC.RSHIFT, nokey,
        KC.LCTL, KC.LGUI, nokey, KC.LALT, nokey, nokey, KC.SPC, nokey, nokey, nokey, KC.RALT, KC.RGUI, nokey, KC.MO(1), KC.RCTL, nokey, nokey,
    ],
    [
    #Layer 1
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, nokey, KC.DEL,
        KC.TAB, nokey, KC.Q, KC.UP, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.PSCR, KC.BSLASH,
        KC.CAPS, nokey, KC.LEFT, KC.DOWN, KC.RIGHT, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.HOME, KC.END, KC.ENT, 
        KC.LSFT, KC.NONUS_BSLASH, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, nokey, KC.RSHIFT, nokey,
        KC.LCTL, KC.LGUI, nokey, KC.LALT, nokey, nokey, KC.SPC, nokey, nokey, nokey, KC.RALT, KC.RGUI, nokey, KC.TRNS, KC.RCTL, nokey, nokey,
    ],
]

def usbfunc():
    
    if __name__ == '__main__':
        envkb.go()
        raise Exception('Something has caused an error.')
        
try:
    usbfunc()
except Exception as e:
    import microcontroller
    print(e)
    led.value = False
    microcontroller.reset()

import microcontroller
microcontroller.reset()
#last ditch effor to reset the MCU, if this is being ran then something really is wrong lol
