def check_letter():
    letter = 'i'  # change to test
    
    if len(letter) !=1:
        print("Invalid")
        return
    
    vowel = "aeiou"
    letters = letter.lower()
    # your logic here
    if letters in vowel:
        print(f'The letter {letter} is a vowel.')
    else:
        print(f'The letter {letter} is a consonant.')


check_letter()


def check_even_or_odd():
    num = 14  # change to test

    if (num % 2 == 0):
        print(f'{num} is even.')
    else:
        print(f'{num}  is odd.')

check_even_or_odd()



def check_temperature():
    temp_c = 15  # change to test

    # your logic here
    if(temp_c < 15):
        print('Cold')
    elif(temp_c >= 15 and temp_c <= 29):
        print('Warm')
    else:
        print('Hot')

check_temperature()


def apply_discount():
    amount = 72.500  # change to test
    discount_rate = 0.10

    # your logic here
    if(amount >= 50):
        amount -= amount * discount_rate
    print(amount)

apply_discount()


def determine_time_of_day():
    hour = 15  # 0-23, change to test

    # your logic here
    if(hour >= 5 and hour <= 11):
        print('Morning')
    elif(hour >= 12 and hour <= 16):
        print('Afternoon')
    elif(hour >= 17 and hour <= 20):
        print('Evening')
    elif(hour >= 21 and hour <= 23 or hour >= 0 and hour <= 4):
        print('Night')

determine_time_of_day()


def check_grade():
    score = 85  # change to test

    # your logic here
    if(score >= 90 and  score <= 100):
        print('A')
    elif(score >= 80 and score <= 89):
        print('B')
    elif(score >= 70 and score <= 79):
        print('C')
    elif(score >= 60 and score <= 69):
        print('D')
    elif(score < 60):
        print('F')
    else:
        print('Invalid score: use 0–100.')


check_grade()