# -*- coding: utf-8 -*-
import re
import unicodedata

CHAR_MAP = {
    'ç': 'c', 'Ç': 'C',
    'ğ': 'g', 'Ğ': 'G',
    'ı': 'i', 'İ': 'I',
    'ö': 'o', 'Ö': 'O',
    'ş': 's', 'Ş': 'S',
    'ü': 'u', 'Ü': 'U',
    '’': "'", '‘': "'", '`': "'",
    '“': '"', '”': '"',
    '–': '-', '—': '-',
    '…': '...',
    '•': '*',
}

def to_ascii_turkish(text: str) -> str:
    if not text:
        return text
    result = []
    for ch in text:
        if ch in CHAR_MAP:
            result.append(CHAR_MAP[ch])
        elif ord(ch) < 128:
            result.append(ch)
        else:
            norm = unicodedata.normalize('NFKD', ch)
            ascii_ch = ''.join(c for c in norm if ord(c) < 128)
            result.append(ascii_ch if ascii_ch else '')
    return ''.join(result)

if __name__ == '__main__':
    sample = "Özgürlük Savaşçıları: Türkçe yama, Christopher Stone, New York sokaklarında Kızıl Ordu'ya karşı!"
    print('Original:', sample)
    print('Converted:', to_ascii_turkish(sample))
