from rest_framework import status

class InvalidInput(Exception):
    code = 'E001'
    http_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self, message):
        self.message = message

class UserDoesNotExist(Exception):
    code = 'E002'
    http_code = status.HTTP_404_NOT_FOUND
    message = 'User not found'
