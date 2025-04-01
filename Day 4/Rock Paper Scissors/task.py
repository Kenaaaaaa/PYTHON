import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand=[rock,paper,scissors]


choice=int(input(f"Choose 0 for {"rock"} , choose 1 for {"paper"} , choose 2 for {"scissors"} "))
print(hand[choice])

computer_choice=print(hand[random.randint()])
