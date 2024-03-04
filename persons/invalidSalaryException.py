class InvalidSalaryException(Exception):
    def __init__(self):
        self.message = "Invalid additional salary. Please provide a positive value."

    def get_message(self):
        return self.message

    def set_message(self, msg):
        self.message = msg
