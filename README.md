# led-matrix

## Hardware

- **Board:** Raspberry Pi Zero W Rev 1.1 (armv6l)
- **HAT:** Adafruit RGB Matrix + RTC HAT (HUB75 / DS1307)
- **Panel:** 64x32 RGB LED matrix, 1 panel chained
- **Memory:** 427 MB RAM
- **Storage:** 6.8 GB SD card (1.6 GB free)

## Network

- **Hostname:** `ledmatrix.local` (mDNS via avahi-daemon)
- **IP:** `192.168.68.67` (DHCP)
- **SSH:** `ssh ledmatrix.local` (key auth via 1Password SSH agent)

## Software

- **OS:** Raspbian 12 (Bookworm), kernel 6.12
- **Python:** 3.11.2
- **LED driver:** [hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) with Python bindings (`rgbmatrix`)
- **Libraries:** Pillow 9.4, Flask 2.2

## Panel Configuration

```python
options.rows = 32
options.cols = 64
options.chain_length = 1
options.gpio_slowdown = 2
```
