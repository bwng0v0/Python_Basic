class player:
    def __init__(self,name,hp,ad):
        self.name = name
        self.hp = hp
        self.ad = ad
    
    def attack(self,target):
        target.hp -= self.ad
        print(f"{self.name} -attack-> {target.name}")
        if target.hp <= 0:
            print(f"<{self.name}> killed {target.name}")
        else:
            print(f"{target.hp}/100")
        

class job_player(player):
    def __init__(self, name, hp, ad):
        super().__init__(name, hp, ad)


p1 = player("민기",100,25)
p2 = player("진수",100,23)

while 1:
    n = int(input())
    if n == 1:
        p1.attack(p2)
    else:
        p2.attack(p1)