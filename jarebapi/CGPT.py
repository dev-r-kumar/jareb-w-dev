import requests
import brotli

# ** BLACK BOX UN_AUTH CONFIGS **
def generateResponse_BB(query):
    user = query
    
    url = "https://chatgpt.com/backend-anon/conversation"

    headers = {
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Ch-Ua-Platform": "Windows",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "Priority": "u=1, i",
        "Content-Security-Policy": "default-src 'self'; script-src 'self' 'nonce-pub1f79f8ac903a5872ae5f53026d20a77c' 'unsafe-inline' 'unsafe-eval' https://*.chatgpt.com https://*.oaistatic.com https://chat.openai.com https://chatgpt.com https://jidori.g1.internal.services.openai.org https://oaistatic.com https://snc.apps.openai.com https://tcr9i.chat.openai.com https://widget.intercom.io js.intercomcdn.com js.stripe.com wss://*.chatgpt.com; script-src-elem 'unsafe-inline' auth0.openai.com challenges.cloudflare.com https://*.chatgpt.com https://*.oaistatic.com https://apis.google.com https://chat.openai.com https://chatgpt.com https://docs.google.com https://jidori.g1.internal.services.openai.org https://js.live.net/v7.2/OneDrive.js https://oaistatic.com https://snc.apps.openai.com https://tcr9i.chat.openai.com https://widget.intercom.io https://www-onepick-opensocial.googleusercontent.com js.intercomcdn.com js.stripe.com wss://*.chatgpt.com; img-src * 'self' data: https: https://docs.google.com https://drive-thirdparty.googleusercontent.com https://ssl.gstatic.com; style-src 'self' 'unsafe-inline' https://*.chatgpt.com https://*.oaistatic.com https://chat.openai.com https://chatgpt.com https://jidori.g1.internal.services.openai.org https://oaistatic.com https://snc.apps.openai.com https://tcr9i.chat.openai.com wss://*.chatgpt.com; font-src 'self' data: https://*.oaistatic.com https://fonts.gstatic.com; connect-src 'self' *.oaiusercontent.com api-iam.intercom.io api-js.mixpanel.com browser-intake-datadoghq.com fileserviceuploadsperm.blob.core.windows.net http://localhost:* https://*.chatgpt.com https://*.oaistatic.com https://api.onedrive.com https://chat.openai.com https://chatgpt.com https://content.googleapis.com https://docs.google.com https://events.statsigapi.net https://featuregates.org https://graph.microsoft.com https://jidori.g1.internal.services.openai.org https://oaistatic.com https://snc.apps.openai.com https://tcr9i.chat.openai.com o33249.ingest.sentry.io statsigapi.net wss://*.chatgpt.com wss://*.webpubsub.azure.com; frame-src challenges.cloudflare.com https://*.sharepoint.com https://content.googleapis.com https://docs.google.com https://onedrive.live.com js.stripe.com tcr9i.chat.openai.com; worker-src blob:; media-src blob: 'self'; report-uri https://browser-intake-datadoghq.com/api/v2/logs?dd-api-key=pub1f79f8ac903a5872ae5f53026d20a77c&dd-evp-origin=content-security-policy&ddsource=csp-report;",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains; preload",
        "X-Envoy-Upstream-Service-Time": "1004",
        "X-Robots-Tag": "nofollow",
        "Cross-Origin-Opener-Policy": "same-origin-allow-popups",
        "Alt-Svc": "h3=':443'; ma=86400",
        "Rndr-Id": "f6926c78-c551-42a6",
        "Cf-Cache-Status": "DYNAMIC",
        "Cf-Ray": "8810b571ee097e43-SYD",
        "Accept": "text/event-stream",
        "Vary": "Origin",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Encoding": "br",
        "Content-Type": "text/event-stream; charset=utf-8",
        "Origin": "https://chatgpt.com/",
        "Content-Length": "637",
        "X-Experimental-Stream-Data": 'false',
        "X-Render-Origin-Server": "Render",
        "Referer": "https://chatgpt.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Cookie": "oai-dm-tgt-c-240329=2024-04-02; oai-hlib=true; oai-did=498e3883-ccdd-4261-9227-7e11b64cb75f; intercom-device-id-dgkjq2bp=de13acd0-bf0e-4905-ae3b-78533c6b10fc; cf_clearance=ZHjkVvRzQzWMwHPc4Z6pVFs4plZBLjpRr0BwFzUSMaY-1715147403-1.0.1.1-Mg4nVvQkL6twc81nAgMmnpaH1HYA9OJWzdZ7LwkAl79AJ5vBZ9dze4Xn_DwZgDHXHqcOrdAOx2aobnKpvwO.SA; cf_clearance=j82aTo0oUvjLhrewT2oGeCpSd24u7dE1Wzc0DOmDu0c-1715240510-1.0.1.1-ps2jAhoTLi.TBC6BfOfaRv0_KtCKWJ5NQ_4wbp69mWgbZFCmT78M7tSxr5WtKaNVv9ivnc4mcnoSuPPqnlBGRg; __Host-next-auth.csrf-token=7e53a4b753a388313ae5117136d152694274ac3c303e680b284d6382c6ef38a1%7C5300a77440451ec03844009325ffcb9b4f8ddd42ce0b994b13f9293b3382f597; __cf_bm=NRZ1uJB8fie8ia3TfRHCc2VzULolXA9zCzl75pivVzA-1715246960-1.0.1.1-FE8ccxruBbAJ23cM1RJC9yEljC4yEOa_5Z8AHmjOjHkr72EqLgkp7ECRSlbQAfteFF6PoRO6i6dPwnD3IOamtg; __cflb=0H28vzvP5FJafnkHxjEtHJf2sVufZd5CAQpU7wvqd7K; _cfuvid=sHlT9ILAeFWKiaSno8a5TfnyL4Pn6ZhyLGYb1.M.cg4-1715246960278-0.0.1.1-604800000; __Secure-next-auth.callback-url=https%3A%2F%2Fauth0.openai.com%2Fv2%2Flogout%3Fclient_id%3DTdJIcbe16WoTHtN95nyywh5E4yOo6ItG%26returnTo%3Dhttps%3A%2F%2Fchatgpt.com; intercom-session-dgkjq2bp=b3hGcUpEc3BrdC9FcHlqd0h6MzFxekFvRkt2WW8wTDBxOWdHb2JjWStwdFhXbkNxV3IwemdIOUVYWEkyMlhqeC0tN21pSkJtOEVTMFZqWWwwMzdCRDhCUT09--d062b65a5560e4a565e362f0ef77bfb523d7cc8e; _dd_s=rum=0&expire=1715248322458",
        "Oai-Device-Id": "498e3883-ccdd-4261-9227-7e11b64cb75f",
        "Oai-Echo-Logs": "1,2973,0,5229,3,12657,1,14448,0,14638,1,18250,0,40683,3,52287,1,54281,0,54524",
        "Oai-Language": "en-US",
        "Openai-Sentinel-Chat-Requirements-Token": "gAAAAABmPJk_8kC_E_sRzlzRhwDFNZYhx-P-bmxG0B7WJgnThXpq6GIA7aBfvjhyswdJYaU8ThVPwWw-_ftZwlhVEwZHaVyQ2x2JZfjB8OQ-DHVvcToVpR_6w-_3h7Fn1QIuoj2JS1NSe3Qz_NamT53fP0FSU_ZREBt70KWVtBFfOGuwKTEX1qsDuhSVPPhodrh4O2Zm2vlHLRB8OKYAvhaCzYWSr_VuRQMPJqg0C4_Iqolr6WxRKWWVoIntj4Tu0FJ5cNHDaq1q40EnTdgaL6O68DZ1BWFnraXM0rDhSMSyTRooXXZ5h0i_vnVaP5v9wSYVIlTAaMrM2YEGPfg8GkqemAv96Beyva0Tk3H-TRCgNIaSCKWhHbPb-A6WdwYo_MJaGhGeuONe5qe-p-p8gFnQcLHJ4uXi3fhdjgKbReV_W795zYjglHWygfkJl2voC-WzLzkBjOIzJK0mUVQo6w-cr5-7el7iqQ==",
        "Openai-Sentinel-Proof-Token": "gAAAAABWzIzMDgsIlRodSBNYXkgMDkgMjAyNCAyMTozNzowMiBHTVQrMTIwMCAoRmlqaSBTdGFuZGFyZCBUaW1lKSIsMjE3MjY0OTQ3MiwzNCwiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiaHR0cHM6Ly9jZG4ub2Fpc3RhdGljLmNvbS9fbmV4dC9zdGF0aWMvY2h1bmtzL3ZlbmRvci1kNDgxNGU2Y2UwOWU1NGJlLmpzP2RwbD00OWU0OTIyNjFkMzhlZmY3ZDc5Y2ZkNzg3OGQ3YWJmYzk5MmMxODk1IiwiZHBsPTQ5ZTQ5MjI2MWQzOGVmZjdkNzljZmQ3ODc4ZDdhYmZjOTkyYzE4OTUiLCJlbi1VUyIsImVuLVVTLGVuIiwxOSwia2V5Ym9hcmTiiJJbb2JqZWN0IEtleWJvYXJkXSIsIl9yZWFjdExpc3RlbmluZ2wyZWU5aTdjeWMiLCJfX1JFQUNUX0lOVExfQ09OVEVYVF9fIl0="
    }

    payload = {
        "action": "next",
        "conversation_id": "3100edd9-b87b-43a7-a7bb-a3454ffdc844",
        "conversation_mode": {"kind": "primary_assistant"},
        "force_nulligen": False,
        "force_paragen": False,
        "force_paragen_model_slug": "",
        "force_rate_limit": False,
        "history_and_training_disabled": False,
        "messages": [{
            "id": "aaa29b46-958e-4f56-8d5f-028273a2106d",
            "author": {
                "role": "user",
            },
            "content": {
                "content_type": "text",
                "parts": ['hi']
            },
            "metadata": {}
        }],
        "model": "text-davinci-002-render-sha",
        "parent_message_id": "6b3405ba-9150-44cf-870f-5f65dbe605d2",
        "reset_rate_limits": False,
        "suggestions": [],
        "timezone_offset_min": -720,
        "websocket_request_id": "d2c4d9dd-9811-44a9-b2fd-43b48650d8a0",
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    # # clean the final response from the AI..
    # try:
    #     filter_response =  (f'\n{response.content.decode('utf-8').split(" (4) ")[1]}')
    #     return filter_response.strip()
    # except:
    #     try:
    #         filter_response =  (f'\n{response.content.decode('utf-8').split(" (3) ")[1]}')
    #         return filter_response.strip()
    #     except:
    #         try:
    #             filter_response =  (f'\n{response.content.decode('utf-8').split(" (2) ")[1]}')
    #             return filter_response.strip()
    #         except:
    #             try:
    #                 filter_response =  (f'\n{response.content.decode('utf-8').split(" (1) ")[1]}')
    #                 return filter_response.strip()
    #             except:
    #                 filter_response =  (f'\n{response.content.decode('utf-8')}')
    #                 return filter_response.strip()
        


# ** CHAT GPT UN_AUTH CONFIGS **

# ** IMAGE GENERATION UN_AUTH CONFIGS **


# ** WOLFRAMALPHA AUTH CONFIGS **



if __name__ == "__main__":
    result = generateResponse_BB("what is prompt engineering ?")
    # print(result)