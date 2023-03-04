import gui
import layers
import random
import file_handler

# Global Declarations
window = gui.Window()


if __name__ == '__main__':
    window.mainloop()


# Old Version using terminal rather than GUI

def generate_hex_key(string, e_key):
    e_string = ""
    count = 0
    key_const_copy = layers.key_constants_list.copy()
    random.shuffle(key_const_copy)
    if e_key == "":
        for i in key_const_copy:
            if i == key_const_copy[len(key_const_copy) - 1]:
                e_key = e_key + i
            else:
                e_key = e_key + i + "-"
    for digit in string:
        if count >= 36:
            count = 0
        count += 1
        e_string = e_string + layers.encrypt_digit(digit, count, key_const_copy) + "/"
    e_list = list(e_string)
    e_list.pop()
    e_string = ''.join(e_list)

    print(f"Encryption Key: {e_key}\n")
    print(f"Encrypted Text: {e_string}\n")
    return e_key, e_string


def decrypt_hex_key(key, string):
    decrypted_string = ""
    encrypted_digit_list = string.split("/")
    encryption_key_list = key.split("-")
    count = 0
    for item in encrypted_digit_list:
        if count >= 36:
            count = 0
        count += 1
        current_key = encryption_key_list[count - 1]
        if item == "0":
            decrypted_string = decrypted_string + "\n"
        else:
            decrypted_string = decrypted_string + layers.decrypt_digit(current_key, item)
    return decrypted_string


if __name__ == 'x__main__':  # Non-Gui version of Hex Vault
    running = True
    while running:
        print("-" * 50)
        choice = str(input("Would you like to encrypt or decrypt?\n 1. Encrypt\n 2. Decrypt\n"))
        print("-" * 50)
        if choice == "1":
            string_input = str(input("Please enter the text you would like to encrypt.\n"))
            key_input = str(
                input("Please enter your desired encryption key. If left blank, a random key will be given\n"))
            final_key, final_string = generate_hex_key(string_input, key_input)
            print("-" * 50)
            file_choice = int(input("Would you like to save this to a file?\n1. Yes\n2. No\n"))
            print("-" * 50)
            if file_choice == 1:
                file_handler.write_to_file(final_key, final_string)
                print("File has been saved.")
        elif choice == "2":
            print("-" * 50)
            file_choice = int(input("Would you like to read from a file?\n1. Yes\n2. No\n"))
            print("-" * 50)
            if file_choice == 1:
                file_name = file_handler.get_file_list()
                d_key, d_string = file_handler.read_from_file(file_name)
                final_string = decrypt_hex_key(d_key, d_string)
                print("-" * 50)
                print(f"Encryption Key: {d_key}\nUnencrypted Text: {final_string}")
                print("-" * 50)
            else:
                print("-" * 50)
                final_string = decrypt_hex_key(
                    str(input("Please enter the key for the encryption.\n")),
                    str(input("Please enter the encrypted text.\n")))
                print("-" * 50)
                print(f"Unencrypted Text: {final_string}")
                print("-" * 50)
        running_input = str(input("Do you wish to encrypt/decrypt another file? Yes/No\n"))
        if str.lower(running_input) not in ["yes", "y"]:
            running = False
