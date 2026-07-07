import re

class DataValidator:
    @staticmethod
    def validate_username(username):
        """
        Validate the username against certain criteria:
        - Must be 3-20 characters long
        - Can contain letters, digits, underscores
        - Cannot start with a digit
        """
        pattern = r'^[a-zA-Z][a-zA-Z0-9_]{2,19}$'
        if re.match(pattern, username):
            return True
        return False

    @staticmethod
    def validate_score(score):
        """
        Validate the score to ensure it is a non-negative integer.
        """
        if isinstance(score, int) and score >= 0:
            return True
        return False

    @staticmethod
    def validate_email(email):
        """
        Validate the email format using regex.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True
        return False