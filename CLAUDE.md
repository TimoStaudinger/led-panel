# LED Panel

## Hardware

- **Board:** Raspberry Pi Zero W Rev 1.1 (armv6l, single-core, 427 MB RAM)
- **HAT:** Adafruit RGB Matrix + RTC HAT (HUB75 / DS1307)
- **Panel:** 64x32 RGB LED matrix, 1 panel chained

## Software (on the Pi)

- **OS:** Raspbian 12 (Bookworm), kernel 6.12
- **Python:** 3.11.2
- **LED driver:** hzeller/rpi-rgb-led-matrix with Python bindings (`rgbmatrix`)
- **Libraries:** Pillow 9.4, Flask 2.2

## Panel Configuration

```python
options.rows = 32
options.cols = 64
options.chain_length = 1
options.hardware_mapping = "adafruit-hat"
options.gpio_slowdown = 2
```

## RPi File Structure

- Repo: `~/rpi-rgb-led-matrix/`
- App code: `~/rpi-rgb-led-matrix/dist/`
- BDF fonts: `~/rpi-rgb-led-matrix/fonts/` (4x6, 5x7, 5x8, 6x10, 7x13, etc.)

## Key APIs

- `RGBMatrix(options)` -- create matrix controller
- `matrix.CreateFrameCanvas()` -- double-buffered off-screen canvas
- `matrix.SwapOnVSync(canvas)` -- atomic display update synced to refresh
- `canvas.SetPixel(x, y, r, g, b)` -- set individual pixel
- `graphics.Font()` / `font.LoadFont(path)` -- load BDF font
- `graphics.DrawText(canvas, font, x, y, color, text)` -- render text (y = baseline)
- `graphics.Color(r, g, b)` -- color for text rendering

## Deployment

- `deploy.sh` -- copies `dist/` to the Pi via scp, runs with `sudo python3`
- `snapshot.sh` -- captures a camera frame via ffmpeg/RTSP (needs `.env` with Tapo credentials)

## Network

- **Hostname:** `ledmatrix.local` (mDNS)
- **SSH:** key auth via 1Password SSH agent
