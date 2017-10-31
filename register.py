import pypandoc

output = pypandoc.convert('README.md', 'rst')
with open('README.txt', 'w+') as f:
    f.write(output)

readme_rst = open('./README.txt').read()

replace = """\
[SendGrid Logo]
(https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)"""

replacement = """\
|SendGrid Logo|

.. |SendGrid Logo| image:: \
https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png
   :target: https://www.sendgrid.com"""

final_text = readme_rst.replace(replace, replacement)
with open('./README.txt', 'w') as f:
    f.write(final_text)
