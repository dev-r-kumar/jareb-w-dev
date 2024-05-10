from MEM import generateResponse_BB
import webbrowser
import random

def nanoQueryEnhance(user):
    # asking basic question..
    if ("what is" in user):
        response = generateResponse_BB(f"{user}. Remember response me in short as posisble as if chatting on messager with me. Don't provide in URL and links in your response. make short and simple answer. Also dont add unusual charcters or emojis in the response. Zero emojis in the response.")
        
        try:
            response = response.split("$@$")[2]
            return response
        except:
            return response


    # paragraph formating..
    elif ("write" and "paragraph" in user):
        response = generateResponse_BB(f'{user}. Remember write in paragrapgh format and dont use bullet points as it is a paragraph writing.')

        return response

    
    # write code formating...
    elif ("write" and "code" in user or "write" and "coding" in user):
        response = generateResponse_BB(f"{user}. Write Summary version of this code snippet below. No explainations abive this snippet just simple summarized version of the code function.")

        return response
    

    # patch V1 [greetings handling]
    elif ("hi" in user and len(user) < 15 or "hello" in user and len(user) < 15):
        response = generateResponse_BB(f"greet me with hi or hello. Remember don't add extra context or any rules in your response.")
        
        try:
            response = response.split("$@$")[1]
            response = response.lower()
            
            if ("blackbox" in response):
                response = response.replace("blackbox", "Jareb")
                
                return response
        except:
            return response
        

    # recieve IMAGEs..
    elif ("send me" in user and "picture" or "image" in user or "send" and "picture" or "image" in user or "show me" and "picture" or "image" in user):
        response = "Jareb is under development to send images"
        return response

    else:
        return generateResponse_BB(user)


   