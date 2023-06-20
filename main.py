import colorama
import requests
import time
from colorama import Fore
colorama.init()

print(" ")
print(Fore.YELLOW + "  ██╗     ██╗   ██╗██████╗ ██╗ █████╗    ██████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ ")
print(Fore.LIGHTYELLOW_EX + "  ██║     ╚██╗ ██╔╝██╔══██╗██║██╔══██╗  ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗")
print(Fore.WHITE + "  ██║      ╚████╔╝ ██████╔╝██║██║  ╚═╝  ╚█████╗ ██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝")
print(Fore.CYAN + "  ██║       ╚██╔╝  ██╔══██╗██║██║  ██╗   ╚═══██╗██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗")
print(Fore.BLUE + "  ███████╗   ██║   ██║  ██║██║╚█████╔╝  ██████╔╝██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║")
print("  ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚════╝   ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝")
print(Fore.CYAN + "  By jameshulk4#2555")
print(" ")
webhook_url = input(Fore.GREEN + "Discord Webhook URL: ")
print(" ")

delay = 0.5


def send_discord_webhook(url, message):
    data = {
        'content': message
    }

    response = requests.post(url, json=data)

    if response.status_code == 204:
        print('Sent Text: "' + line + '"')
    else:
        print(f'Failed to send message. Error: {response.status_code}')


# Aqua - Barbie Girl
line = "# @everyone Hiya, Barbie"
send_discord_webhook(webhook_url, line)
line = "# @everyone Hi, Ken"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone You want to go for a ride?"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Sure, Ken"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Jump in"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone I'm a Barbie girl, in the Barbie world"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Life in plastic, it's fantastic"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone You can brush my hair, undress me everywhere"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Imagination, life is your creation"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone I'm a blonde bimbo girl in a fantasy world"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Dress me up, make it tight, I'm your dolly"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone You're my doll, rock'n'roll, feel the glamour in pink"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Kiss me here, touch me there, hanky panky"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone You can touch"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone You can play"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone If you say, \"I'm always yours\" (ooh, oh)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone I'm a Barbie girl, in the Barbie world"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Life in plastic, it's fantastic"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone You can brush my hair, undress me everywhere"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Imagination, life is your creation"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come on, Barbie, let's go party (ah ah ah yeah)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come on, Barbie, let's go party (ooh oh, ooh oh)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come on, Barbie, let's go party (ah ah ah yeah)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come on, Barbie, let's go party (ooh oh, ooh oh)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Make me walk, make me talk, do whatever you please"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone I can act like a star, I can beg on my knees"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come jump in, bimbo friend, let us do it again"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Hit the town, fool around, let's go party"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone You can touch"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone You can play"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone If you say, \"I'm always yours\""
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone You can touch"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone You can play"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone If you say, \"I'm always yours\""
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come on, Barbie, let's go party (ah ah ah yeah)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come on, Barbie, let's go party (ooh oh, ooh oh)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come on, Barbie, let's go party (ah ah ah yeah)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come on, Barbie, let's go party (ooh oh, ooh oh)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone I'm a Barbie girl, in the Barbie world"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Life in plastic, it's fantastic"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone You can brush my hair, undress me everywhere"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Imagination, life is your creation"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone I'm a Barbie girl, in the Barbie world"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Life in plastic, it's fantastic"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone You can brush my hair, undress me everywhere"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Imagination, life is your creation"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come on, Barbie, let's go party (ah ah ah yeah)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come on, Barbie, let's go party (ooh oh, ooh oh)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come on, Barbie, let's go party (ah ah ah yeah)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Come on, Barbie, let's go party (ooh oh, ooh oh)"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Oh, I'm having so much fun"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Well, Barbie, we're just getting started"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
line = "# @everyone Oh, I love you, Ken"
time.sleep(delay)
send_discord_webhook(webhook_url, line)
