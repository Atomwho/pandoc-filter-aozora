# !/usr/bin/env python
# coding: utf-8

from pandocfilters import toJSONFilter, Str, RawInline
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def aozora_to_html_ruby(text):
    '''aozorabunko format ruby to html
    e.g,
    難読|漢字《かんじ》でも読《よ》めますよ。
    to
    難読|<ruby>漢字<rt>かんじ</rt></ruby>でも<ruby>読<rt>よ</rt></ruby>めますよ'''
    s = text.decode('utf-8')
    pattern = ur'｜?([\u4e00-\u9fff]+?)《([\u3040-\u309f]+?)》'
    repl = ur"<ruby>\1<rt>\2</rt></ruby>"
    return re.sub(pattern, repl, s)


def for_japanese(key, value, format, meta):
    if key == 'Str':
        return RawInline(u'html',aozora_to_html_ruby(value))

if __name__ == "__main__":
    toJSONFilter(for_japanese)
