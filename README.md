# Excalidraw Inline Colors

Generate grouped, individually editable Excalidraw text runs for a paragraph with selected words in different colors. Measure each position against the chosen font so authors can skip aligning the pieces by hand.

## Install as an Agent Skill

Download the **versioned ZIP** from [Releases](https://github.com/Uone100/excalidraw-inline-colors/releases/latest). Extract its contents into `.agents/skills/excalidraw-inline-colors/` in a Codex project or `.claude/skills/excalidraw-inline-colors/` in a Claude Code project. The installed folder should contain SKILL.md directly. Start a new session and ask for the task described above. You can also run the helper directly.

## Worked example

Python 3.9+, Pillow (python -m pip install Pillow), and a local Arial or compatible TrueType font matching the destination.

```sh
python scripts/annotation.py examples/annotation.json annotation.excalidraw --font C:/Windows/Fonts/arial.ttf
```

Expected: seven text elements in one group. Only the second “Read” is blue. Open the scene and copy its group into your drawing. Newlines are explicit; after a text edit use the JSON to recalculate spacing. Browser font substitution can change alignment. Complex bidirectional or mixed-fallback-font layouts require visual review.

## Why it exists

[185 👍 on the paragraph highlight request](https://github.com/excalidraw/excalidraw/issues/5138). A separate [word-color request](https://github.com/excalidraw/excalidraw/issues/12090) describes the manual alignment problem. This is an importable workaround, not a native rich-text editor. Reaction counts were observed on 2026-11-20. They measure interest in the upstream request. This specific Skill's adoption is measured separately through its Release attachment.
