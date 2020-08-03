import base64
import os
import random
from io import BytesIO

from io import StringIO
from PIL import Image, ImageDraw, ImageFont

class Captcha(object):

    def __init__(self, request):
        self.django_request = request
        self.session_key = request.session.session_key
        self.charsource = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        # image size
        self.img_width = 100
        self.img_height = 48

    def _createColor(self):
        # 随机生成颜色
        red = random.randint(0,255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)

    def _saveCodeSession(self, code):
        # 将验证码放入服务器内存和设置过期时间
        self.django_request.session[self.session_key] = code
        self.django_request.session.set_expiry(60)

    def getVerificationCode(self):
        image = Image.new("RGB", (self.img_width, self.img_height), self._createColor())
        imageDraw = ImageDraw.Draw(image, "RGB")
        ttf_cur_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "files"),"FZSJ-NIDBYJSW.TTF")
        imageFont = ImageFont.truetype(ttf_cur_path, 24)

        code = ""
        for i in range(4):
            ch = random.choice(self.charsource)
            imageDraw.text((5+i*20,10), ch, fill=self._createColor(), font=imageFont)  # 坐标， 写入内容， 背景颜色， 字体样式
            code +=ch
        self._saveCodeSession(code)
        # 画图片上的麻子
        for i in range(500):
            x = random.randint(0,100)
            y = random.randint(0,48)
            imageDraw.point((x,y), fill=self._createColor())
        # 将Image图片转为base64字节流返回出去
        buf = BytesIO()
        image.save(buf, format='gif')
        byte_data = buf.getvalue()
        data = base64.b64encode(byte_data)
        # image.show()
        return data
