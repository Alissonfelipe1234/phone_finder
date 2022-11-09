import sys
from concurrent.futures import as_completed
from controller import get_icon, get_phones_number
from requests_futures.sessions import FuturesSession

urls = sys.stdin
session = FuturesSession()
results = []

futures=[session.get(i) for i in urls]

for future in as_completed(futures, timeout=5):
    resp = future.result()
    results.append({
        'logo': get_icon(resp.request.url, resp.text),
        'phones': get_phones_number(resp.text),
        'website': resp.request.url,
    })


for item in results:
    print(item)