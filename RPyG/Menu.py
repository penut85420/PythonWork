class Menu:
    def __init__(self, menuItems, menuAllow=None):
        if not menuAllow:
            self.allow = [True] * len(menuItems)
        else: self.allow = menuAllow
        self.items = menuItems
    
    def show(self):
        for i, s in enumerate(self.items):
            if self.allow[i]: print(s)
        print(end=' > ')

class MainMenu(Menu):
    def __init__(self):
        items = [
            '[N] 開始遊戲',
            '[C] 繼續遊戲',
            '[S] 系統設定',
            '[G] 離開遊戲',
        ]
        Menu.__init__(self, items)
    
if __name__ == "__main__":
    ss = ['[A] Apple', '[B] Banana', '[C] Candy']
    m = Menu(ss)
    m.show()
    print()
    m = Menu(ss, [True, False, True])
    m.show()
    print()
    m = MainMenu()
    m.show()