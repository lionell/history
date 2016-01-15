from grab import Grab

PATH = 'http://zno.osvita.ua/ukraine-history/all/'
HEADER = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="uk" lang="uk" xmlns:og="http://ogp.me/ns#" xmlns:fb="http://ogp.me/ns/fb#">
<head>
<title>Всі запитання з предмета «Історія України», починаючи з 1 – сайт ЗНО – Освіта.UA</title>
<!-- 0.30132508277893 -->
<meta name="title" content="Всі запитання з предмета «Історія України», починаючи з 1 – сайт ЗНО – Освіта.UA" />
<meta name="alexaVerifyID" content="" />
<meta name="verify-v1" content="" />
<meta name='yandex-verification' content='6f08c6e0449e58ec' />
<meta http-equiv="Expires" content="Thu, Jan 1 1970 00:00:00 GMT">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Cache-Control" content="no-cache">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Content-language" content="uk" />
<meta property="og:url" content="http://zno.osvita.ua/ukraine-history/all/1/" />
<meta property="og:type" content="article" />
<meta property="og:locale" content="uk_UA" />
<meta property="og:site_name" content="Освіта.UA" />
<meta property="og:title" content="Всі запитання з предмета «Історія України», починаючи з 1 – сайт ЗНО – Освіта.UA" />
<meta property="og:description" content="" />
<meta property="og:image" content="http://osvita.ua/doc/i/zno_300x300.jpg" />
<meta property="og:image:width" content="300" />
<meta property="og:image:height" content="300" />
<meta property="fb:app_id" content="178406328912732" />
<link rel="shortcut icon" type="image/x-icon" href="http://zno.osvita.ua/doc/i/favicon.ico" />
<link rel="apple-touch-icon" href="/doc/i/apple-touch-icon.png" />
<link rel="apple-touch-icon-precomposed" href="/doc/i/apple-touch-icon.png" />
<base href="http://zno.osvita.ua/" />
<link rel="stylesheet" href="http://zno.osvita.ua/doc/css/css.css?v=0501" type="text/css" />
<link type="text/css" rel="stylesheet" href="http://zno.osvita.ua/doc/css/social-likes_birman.css" />

<script type="text/javascript" src="http://zno.osvita.ua/doc/js/znoscript.js?v=0501"></script>
<script type="text/javascript" src="http://zno.osvita.ua/doc/js/social-likes.min.js"></script>
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML"></script>
<!--[if lte IE 8]>
<style type="text/css"> @import "http://zno.osvita.ua/doc/css/ie7.css"; </style>
<script src="http://zno.osvita.ua/doc/js/enough.js" type="text/javascript"></script>
<script src="http://zno.osvita.ua/doc/js/unitpngfix.js" type="text/javascript"></script>
<![endif]-->

</head>
<body>
'''

FOOTER = '''
</body>
</html>
'''

g = Grab()
with open('index.html', encoding='utf-8', mode="w") as f:
    f.write(HEADER)
    for number in range(0, 1108):
        print(number)
        g.go(PATH + str(number))
        form = g.doc.select('//form[@id="q' + str(number + 1) + '-form"]')
        question = form.select('div[@class="q-txt "]').html()
        answers = ''
        for x in form.select('div[@class="quest col"]'):
            answers += x.html()
        answer_key = form.select('div[@class="q-button-wrap"]/input[@name="result"]/@value').text()
        # print(question)
        # print(answer)
        f.write('<h3>Питання ' + str(number) + '</h3>')
        f.write(question)
        f.write(answers)
        f.write('<h5>Відповідь: ' + answer_key + '</h5>')
        f.write('<hr>')
    f.write(FOOTER)
# open('index.html', encoding='utf-8', mode='w').write(question)
