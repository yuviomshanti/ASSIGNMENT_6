class BracketValidator:
    def __init__(self, string):
        self.string = string

    def is_valid(self):
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}

        for char in self.string:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if not stack or brackets[stack.pop()] != char:
                    return False

        return not stack

string1 = "()"  # Valid string
validator1 = BracketValidator(string1)
print(validator1.is_valid())  # Output: True

string2 = "()[]{}"  # Valid string
validator2 = BracketValidator(string2)
print(validator2.is_valid())  # Output: True

string3 = "[)"  # Invalid string
validator3 = BracketValidator(string3)
print(validator3.is_valid())  # Output: False

string4 = "({[)]"  # Invalid string
validator4 = BracketValidator(string4)
print(validator4.is_valid())  # Output: False

string5 = "{{{"  # Invalid string
validator5 = BracketValidator(string5)
print(validator5.is_valid())  # Output: False

