text = input('Enter the text: ')
vowel_letters = 'ёйуеыаоэяию'

new_roster_vowel_letters = [letter for letter in text
                            for symbol in vowel_letters
                            if letter == symbol]

print(f'roster vowel letters: {new_roster_vowel_letters}')
print(f'roster length: {len(new_roster_vowel_letters)}')

