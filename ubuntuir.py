#!/usr/bin/env python
import requests
from headers import HEADERS

def paste(text: str) -> str:
    DATA = {
        'text': f'{text}',
    }

    response = requests.post('https://paste.ubuntu.ir/', headers=HEADERS, data=DATA)

    return response.url

if __name__ == '__main__':
    print(paste(
        """
        this is the sample text.
        to use this script you should write another simple scritp which will let you
        to post texts on paste.ubuntu.ir.

        the script is simple as this:

        ```python3
        from pastebin import ubutnuir
        result = ubutnuir.post2PasteUbuntuIr('put your text here')
        print(result)
        ```
        """
    ))
