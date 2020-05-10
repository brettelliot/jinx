class JinxAuthenticationError(Exception):
    """
    This error is thrown when there is an authentication issue with an IEX
    cloud request.
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class JinxQueryError(Exception):
    """
    This error is thrown when an error occurs with the query to IEX, be it a
    network problem or an invalid query.
    """

    _DEFAULT_MSG = (
        "The query could not be completed. There was a "
        "client-side error with your request."
    )

    def __init__(self, status, response):
        self.response = response
        self.status = status

    def __str__(self):
        return "An error occurred while making the query ({}): {}".format(
            self.status, self.response
        )

class JinxSymbolError(Exception):
    """
    This error is thrown when an invalid symbol is given.
    """

    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return "Symbol " + self.symbol + " not found."
