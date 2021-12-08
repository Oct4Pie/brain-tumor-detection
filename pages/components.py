import os

print(os.getcwd())
def title():
    return open("pages/componenets/title.html", "r").read()

def github_iframe():
    return open("pages/componenets/github_iframe.html", "r").read()

def github_card():
    return open("pages/componenets/github_card.html", "r").read()