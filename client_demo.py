import aiohttp
import json


ENDPOINT = 'http://127.0.0.1:50505/post'


async def call(payload: dict):

    async with aiohttp.ClientSession() as session:
        async with session.post(ENDPOINT,
                      data=bytes(json.dumps(payload), 'utf-8')
                  ) as resp:
            #print(resp.status)
            return await resp.json()


# Be sure to set `multiline` flag = True when sending definitions etc. that
# span multiple input lines
payload = {'input': 'def f(x):\n  return x + 5',
           'multiline': True}

#payload = {'input': 'def f(x): return x + 5'}

#payload = {'input': 'f(3)'}

#payload = {'input': 'ls doc'}

# Use the strip_newlines flag to avoid the console's newline formatting of the
# output from the `cat` command, so you can download the whole file as-is in base64
# format (if it's < 100KB in size).
#payload = {'input': 'cat -b attachments/bday.png',
#           'strip_newlines': True}
# Use base64.b64decode(r['response']) and write the resulting bytes to a binary file.


r = await call(payload)

if r['response'] != "":
    try:
        return_value = json.loads(r['response'])
    except json.JSONDecodeError:
        # e.g. output from executed function could be plain text
        return_value = r['response']
else:
    return_value = None
