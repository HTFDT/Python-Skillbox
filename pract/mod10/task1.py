import re


def validate_password(password: str) -> bool:
    """
    validates the password
    criterias:
        allowed chars: digits, latin letters of any case, ^$%@#&*,
        length: >8,
        at least two lowercase latin letters,
        at least one digit,
        at least three different special characters,
        no ,.!? characters;

    >>> validate_password("rtG&3FG#Tr^e")
    True
    >>> validate_password("a^A1@*@1Aa")
    True
    >>> validate_password("oF^a1D@y5%e6")
    True
    >>> validate_password("enroi#$*rkdeR#$*092uwedchf34tguv394h")
    True
    >>> validate_password("пароль")
    False
    >>> validate_password("password")
    False
    >>> validate_password("qwerty")
    False
    >>> validate_password("lOngPa$$W0Rd")
    False

    """

    regex = re.compile(r"^(?=[A-Za-z\d^$%@#&*]{8,})(?=(?:.*[a-z].*){2,})(?=(?:.*[1-9].*)+)(?=[^,.!?]*$).*([\^$%@#&*])"
                       r".*(?!\1)([\^$%@#&*]).*(?!\1)(?!\2)([\^$%@#&*]).*$")
    return bool(regex.match(password))
