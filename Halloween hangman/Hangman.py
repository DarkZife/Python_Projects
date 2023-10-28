import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

# Sets up our screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Loads our Halloween words
with open("Halloween_hangman.txt", "r") as file:
    words = file.read().splitlines()

# Chooses a Random word from our Halloween list
word = random.choice(words).upper()
guessed_letters = set()

# Loading Halloween images
hangman_images = [pygame.image.load(f"hangman{i}.png") for i in range(7)]
current_image = 0

# Fonts
font = pygame.font.Font(None, FONT_SIZE)

# Game variables
correct_guesses = 0
max_attempts = len(hangman_images) - 1



# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key >= 97 and event.key <= 122:
            letter = chr(event.key).upper()
            if letter not in guessed_letters:
                guessed_letters.add(letter)
                if letter in word:
                    correct_guesses += word.count(letter)
                else:
                    current_image += 1

    # Clear the screen
    screen.fill(WHITE)
    

    # This is the display of the underscores for how many letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_ "
    text = font.render(display_word, True, BLACK)
    screen.blit(text, (50, 50))

    # This puts in our halloween_hangman image
    if current_image < len(hangman_images):
        screen.blit(hangman_images[current_image], (400, 100))

    # Check to see if guessed correct or not
    if len(set(guessed_letters) & set(word)) == len(set(word)):
        text = font.render("YOU WIN, HAVE A HAPPY HALLOWEEN!", True, BLACK)
        screen.blit(text, (350, 300))
    elif current_image >= max_attempts:
        text = font.render("BOO! The word was: " + word, True, BLACK)
        screen.blit(text, (200, 300))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
