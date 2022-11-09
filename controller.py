import re

# FOR BRASILIAN PHONES WITHOUT LINK TAG REGEX_PHONES = r"\+{0,1}[0-9]{0,3}[ (]{0,1}[\(]{0,1}[1-9]{2}[\)]{0,1}[ ]{0,1}[0-9]{4,9}[ \,\.\-]{0,1}[0-9]{4,5}"
REGEX_PHONES = r"(?<=tel:)([^\"\'(&quot;)]*)\""
REGEX_ICON = [
    r"<link .*? href=\"(.*?.ico)\"",
    r"rel=\"icon\".*?href=\".*?\"",
    r"rel=\"alternate icon\".*?href=\"(.*?)\"",
    r"(?<=href=[\"\']).*(?=[\"\'])"
]
REGEX_URL = r"^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)"
REGEX_CLEAR_STRING = r"[^0-9\+\s\(\)]"


def get_phones_number(text):
    text = text.split("/head>")[1]
    numbers = re.findall(REGEX_PHONES, text)
    return numbers


def get_icon(url, text):
    icon = None
    index = 0
    while not icon:
        if index == 3:
            return f"{url}favicon.ico"
        icon = re.search(REGEX_ICON[index], text)
        index += 1
    icon = re.search(REGEX_ICON[3], icon.group()).group().replace('"', '')
    if icon.startswith("http"):
        return icon
    url = re.search(REGEX_URL, url).group()
    return f"{url}{icon}"
