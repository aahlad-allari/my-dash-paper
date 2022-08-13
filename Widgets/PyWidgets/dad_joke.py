import os
import requests
import random

JOKE_URL = "https://raw.githubusercontent.com/wesbos/dad-jokes/master/readme.md"
class DAD_JOKE():
    def __init__(self,root_dir="./"):
        self.root_dir = root_dir

    def get_content(self):
        f = requests.get(JOKE_URL)
        content = f.text
        jokes = content.split("---")[2:]
        return jokes
    
    def shoot(self):
        jokes = self.get_content()
        rand_index = random.randint(0,len(jokes))
        joke = jokes[rand_index]
        joke = joke.replace('\n\n','\n')
        joke = joke.replace('**',' ')
        return joke
