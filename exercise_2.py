from idlelib.editor import darwin
from idlelib.outwin import file_line_pats
from os import write
from tkinter import ttk
import tkinter as tk

from django.utils.text import normalize_newlines

root = tk.Tk()
root.geometry('850x900')

max_entry = 20
cont_entry = []
text_area = None
scrollbar = None

def error(word):
    entyon.config(state='normal')
    entyon.delete(0, tk.END)
    entyon.insert(0, f'Неизвестная команда: {word}')
    entyon.config(state='readonly')
    print(f'Неизвестная команда: {word}')

def insert_entry():
    entyon.config(state='normal')
    entyon.delete(0, tk.END)
    entyon.insert(0, 'Успешно код: 00')
    entyon.config(state='readonly')
    print('Успешно код: 00')


def balance(valueR):
    print(valueR)
    entyon.config(state='normal')
    entyon.delete(0, tk.END)
    if valueR == 'NO CLIENT':
        entyon.insert(0, 'NO CLIENT')

        print('NO CLIENT')
    else:
        entyon.insert(0, f'Баланс: {valueR}')

        print(f'Ваш баланс: {valueR}')

    entyon.config(state='readonly')

def calculate():
    global text_area, scrollbar
    data_dict = {}
    if text_area is not None:
        text_area.destroy()
        scrollbar.destroy()
    with open('resourse_2.txt', 'r') as file:
        for line in file:
            pats = line.strip().split()
            if len(pats) == 2:
                key = pats[0]
                value = pats[1]
                data_dict[key] = value

        file.close()

    val = [entry.get() for entry in cont_entry]
    for i, values in enumerate(val, start=1):
        print(f'Поле {i}: значение {values}')
        words = values.split()
        first_word = words[0]
        if len(words) == 3:
            second_word = words[1]
            third_words = words[2]

            if first_word == 'DEPOSIT':
                summa = int(third_words)
                if second_word in data_dict:
                    val_sur = int(data_dict[second_word])
                    data_dict[second_word] = val_sur + summa
                    insert_entry()
                else:
                    data_dict[second_word] = summa
                    insert_entry()



            elif first_word == 'WITHDRAW':
                summa = int(third_words)
                if second_word in data_dict:
                    val_sur = int(data_dict[second_word])
                    data_dict[second_word] = val_sur-summa
                    insert_entry()
                else:
                    data_dict[second_word] = 0 - summa
                    insert_entry()

            else:
                error(first_word)

            with open('resourse_2.txt', 'w') as file:
                for key, value in data_dict.items():
                    file.write(f'{key} {value}\n')

                file.close()

        elif len(words) == 2:
            second_word = words[1]

            if first_word == 'BALANCE':
                if second_word in data_dict:
                    balance(data_dict[second_word])

                else:
                    balance('NO CLIENT')

            elif first_word == 'INCOME':
                proc = int(second_word)
                for key, value in data_dict.items():
                    if int(data_dict[key]) >0:
                        balance_n = int((int(data_dict[key]) *proc) // 100)
                        data_dict[key] = int(data_dict[key]) + balance_n
                    else:
                        data_dict[key] = value

                insert_entry()

                with open('resourse_2.txt', 'w') as file:
                    for key, value in data_dict.items():
                        file.write(f'{key} {value}\n')

                    file.close()

            else:
                error(first_word)

        elif  len(words) == 1:
            if first_word == 'BALANCE':
                text_area = tk.Text(root, wrap='word', height=10, width=40)
                scrollbar = ttk.Scrollbar(root, command=text_area.yview)
                text_area.grid(row=4, column=5, padx=10, pady=10)

                scrollbar.grid(row=4, column=6, sticky='ns')
                text_area['yscrollcommand'] = scrollbar.set

                for key, value in data_dict.items():
                    text_area.insert(tk.END, f'{key}: {value}\n')
                    print(f'{key}: {value}\n')

                text_area.config(state='disabled')

                # Запрещаем фокусировку на текстовом поле
                text_area.bind("<Button-1>", lambda e: "break")


            else:
                error(first_word)

        elif len(words) == 4:
            second_word = words[1]
            third_words = words[2]
            four_words = words[3]
            if first_word == 'TRANSFER':
                summa = int(four_words)

                if second_word not in data_dict and third_words in data_dict:
                    data_dict[second_word] = 0 - summa
                    data_dict[third_words] = int(data_dict[third_words]) + summa
                    insert_entry()

                elif third_words not in data_dict and second_word in data_dict:
                    data_dict[second_word] = int(data_dict[second_word]) - summa
                    data_dict[third_words] = 0 + summa
                    insert_entry()

                elif second_word in data_dict and third_words in data_dict:
                    data_dict[second_word] = int(data_dict[second_word]) - summa
                    data_dict[third_words] = int(data_dict[third_words]) + summa
                    insert_entry()

                else:
                    data_dict[second_word] = 0 - summa
                    data_dict[third_words] = 0 + summa
                    insert_entry()

                with open('resourse_2.txt', 'w') as file:
                    for key, value in data_dict.items():
                        file.write(f'{key} {value}\n')

                    file.close()

            else:
                error(first_word)






def add_entry():
    if len(cont_entry)<max_entry:
        entry = ttk.Entry(root)
        entry.grid(row=(len(cont_entry)+1), column=0, padx=10, pady=10)
        cont_entry.append(entry)

    else:
        print('Максимальное количество полей')


def delete_entry():
    if len(cont_entry)!= 0:
        entry = cont_entry.pop()
        entry.destroy()

    else:
        print('Больше нет полей')


def clear_val():
    for field in cont_entry:
        field.delete(0, tk.END)  # Очищаем текст в каждом поле
    cont_entry.clear()


btnplus = ttk.Button(text='+', command=add_entry)
btnminus = ttk.Button(text='-', command=delete_entry)
btnclear = ttk.Button(text='Clear', command=clear_val)
btncalc = ttk.Button(text='Calculate', command=calculate)
labels = ttk.Label(text='Ответ программы:')
entyon = ttk.Entry(state='readonly', width=50)

btnminus.grid(row=0, column=1, padx=10, pady=10)
btnplus.grid(row=0, column=0, padx=10, pady=10)
btnclear.grid(row=0, column=3,padx=10, pady=10)
btncalc.grid(row=1, column=3, padx=10, pady=10)
labels.grid(row=0, column=4, padx=15,pady=10)
entyon.grid(row=0, column=5, padx=15,pady=10)

root.mainloop()
