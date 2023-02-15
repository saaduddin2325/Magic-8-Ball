import random
name = "Saad"
question = "Will I become rich?"
answer = ""
random_number = random.randint(1,9)
print(random_number)
if name == "":
  print(question)
elif question == "":
  print("Please ask a question")
else: print(name + " asks: " + question)
if random_number == 1:   
  answer = "Yes - definitely" 
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Reply hazy, try again."
elif random_number == 4:
  answer = "Ask again later."
elif random_number == 5:
  answer = "Better not tell you now."
elif random_number == 6:
  answer = "My sources say no."
elif random_number == 7:
  answer = "Outlook not so good."
elif random_number == 8:
  answer = "Very doubtful."
elif random_number == 9:
  answer = "Without a doubt."
print("Magic eight ball's answer:" + answer)