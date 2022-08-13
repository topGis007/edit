import telnyx
import os
import platform
import json
from datetime import datetime
import time


# TODO: add randomizer functions (token, number)
# TODO: add timeout each count
# TODO: check if apiKey alive first


fg = [
    '\033[91;1m', #RED     0
    '\033[92;1m', #GREEN   1
    '\033[93;1m', #YELLOW  2
    '\033[94;1m', #BLUE    3
    '\033[95;1m', #MAGENTA 4
    '\033[96;1m', #CYAN    5
    '\033[97;1m'  #WHITE   6
]

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def banner():
    print(f'''\n{fg[0]}    ╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔╦╗╔═╗╦═╗
    ╚═╗║║║╚═╗  ╚═╗║╣ ║║║ ║║║╣ ╠╦╝
    ╚═╝╩ ╩╚═╝  ╚═╝╚═╝╝╚╝═╩╝╚═╝╩╚═
           {fg[3]}More Tools : {fg[1]}-->>> https://t.me/hackingtoolsprvi8\n''')

def settings():
    global config
    if not os.path.isfile('settings.json'):
        config = {'apiKey': 'KEY0181640953FE68A6E09F3936E7AFEC73_hwsDn1cLF1ERxRmjeS1iyo',
                  'profileId': 'info',
                  'senderId': 'INFO',
                  'message': 'TESTING MODE',
                  'count': 10,
                  'timeout': 60}
        with open('settings.json', 'w+') as json_file:
            json.dump(config, json_file, indent=4)
    else:
        with open('settings.json', encoding='utf-8') as json_file:
            config = json.load(json_file)

def main():
    ncount = 1
    tcount = 0
    try:
        numbers =  open('numbers.txt', mode='r', encoding='utf-8').readlines()
        total_numbers = len(numbers)
        for number in numbers:
            number = number.strip()
            if number == '':
                continue
            # print(telnyx.Balance.retrieve())
            telnyx.api_key = config['apiKey']
            telnyx.Message.create(
            from_= str(config['senderId']),
            to=number,
            text=str(config['message']),
            messaging_profile_id=str(config['profileId'])
            )
            print(f'\t{fg[5]}[{fg[4]}{datetime.now().strftime("%H:%M:%S")}{fg[5]}]╾╼[{fg[0]}{ncount}{fg[5]}/{fg[0]}{total_numbers}{fg[5]}]╾╼[{fg[1]}SENT{fg[5]}]╾╼[{fg[3]}{config["senderId"]}{fg[5]}]╾╼[{fg[2]}{number}{fg[5]}]') #? time - status - sender name - number
            ncount += 1
            tcount += 1
            if tcount == config['count']:
                print(f'\t{fg[0]}• {fg[1]}Timeout for {fg[0]}{config["timeout"]} {fg[1]}seconds...')
                time.sleep(config['timeout'])
                tcount = 0
    except Exception as err:
        print(f'{fg[5]}[{fg[4]}{datetime.now().strftime("%H:%M:%S")}{fg[5]}]╾╼[{fg[0]}FAIL{fg[5]}]╾╼[{fg[3]}{config["senderId"]}{fg[5]}]╾╼[{fg[2]}{number}{fg[5]}]') #? time - status - sender name - number
        print(err)


if __name__ == '__main__':
    try:
        clear()
        banner()
        settings()
        main()
    except KeyboardInterrupt:
        exit()
