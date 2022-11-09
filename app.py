import sys
from concurrent.futures import as_completed
from controller import get_icon, get_phones_number
from requests_futures.sessions import FuturesSession

urls = sys.stdin
session = FuturesSession()
results = []

futures=[session.get(i.strip()) for i in urls]

for future in as_completed(futures):
    try:
        response = future.result(timeout=5)
        if response.status_code != 200:
            raise Exception
    except:
        results.append("DeadPage")
        continue
    
    text = response.text
    url = response.request.url
    results.append({
        'logo': get_icon(url, text),
        'phones': get_phones_number(text),
        'website': url,
    })


for item in results:
    print(item)