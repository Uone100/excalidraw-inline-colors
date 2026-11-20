"""Create a fresh Excalidraw scene of font-measured, grouped colored text fragments."""
import argparse
import json
import re
import secrets
import uuid
from pathlib import Path
from PIL import ImageFont


def color(value):
    if not isinstance(value,str) or not re.fullmatch(r"#[a-fA-F0-9]{6}",value):
        raise ValueError("Use six-digit hex colors")
    return value


def intervals(text, highlights):
    result=[]
    for item in highlights:
        needle=item["text"]
        if not isinstance(needle,str) or not needle or "\n" in needle:
            raise ValueError("Select a nonempty single-line literal")
        hits=list(re.finditer(re.escape(needle),text))
        number=item.get("occurrence",1 if len(hits)==1 else None)
        if type(number) is not int or not 1<=number<=len(hits):
            raise ValueError(f"Selection missing or ambiguous: {needle}")
        start,end=hits[number-1].span()
        result.append((start,end,color(item["color"])))
    result.sort()
    if any(a[1]>b[0] for a,b in zip(result,result[1:])):
        raise ValueError("Color selections overlap")
    return result


def scene(data,font_file):
    text=data["text"]
    if not isinstance(text,str) or not text.strip() or "\r" in text or "\t" in text:
        raise ValueError("Supply nonempty text with LF line breaks and spaces")
    size=data.get("fontSize",24)
    if type(size) is not int or not 6<=size<=256:
        raise ValueError("fontSize must be an integer from 6 to 256")
    default=color(data.get("defaultColor","#202124"))
    selections=intervals(text,data["highlights"])
    if not selections:
        raise ValueError("Supply at least one highlight")
    font=ImageFont.truetype(str(font_file),size)
    gid=uuid.uuid4().hex
    elements=[]
    offset=0
    for row,line in enumerate(text.split("\n")):
        bounds={0,len(line)}
        chosen={}
        for start,end,tint in selections:
            if offset<=start<offset+len(line):
                bounds.update((start-offset,end-offset))
                chosen[start-offset]=tint
        ordered=sorted(bounds)
        for left,right in zip(ordered,ordered[1:]):
            run=line[left:right]
            if not run.strip():
                continue
            # Start each visible run at the advance of the preceding full prefix.
            # Ignore outer spaces inside the element itself; their advance is in the next position.
            start=left+len(run)-len(run.lstrip(" "))
            visible=run.strip(" ")
            elements.append(dict(id=uuid.uuid4().hex,type="text",x=32+font.getlength(line[:start]),
                y=32+row*size*1.15,width=max(1,font.getlength(visible)),height=size*1.15,
                angle=0,strokeColor=chosen.get(left,default),backgroundColor="transparent",fillStyle="solid",
                strokeWidth=1,strokeStyle="solid",roughness=0,opacity=100,groupIds=[gid],frameId=None,
                roundness=None,seed=secrets.randbelow(2**30),version=1,versionNonce=secrets.randbelow(2**30),
                isDeleted=False,boundElements=None,updated=1,link=None,locked=False,text=visible,
                originalText=visible,fontSize=size,fontFamily=2,textAlign="left",verticalAlign="top",
                containerId=None,autoResize=True,lineHeight=1.15))
        offset += len(line)+1
    return {"type":"excalidraw","version":2,"source":"https://github.com/Uone100/excalidraw-inline-colors",
            "elements":elements,"appState":{"viewBackgroundColor":"#ffffff"},"files":{}}


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input",type=Path)
    ap.add_argument("output",type=Path)
    ap.add_argument("--font",required=True,type=Path)
    args=ap.parse_args()
    try:
        result=scene(json.loads(args.input.read_text(encoding="utf-8-sig")),args.font)
        with args.output.open("x",encoding="utf-8") as out:
            json.dump(result,out,ensure_ascii=False,indent=2)
        print(f"{len(result['elements'])} editable runs")
    except (ValueError,OSError,KeyError,TypeError) as exc:
        ap.exit(2,f"{exc}\n")
