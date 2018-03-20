#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of d2quoter.
# https://github.com/d2emon/quoter.git

# Licensed under the GPL-3.0 license:
# http://www.opensource.org/licenses/GPL-3.0-license
# Copyright (c) 2018, Dmitry Kutsenko <d2emonium@gmail.com>

from preggy import expect

from quoter import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
