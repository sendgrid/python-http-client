import pypandoc
import os


output = pypandoc.convert('README.md', 'rst')

with open('README.txt', 'w+') as f:
    f.write(output)

with open('./README.txt') as f:
    readme_rst = f.read()

replace = ('[SendGrid Logo]\n'
           '(https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)')

replacement = ('|SendGrid Logo|\n\n.. |SendGrid Logo| image:: '
               'https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png'
               '\n   :target: https://www.sendgrid.com')

final_text = readme_rst.replace(replace, replacement)

with open('./README.txt', 'w') as f:
    f.write(final_text)
