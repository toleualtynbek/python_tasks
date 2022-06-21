import time
import colorama
from colorama import Fore

colorama.init()

class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            a = self.__color
            b=' '
            for i in a:
                if i == 'red':
                    print(Fore.RED + f'{i}', end='')
                    time.sleep(7)
                    print(f'{b}\r', end='',)
                elif i == 'yellow':
                    print(Fore.YELLOW + f'{i}', end='')
                    time.sleep(2)
                    print(f'{b}\r', end='', )
                else:
                    print(Fore.GREEN + f'{i}', end='')
                    time.sleep(5)
                    print(f'{b}\r', end='', )

tl = TrafficLight()
tl.running()
