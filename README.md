# randcaptcha
Genera una imagen de una captcha random | generate a random captcha image with Python2 or Python3


## Dependencies:
```
pip install Pillow
```


## Example:

CreateImageCaptcha(..) return text content on captcha and filename of captcha.

``` Python
>>> CreateImageCaptcha("arial", 22);
('JM9M6', 'C:\Users\..\AppData\Local\Temp\captchagjyg65yw.jpg')

>>> CreateImageCaptcha(["impact", "arial"], 25, background=(180, 180, 180));
('QBLGG', 'C:\Users\..\AppData\Local\Temp\captcha31t3_kho.jpg')

>>> CreateImageCaptcha(["impact", "arial"], 25, length=6, background=(180, 180, 180));
('4LU9EH', 'C:\Users\..\AppData\Local\Temp\captchaot67ifqf.jpg')

>>> CreateImageCaptcha("impact", 25, filename_out="micaptcha.jpg", background=(20, 20, 20));
('QYGYU', 'micaptcha.jpg')

>>> CreateImageCaptcha("C:/users/../desktop/consolab.ttf", 30);
('PKYEL', 'C:\\Users\\User\\AppData\\Local\\Temp\\captchadyhhcqu0.jpg')

>>> CreateImageCaptcha("C:/users/../desktop/FORTE.TTF", 26);
('59YHN', 'C:\\Users\\User\\AppData\\Local\\Temp\\captchafbrlad8g.jpg')
```

### 1
![image](https://user-images.githubusercontent.com/95723749/213705834-55369e0b-61e6-4a18-a8f1-90cc98b108c7.png)

### 2
![image](https://user-images.githubusercontent.com/95723749/213329522-4aeadf05-c9d0-4d39-ad2d-33071199807b.png)

### 3
![image](https://user-images.githubusercontent.com/95723749/213329583-f6ed9648-40e2-4222-a550-977b3fc7b199.png)

### 4
![image](https://user-images.githubusercontent.com/95723749/213329625-2d99be9b-7e08-4af3-b833-ce56b9e568a5.png)

### 5
![image](https://user-images.githubusercontent.com/95723749/213712785-29be8694-b53b-4b51-9476-acae40a6db93.png)

### 6
![image](https://user-images.githubusercontent.com/95723749/213717521-208183cc-4fa0-4cec-ac66-a626d7846fe6.png)


## Last Changes:
---------------

## version 0.2

Added params **kw, can use new param "rotate" for specify random angle of rotation. Module compatibility with Py2 and Py3
