#!/usr/bin/env python3
"""Download Quran text from Al Quran Cloud and build app/assets/www/quran.js.
Editions: quran-uthmani (Arabic), en.transliteration, ar.muyassar (Tafsir al-Muyassar)."""
import json, os, urllib.request
os.makedirs('data', exist_ok=True)
E_ = ['quran-uthmani', 'en.transliteration', 'ar.muyassar']
for e in E_:
    f = f'data/{e}.json'
    if not os.path.exists(f):
        urllib.request.urlretrieve(f'https://api.alquran.cloud/v1/quran/{e}', f)
L = lambda e: json.load(open(f'data/{e}.json'))['data']['surahs']
U, T, M = map(L, E_)
sk = lambda s: ''.join(c for c in s if 0x621 <= ord(c) <= 0x64A or c == '\u0671')
BASMALA = sk('بسمٱللهٱلرحمنٱلرحيم')
S, A = [], []
for su, st, sm in zip(U, T, M):
    S.append([su['number'], su['name'], su['englishName'], len(su['ayahs'])])
    for a, t, m in zip(su['ayahs'], st['ayahs'], sm['ayahs']):
        assert a['number'] == t['number'] == m['number']
        txt = a['text'].replace('\ufeff', '')
        w = txt.split(' ')
        # API prefixes ayah 1 of each surah (except 1 and 9) with the Basmala; strip it
        if su['number'] not in (1, 9) and a['numberInSurah'] == 1 and len(w) > 4 and sk(''.join(w[:4])) == BASMALA:
            txt = ' '.join(w[4:])
        A.append([su['number'], a['numberInSurah'], a['juz'], txt, t['text'], m['text']])
assert len(S) == 114 and len(A) == 6236, (len(S), len(A))
open('app/assets/www/quran.js', 'w').write('window.Q=' + json.dumps({'s': S, 'a': A}, ensure_ascii=False, separators=(',', ':')))
print('OK', len(S), 'surahs', len(A), 'ayat')
