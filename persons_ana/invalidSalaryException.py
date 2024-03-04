# defining a new exception class derived from the in-built base class Exception
class InvalidSalaryException(Exception):
    # constructor
    def __init__(self):
        # attribute
        self.message = "Invalid additional salary. Please provide a positive value."

    # getters and setters
    def get_message(self):
        return self.message

    def set_message(self, msg):
        self.message = msg
