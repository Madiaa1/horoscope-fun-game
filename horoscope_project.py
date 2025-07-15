def main():
    print("Welcome to the Horoscope Game!✨")
    print("Are you ready to discover what the stars say about you?✨")
    print("The universe has secrets to share... but only if you are brave enough to ask!")
    introduction()

def introduction():
    birth_months_list = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    print("Game Explanation: In this game, you enter your birth month and it will immediately reveal your special horoscope.")
    print("You will get a personalized message, a lucky color, and maybe even a small challenge for today!😉")
    
    while True:
        user_response = input("Would you like to see your horoscope now? (yes/no): ").strip().lower()
        if user_response == 'no':
            print("Oh, come on! The stars were so excited to talk to you... Maybe next time!😃")
            break
        elif user_response == 'yes':
            birth_month_input = input("Great! Now, tell me... in which month were you born? (Type the full month name like 'January'): ").strip()

            horoscopes = {
                'January': "People born in January often have a strong personality and a desire for independence...",
                'February': "People born in February are creative and innovative...",
                # Continue with your full text...
                'December': "December people are free-spirited and adventurous..."
            }

            if birth_month_input in horoscopes:
                print(horoscopes[birth_month_input])
                real = input("Does this Horoscope sound like you? (yes/no): ").strip().lower()
                if real == 'yes':
                    print("Great!")
                elif real == 'no':
                    ask = input("Then, want to see your lucky number for today? (yes/no): ").strip().lower()
                    if ask == 'yes':
                        print("🎉 Your lucky number is... 2! 🎉")
                        print("May this lucky number bring you success, joy, and happiness.")
                    else:
                        print("That's okay!")
                break
            else:
                print("Oops! That doesn't seem like a valid month. Please try again.")
        else:
            print("Please answer with 'yes' or 'no'.")
main()

