import os
import unittest
from pathlib import Path
from scripts.annotation import intervals,scene

class AnnotationTest(unittest.TestCase):
    def test_missing_duplicate_and_overlap(self):
        for rules in ([{"text":"absent","color":"#111111"}],
                      [{"text":"ab","color":"#111111"}],
                      [{"text":"ab","occurrence":1,"color":"#111111"},{"text":"abc","color":"#222222"}]):
            with self.assertRaises(ValueError):
                intervals("abc ab",rules)

    def test_editable_runs_and_measured_offset(self):
        from PIL import ImageFont
        path=os.environ.get("ANNOTATION_FONT","C:/Windows/Fonts/arial.ttf")
        if not Path(path).is_file():
            self.skipTest("Set ANNOTATION_FONT to a local Arial-compatible .ttf")
        data={"text":"wide word\nwide","highlights":[{"text":"wide","occurrence":2,"color":"#102030"},{"text":"word","color":"#102030"}]}
        a,b,c=scene(data,path)["elements"]
        self.assertEqual([a["text"],b["text"],c["text"]],["wide","word","wide"])
        self.assertNotEqual(a["strokeColor"],c["strokeColor"])
        self.assertEqual(a["groupIds"],b["groupIds"])
        self.assertAlmostEqual(b["x"]-a["x"],ImageFont.truetype(path,24).getlength("wide "))
        self.assertEqual(a["x"],c["x"])
        self.assertGreater(c["y"],a["y"])
