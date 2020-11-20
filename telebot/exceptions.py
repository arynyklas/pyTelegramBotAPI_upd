class HTTPStatus():
    pass

class BlockedByUser(Exception):
    pass

class ChatNotFound(Exception):
    def __init__(self, result_json):
        super(ChatNotFound, self).__init__(
            f"Chat not found: Error code: {result_json['error_code']}, "
            f"Description: {result_json['description']}",
        )

        self.json = result_json
        self.ok = result_json['ok']
        self.error_code = result_json['error_code']
        self.description = result_json['description']

class MessageNotFound(Exception):
    pass

class TokenIsInvalid(Exception):
    pass

class BadRequest(Exception):
    pass