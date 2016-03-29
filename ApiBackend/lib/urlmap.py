# -*- coding: utf-8 -*-
__author__ = 'Hipeace86'
__datetime__ = '15-4-13'


class Urlmap(object):
    def __init__(self):
        self.handlers = []

    def __call__(self, url, **kwds):
        def _(cls):
            self.handlers.append((url, cls, kwds))
            return cls

        return _


def handlers(*args):
    handlers = []
    for i in args:
        handlers.extend(i.urlmap.handlers)
    return handlers


urlmap = Urlmap()
