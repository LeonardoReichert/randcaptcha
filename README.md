# randcaptcha
Genera una imagen de una captcha random | generate a random captcha image with Python2 or Python3


## Dependencies:
```
pip install Pillow
```


## Example:

CreateImageCaptcha(..) return text content on captcha and filename of captcha.

``` Python
>>> CreateImageCaptcha(["impact", "arial"], 25, background=(180, 180, 180));
('QBLGG', 'C:\Users\..\AppData\Local\Temp\captcha31t3_kho.jpg')
...
>>> CreateImageCaptcha(["impact", "arial"], 25, length=6, background=(180, 180, 180));
('4LU9EH', 'C:\Users\..\AppData\Local\Temp\captchaot67ifqf.jpg')
...
>>> CreateImageCaptcha("impact", 25, filename_out="micaptcha.jpg", background=(20, 20, 20));
('QYGYU', 'micaptcha.jpg')
```

### 1
![image](https://user-images.githubusercontent.com/95723749/213329522-4aeadf05-c9d0-4d39-ad2d-33071199807b.png)

### 2
![image](https://user-images.githubusercontent.com/95723749/213329583-f6ed9648-40e2-4222-a550-977b3fc7b199.png)

### 3
![image](https://user-images.githubusercontent.com/95723749/213329625-2d99be9b-7e08-4af3-b833-ce56b9e568a5.png)



## Last Changes:
---------------

## version 0.2

Added params **kw, can use new param "rotate" for specify random angle of rotation. Module compatibility with Py2 and Py3
