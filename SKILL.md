---
name: excalidraw-inline-colors
description: Produce a native editable Excalidraw annotation in which selected words have different colors. Use for teaching notes, formulas described in plain text, and flowchart annotations where the user wants to keep editing the words.
---
Capture the exact text and the requested word colors. For an existing canvas, work from a copy of the text and deliver an importable annotation. The output consists of grouped, individually editable text runs. For a user who requires one rich-text object with automatic reflow, explain this limitation before using the workaround.

1. Put the full text and literal selections in a UTF-8 JSON file like examples/annotation.json. Duplicate matches require a 1-based occurrence. Preserve explicit newlines. Do not split grapheme clusters or bidirectional text into runs; those need visual/typesetting review.
2. Run `python scripts/annotation.py input.json output.excalidraw --font PATH_TO_ARIAL_TTF` with Pillow installed. Choose the actual local Arial/Helvetica-compatible font that the destination will use. Its glyph advances position each run; differences in the destination font can change spacing.
3. Open the new scene in Excalidraw. Copy the group to the target board. Confirm the full text, word colors and alignment. Keep the source JSON to regenerate after text or wrap changes. Report whether a scene readback or an interactive import was verified.
