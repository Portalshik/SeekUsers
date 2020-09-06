import requests
import os
from termcolor import colored
from jpg import jpg

os.system("clear")

print(colored(jpg, "blue"))

name = input(colored('User name: ', "green"))
save = input("Save it? [y/n]: ")

inst = ['https://www.instagram.com/' + name, "Instagram"]
vk = ['https://vk.com/' + name, "Vk"]
fb = ['https://www.facebook.com/' + name, "Facebook"]
yout = ['https://www.youtube.com/' + name, "YouTube"]
gh = ['https://www.github.com/' + name, "GitHub"]

sites = [inst, vk, fb, yout, gh]

site = int(len(sites))
for i in range(site):
    name_s = sites[i][1]
    r = requests.get(sites[i][0])
    if r.status_code == 200:
        print(colored(f"{name_s}: Found! ({sites[i][0]})", "green"))
        if save == 'y':
            file = open(f'{name}.txt', 'a')
            file.write(f"{sites[i][0]}\n")
            file.close()
    else:
        print(colored(f'{name_s}: Not Found!', "red"))
if save == "y":
    print(f"Save in {name}.txt")
