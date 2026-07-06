

class UserException(Exception):
    pass


class UserNotFoundError(UserException):
    pass

class UserBlockedError(UserException):
    pass