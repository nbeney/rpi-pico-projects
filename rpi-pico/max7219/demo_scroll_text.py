"""
Scroll text with four MAX7219 8x8 LED matrices daisy-chained together.

Wiring:
* MAX7219 VCC pin to VBUS (5V)
* MAX7219 GND pin to GND
* MAX7219 DIN pin to digital GPIO3
* MAX7219 CS  pin to digital GPIO5
* MAX7219 CLK pin to digital GPIO2
"""

from machine import Pin, SPI
import max7219
import time

MATRIX_WIDTH = 8  # in pixels
MATRIX_HEIGHT = 8  # in pixels
NUM_MATRICES = 4
DISPLAY_WIDTH = MATRIX_WIDTH * NUM_MATRICES  # in pixels
DISPLAY_HEIGHT = MATRIX_HEIGHT  # in pixels
CHAR_WIDTH = 8  # in pixels

GPIO_DIN = 3
GPIO_CS = 5
GPIO_CLK = 2

def create_display(gpio_din, gpio_cs, gpio_clk):
    pin_DIN = Pin(gpio_din)
    pin_CS = Pin(gpio_cs, Pin.OUT)
    pin_CLK = Pin(gpio_clk)
    spi = SPI(0, baudrate=10_000_000, polarity=1, phase=0, sck=pin_CLK, mosi=pin_DIN)
    return max7219.Matrix8x8(spi, pin_CS, NUM_MATRICES)
    
def scroll_text(text, delay_secs=0.05):
    total_width = len(text) * CHAR_WIDTH
    for x in range(DISPLAY_WIDTH, -total_width, -1):
        display.fill(0)
        display.text(text, x, 0, 1)
        display.show()
        time.sleep(delay_secs)

if __name__ == "__main__":
    display = create_display(GPIO_DIN, GPIO_CS, GPIO_CLK)
    display.brightness(3)  # 1=dim to 15=bright

    while True:
        scroll_text("RASPBERRY PI PICO AND MAX7219")
