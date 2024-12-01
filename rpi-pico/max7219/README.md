# Website

https://www.instructables.com/Raspberry-Pi-Pico-MAX7219-8x8-Dot-Matrix-Scrolling/

# Functions

## hline

display.hline(17, 1, 6, value)  # x, y, w, on/off

## vline

display.vline(17, 3, 4, value)  # x, y, w, on/off

## line

display.line(25, 1, 30, 6, value)  # x1, y1, x2, y2, on/off

## rect

display.rect(1, 1, 6, 6, 1)  # x, y, w, h, on/off

## fill_rect

display.fill_rect(9, 1, 6, 6, value)  # x, y, w, h, on/off

## pixel

display.pixel(25, 6, value)  # x, y, on/off

## fill

display.fill(0)  # on/off
