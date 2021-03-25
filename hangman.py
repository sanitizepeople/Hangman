import random 
import time
from typing import Counter

# Awal masuk game
print("\n Selamat datang di permainan Hangman\n")
name = input("Masukkan nama kamu:")
print("Halo " + name + " Semoga beruntung!" )
time.sleep(2)
print("Permainannya akan dimulai!\n Ayo main!")
time.sleep(3)

def main(): 
  global count 
  global display
  global word
  global already_guessed
  global length
  global play_game
  words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
  word = random.choice(words_to_guess)
  length = len(word)
  count = 0
  display = '_' * length
  already_guessed = []
  play_game = ""

def play_loop():
  global play_game
  play_game = input("Mau main lagi gak? y = iya, n = tidak \n")
  while play_game not in ["y","n","Y","N"]:
    play_game = input("Mau main lagi gak? y = iya, n = tidak \n")
  if play_game == "y":
    main()
  elif play_game == "n":
    print("Terima kasih sudah bermain! kita harap kamu kembali lagi")
    exit()

def hangman():
  global count
  global display
  global word
  global already_guessed
  global play_game
  limit = 5
  guess = input("Ini kata hangman: " + display + " Masukkan tebakanmu: \n")
  guess = guess.strip()
  if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
    print("Salah, coba kata yang lain\n")
    hangman()

  elif guess in word:
    already_guessed.extend([guess])
    index = word.find(guess)
    word = word[:index] + "_" + word[index + 1:]
    display = display[:index] + guess + display[index + 1:]
    print(display + "\n")

  elif guess in already_guessed:
     print("Coba kata lain.\n")

  else:
      count += 1
      if count == 1:
        time.sleep(1)
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Masih salah " + "sisa " + str(limit - count) + " tebakan lagi\n")
      elif count == 2:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Masih salah " + "sisa " + str(limit - count) + "tebakan lagi\n")
      elif count == 3:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Masih salah " + "sisa " + str(limit - count) + " tebakan lagi\n")
      elif count == 4:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Masih salah " + "sisa " + str(limit - count) + " tebakan lagi\n")
      elif count == 5:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")
        print("Masih salah. Kamu digantung!!!\n")
        print("Katanya adalah: ",already_guessed,word)
        play_loop()
  if word == '_' * length:
    print("Selamat! Kamu telah menebak katanya dengan benar!")
    play_loop()
  elif count != limit:
    hangman()

main()

hangman()