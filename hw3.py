import random
secret = random.randint(1, 10)
for i in range(3):
    guess = int(input("Вгадайте число (1-10): "))
    if guess == secret:
        print("Ви вгадали!")
        break
    print("Більше" if guess < secret else "Менше")
else:
    print(f"Спроби вичерпано. Число було: {secret}")