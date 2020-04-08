class MustContainAtSymbolError(Exception):
    """Raise when there is no "@" in the email"""

    def __init__(self):
        self.message = "Email must contain @"

    def __str__(self):
        return self.message


class NameTooShortError(Exception):
    """Raise when name in the email is
    less than or equal to 4 """

    def __init__(self):
        self.message = "Name must be more than 4 characters"

    def __str__(self):
        return self.message


class InvalidDomainError(Exception):
    """ Raise when domain of the email is invalid
    (valid domains are: .com, .bg, .net, .org)"""

    def __init__(self):
        self.message = "Domain must be one of the following: .com, .bg, .org, .net"

    def __str__(self):
        return self.message


command = input()
valid_domains = ["com", "bg", "net", "org"]

while command != "End":
    email = command

    if "@" not in email:
        raise MustContainAtSymbolError
    if len(email.split("@")[0]) <= 4:
        raise NameTooShortError
    if not email.split(".")[-1] in valid_domains:
        raise InvalidDomainError

    print("Email is valid")
    command = input()
