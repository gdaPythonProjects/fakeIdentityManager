# https://www.pythoncentral.io/how-to-check-if-a-string-is-a-number-in-python-including-unicode/


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
