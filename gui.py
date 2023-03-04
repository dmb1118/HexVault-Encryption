import tkinter as tk
import tkinter.filedialog
import textract

import layers
import random
import os

# global decs
font = "arial"


def output(string, key):
    output_window = Output()
    output_window.output_key.insert("end", key)
    output_window.output_string.insert("end", string)
    output_window.output_key.config(state="disabled")
    output_window.output_string.config(state="disabled")
    output_window.mainloop()


def gui_decrypt_hex_key(string, key):
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
    return key, decrypted_string


def gui_generate_hex_key(string, e_key):
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
    return e_key, e_string


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # Attributes
        self.title("Hex Vault")
        self.input_string = tk.Text(self)
        self.input_key = tk.Text(self)
        self.minsize(width=1000, height=500)
        self.maxsize(width=1000, height=500)
        self.geometry("1000x500")

        self.frame = tk.Frame(self)
        self.frame.pack(expand=True, fill="both")

        self.message = tk.Label(self.frame,
                                text="Please choose whether to Encrypt or Decrypt text", font=('arial', '16'))
        self.message.pack(side='top', padx=5, pady=5)

        self.encrypt_button = tk.Button(self.frame, text="Encrypt Text", font=font)
        self.encrypt_button.bind("<1>", self.encrypt_button_press)
        self.encrypt_button.place(x=850, y=200)

        self.decrypt_button = tk.Button(self.frame, text="Decrypt Text", font=font)
        self.decrypt_button.bind("<1>", self.decrypt_button_press)
        self.decrypt_button.place(x=850, y=250)

        self.close_button = tk.Button(self.frame, text="Close", font=font)
        self.close_button.bind("<1>", self.close_button_press)
        self.close_button.place(x=920, y=450)

        self.open_button = tk.Button(self.frame, text="Open File", font=font)
        self.open_button.bind("<1>", self.open_button_press)
        self.open_button.place(x=860, y=355)

        self.convert_button = tk.Button(self.frame, text="Convert File", font=font)
        self.convert_button.bind("<1>", self.convert_button_press)
        self.convert_button.place(x=860, y=325)
        self.string_entry_frame = tk.Frame(self)
        self.string_entry_frame.place(height=390, width=800, x=25, y=105)
        self.string_entry_frame.config(bg="darkgrey")

        self.string_entry_label = tk.Label(self.string_entry_frame, text="Enter Text: ")
        self.string_entry_label.place(x=10, y=95)

        self.string_entry = tk.Text(self.string_entry_frame, height=22, width=85, wrap="word")
        self.string_entry.place(x=80, y=20)

        self.key_entry_frame = tk.Frame(self)
        self.key_entry_frame.place(height=55, width=800, x=25, y=50)
        self.key_entry_frame.config(bg="darkgrey")

        self.key_entry_label = tk.Label(self.key_entry_frame, text="Enter Key:")
        self.key_entry_label.place(x=20, y=25)

        self.key_entry_label = tk.Label(self.key_entry_frame, text="Blank = Random Key for Encryption, "
                                                                   "Key Required for Decryption")
        self.key_entry_label.place(x=100, y=2)

        self.key_entry = tk.Text(self.key_entry_frame, height=2, width=130, font=(font, 7), padx=16, pady=8)
        self.key_entry.place(x=80, y=25)

        self.file_name = ""
        self.path = ""

    # Methods
    def close_button_press(self, event):
        self.destroy()

    def open_button_press(self, event):
        start_path = os.getcwd() + "\\files"
        self.path = tkinter.filedialog.askopenfilename(initialdir=start_path, filetypes=[("Text Files", "*.txt")])
        self.gui_read_from_file()

    def convert_button_press(self, event):
        pass

    def encrypt_button_press(self, event):
        string, key = gui_generate_hex_key(self.string_input(), self.key_input())
        output(key, string)
        # print(f"Encrypted Text: {string}\nEncryption Key: {key}")

    def decrypt_button_press(self, event):
        string, key = gui_decrypt_hex_key(self.string_entry.get("1.0", "end-1c"), self.key_entry.get("1.0", "end-1c"))
        output(key, string)
        # print(f"Encrypted Text: {string}\nEncryption Key: {key}")

    def string_input(self):
        string = self.string_entry.get("1.0", 'end-1c')
        return string

    def key_input(self):
        key = self.key_entry.get("1.0", 'end-1c')
        return key

    def gui_read_from_file(self):
        with open(f"{self.path}", "r+") as file:
            lines = file.readlines()
        x_string = "".join(lines)
        split_list = x_string.split(":")
        key = split_list[0]
        string = split_list[1]
        # print(key + "\n" + string)
        self.key_entry.delete("1.0", "end")
        self.string_entry.delete("1.0", "end")
        self.key_entry.insert("end", key)
        self.string_entry.insert("end", string)
        return key, string

    def reset(self):
        pass


class Output(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Output")
        self.output_string = tk.Text(self)
        self.output_key = tk.Text(self)
        self.minsize(width=1000, height=500)
        self.maxsize(width=1000, height=500)
        self.geometry("1000x500")

        self.frame = tk.Frame(self)
        self.frame.pack(expand=True, fill="both")

        self.message = tk.Label(self.frame,
                                text="Output", font=('arial', '16'))
        self.message.pack(side='top', padx=5, pady=5)

        self.save_button = tk.Button(self.frame, text="Save To File", font=font)
        self.save_button.bind("<1>", self.save_button_press)
        self.save_button.place(x=880, y=355)

        self.file_name_entry = tk.Entry(self.frame)
        self.file_name_entry.place(x=870, y=335)

        self.file_name_label = tk.Label(self.frame, text="Write File Name")
        self.file_name_label.place(x=885, y=310)

        self.file_name = ""

        self.close_button = tk.Button(self.frame, text="Close", font=font)
        self.close_button.bind("<1>", self.close_button_press)
        self.close_button.place(x=920, y=450)

        self.string_entry_frame = tk.Frame(self)
        self.string_entry_frame.place(height=390, width=800, x=25, y=105)
        self.string_entry_frame.config(bg="darkgrey")

        self.string_entry_label = tk.Label(self.string_entry_frame, text="Output Text: ")
        self.string_entry_label.place(x=10, y=95)

        self.output_string = tk.Text(self.string_entry_frame, height=22, width=85, wrap="word")
        self.output_string.place(x=80, y=20)

        self.key_entry_frame = tk.Frame(self)
        self.key_entry_frame.place(height=55, width=800, x=25, y=50)
        self.key_entry_frame.config(bg="darkgrey")

        self.key_label = tk.Label(self.key_entry_frame, text="Key: ")
        self.key_label.place(x=20, y=25)

        self.output_key = tk.Text(self.key_entry_frame, height=2, width=130, font=(font, 7), padx=16, pady=8)
        self.output_key.place(x=80, y=25)

    # Methods

    def close_button_press(self, event):
        self.destroy()

    def save_button_press(self, event):
        output_text = self.output_string.get("1.0", 'end-1c')
        output_key = self.output_key.get("1.0", 'end-1c')
        self.file_name = self.file_name_entry.get()
        self.output_key.config(state="disabled")
        self.gui_write_to_file(output_key, output_text)

    def gui_write_to_file(self, key, string):
        path = os.getcwd() + "\\files"
        file_name = self.file_name + ".txt"
        with open(f"{path}\\{file_name}", "a+") as file:
            file.write(key + ":" + string)
