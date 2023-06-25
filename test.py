# XwjyvWRZojfneo_8saFPAbPE8z8t7RvRuyQg_PlnJifsYhki0gu68UbvZM62l95A6Y6w9g.
from bardapi import Bard
import os
import json

with open('credentials.json', 'r') as f:
    file = json.load(f)
    token = file['output']

os.environ['_BARD_API_KEY'] = token
bard = Bard(timeout=30)
response = bard.get_answer("what is bard?")['content']
print(response)

