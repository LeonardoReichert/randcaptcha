

"""

    Generate a random image for captcha and save the image on a file.
    return two strings (text random, path of image).


see help(module) for use

changes on versions:
- from 0.1 to 0.2
    Added kw args, rotate arg change the angle of rotates
    Added retro-compatibility with python 2.7 (compatibility with py3 and py2)

---------------------------------------------------------------------------------

MIT License

Copyright (c) 2023 LeonardoReichert

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from PIL import Image, ImageFont, ImageDraw; #modules
from tempfile import TemporaryFile;
from random import randint, choice;



version = 0.2;

_textRandom = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
_textRandom += "0123456789";


def _invertColor(rgb):
    return tuple([255-color for color in rgb]);

def _getTextLength(font_pillow, text):
    #calculate the width of char or text
    if hasattr(font_pillow, "getlength"):
        #python3x
        return int(font_pillow.getlength(text));
    else:
        #python2x (will be deprecated method on python3)
        return int(font_pillow.getsize(text)[0]);

def _getRandomContrastColor(background):
    #select a random color with a contrast:
    color = background;
    while abs(sum(background) - sum(color)) < 300:
        color = tuple([randint(0, 255) for i in range(3)]);
    return color;


_validOptions = ("rotate",);
def CreateImageCaptcha(fontnames, fontsize, filename_out=None,
                        length=5, valid=_textRandom, background=(200, 200, 200), addgarbage=True, **kw):

    """
    Generate a random image for captcha and save the image on a file.
    return two strings (text random, path of image).

    Example:
    ...
    >>> GenImageCapcha(["arial", "impact"], 25, background=(180, 180, 180));
    ("MA0P6", "C:/Users/../AppData/Local/Temp/captchaildzt585.jpg")
    >>>

    The function should throw an error if it can't open any font

    fontnames: the family string, or families in a list or tuple.
        The first source that is successful will be used.
        example 1: ["first", "arial", "impact"]
        example 2: "arial"
    
    fontsize: the size of the font

    filename_out: the file with a extension of image, needs to have an extension supported by PIL (Pillow).
        Can use a None value, a new name will be created in the temporary file directory,
        this default will be a .jpg, the file must be deleted by the caller of this function,
        the temporary file is not automatically deleted.
        default: None
    
    length: the size, length of random characters,
        default: 5

    valid: use a string, used for generate the random characters.
        default: "ABCD...XYZ01...89"

    background: color RGB background for captcha,
        default: (200, 200, 200)

    addgarbage: use a True or False boolean, this flag controls additional drawing of line shapes,
        default: True

    **kw extras:
        rotate: the range of random rotations of a char,
                can be a pair of angles from -360 to 360 each.
                Can set this param to None value (no rotations, simple)
        default: (-60, 60)

    """

    for opt in kw:
        if not opt in _validOptions:
            raise Exception("option %s not in (%s)" % (opt, str(_validOptions)));

    
    rotate = kw.get("rotate", (-60, 60));
    try:
        #need validate the rotate param
        if rotate != None:
            minAngle, maxAngle = rotate;
            assert minAngle >= -360 and minAngle <= 360;
            assert maxAngle >= -360 and maxAngle <= 360;
        
    except:
        raise Exception(
        """param -rotate can be a pair of angles from -360 to 360 each,
                  example: (-100, 100) or (10, 60) or None (do not rotate, no angle).""");

    assert length > 0;

    #creating text random:
    text = "".join([choice(valid) for i in range(length)]);

    #creating font:
    if not type(fontnames) in (tuple, list):
        fontnames = [fontnames];

    font = None;
    for family in fontnames:
        try:
            font = ImageFont.truetype(family, fontsize);
            break;
        except:
            pass;
    
    if not font:
        raise Exception("Can't open those fonts");  
    
    pad = 5;
    heightFont = sum(font.getmetrics());

    #drawing images of chars:

    if rotate != None:
        rotatedImagesChar = [];
        for char in text:
            #calculate the width of char:
            widthChar = _getTextLength(font, char);
            
            #select a random color with a contrast:
            color = _getRandomContrastColor(background);

            #new image char rotated:
            imgChar = Image.new("RGB", (widthChar, heightFont), background);
            ImageDraw.Draw(imgChar).text((0, 0), char, color, font=font);
            imgChar = imgChar.rotate(randint(minAngle, maxAngle),
                                     expand=True, fillcolor=background);
                
            rotatedImagesChar.append(imgChar)
        
        tatalWidth = pad + sum([img.width+pad for img in rotatedImagesChar]);

        #create image main container:
        imgCaptcha = Image.new("RGB", (tatalWidth, heightFont+pad*2), background);
            
        lastx = pad;
        #add images into container:
        for imgChar in rotatedImagesChar:
            imgCaptcha.paste(imgChar, (lastx, pad));
            lastx += imgChar.width+pad;
    else:
        #no-rotated chars:
        tatalWidth = _getTextLength(font, text) + (pad*(len(text)+1));
        imgCaptcha = Image.new("RGB", (tatalWidth, heightFont+pad*2), background);
        draw = ImageDraw.Draw(imgCaptcha);
        lastx = pad;
        for char in text:
            color = _getRandomContrastColor(background);
            draw.text((lastx, pad), char, color, font=font);
            lastx += _getTextLength(font, char) + pad;

    #add garbage ? :
    if addgarbage:
        draw = ImageDraw.Draw(imgCaptcha);
        color = _invertColor(background);
        
        for nline in range(1): #more ? not
            line = [];
            for x in range(0, length+1):
                x = tatalWidth/length * x;
                points = (x+randint(0,3),
                          randint(0,imgCaptcha.height));
                line.append(points);

            draw.line(line, color, 2, "curve");
    
    #saving image base:
    if not filename_out:
        ftemp = TemporaryFile(mode="wb", suffix=".jpg", prefix="captcha", delete=False);
        filename_out = ftemp.name;
        imgCaptcha.save(ftemp);
        ftemp.close();
    else:
        ftemp = None;
        imgCaptcha.save(filename_out);

    return text, filename_out;


if __name__ == "__main__":

    from time import time as timer;

    t1 = timer();
    text, fname = CreateImageCaptcha(["impact", "arial"], 25,
                    filename_out="micaptcha.jpg", background=(20, 20, 20));

    t1 = timer()-t1;

    print(text, fname);
    print("%f seconds transcurred" % t1);

    #windows:
    from os import startfile;
    startfile(fname);

    input("Pause - press enter to exit...");


