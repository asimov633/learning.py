
import time
print("""
    Kill The Enemey
    """)
class Enemy:
    enemy_healt=int(input("Enter Enemy Health: "))

    def attack(self):
        print("1 was attack on enemy")
        self.enemy_healt=self.enemy_healt-1
    def swordattack(self):
        print("2 was attack on enemy")
        self.enemy_healt=self.enemy_healt-2
    def enemyinlifeornot(self):
        if self.enemy_healt>0:
            print("{}-has healt on enemy he is alive".format(self.enemy_healt))
        else:
            print("Enemy was dead...")

print("Welcome To The Game...")
time.sleep(2)
print("You Can Attack when entering enemy healt...")
time.sleep(2)
print("Attack commands could be (attack or swordattack)...")
time.sleep(2)
print("After Attack you can learn enemy in alive or not...")
time.sleep(2)
print("Game Starting...")
time.sleep(5)

enemy1=Enemy()
attacking=int(input("How Much Attack: "))
swordattacking=int(input("How Much Sword Attack: "))

i=1
a=1
while i<=attacking:
    enemy1.attack()
    i=i+1
while a<=swordattacking:
    enemy1.swordattack()
    a=a+1
print("Attack is done are you wanna know enemy is alive or not ")

answer=input("Answer: ")

if answer.lower()=="yes":
    enemy1.enemyinlifeornot()
elif answer.lower()=="not":
    print("Not Have About Enemy...")
else:
    print("Please Entering (yes or not)...")
