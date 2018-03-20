#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of d2quoter.
# https://github.com/d2emon/quoter.git

# Licensed under the GPL-3.0 license:
# http://www.opensource.org/licenses/GPL-3.0-license
# Copyright (c) 2018, Dmitry Kutsenko <d2emonium@gmail.com>

from quoter import quotes, randomQuote


def main():
    print(quotes)
    print('-=' * 80 + '-')
    for id, q in enumerate(randomQuote(20)):
        print("%d. %s" % (id + 1, q))


if __name__ == "__main__":
    main()
