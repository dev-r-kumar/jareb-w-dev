from bs4 import BeautifulSoup as bs
import requests

fetch_of = ""

res = requests.get(f"https://www.google.com/search?q={fetch_of}&sca_esv=32288416509471f0&sca_upv=1&tbm=isch&sxsrf=ADLYWIK4tuRNQNFyhhqeZpvK3RgTo6vu1A%3A1715305106025&source=hp&biw=1278&bih=937&ei=kXo9ZuPPPKni2roPjNuXiAE&iflsig=AL9hbdgAAAAAZj2IolBZzxtF2nOhEdqtMshVWUsqjKwG&ved=0ahUKEwij3Ji8-YGGAxUpsVYBHYztBREQ4dUDCA8&uact=5&oq=car&gs_lp=EgNpbWcaAhgDIgNjYXIyBBAjGCcyCBAAGIAEGIsDMggQABiABBiLAzIIEAAYgAQYiwMyCBAAGIAEGIsDMggQABiABBiLAzIIEAAYgAQYiwMyCBAAGIAEGIsDMggQABiABBiLAzIIEAAYgAQYiwNIpBBQ7gdYpQtwAXgAkAEAmAGSAqABjQaqAQMyLTO4AQPIAQD4AQGKAgtnd3Mtd2l6LWltZ5gCBKACpwaoAgrCAgcQIxgnGOoCmAMNkgcFMS4wLjOgB90S&sclient=img")


soup = bs(res.content, "html.parser")

print(soup)