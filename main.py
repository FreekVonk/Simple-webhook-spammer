try:
    import time
    import os
    from dhooks import Webhook
    import fade
    import colorama
    import webbrowser
    from colorama import Fore
    import keyboard

except ModuleNotFoundError:
    print("Module not found error... Installing ALL Requirements!")
    os.system("pip install requests")
    os.system("pip install dhooks")
    os.system("pip install colorama")
    os.system("pip install fade")
    os.system("pip install keyboard")
    os.system("pip install webbrowser")

text = fade.purplepink("""
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝███████║██╔████╔██║
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
                                                                                                   
""")

colorama.init(autoreset=True)
print(text)

webbrowser.open("https://discord.gg/kHjH7RbYbF")
# system
os.system("title Made by Freek! / @qixvii.exe")
#prompt
webhookurl = Webhook(input(Fore.CYAN +"Enter the webhook url: "))
message = input(Fore.RED + "What do you wanna spam?: ")
delay = int(input( Fore.GREEN +"Enter a delay: "))
button_to_stop = input(Fore.RED+'What would you like to hold to stop webhook spam? (EG: F9): ')

while True:
    time.sleep(delay)
    webhookurl.send(message)
    print(f"{Fore.RED}[X] Sent Message: {Fore.MAGENTA}{message} [X]")
    if keyboard.is_pressed(button_to_stop):
        quit()
