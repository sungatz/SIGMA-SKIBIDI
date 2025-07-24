import time
class Detroit:
    def __init__(s, name, health, power, lvl):
        s.name = name
        s.health = int(health)
        s.power = int(power)
        s.lvl = int(lvl)
        if s.health > 100:
            s.health = 100
    def attack(bro, target):
        if bro.health <= 20:
            print('get the hell, you weak')
        elif 20 < bro.health :
            target.hp -= bro.power * bro.lvl
            target.canAttack = True
            target.counter -= 5
class MiniDetroit:
    def __init__(self, name, hp, canAttack, counter):
        self.name = name
        self.hp = int(hp)
        self.canAttack = canAttack
        self.counter = int(counter)
        self.isDead = False
        self.mood = None  
        self.update_state()
    def update_state(self):
        if self.hp <= 0:
            self.isDead = True
        if self.counter > 10:
            self.counter = 10
            self.mood = "veryAngry"
        elif self.counter in (8, 9):
            self.mood = "angry"
        elif self.counter == 7:
            self.mood = "placebo"
        else:
            self.mood = "kind"
    def attack(self, myTarget):
        if self.canAttack is not False:
            myTarget.health -= 10
        else:
            print("you can't")
a = (input('напиши что то в формате: Андрейка, 45, 2, 1').strip().split(','))
ab = Detroit(*a)
b = (input('а теперь: Сигма, 100, True, 3').strip().split(','))
bb = MiniDetroit(*b)

print(f'{a.name} пришел на миссию. Ему надо войти в доверие {b.name} а затем убить и развалить его компанию.')
time.sleep(3)
print(f'{a.name} увидел его. Твои действия: \n1.Подойти \n2.Крикнуть его имя\n3. Превратиться В КРУТОСА и выстрелить ему в спину')
c = str(input('Что ты выбрал?)'))
mood_reactions = {
    'veryAngry': 'Он тебя послал, лол',
    'angry':     'Он тебя послал, лол',
    'placebo':   'ОН МОЛЧИТ.',
    'kind':      'Он знакомится. Но не с тобой(ладно, шутка).'
}
if c in ['1', '1.', 'Подойти', 'Первое']:
    print(mood_reactions.get(b.mood, 'Ну крч ты все сломал и игра сдохла.'))
else:
    print('SUDO BAN')
if c in ['2', '2.', 'Крикнуть', 'Орать']:
    print('ну ты сломал. Он ушел крч. Заново делай, жопорук')
if c in ['3', '3.', 'КРУТОС']:
    print('+1000000000000000 aura, SIGMA')