# we can add whaterver language letters as long as it is an array of those
from English_dict import ENGLISH_LETTERS
# we should have the most frequent letter in the language
from English_dict import most_frequent_letter

from messages import ENCRYPTED_MESSAGES


encrypted_message = ENCRYPTED_MESSAGES[2]


def create_frequency_dict(string_meesage):
    frequency_dict = {}
    for letter in string_meesage:
        if letter in ENGLISH_LETTERS:
            if not letter in frequency_dict:
                frequency_dict[letter] = 0
            else:
                frequency_dict[letter] += 1

    return frequency_dict


def find_most_frequent_letters(frequency_dict):
    max_value = max(frequency_dict.values())

    return [key for key, value in frequency_dict.items() if value == max_value]


def compute_shift_guess(language_dict, most_frequent_letter, message_mf_letter):
    return language_dict.index(most_frequent_letter) - language_dict.index(message_mf_letter)


def decrypt_message(shift_guess, message):
    decrypted_message = ""
    for letter in message:
        if letter not in ENGLISH_LETTERS:
            decrypted_message += letter
        else:
            shifted_index = ENGLISH_LETTERS.index(letter) + shift_guess
            if shifted_index > len(ENGLISH_LETTERS):
                shifted_index %= len(ENGLISH_LETTERS)
            decrypted_message += ENGLISH_LETTERS[shifted_index]

    return decrypted_message

freq_dict = create_frequency_dict(encrypted_message)
mf_letter = find_most_frequent_letters(freq_dict)[0]
shift_guess = compute_shift_guess(ENGLISH_LETTERS, most_frequent_letter, mf_letter)

message = decrypt_message(shift_guess, encrypted_message)
print(shift_guess)
print(message)