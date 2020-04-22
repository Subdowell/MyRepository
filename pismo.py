

def gift_children(name,children):
    children_gift = ["1)Велосипед " , " 2)Носки " , " 3)Машинка на радиоуправлении " , " 4)Кукла " , " 5)Уран 235 " , " 6)Футбольный мяч. "]
    if children == True:
        print("Тогда", name, ", ты можешь выбрать 1 подарок из списка!")
        print(",".join(children_gift))
        gift = int(input("Введи номер подарка, который тебе по вкусу!:"))
        if gift == 1:
            print("Ты получаешь подарок!", children_gift[0])
        elif gift == 2:
            print("Ты получаешь подарок!", children_gift[1])
        elif gift == 3:
            print("Ты получаешь подарок!", children_gift[2])
        elif gift == 4:
            print("Ты получаешь подарок!", children_gift[3])
        elif gift == 5:
            print("Ты получаешь подарок!", children_gift[4])
        elif gift == 6:
            print("Ты получаешь подарок!", children_gift[5])
        else:
            print("Жаль, ты не получаешь подарка, так как не ввел номер подарка! :(")
    else:
        print(f"Извини {name}, ты плохо себя вёл, подарка ты не получишь! :(")
def behavior_check():
    name = input("Здравствуй мой дорогой друг, назови свое имя:")
    children_good = input("Ты хорошо себя вёл в этом году? Y/N:")
    if children_good == "Y":
        children_good = True
    else:
        children_good = False
    x = gift_children(name=name, children=children_good)
def save_txt(name)
    file=open("letter.txt",'w')

d = behavior_check()



