import codecs
import os

from markdown import markdown

basedir = os.path.abspath(os.path.dirname(__file__))


def md2text(filename):
    if filename == 'about':
        input_file = codecs.open(basedir+"/static/md/about.md", mode="r", encoding="utf-8")
        text = input_file.read()
        return text

