import requests
import brotli

# ** BLACK BOX UN_AUTH CONFIGS **
def generateResponse_BB(query):
    user = query
    
    url = "https://www.blackbox.ai/api/chat"

    headers = {
        "Alt-Svc": "h3=':443'; ma=86400",
        "Rndr-Id": "f6926c78-c551-42a6",
        "Cf-Cache-Status": "DYNAMIC",
        "Cf-Ray": "87935640289aa7ed-SYD",
        "Accept": "*/*",
        "Vary": "Accept-Encoding",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Encoding": "br",
        "Content-Type": "text/plain; charset=utf-8",
        "Origin": "https://www.blackbox.ai",
        "Content-Length": "325",
        "X-Experimental-Stream-Data": 'false',
        "X-Render-Origin-Server": "Render",
        "Referer": "https://www.blackbox.ai/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Cookie": "sessionId=f6ed8395-0db0-43a0-a606-1f860ac3a6ce; intercom-id-jlmqxicb=d5fe1014-a550-4eae-baea-13ee56646a69; intercom-session-jlmqxicb=; intercom-device-id-jlmqxicb=470f45e7-b5a1-44cb-994c-bba9893f4e09",
    }

    payload = {
        "agentMode": {},
        "clickedAnswer2": False,
        "clickedAnswer3": False,
        "codeModelMode": True,
        "githubToken": None,
        "id": "NOadk0x",
        "isChromeExt": True,
        "isMicMode": False,
        "messages": [
            {"id": "NOadk0x", "content": user, "role": "user"}
        ],
        "previewToken": None,
        "trendingAgentMode": {},
        "userId": "a8be1ea5-b300-4320-9755-0fbb76c0369d",
        "visitFromURL": None
    }

    response = requests.post(url, json=payload, headers=headers)

    # clean the final response from the AI..
    try:
        filter_response =  (f'\n{response.content.decode('utf-8').split(" (4) ")[1]}')
        return filter_response.strip()
    except:
        try:
            filter_response =  (f'\n{response.content.decode('utf-8').split(" (3) ")[1]}')
            return filter_response.strip()
        except:
            try:
                filter_response =  (f'\n{response.content.decode('utf-8').split(" (2) ")[1]}')
                return filter_response.strip()
            except:
                try:
                    filter_response =  (f'\n{response.content.decode('utf-8').split(" (1) ")[1]}')
                    return filter_response.strip()
                except:
                    filter_response =  (f'\n{response.content.decode('utf-8')}')
                    return filter_response.strip()
        


# ** IMAGE GENERATION UN_AUTH CONFIGS **


# ** WOLFRAMALPHA AUTH CONFIGS **



if __name__ == "__main__":
    result = generateResponse_BB("what is prompt engineering ?")
    print(result)