#This is a teacher led demo.
#Watch this video or follow along in class.


def AddTwoNumbers(number1, number2):
    result = number1 + number2
    return result

def HelloTen():
    for _ in range(10):
        print("hello")

def CheckHit(HitTarget, DiceRoll):
    HitResult = False
    if DiceRoll >= HitTarget:
        print("That is a hit!")
        HitResult = True
    else:
        print("That is a miss!")
        HitResult = False
    return HitResult

x =  5
y = 10

result = AddTwoNumbers(x,y)

HelloTen()

print(result)

print(CheckHit(5,10))
print()
print(CheckHit(10,5))