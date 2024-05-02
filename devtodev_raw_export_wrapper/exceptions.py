class DevtodevWrapperError(Exception):
    def __init__(self, original_exception, message='DevToDev Wrapper Error'):
        self.original_exception = original_exception
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.original_exception}'


class DevtodevApiError(Exception):
    def __init__(self, error_msg, message='DevToDev API Error'):
        self.error_msg = error_msg
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.error_msg}'
