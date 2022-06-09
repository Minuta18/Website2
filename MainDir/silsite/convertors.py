import base64


class B64Converter:
    # decide on complexity of your b64 regex by
    # referring to https://stackoverflow.com/a/475217

    def to_python(self, value):
        return base64.urlsafe_b64decode(value)

    def to_url(self, value):
        return base64.urlsafe_b64encode(value)