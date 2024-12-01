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
import random

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
        
def demo_brightness():
    scroll_text("brightness(1-15)")
    display.fill(0)
    display.fill_rect(12, 2, 8, 4, 1)
    display.show()
    for b in range(1, 16):
        display.brightness(b)    
        time.sleep(0.1)
    for b in range(15, 2, -1):
        display.brightness(b)    
        time.sleep(0.1)
    time.sleep(1)
        
def demo_fill():
    for v in (0, 1):
        scroll_text(f"fill({v})")
        display.fill(v)
        display.show()
        time.sleep(1)
        
def demo_pixel():
    scroll_text("pixel(x,y,0/1)")
    display.fill(0)
    for x in range(250):
        x = random.randint(0, DISPLAY_WIDTH)
        y = random.randint(0, DISPLAY_HEIGHT)
        v = random.randint(0, 1)
        display.pixel(x, y, v)
        display.show()
        time.sleep(0.01)
        
def demo_line():
    scroll_text("line(x1,y1,x2,y2,0/1)")
    for x in range(DISPLAY_WIDTH):
        display.fill(0)
        display.line(x, 0, DISPLAY_WIDTH-1, DISPLAY_HEIGHT-1, 1)
        display.show()
        time.sleep(0.1)
    for x in range(DISPLAY_WIDTH-1, -1, -1):
        display.fill(0)
        display.line(DISPLAY_WIDTH-1, 0, x, DISPLAY_HEIGHT-1, 1)
        display.show()
        time.sleep(0.1)
    time.sleep(0.5)
        
def demo_hline():
    scroll_text("hline(x,y,w,0/1)")
    for i in range(5):
        x = random.randint(0, DISPLAY_WIDTH)
        y = random.randint(0, DISPLAY_HEIGHT)
        w = random.randint(5, DISPLAY_WIDTH)
        display.fill(0)
        display.hline(x, y, w, 1)
        display.show()
        time.sleep(0.5)
        
def demo_vline():
    scroll_text("vline(x,y,h,0/1)")
    display.fill(0)
    for x in range(0, DISPLAY_WIDTH, 2):
        y = random.randint(0, DISPLAY_HEIGHT)
        h = random.randint(1, DISPLAY_HEIGHT-2)
        display.vline(x, y, h, 1)
        display.show()
        time.sleep(0.2)
                
def demo_rect():
    scroll_text("rect(x,y,w,h,0/1)")
    display.fill(0)
    display.rect(8, 2, 16, 4, 1)
    display.show()
    time.sleep(1)
                
def demo_fill_rect():
    scroll_text("fill_rect(x,y,w,h,0/1)")
    display.fill(0)
    display.fill_rect(8, 2, 16, 4, 1)
    display.show()
    time.sleep(1)

def demo_text():
    scroll_text("text(str,x,y,0/1)")
    for y in range(-8, 1):
        display.fill(0)
        display.text("PICO", 0, y, 1)
        display.show()
        time.sleep(0.2)
    time.sleep(1)
        
def demo_scroll():
    scroll_text("scroll(dx,dy)")
    display.fill(0)
    display.rect(8, 2, 16, 4, 1)
    display.show()
    time.sleep(1)
    for i in range(16):
        display.scroll(1, 0)
        display.show()
        time.sleep(0.1)
    time.sleep(0.5)
    for i in range(16):
        display.scroll(-1, 0)
        display.show()
        time.sleep(0.1)
    time.sleep(2)

if __name__ == "__main__":
    display = create_display(GPIO_DIN, GPIO_CS, GPIO_CLK)
    display.brightness(3)  # 1=dimmed to 15=bright
    
    while True:
        demo_brightness()
        demo_fill()
        demo_pixel()
        demo_line()
        demo_hline()
        demo_vline()
        demo_rect()
        demo_fill_rect()
        demo_text()
        demo_scroll()

