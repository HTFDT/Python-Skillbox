import re


def validate_date(date: str) -> bool:
    """
        validates the date
        valid date formats:
            день.месяц.год (14.09.2022, 5.02.1995, 01.4.2012)
            день/месяц/год (14/09/2022, 5/02/1995, 01/4/2012)
            день-месяц-год (14-09-2022, 5-02-1995, 01-4-2012)
            год.месяц.день (2022.09.14, 1995.02.5, 2012.4.01)
            год/месяц/день (2022/09/14, 1995/02/5, 2012/4/01)
            год-месяц-день (2022-09-14, 1995-02-5, 2012-4-01)
            день месяц_rus год (14 сентября 2022, 5 февраля 1995, 01 апреля 2012)
            Месяц_eng день, год (September 14, 2022, February 5, 1995, April 01, 2012)
            Мес_eng день, год (Sep 14, 2022, Feb 5, 1995, Apr 01, 2012)
            год, Месяц_eng день (2022, September 14, 1995, February 5, 2012, April 01)
            год, Мес_eng день (2022, Sep 14, 1995, Feb 5, 2012, Apr 01)

        >>> validate_date("20 января 1806")
        True
        >>> validate_date("1924, July 25")
        True
        >>> validate_date("26/09/1635")
        True
        >>> validate_date("3.1.1506")
        True
        >>> validate_date("25.08-1002")
        False
        >>> validate_date("декабря 19, 1838")
        False
        >>> validate_date("8.20.1973")
        False
        >>> validate_date("Jun 7, -1563")
        False
        >>> validate_date("31 февраля 2023")
        False
        >>> validate_date("31 июня 2015")
        False
    """
    regex = re.compile(r"^(?:(?:0?\d|[12]\d|3[01])([./-])(?:(?<!3[01][./-])0?2|(?<!31[./-])0?[469]|0?[^2469]|12)"
                       r"\1\d{4}|\d{4}([./-])(?:0?2(?![./-]3[01])|0?[469](?!31[./-])|0?[^2469]|12)\2(?:0?\d|"
                       r"[12]\d|3[01])|(?:[0-2]\d|3[01]) (?:января|(?<!3[01] )февраля|марта|(?<!31 )(?:апреля|июня|"
                       r"сентября|ноября)|мая|июля|августа|октября|декабря) \d{4}|(?:Jan(?:uary)?|Feb(?:ruary)?"
                       r"(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|Nov(?:ember)?)(?! 31)|May|"
                       r"July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) (?:[0-2]\d|3[01]), \d{4}|\d{4}, "
                       r"(?:Jan(?:uary)?|Feb(?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|"
                       r"Nov(?:ember)?)(?! 31)|May|July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) "
                       r"(?:[0-2]\d|3[01]))$")
    return bool(regex.match(date))
