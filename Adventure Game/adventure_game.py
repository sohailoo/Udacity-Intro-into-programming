import time
import random


def delay_print(msg):
    print(msg)
    time.sleep(2)


def starting_msg(weapon, choice):
    delay_print(f"You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    delay_print(f"Rumor has it that a {choice} is somewhere around "
                "here, and has been terrifying the nearby village.")
    delay_print("In front of you is a house.")
    delay_print("To your right is a dark cave.")
    delay_print("In your hand you hold your trusty"
                " (but not very effective) dagger.")


def in_cave(weapon, choice):
    if "sword" in weapon:
        delay_print("You peer cautiously into the cave.")
        delay_print(
            "You've been here before, and gotten all"
            " the good stuff. It's just an empty cave"
            " now."
        )
        delay_print("You walk back to the field.")
    else:
        delay_print("You peer cautiously into the cave.")
        delay_print("It turns out to be only a very small cave.")
        delay_print("Your eye catches a glint of metal behind a " "rock.")
        delay_print("You have found the magical" " Sword of Ogoroth!")
        delay_print("You discard your silly old "
                    "dagger and take the sword with you.")
        delay_print("You walk back out to the field.")
        weapon.append("sword")
    first_choice(weapon, choice)


def in_house(weapon, choice):
    delay_print("You approach the door of the house.")
    delay_print(f"You are about to knock when the "
                f"door opens and out steps a {choice}.")
    delay_print(f"Eep! This is the {choice}'s house!")
    delay_print(f"The {choice} attacks you!")
    if "sword" not in weapon:
        delay_print(
            "You feel a bit under-prepared for this, "
            "what with only having a tiny dagger."
        )
    while True:
        choice2 = input("Would you like to (1) fight or (2) " "run away?")
        if choice2 == "1":
            if "sword" in weapon:
                delay_print(
                    f"As the {choice} moves to attack, "
                    "you unsheath your new sword."
                )
                delay_print(
                    "The Sword of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the "
                    "attack."
                )
                delay_print(
                    f"But the {choice} takes one look at "
                    "your shiny new toy and runs away!"
                )
                delay_print(
                    f"You have rid the town of the"
                    f" {choice}. You are victorious!"
                )
            else:
                delay_print("You do your best...")
                delay_print(f"but your dagger is no match for the {choice}.")
                delay_print("You have been defeated!")
            replay()
            break
        if choice2 == "2":
            delay_print(
                "You run back into the field. "
                "Luckily, you don't seem to have been "
                "followed."
            )
            first_choice(weapon, choice)
            break


def first_choice(item, option):
    delay_print("Enter 1 to knock on the door of the house.")
    delay_print("Enter 2 to peer into the cave.")
    delay_print("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)")
        if choice1 == "1":
            in_house(item, option)
            break
        elif choice1 == "2":
            in_cave(item, option)
            break


def replay():
    play_again = input("Would you like to play again? (y/n)").lower()
    if play_again == "y":
        delay_print("Excellent! Restarting the game ...")
        play()
    elif play_again == "n":
        delay_print("Thanks for playing! See you next time.")
    else:
        replay()


def play():
    weapon = []
    choice = random.choice(["wicked fairie", "pirate",
                            "dragon", "troll", "gorgon"])
    starting_msg(weapon, choice)
    first_choice(weapon, choice)


play()
