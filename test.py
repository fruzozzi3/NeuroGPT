import g4f
from fp.fp import FreeProxy
import os, requests
from g4f.typing import sha256, Dict, get_type_hints
import json

proxy = FreeProxy(country_id=['FL'], timeout=0.5, rand=True).get()
stream = False
#print(proxy)
response = g4f.ChatCompletion.create(model='gpt-4', provider=g4f.Provider.i207, messages=[
                                    {"role": "user", "content": "hello"}], stream=False)



if stream:
    for message in response:
        print(message)
else:
    print(response)
    
