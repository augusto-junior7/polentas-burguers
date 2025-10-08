import re


def is_valid_phone(phone: str) -> bool:
    if not isinstance(phone, str):
        return False

    cleaned_phone = re.sub(r"\D", "", phone)
    regex = r"^[1-9]{2}(?:[2-8]|9[1-9])[0-9]{3,4}[0-9]{4}$"

    if re.fullmatch(regex, cleaned_phone):
        return True
    else:
        return False
