import tkinter as tk
from tkinter import *
import math
import re

from django.contrib.sitemaps.views import index
from django.utils.autoreload import ensure_echo_on
from pyexpat.errors import messages

root = tk.Tk()
root.geometry('400x500')
root.title('Калькулятор - Обычный режим')

id = None
buttons = []
buttons2 = []
memory = {}
value1 = None
value2 = None

def menu():
    global id
    global buttons
    id = entry2.get()
    print(id)
    if buttons:
        root.geometry('400x500')
        root.title('Калькулятор - Обычный режим')
        for button in buttons:
            button.destroy()
        buttons.clear()
        return
    elif id == None or id == '':
        root.geometry('700x500')
        root.title('Калькулятор - Расширенный режим')
        btn1 = tk.Button(text='M+', command=lambda idx=1, val='M+': memory_command(idx, val))
        buttons.append(btn1)
        btn1.grid(row=4, column=6, padx=5, pady=5)
        btn2 = tk.Button(text='M-', command=lambda idx=1, val='M-': memory_command(idx, val))
        buttons.append(btn2)
        btn2.grid(row=4, column=7, padx=5, pady=5)
        btn3 = tk.Button(text='MC', command=lambda idx=1, val='MC': memory_command(idx, val))
        buttons.append(btn3)
        btn3.grid(row=4, column=8, padx=5, pady=5)
        btn4 = tk.Button(text='MR', command=lambda idx=1, val='MR': memory_command(idx, val))
        buttons.append(btn4)
        btn4.grid(row=4, column=9, padx=5, pady=5)
        btn5 = tk.Button(text='MS', command=lambda idx=1, val='MS': memory_command(idx, val))
        buttons.append(btn5)
        btn5.grid(row=4, column=10, padx=5, pady=5)
        asin_btn = tk.Button(text='asin', command= asin)
        buttons.append(asin_btn)
        asin_btn.grid(row=3, column=6, padx=5, pady=5)
        acos_btn = tk.Button(text='acos', command=acos)
        buttons.append(acos_btn)
        acos_btn.grid(row=3, column=7, padx=5, pady=5)
        atg_btn = tk.Button(text='atg', command=atg)
        buttons.append(acos_btn)
        atg_btn.grid(row=3, column=8, padx=5, pady=5)
        log_btn = tk.Button(text='log', command=lambda :log())
        buttons.append(log_btn)
        log_btn.grid(row=3, column=9, padx=5, pady=5)
        fc_btn = tk.Button(text='n!', command=factor)
        buttons.append(log_btn)
        fc_btn.grid(row=3, column=10, padx=5, pady=5)
    else:
        root.geometry('700x500')
        root.title('Калькулятор - Расширенный режим')
        new_id = id[-3:]
        count_memory = memory_block(new_id)
        print(f'Количество ячеек - {count_memory}')
        cl = 6
        for i in range(count_memory):
            if cl == 12:
                cl = 6
            btn1 = tk.Button(text='M+', command= lambda idx = i, val = 'M+': memory_command(idx, val))
            buttons.append(btn1)
            btn1.grid(row = i +4, column = cl, padx = 5, pady = 5)
            btn2 = tk.Button(text='M-', command= lambda idx = i, val = 'M-': memory_command(idx, val))
            buttons.append(btn2)
            btn2.grid(row=i + 4, column=cl+1, padx=5, pady=5)
            btn3 = tk.Button(text='MC', command= lambda idx = i, val = 'MC': memory_command(idx, val))
            buttons.append(btn3)
            btn3.grid(row=i + 4, column=cl+2, padx=5, pady=5)
            btn4 = tk.Button(text='MR', command= lambda idx = i, val = 'MR': memory_command(idx, val))
            buttons.append(btn4)
            btn4.grid(row=i + 4, column=cl+3, padx=5, pady=5)
            btn5 = tk.Button(text='MS', command= lambda idx = i, val = 'MS': memory_command(idx, val))
            buttons.append(btn5)
            btn5.grid(row=i + 4, column=cl+4, padx=5, pady=5)
            asin_btn = tk.Button(text='asin', command=asin)
            buttons.append(asin_btn)
            asin_btn.grid(row=3, column=6, padx=5, pady=5)
            acos_btn = tk.Button(text='acos', command=acos)
            buttons.append(acos_btn)
            acos_btn.grid(row=3, column=7, padx=5, pady=5)
            atg_btn = tk.Button(text='atg', command=atg)
            buttons.append(acos_btn)
            atg_btn.grid(row=3, column=8, padx=5, pady=5)
            log_btn = tk.Button(text='log', command=lambda: log())
            buttons.append(log_btn)
            log_btn.grid(row=3, column=9, padx=5, pady=5)
            fc_btn = tk.Button(text='n!', command=factor)
            buttons.append(log_btn)
            fc_btn.grid(row=3, column=10, padx=5, pady=5)


def asin():
    value = entry.get()
    try:
        value = float(value)
        if -1 <= value <= 1:
            result = math.asin(value)
            entry.delete(0, tk.END)
            entry.insert(0, result)
            add_history(f'asin({value}) = {result}')
        else:
            result = 0
            entry.delete(0, tk.END)
            entry.insert(0, result)
            add_history(f'asin({value}) = {result}')
    except Exception as e:
            add_history(f'Error - {e}')

def acos():
    value = entry.get()
    try:
        value = float(value)
        if -1 <= value <= 1:
            result = math.acos(value)
            entry.delete(0, tk.END)
            entry.insert(0, result)
            add_history(f'acos({value}) = {result}')
        else:
            result = 0
            entry.delete(0, tk.END)
            entry.insert(0, result)
            add_history(f'acos({value}) = {result}')
    except Exception as e:
        add_history(f'Error - {e}')

def atg():
    value = entry.get()
    try:
        value = float(value)
        result = math.atan(value)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        add_history(f'atg({value}) = {result}')
    except Exception as e:
        add_history(f'Error - {e}')

def log():
    global buttons2, value1,value2
    if buttons2:
        for button in buttons2:
            button.destroy()
        buttons2.clear()
        text_result.config(state='normal')
        text_result.delete(1.0, tk.END)
        value1 = None
        value2 = None
    else:
        text_result.config(state='normal')
        text_result.delete(1.0, tk.END)
        text_result.config(state='disabled')
        message = 'Введите, сначала число для подсчёта логарифма и нажмите кнопку добавить "Добавить". После чего введите второе число, но для основания и также нажмите соответствующую кнопку'
        add_history(message)
        add_history('Введите число для подсчета логарифма ...')
        btn = tk.Button(text='Добавить', command=lambda :add_log())
        buttons2.append(btn)
        btn.grid(row=1, column=5, padx=5, pady=5, columnspan =2)

def add_log():
    global value1,value2
    if value1 is None and value2 is None:
        value1 = float(entry.get())
        add_history(value1)
        message = 'Введите основание для логарифма...'
        add_history(message)
        entry.delete(0, tk.END)
        entry.insert(0, '0')
    elif value1 is not None and value2 is None:
        value2=float(entry.get())
        result = math.log(value1, value2)
        add_history(value2)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        add_history(f' log({value1}, {value2}) = {result}')

def factor():
    try:
        n = int(entry.get())
        result = math.factorial(n)
        add_history(f'{n}! = {result}')
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except ValueError as e:
        add_history(f'Error - {e}')

    print(value1)
    print(value2)

def add_digit(digit):
    value = entry.get()
    if value == '0' and digit == '-':
        entry.delete(0, tk.END)
        entry.insert(0, digit)
    elif value == '0' and digit == '.':
        value = value + digit
        entry.delete(0, tk.END)
        entry.insert(0, value)
    elif digit == '.' and digit in value:
        entry.delete(0, tk.END)
        entry.insert(0, value)
    elif value == '-' and digit in '+/*^':
        new_value = '0' + digit
        entry.delete(0, tk.END)
        entry.insert(0, new_value)
    elif value == '0' and digit not in '+/*^':
        entry.delete(0, tk.END)
        entry.insert(0,digit)
    elif value[-1] in '+-*/':
        if digit in '+-*/':
            value = value[:-1]
            entry.delete(0, tk.END)
            entry.insert(0, value + digit)
        else:
            new_val = value + digit
            entry.delete(0, tk.END)
            entry.insert(0, new_val)
    elif value == '0' and digit in '+/*':
        new_value = '0' + digit
        entry.delete(0,tk.END)
        entry.insert(0, new_value)
    elif value =='0' and digit =='0':
        return

    else:
        new_digit = entry.get()+ str(digit)
        entry.delete(0,tk.END)
        entry.insert(0,new_digit)
'''
def add_operation(operation):
    value = entry.get()
    if not value or value == '0':
        entry.delete(0, tk.END)
        entry.insert(0, operation)
    elif value[-1] in '+-*/':
        value = value[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, value+operation)
'''

def clear():
    entry.delete(0,tk.END)
    entry.insert(0, 0)

def entry_get():
    value = entry.get()
    calculate(value)

def calculate(val):
        value = val
        print(value)
        match = re.search(r'(\d+)\s*\^\s*(\d+)', value)
        try:
            if match:
                    base = int(match.group(1))
                    exp = int(match.group(2))
                    print(f'znach-1 = {base} and znach-2 = {exp}')
                    res = math.pow(base, exp)
                    new_value = re.sub(r'(\d+)\s*\^\s*(\d+)', str(res), value, count=1)
                    print(value)
                    return calculate(new_value)
            else:
                result = eval(value)
                add_history(f'{entry.get()} = {result}')
                entry.delete(0, tk.END)
                entry.insert(0, result)
        except Exception as e:
            add_history(f'Error - {e}')


def pow_dig(base,exp):
    res = math.pow(base,exp)
    print(res)
    return int(res)


def proc():
    value = entry.get()
    match = re.search(r'(\d+)\s*([+\-/*])\s*(\d+)', value)
    match2 = re.search(r'(\d+)', value)
    if match or match2:
        if match:

            result = (int(match.group(1)) * int(match.group(3)))/100
            res = str(match.group(1) + match.group(2) + str(result))
            result = eval(res)
        elif match2:
            result = int(match2.group(0))/100

    else:
        result = None

    entry.delete(0,tk.END)
    entry.insert(0,result)

def pow_dig2():
    value = entry.get()
    result = int(value)**2
    add_history(f'{value} ^ 2 = {result}')
    entry.delete(0, tk.END)
    entry.insert(0, result)

def result_sqrt():
    try:
        value = entry.get()
        result = math.sqrt(int(value))
        add_history(f'{result}')
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        add_history(f'Ошибка {e}')
        entry.delete(0, tk.END)

def sum_rec(val):
    if int(val) <= 10:
        if int(val) == 1:
            return 2
        else:
            return val
    else:
        new_val = sum(int(digit) for digit in str(val))
        return sum_rec(new_val)

def memory_block(val):
    if int(val) <= 9:
        if int(val) == 1:
            return 2
        else:
            return val
    else:
        new_val = sum(int(digit) for digit in str(val))
        return memory_block(new_val)

def memory_command(index, digit):
    global memory
    value = entry.get()
    if digit == 'M+':
        value = value.replace('-', '')
        memory[index] = value
    elif digit == 'M-':
        if value[0] == '-':
            memory[index] = value
        else:
            value = '-' + value
            memory[index] = value
    elif digit == 'MC':
        memory.pop(index)
    elif digit == 'MR':
        val = memory[index]
        if value[-1] in '+-*/':
            value = value + val
            entry.delete(0, tk.END)
            entry.insert(0,value)
        else:
            entry.delete(0, tk.END)
            entry.insert(0, val)
    elif digit == 'MS':
        pass

    print(f'Кнопка {digit}, Ячейка памяти {index}')

def rec():
    global id
    digit = entry2.get()
    id = digit
    res = sum_rec(digit)
    print(f'Количество строк - {res}')
    text_result.config(height=res)

def add_history(operation):
    text_result.config(state='normal')
    text_result.insert(tk.END,f'{operation}\n')
    text_result.config(state='disabled')


expression = tk.StringVar(value="0")
text_result = tk.Text(root, height=11, width=33,state='disabled', wrap='word')
entry = tk.Entry(root, justify=tk.RIGHT, textvariable=expression)
tk.Label(text='Введите ID студента').grid(row=8, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
tk.Button(text='C', command=clear, width=5).grid(row=2,column=3,padx=5,pady=5, sticky = 'wens')
tk.Button(text='Menu', command=menu).grid(row=2,column=0,padx=5,pady=5, sticky = 'wens')
tk.Button(text='<>', command=rec).grid(row=2,column=1,padx=5,pady=5, sticky = 'wens')
tk.Button(text='.', command= lambda :add_digit('.')).grid(row=3,column=2,padx=5,pady=5, sticky = 'wens')
tk.Button(text='=', command=entry_get).grid(row=7, column=1,padx=5,pady=5,sticky ='wens', columnspan=2)
tk.Button(text="+", command = lambda :add_digit('+')).grid(row=4, column=3, padx=5, pady=5, sticky='wens')
tk.Button(text="^", command = lambda :add_digit('^')).grid(row=3, column=3, padx=5, pady=5, sticky='wens')
tk.Button(text="%", command = lambda :proc()).grid(row=3, column=5, padx=5, pady=5, sticky='wens')
tk.Button(text="^2", command = lambda :pow_dig2()).grid(row=5, column=5, padx=5, pady=5, sticky='wens')
tk.Button(text="#", command = lambda :result_sqrt()).grid(row=4, column=5, padx=5, pady=5, sticky='wens')
tk.Button(text="-", command = lambda :add_digit('-')).grid(row=5, column=3, padx=5, pady=5, sticky='wens')
tk.Button(text="*", command = lambda :add_digit('*')).grid(row=6, column=3, padx=5, pady=5, sticky='wens')
tk.Button(text="/", command = lambda :add_digit('/')).grid(row=7, column=3, padx=5, pady=5, sticky='wens')
tk.Button(text='1', command=lambda: add_digit('1')).grid(row=4, column=0,padx=5,pady=5,sticky ='wens')
tk.Button(text='2', command=lambda: add_digit('2')).grid(row=4, column=1,sticky ='wens',padx=5,pady=5)
tk.Button(text='3', command=lambda: add_digit('3')).grid(row=4, column=2,padx=5,pady=5,sticky ='wens')
tk.Button(text='4', command=lambda: add_digit('4')).grid(row=5, column=0,padx=5,pady=5,sticky ='wens')
tk.Button(text='5', command=lambda: add_digit('5')).grid(row=5, column=1,padx=5,pady=5,sticky ='wens')
tk.Button(text='6', command=lambda: add_digit('6')).grid(row=5, column=2,padx=5,pady=5,sticky ='wens')
tk.Button(text='7', command=lambda: add_digit('7')).grid(row=6, column=0,padx=5,pady=5,sticky ='wens')
tk.Button(text='8', command=lambda: add_digit('8')).grid(row=6, column=1,padx=5,pady=5,sticky ='wens')
tk.Button(text='9', command=lambda: add_digit('9')).grid(row=6, column=2,padx=5,pady=5,sticky ='wens')
tk.Button(text='0', command=lambda: add_digit('0')).grid(row=7, column=0,padx=5,pady=5,sticky ='wens')
text_result.grid(row=0, column=0,padx=5,pady=5, sticky = 'wens',columnspan=3)
entry.grid(row = 1, column=0, padx=5,pady=5, sticky='wens', columnspan= 3)
entry2.grid(row=9, column=0,padx = 5, pady=5, columnspan=2)

root.mainloop()