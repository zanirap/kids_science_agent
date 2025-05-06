import random

science_facts = [
    "Did you know that the Eiffel Tower can be about 15 cm taller during the summer due to thermal expansion?",
    "Did you know that a teaspoonful of a neutron star would weigh about 6 billion tons?",
    "Did you know that the fastest spinning planet in our solar system is Jupiter?",
    "Did you know that bamboo can grow up to 91 cm (3 feet) in 24 hours?",
    "Did you know that the average person walks the equivalent of five times around the Earth in their lifetime?",
    "Did you know that sound travels about 4 times faster in water than in air?",
    "Did you know that there are more trees on Earth than stars in the Milky Way galaxy?",
    "Did you know that your brain uses about 20% of your body's total oxygen and calorie intake?",
    "Did you know that honey never spoils?",
    "Did you know that the Earth's atmosphere has several layers?",
    "Did you know that lightning strikes the Earth about 100 times every second?",
    "Did you know that the Great Barrier Reef is the largest living structure on Earth?",
    "Did you know that sharks have been around for more than 450 million years?",
    "Did you know that the human nose can detect about 1 trillion different scents?",
    "Did you know that spiders have blue blood?",
    "Did you know that the Sahara Desert used to be a lush, green forest?",
    "Did you know that the water in the oceans contains dissolved gold?",
    "Did you know that the Statue of Liberty was a gift from France to the United States?",
    "Did you know that the coldest naturally occurring place on Earth is Antarctica?",
    "Did you know that the Sun is about 109 times the diameter of the Earth?"
]

science_riddles = [
    "What has an eye, but cannot see?",
    "What is full of holes but still holds water?",
    "What has to be broken before you can use it?",
    "What is always in front of you but can’t be seen?",
    "What has cities, but no houses; forests, but no trees; and water, but no fish?",
    "What is light as a feather, yet the strongest person can't hold it for five minutes?",
    "What has one head, one foot, and four legs, but can't walk?",
    "What can you hold in your right hand, but never in your left?",
    "What is tall when it is young, and short when it is old?",
    "What month of the year has 28 days?",
    "What question can you never answer yes to?",
    "What has many teeth, but cannot eat?",
    "What is always coming, but never arrives?",
    "What has a neck without a head?",
    "What has no voice, yet can still speak to you?",
    "What gets wetter the more it dries?",
    "What is born big but gets smaller the more it takes a bath?",
    "What has no legs, but gets around?",
    "What has no beginning, end, or middle?",
    "What travels around the world while staying in a corner?"
]
riddle_answers = [
    "A needle",
    "A sponge",
    "An egg",
    "The future",
    "A map",
    "Your breath",
    "A bed",
    "Your left elbow",
    "A candle",
    "All of them",
    "Are you asleep yet?",
    "A comb",
    "Tomorrow",
    "A bottle",
    "A book",
    "A towel",
    "A bar of soap",
    "Sound",
    "A circle",
    "A stamp"
]

science_questions = [
    "What is the chemical symbol for water?",
    "What planet is known as the 'Red Planet'?",
    "What is the process by which plants make their own food?",
    "What is the main gas in Earth's atmosphere?",
    "What is the speed of light in a vacuum?",
    "What is the powerhouse of the cell?",
    "What is the force that pulls objects towards each other?",
    "What are the three states of matter?",
    "What is the chemical symbol for gold?",
    "What is the largest planet in our solar system?",
    "What is the name of our galaxy?",
    "What is the closest star to Earth?",
    "What is the natural satellite of Earth?",
    "What is the boiling point of water in Celsius?",
    "What is the freezing point of water in Celsius?",
    "What is the unit of measurement for force?",
    "What is the unit of measurement for energy?",
    "What is the name of the force that opposes motion?",
    "What is the process of a liquid turning into a gas?",
    "What is the process of a gas turning into a liquid?"
]
question_answers = [
    "H2O",
    "Mars",
    "Photosynthesis",
    "Nitrogen",
    "299,792,458 meters per second",
    "Mitochondria",
    "Gravity",
    "Solid, liquid, and gas",
    "Au",
    "Jupiter",
    "Milky Way",
    "Sun",
    "Moon",
    "100",
    "0",
    "Newton",
    "Joule",
    "Friction",
    "Evaporation or Vaporization",
    "Condensation"
]

def tell_fact():
    """Selects and displays a random science fact."""
    random_fact = random.choice(science_facts)
    print("Agent: Here's an interesting science fact:")
    print(random_fact)
    return True # To continue the game

def ask_riddle():
    """Selects and asks a random riddle and checks the user's answer."""
    index = random.randint(0, len(science_riddles) - 1)
    riddle = science_riddles[index]
    answer = riddle_answers[index].lower()
    print("Agent: Riddle time!")
    print(riddle)
    user_answer = input("Your answer? ").lower()
    if user_answer == answer:
        print("Agent: That's correct! Well done!")
        return True
    else:
        print(f"Agent: Not quite! The correct answer was '{riddle_answers[index]}'.")
        return False

def ask_single_question():
    """Asks a single science question and returns True if the answer is correct, False otherwise."""
    index = random.randint(0, len(science_questions) - 1)
    question = science_questions[index]
    answer = question_answers[index].lower()
    print("Agent: Here's a science question for you:")
    print(question)
    user_answer = input("Your answer? ").lower()
    if user_answer == answer:
        print("Agent: That's right!")
        return True
    else:
        print(f"Agent: The correct answer was '{question_answers[index]}'.")
        return False

def play_question_game():
    """Asks 5 science questions and announces the result."""
    correct_answers = 0
    for i in range(5):
        print(f"\nQuestion {i+1}:")
        if ask_single_question():
            correct_answers += 1
    print(f"\nYou answered {correct_answers} out of 5 questions correctly.")
    if correct_answers >= 3:
        print("Agent: You're a super smart kid! Keep exploring!")
    else:
        print("Agent: Great effort! Let's learn more together next time!")
    return True # To continue the game

def show_menu():
    """Displays the game selection menu."""
    print("\nWelcome to the Science Fun Zone!")
    print("Type (f) for a fun science fact.")
    print("Type (r) for a tricky riddle.")
    print("Type (q) for a science quiz game (5 questions).")
    print("Type (x) to exit.")
    return input("Your choice: ").lower()

def main():
    while True:
        choice = show_menu()
        if choice == 'f':
            tell_fact()
        elif choice == 'r':
            ask_riddle()
        elif choice == 'q':
            play_question_game()
        elif choice == 'x':
            print("Goodbye! Keep learning!")
            break
        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()