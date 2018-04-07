import requests
import json
from colorama import init
from colorama import Fore, Back, Style
init()

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'If-None-Match': '"MnhlSMUKPPVW1gPfswixCrrWB9Y="',
}

print(Fore.RED + "=================================================================")
print(Fore.CYAN + "                     Supreme ID Scraper")
print(Fore.CYAN + "                     made by @greysonhur")
print(Fore.RED + "=================================================================")

s = requests.session()

def scrape():

    response = requests.get('http://www.supremenewyork.com/shop.json', headers=headers)
    a = json.loads(response.text)

    products = a['products_and_categories']

    fname = input("What do you want the file to be named? (eg. 'pids')\n")
    print(Fore.CYAN + "Scraping...")
    print(Fore.WHITE)

    f = open('{}.txt'.format(fname),"w")
    f.truncate()

    for product in products['new']:
        pid = product['id']
        pname = product['name']
        pcategory = product['category_name']
        f.write(str(pid) + "\n")
        print(str(pid) + " - "+ str(pname) + " - " + str(pcategory))

    print(Fore.GREEN + "Successfully grabbed product ID's")
    print(Fore.GREEN + "Check the directory for the .txt file ;")
    print(Fore.CYAN + "HMU On twitter https://twitter.com/greysonhur")
