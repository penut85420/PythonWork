import threading
import time

class Player:
    def __init__(self):
        self.HP = 300
        self.MaxHP = 300
        self.GenHP = 3
    
    def damage(self, n):
        self.HP -= n
    
    def heal(self, n):
        self.HP += n
        if self.HP > self.MaxHP:
            self.HP = self.MaxHP

    def period_heal(self):
        while True:
            self.heal(self.GenHP)
            time.sleep(1)
    
    def show(self):
        print('HP:', self.HP)

if __name__ == "__main__":
    p = Player()
    p.show()

    threading.Thread(target=p.period_heal).start()

    while True:
        a = input()
        print('Cmd:', a)
        if a == 'd':
            p.damage(100)
        elif a == 'l':
            p.show()