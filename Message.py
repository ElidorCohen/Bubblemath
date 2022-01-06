class Message:
    def __init__(self, from_id=None, to_id=None, text=None):
        self.from_user_id = from_id
        self.to_user_id = to_id
        self.text = text


class Feedback:
    def __init__(self, from_id=None, to_id=None, text=None, grade = None):
        self.from_user_id = from_id
        self.to_user_id = to_id
        self.text = text
        self.grade = grade
