from captcha.image import ImageCaptcha

image = ImageCaptcha(width=200, height=100)

captcha_text = "GreekGod"

data = image.generate(captcha_text)

image.write(captcha_text, "Captcha.png")