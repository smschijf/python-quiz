from operator import truediv
from urllib import response


def new_game():
  guesses = []
  correct_guesses = 0
  question_num = 1

  for key in questions:
    print("-----------------")
    print(key)
    for i in options[question_num-1]:
      print(i)
    guess = input("Enter (A, B or C):")
    guess = guess.upper()
    guesses.append(guess)

    correct_guesses += check_answer(questions.get(key),guess)
    question_num += 1

  display_score(correct_guesses, guesses)
# ------------
def check_answer(answer, guess):
  if answer == guess:
    print("Correct")
    return 1
  else:
    print("Wrong")
    return 0
# ------------
def display_score(correct_guesses, guesses):
  print("-----------------")
  print("Results")
  print("-----------------")
  
  print("Answers: ", end="")
  for i in questions:
    print(questions.get(i), end=" ")
  print()

  print("Guesses: ", end="")
  for i in guesses:
    print(i, end=" ")
  print()

  score = int((correct_guesses/len(questions))*100)
  print("Your score is "+str(score)+"%")
#-------------
def play_again():
  response = input("Do you want to play again? (yes or no): ")
  response = response.upper()

  if response == "YES":
    return True
  else:
    return False
#-------------
questions = {
  "What's the name of the intelligence agency Twilight works for?":"A",
  "Twilight's mission is to prevent war between which two nations?":"A",
  "What's the name of Twilight's target who is considered a threat to the truce between the East and the West?":"C",
  "What's the name of Twilight’s mission?":"B",
  "OK here's an easy one: What ability does Anya possess?":"A",
  "Yor Briar is a ruthless assassin but what's her code name?":"C",
  "Where did Loid meet Yor before creating their fake family?":"A",
  "What's the name of the prestigious school Anya must attend?":"C",
  "Who punched Mr. Swan after he made Anya cry in the school's interview?":"C",
  "What's the name of the Handler?":"A"
}

options = [["A. WISE", "B. OSTI", "C. SEIP"],
          ["A. Westalis and Ostania", "B. Wymal and Ostamia", "C. Oldania and Wegeris"],
          ["A. Ronovan Monson", "B. Donald Cosmos", "C. Donovan Desmond"],
          ["A. Operation swift", "B. Operation Strix", "C. Operation dawn"],
          ["A. Telepathy", "B. Levitation", "C. Precognition"],
          ["A. Lady Thorn", "B. Swan Princess", "C. Thorn Princess"],
          ["A. Tailor shop", "B. Party", "C. Grocery store"],
          ["A. Berlint College", "B. Ostania College", "C. Eden College"],
          ["A. Yor", "B. Loid", "C. Henry"],
          ["A. Sylvia Sherwood", "B. Cecelia Charwood", "C. Sylvia Underwood"]]

new_game()

while play_again():
  new_game()

print ("bye!")