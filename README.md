# randcaptcha
Genera una imagen de una captcha random | generate a random captcha image with Python


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
>>> CreateImageCaptcha(["impact", "arial"], 25, filename_out="micaptcha.jpg", background=(20, 20, 20));
('QYGYU', 'micaptcha.jpg')
```





