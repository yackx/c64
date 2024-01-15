# Record from VICE

To record a video sequence from VICE and turn it into an animated GIF:

1. Go to Snapshots > Save/Record media > Video recording.
2. Choose a suitable export format. I have encountered issues with `mp4`. Try another format if the first one fails to work.
3. Click Save.
4. Let the emulator run for the desired duration.
5. Go to Snapshots > Stop media recording.
6. Convert to an animated GIF using `ffmpeg`.

```bash
ffmpeg -i input.ogg -t 3 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
```

- `-i input.ogg`: This is the input file.
- `-vf`: This stands for video filter. This is where most of the magic happens.
- `fps=10`: This sets the frames per second.
- `scale=320:-1`: This scales the width of the output to 320 pixels. The height is automatically determined to maintain the aspect ratio.
- `flags=lanczos`: This is a high-quality downsampling filter.
- `split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse`: This complex filterchain is used to generate and apply a palette. It's necessary because GIFs use a global palette and ffmpeg needs to generate this palette before creating the GIF.
- `-loop 0`: This makes the GIF loop indefinitely.
- `output.gif`: This is the output file.
- `-t 3` option tells ffmpeg to only process the first 3 seconds of the input.
