from jinx.base import _JinxBase

class Stock(_JinxBase):

    def __init__(self, symbols=None, **kwargs):
        super(JinxStock, self).__init__(**kwargs)
