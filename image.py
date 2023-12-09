from colorama import init
from colorama import Fore, Back, Style

init()

def printImage():
          fox = """
                __________________
               | Debug your app,  |
               | or I've done it!\033[0;0m |
                ==================
                         \                            \033[38;5;208m,'|
                          \033[0;0m\\\033[38;5;208m      /\/\                |  |
    		            o--'O   |               /   |
                             `--.    `----------._,'   ,'
                  /              \              ,-----'
                 //\              ) )    _,--(  |
                (o\              /,^.---'     )/\\\\
                 ) \	        ((   \\\      ((  \\\\
                (___()           \)   \)      \) (/                     """

          txt = """                                                    
  ▀██▀▀▀▀█  ▄▄█▀▀██   ▀██▀ ▀█▀ ▀██▀  ▀██▀ ▀██▀  ▀█▀ ▀█▄   ▀█▀ █▀▀██▀▀█ 
   ██  ▄   ▄█▀    ██    ██ █    ██    ██   ██    █   █▀█   █     ██    
   ██▀▀█   ██      ██    ██     ██▀▀▀▀██   ██    █   █ ▀█▄ █     ██    
   ██      ▀█▄     ██   █ ██    ██    ██   ██    █   █   ███     ██    
  ▄██▄      ▀▀█▄▄▄█▀  ▄█   ██▄ ▄██▄  ▄██▄   ▀█▄▄▀   ▄█▄   ▀█    ▄██▄                          
                         
      \033[0;0mWelcome to Foxhunt utility! It is a simple compiler capable
of creating applications for Android or iOS and based on Cython and Java"""
              
          print(fox)
          print(Fore.LIGHTYELLOW_EX, txt, Style.BRIGHT)
          print(Fore.WHITE, Style.BRIGHT)
