import os, requests

key = None
with open(r'media_prospecting\.env') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY='):
            key = line.strip().split('=', 1)[1].strip()

models = [
    'gemini-2.5-flash-lite',
    'gemini-flash-latest',
    'gemini-flash-lite-latest',
    'gemini-3-flash-preview',
    'gemini-3.1-flash-lite'
]

for m in models:
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={key}'
    try:
        r = requests.post(url, json={'contents': [{'parts': [{'text': 'Hello'}]}]}, timeout=5)
        print(f'{m}: status={r.status_code}')
        if r.status_code == 200:
            print(f'   SUCCESS with {m}!')
        else:
            msg = r.json().get('error', {}).get('message', '')[:100]
            print(f'   {msg}')
    except Exception as e:
        print(f'{m}: error={e}')
