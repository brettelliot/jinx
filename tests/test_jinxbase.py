# -*- coding: utf-8 -*-

import pytest

from jinx.base import _JinxBase

class TestBase(object):
    def test_all_defaults(self):
        base = _JinxBase()

        assert base.pause == 0.5
