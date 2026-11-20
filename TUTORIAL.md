# Highlight selected words in an Excalidraw paragraph

You will build a two-line annotation, highlight the second “Read” in blue, then move the annotation into a drawing as one group.

## Make the example

Download the named ZIP under **Assets** on the [release page](https://github.com/Uone100/excalidraw-inline-colors/releases/latest), extract it and open a terminal beside `SKILL.md`. Use Python 3.9 or newer.

```sh
python -m pip install Pillow
python scripts/annotation.py examples/annotation.json annotation.excalidraw --font "C:/Windows/Fonts/arial.ttf"
```

On macOS or Linux, replace the font argument with the path to a local Arial or metrically compatible TrueType font. The font controls how the helper measures text, so use one that matches the destination drawing.

1. Open `annotation.excalidraw` in Excalidraw. The two lines contain **seven editable text elements** in one group.
2. Check the first “Read” is the default color, the second is blue, “draft” is brown and “final copy” is green.
3. Select the group, copy it and paste it into your own scene. Zoom in to check spacing with your browser's fonts.

## Customize it

Copy `examples/annotation.json`, change `text`, and edit the entries in `highlights`. The example uses `"occurrence": 2` to select a repeated word. Use an explicit newline in the JSON string to move text onto the next line. Run the same command with the new input and a fresh output filename. If alignment changes after editing words in Excalidraw, regenerate from the updated JSON.

## Ask an agent

Install the folder as described in the [README](README.md), then try “Create an editable Excalidraw annotation from this paragraph. Highlight the second occurrence of Read in blue and give me the scene file.”
