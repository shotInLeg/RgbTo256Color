# RgbTo256Color
[Python] CLI tool to get closest to select color

## Help

```
usage: rgb_to_256_color.py [-h] 
                           -a {closest_rgb_color,closest_256_color,term256_to_rgb,rgb_to_term256}
                           -c COLOR

Script to get closest color from the palette.

optional arguments:
  -h, --help            show this help message and exit
  -a {closest_rgb_color,closest_256_color,term256_to_rgb,rgb_to_term256}, --action {closest_rgb_color,closest_256_color,term256_to_rgb,rgb_to_term256}
                        Mode to get color.
  -c COLOR, --color COLOR
                        Color RGB or 256term ("256,76,98" or "#ff54e1" or "13")
```

## Examples

### Term256 color to RGB

```bash
$ ./rgb_to_256_color.py -a term256_to_rgb -c 13
((255, 0, 255), '#ff00ff')
```

### RGB to Term256

```bash
$ ./rgb_to_256_color.py -a rgb_to_term256 -c "255,0,255"
13

$ ./rgb_to_256_color.py -a rgb_to_term256 -c "#ff00ff"
13
```

### Closest RGB color

```bash
$ ./rgb_to_256_color.py -a closest_rgb_color -c "#ff22ff"
((255, 0, 255), '#ff00ff')
```

### Closest Term256 color

```bash
$ ./rgb_to_256_color.py -a closest_256_color -c "#ff22ff"
13
```
