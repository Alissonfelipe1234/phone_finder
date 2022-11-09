import re

# FOR BRASILIAN PHONES WITHOUT LINK TAG REGEX_PHONES = r"\+{0,1}[0-9]{0,3}[ (]{0,1}[\(]{0,1}[1-9]{2}[\)]{0,1}[ ]{0,1}[0-9]{4,9}[ \,\.\-]{0,1}[0-9]{4,5}"
REGEX_PHONES = r"(?<=tel:)([^\"\'(&quot;)]*)\""
REGEX_ICON = [
    r"<link ([^\"\'(&quot;)]*) href=\"(.*?.ico)\"",
    r"rel=\"icon\".*?href=\".*?\"",
    r"rel=\"alternate icon\".*?href=\"(.*?)\"",
    r"(?<=href=[\"\']).*(?=[\"\'])"
]
REGEX_DOMAIN = r"^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)"
REGEX_CLEAR_STRING = r"[^0-9\+\s\(\)]"


def get_body_content(html):
    return html.split("/head>")[1]


def get_phones_number(text):
    text = get_body_content(text)
    numbers = re.findall(REGEX_PHONES, text)
    return numbers


def get_href_content(text):
    return re.search(REGEX_ICON[3], text).group().replace('"', '')


def get_domain(url):
    domain = re.search(REGEX_DOMAIN, url).group()
    if domain.endswith("/"):
        return domain
    return domain + "/"


def get_icon(url, text):
    icon = None
    index = 0
    domain = get_domain(url)
    while not icon:
        if index == 3:
            return f"{domain}favicon.ico"
        icon = re.search(REGEX_ICON[index], text)
        index += 1

    icon = get_href_content(icon.group())
    if icon.startswith("http"):
        return icon

    return f"{domain}{icon}"
