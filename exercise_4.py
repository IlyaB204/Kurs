import tkinter as tk
from tkinter import ttk, Canvas, messagebox
from tkinter.ttk import Style
import math
import copy
from tkinter import  *


root = tk.Tk()
root.geometry('900x900')


class Hanoi:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=900, height=600)
        self.canvas.pack()
        self.splinders = [[],[],[],[],[],[],[],[]]
        self.x_base = 50
        self.y_base = 450
        self.height_disk = 15
        self.zav = []
        self.id_str = '0'
        self.colors = ("gray", "pink", "brown", "cyan", "magenta", "lime", "teal", "purple")
        self.height_zav = 50
        self.digit = '0'
        self.max_iter = 0
        self.flag_zav = False
        self.schetchik = 0
        self.maks_iter = 0
        self.vrem_iter = 0
        self.tekushaya_pozitsiya = []
        self.iter = 0

        self.draw_spl()
        self.panel()



    def draw_spl(self):
        print('Вызван метод draw_sp')
        self.canvas.delete('all')
        self.canvas.create_rectangle(40, 450, 760, 480, width=3, outline="#783636")
        x = self.x_base
        y0 = self.y_base
        for i in reversed(range(len(self.splinders))):
            self.canvas.create_rectangle(x - 2, 100, x + 2, y0, fill='white', width=3, outline='#783636')
            label = tk.Label(text=str(i + 1), font="Times 12")
            label.place(x=x-5, y=y0+3)
            x += 100
        print('Метод draw_spl полностью выполнен')

    def draw_disk(self, stergni):
        print('Вызван метод draw_disk')
        self.canvas.delete("all")
        self.draw_spl()
        x = self.x_base
        for num, i in enumerate(stergni):
            y = self.y_base
            if self.zav and self.zav[0] == num:
                for j in i[0:-1]:
                    self.canvas.create_rectangle(x - math.floor(j / 2), y, x + math.ceil(j / 2), y - self.height_disk,
                                          fill=self.colors[j % 8])
                    self.canvas.create_text(x, y - 5, text=(j), font="Times 8")
                    y -= self.height_disk
                j = i[-1]
                sdvig = 100 * (self.zav[1] - self.zav[0]) / 2
                self.canvas.create_rectangle(x - math.floor(j / 2) + sdvig, self.height_zav, x + math.ceil(j / 2) + sdvig,self.height_zav - self.height_disk, fill=self.colors[j % 8])
                self.canvas.create_text(x + sdvig, self.height_zav - 5, text=(j), font="Times 8")
            else:
                for j in i:
                    self.canvas.create_rectangle(x - math.floor(j / 2), y, x + math.ceil(j / 2), y - self.height_disk,
                                          fill=self.colors[j % 8])
                    self.canvas.create_text(x, y - 5, text=(j), font="Times 8")
                    y -= self.height_disk
            x += 100

    def spl_val(self):
        self.splinders = [[],[],[],[],[],[],[],[]]

    def get_id(self):
            self.id_str = str(self.entry.get())
            self.spl_val()
            print(self.id_str)
            if len(self.id_str) > 8:
                messagebox.showinfo("Error",f'Количество цифр в id превышает 9!')
                return
            else:
                for i, j in enumerate(self.id_str):
                    print(j)
                    for i1 in reversed(range(int(j))):
                        self.splinders[i].append((len(self.id_str) - i) * 10 + i1 + 1)
                print(self.splinders)
                self.draw_disk(self.splinders)
                self.count_one()

    def get_btn(self, btn):
        print('Вызван метод get_btn')
        if btn == '1':
            value = int(self.entry_p_1.get())
        elif btn == '2':
            value = int(self.entry_p_2.get())
        elif btn == '3':
            value = int(self.entry_p_3.get())
        else:
            value = int(self.entry_p_4.get())

        self.obrabotka_procentov(value)

    def panel(self):
        btn_style = ttk.Style()
        btn_style.configure('TButton', width=20, height=50, background='#783636')

        self.entry = tk.Entry(self.master)
        self.entry.place(x=400, y=700)
        self.entry_p_1 = ttk.Entry(self.master, width=5)
        self.entry_p_1.place(x=380,y=550)
        self.entry_p_1.insert(0,'70')
        self.entry_p_2 = ttk.Entry(self.master, width=5)
        self.entry_p_2.place(x=430, y=550)
        self.entry_p_2.insert(0,'20')
        self.entry_p_3 = ttk.Entry(self.master, width=5)
        self.entry_p_3.place(x=480,y=550)
        self.entry_p_3.insert(0,'62')
        self.entry_p_4 = ttk.Entry(self.master, width=5)
        self.entry_p_4.place(x=530, y=550)
        self.entry_p_4.insert(0,'39')

        btn_1 = ttk.Button(text='П.1', command=lambda: self.get_btn('1'), width=5)
        btn_1.place(x=380, y=600)
        btn_2 = ttk.Button(text='П.2', command=lambda: self.get_btn('2'), width=5)
        btn_2.place(x=430, y=600)
        btn_3 = ttk.Button(text='П.3', command=lambda: self.get_btn('3'), width=5)
        btn_3.place(x=480, y=600)
        btn_4 = ttk.Button(text='П.4', command=lambda: self.get_btn('4'), width=5)
        btn_4.place(x=530, y=600)
        btn_save = ttk.Button(text='Save', style='TButton', command=self.get_id)
        btn_save.place(x=400, y=750)
        btn_start = ttk.Button(text='Start', style='TButton', command=self.start)
        btn_start.place(x=150, y=550)
        btn_end = ttk.Button(text='End', style='TButton', command=self.end)
        btn_end.place(x=650, y=550)

        self.label = ttk.Label(self.master,text=f'Итераций: {self.digit}')
        self.label.place(x=400, y=500)

    def update_label(self):
        try:
            print(f'Label exists: {self.label}')
            self.label.config(text=f'Итераций: {self.digit}')
        except AttributeError as e:
            print("AttributeError caught:", e)

    def start(self):
        self.zav= []
        self.draw_disk(self.splinders)
        self.digit = '0'
        self.update_label()

    def end(self):  # показываем, как всё будет в конце
        self.zav = []
        end_pos = []
        last_st = []
        for i in self.splinders:
            last_st += i
            end_pos.append([])
        end_pos[len(self.splinders) - 1] = last_st
        self.draw_disk(end_pos)
        self.vrem_iter = str(self.max_iter)
        self.digit = self.vrem_iter
        self.update_label()


    def count_one(self):
        print("Вызван метод count_one")
        self.max_iter = 0
        l_rod = 0
        for i in reversed(range(3)):
            l_rod += len(self.splinders[i])
            self.max_iter += 2 ** l_rod - 1
        for i in range(3, len(self.splinders)):
            self.max_iter += (2 ** len(self.splinders[i]) - 1)
            l_rod += len(self.splinders[i])
            self.max_iter += 2 ** l_rod - 1
        print('Метод count_move полностью выполнен')

    def count_move(self, num, pl1, pl2, pl3, dlina, fix1, fix2, fix3):  # рекурсия для подсчета ходов
        pw = 2 ** dlina

        # Условие выхода из рекурсии
        if dlina < 0:
            return (pl1, pl2, pl3)  # или возвращайте что-то иное, если dlina меньше 0

        if (pw < num):
            num2 = num - pw
            pl2.append(pl1[len(pl1) - 1 - dlina])
            pl3 += pl1[len(pl1) - dlina:]
            pl1 = pl1[:len(pl1) - 1 - dlina]
            return self.count_move(num2, pl3, pl2, pl1, dlina - 1, fix3, fix2, fix1)

        elif pw > num:
            return self.count_move(num, pl1, pl3, pl2, dlina - 1, fix1, fix3, fix2)

        else:  # pw == num
            pl2.append(pl1[len(pl1) - dlina - 1])
            pl3 += pl1[len(pl1) - dlina:]
            pl1 = pl1[:len(pl1) - 1 - dlina]
            if self.flag_zav:
                self.zav.append(fix2)
                self.zav.append(fix1)
        self.update_label()

        return (pl1, pl2, pl3)

    def run(self):  # выполняем перемещения
        self.zav = []
        self.tekushaya_pozitsiya = copy.deepcopy(self.splinders)
        self.vrem_iter = 0
        l_rod = 0
        flag = False
        ind1 = [2, 0, 1]
        ind2 = [1, 2, 0]
        for i in reversed(range(3)):
            l_rod += len(self.splinders[i])
            old_vrem_iter = self.vrem_iter
            self.vrem_iter += 2 ** l_rod - 1
            if self.vrem_iter >= self.iter:
                st1 = self.tekushaya_pozitsiya[i]
                st2 = []
                st3 = []
                st1, st2, st3 = self.count_move(self.iter - old_vrem_iter, st1, st2, st3, len(self.tekushaya_pozitsiya[i]) - 1, i,ind1[i], ind2[i])
                self.tekushaya_pozitsiya[i] = st1
                self.tekushaya_pozitsiya[ind1[i]] += st2
                self.tekushaya_pozitsiya[ind2[i]] += st3
                flag = True

                break
            else:
                self.tekushaya_pozitsiya[ind1[i]] += self.tekushaya_pozitsiya[i]
                self.tekushaya_pozitsiya[i] = []

        if not flag:
            for i in range(3, len(self.splinders)):
                old_vrem_iter = self.vrem_iter
                self.vrem_iter += (2 ** len(self.splinders[i]) - 1)
                if self.vrem_iter >= self.iter:
                    st1 = self.tekushaya_pozitsiya[i]
                    st2 = []
                    st3 = []
                    st1, st2, st3 = self.count_move(self.iter - old_vrem_iter, st1, st2, st3, len(self.tekushaya_pozitsiya[i]) - 1,i, i - 1, i - 2)
                    self.tekushaya_pozitsiya[i] = st1
                    self.tekushaya_pozitsiya[i - 1] += st2
                    self.tekushaya_pozitsiya[i - 2] += st3

                    break
                else:

                    self.tekushaya_pozitsiya[i - 1] += self.tekushaya_pozitsiya[i]
                    self.tekushaya_pozitsiya[i] = []
                l_rod += len(self.splinders[i])
                old_vrem_iter = self.vrem_iter
                self.vrem_iter += 2 ** l_rod - 1
                if self.vrem_iter >= self.iter:
                    st1 = self.tekushaya_pozitsiya[i - 1]
                    st2 = []
                    st3 = []
                    st1, st2, st3 = self.count_move(self.iter - old_vrem_iter, st1, st2, st3,
                                                   len(self.tekushaya_pozitsiya[i - 1]) - 1, i - 1, i, i - 2)
                    self.tekushaya_pozitsiya[i - 1] = st1
                    self.tekushaya_pozitsiya[i] += st2
                    self.tekushaya_pozitsiya[i - 2] += st3

                    break
                else:

                    self.tekushaya_pozitsiya[i] += self.tekushaya_pozitsiya[i - 1]
                    self.tekushaya_pozitsiya[i - 1] = []
        self.draw_disk(self.tekushaya_pozitsiya)


    def obrabotka_procentov(self,cs):  # обрабатываем проценты

        self.vrem_iter = int(cs) * self.max_iter / 100
        self.iter = int(self.vrem_iter)
        if self.vrem_iter == self.iter:
            self.flag_zav = False
        else:
            self.iter += 1
            self.flag_zav = True
        self.digit = self.vrem_iter
        self.update_label()
        self.schetchik = 0
        if 0 <= int(cs) <= 100:
            self.run()
        else:
            messagebox.showerror("Error", "Неверный ввод процента")


app = Hanoi(root)
root.mainloop()


