#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of d2quoter.
# https://github.com/d2emon/quoter.git

# Licensed under the GPL-3.0 license:
# http://www.opensource.org/licenses/GPL-3.0-license
# Copyright (c) 2018, Dmitry Kutsenko <d2emonium@gmail.com>

from quoter.version import __version__  # NOQA
import random
import json


def load():
    data_file = open("data/quotes", "r")
    quotes = ''.join(data_file.readlines())
    print(quotes)
    return json.loads(quotes)


class Quote:
    def __init__(self, **kwargs):
        self.quote = kwargs.get('quote', '...')
        self.author = kwargs.get('author', '')
        self.source = kwargs.get('source', '')
        self.comment = kwargs.get('comment', '')

    def __str__(self):
        source = ''
        author = ''
        comment = ''

        if self.source:
            source = "(%s)" % (self.source)
        if self.author:
            author = "%s%s:" % (self.author, source)
        else:
            author = source
        if author:
            author += "\t"
        if self.comment:
            comment = "\n\t%s" % (self.comment)

        return "%s\"%s\"%s" % (
            author,
            self.quote,
            comment
        )


def randomQuote(count=1):
    global quotes
    res = []
    for i in range(count):
        q = random.choice(quotes)
        if type(q) is dict:
            yield Quote(**q)
        else:
            yield Quote(quote=q)


quotes = load()
