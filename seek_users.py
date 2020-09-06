import requests
import os
from termcolor import colored
from jpg import jpg

os.system("clear")

print(colored(jpg, "blue"))

name = input(colored('User name: ', "green"))
save = input("Save it? [y/n]: ")

inst = 'https://www.instagram.com/' + name
vk = 'https://vk.com/' + name
fb = 'https://www.facebook.com/' + name
yout ='https://www.youtube.com/' + name
gh = 'https://www.github.com/' + name

sites = [inst, vk, fb, yout, gh]

site = int(len(sites))
for i in range(site):
    if i == 0:
        name_s = "Insragram"
    elif i == 1:
        name_s = "Vk"
    elif i == 2:
        name_s = "Facebook"
    elif i == 3:
        name_s = "YouTube"
    elif i == 4:
        name_s = "GitHub"
    r = requests.get(sites[i])
    if r.status_code == 200:
        print(colored(f"{name_s}: Found! ({sites[i]})", "green"))
        if save == 'y':
            file = open(f'{name}.txt', 'a')
            file.write(f"{sites[i]}\n")
            file.close()
    else:
        print(colored(f'{name_s}: Not Found!', "red"))
if save == "y":
    print(f"Save in {name}.txt")
