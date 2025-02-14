import random
import turtle

def get_word():
  randnum = random.randint(1, 10)
  line_number = 1
  with open("words.txt") as file:
    for line in file:
      line_number += 1
      if line_number == randnum:
        return line.strip()
def draw_gallows():
  # draw gallows
  t.speed(3)
  t.penup()
  t.goto(-60, -90)
  t.pendown()
  t.goto(-140, -90)
  t.goto(-100, -90)
  t.goto(-100, 110)
  t.goto(0, 110)
  t.goto(0, 60) 
  t.speed(1)
def draw_hangman(guesses_left):
  guesses = abs(guesses_left - 6)
  if guesses == 1:
    # draw head
    t.setheading(180)
    t.circle(20)
    t.penup()
  elif guesses == 2:
    # draw torso
    t.goto(0, 20)
    t.pendown()
    t.goto(0, -20)
  elif guesses == 3:
    # draw left arm
    t.goto(0, 10)
    t.goto(-20, -20)
  elif guesses == 4:
    # draw right arm
    t.goto(0, 10)
    t.goto(20, -20)
    t.penup()
  elif guesses == 5:
    # draw left leg
    t.goto(0, -20)
    t.pendown()
    t.goto(-20, -50)
  elif guesses == 6:
    # draw right leg
    t.goto(0, -20)
    t.goto(20, -50)
def check_letter(letter):
  if letter in word_to_guess:
    count = word_to_guess.count(letter)
    if count == 1:
      index = word_to_guess.index(letter)
      correct_guesses[index] = letter
    else:
      word = word_to_guess
      for i in range(count):
        index = word.index(letter) + (len(word_to_guess) - len(word))
        correct_guesses[index] = letter
        word = word[index + 1:]
def play_game():
  global word_to_guess
  global correct_guesses
  t.clear()
  word_to_guess = get_word()
  draw_gallows()
  guesses_left = 6
  incorrect_guesses = []
  correct_guesses = []
  for char in word_to_guess:
    correct_guesses.append("_")
  while guesses_left != 0 and ''.join(correct_guesses) != word_to_guess:
    print(f"\nNot in word: {incorrect_guesses}")
    print(f"Word: {correct_guesses}")
    guess = input("Guess a letter: ")
    if guess in word_to_guess:
      print("Correct! You have", guesses_left, "guesses left.")
      check_letter(guess)
    else:
      if guess not in incorrect_guesses:
        guesses_left -= 1
        incorrect_guesses.append(guess)
        print("Incorrect. You have", guesses_left, "guesses left.")
        draw_hangman(guesses_left)
      else:
        print(f"You already guessed {guess}.  Try again.")

  if guesses_left == 0:
    print("\nYou lose! The word was", word_to_guess)
  else:
    print("\nYou win! The word was", word_to_guess)
  next_game = input("Would you like to play again? (y/n) ")
  return next_game == "y"

t = turtle.Turtle()
t.hideturtle()


while True:
  if not play_game():
    break;
t.clear()
print("Goodbye! Thanks for playing!")