# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:38:37 2020

@author: J
"""
import tkinter as tk
from tkinter import ttk


class Lv2p1:
    def __init__(self):
        root2 = tk.Tk()
        self.root2 = root2
        root2.title("Mastermind: Level 2")
        tk.Label(root2, text="Enter the 9-digit key(all numbers) to guess", font="Arial 13 bold").pack()
        self.a = tk.Entry(root2, width=10, font="Arial 15")
        self.a.pack()
        tk.Button(root2, text="Submit", height=1, width=5, command=lambda: self.checknum()).pack()
        root2.protocol("WM_DELETE_WINDOW", lambda: (root.deiconify(), root2.destroy()))
        root2.mainloop()

    def checknum(self):
        v = self.a.get()
        if len(v) > 9 or len(v) < 9:
            root3 = tk.Tk()
            root3.title("Incorrect key")
            tk.Label(root3, text="Only put a 9-digit code, no more, no less").pack()
            tk.Button(root3, text="Ok", height=1, width=3, command=root3.destroy).pack()
        else:
            ercount = False
            for i in v:
                if ord(i) in range(48, 58):
                    pass
                else:
                    ercount = True
                    break
            if ercount == True:
                root4 = tk.Tk()
                root4.title("Incorrect key")
                tk.Label(root4, text="Looks like you put a character/symbol/space instead of number").pack()
                tk.Button(root4, text="Ok", height=1, width=3, command=root4.destroy).pack()
            else:
                self.root2.withdraw()
                Lv2p2(v, self.root2)


class Lv2p2:
    def __init__(self, v1, root2):
        self.root2 = root2
        self.v1 = v1
        root3 = tk.Tk()
        self.root3 = root3
        root3.title("Mastermind: Level 2")
        root3.geometry("350x80")
        tk.Label(root3, text="Enter the 9-digit code", font="Arial 13 bold").pack()
        self.a = tk.Entry(root3, width=10, font="Arial 15")
        self.a.pack()
        self.root6 = tk.Toplevel(root3)
        self.root6.title("Hints")
        self.root6.geometry("400x500")
        self.txt = tk.Text(self.root6, height=2, width=60)
        self.txt.pack(fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self.txt, orient=tk.VERTICAL, command=self.txt.yview)
        scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
        self.txt.config(yscrollcommand=scrollbar.set)
        self.root6.withdraw()
        tk.Button(root3, text="Submit", height=1, width=5, command=lambda: self.checknum()).pack()
        root3.protocol("WM_DELETE_WINDOW", lambda: [self.root6.destroy(), root3.destroy(), self.root2.deiconify()])
        root3.mainloop()

    def checknum(self):
        v = self.a.get()
        if len(v) > 9 or len(v) < 9:
            root4 = tk.Tk()
            root4.title("Incorrect key")
            tk.Label(root4, text="Only put a 9-digit code, no more, no less").pack()
            tk.Button(root4, text="Ok", height=1, width=3, command=root4.destroy).pack()
        else:
            ercount = False
            for i in v:
                if ord(i) in range(48, 58):
                    pass
                else:
                    ercount = True
                    break
            if ercount == True:
                root5 = tk.Tk()
                root5.title("Incorrect key")
                tk.Label(root5, text="Looks like you put a character/symbol/space instead of number").pack()
                tk.Button(root5, text="Ok", height=1, width=3, command=root5.destroy).pack()
            else:
                self.compare(v, self.v1)

    def compare(self, n1, n2):
        if n1 == n2:
            self.root6.destroy()
            root4 = tk.Tk()
            root4.title("Correct!!!")
            tk.Label(root4, text="Congrats! You guessed the correct code", font="Arial 25 bold").pack()
            tk.Button(root4, text="Ok", height=1, width=3,
                      command=lambda: (root4.destroy(), self.root3.destroy(), self.root2.deiconify())).pack()
        else:
            cd = dict()
            exi = 0
            pos = 0
            s1 = list(n1)
            s2 = list(n2)
            for i in range(9):
                if s1[i] in s2:
                    exi += 1
                    if s1[i] == s2[i]:
                        pos += 1

                    if s1[i] in cd:
                        pass
                    else:
                        cd[s1[i]] = s2.count(s1[i])
            count = 0
            for i, j in cd.items():
                if j > 1:
                    count += 1
            self.root6.deiconify()
            self.root6.update()
            T = f"{n1}, Exist: {exi}, position {pos}\nExists and Repeated: {count}, Total with Repeated: {sum(list(cd.values()))}\n"
            self.txt.insert(tk.END, T)
            self.txt.see(tk.END)
            self.root6.protocol("WM_DELETE_WINDOW", lambda: [self.root6.withdraw()])


class s:
    def __init__(self, c, root2):
        self.root2 = root2
        self.C = c

    def k(self):
        B = self.C.get()

        def I():
            D = A.get()
            if D in [""]:
                root11 = tk.Tk()
                root11.title("Key incorrect!")
                tk.Label(root11, text="oops! There is no key. Please put a valid key").pack()
                tk.Button(root11, text="OK", height=1, width=2, command=root11.destroy).pack()
            else:
                for i in range(len(D)):
                    if D[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        root12 = tk.Tk()
                        root12.title("Key incorrect!")
                        tk.Label(root12, text="The entered key is not valid, please enter a valid key").pack()
                        tk.Button(root12, text="OK", height=1, width=2, command=root12.destroy).pack()
                        root12.mainloop()
                        break
                    elif D[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        pass
                if len(D) == 4:
                    l4 = []
                    l5 = []
                    l6 = []
                    for i in range(len(D)):
                        if D.count(D[i]) > 1:
                            l4.append(D[i])
                        else:
                            l5.append(D[i])
                        l6.append(D[i])
                    if l4 == []:
                        root16.protocol("WM_DELETE_WINDOW", root16.withdraw)
                        if B == D:
                            root13 = tk.Tk()
                            root13.title("Congrats!")
                            root16.destroy()
                            tk.Label(root13, text="You guessed the correct Code", font="Arial 25 bold").pack()
                            tk.Button(root13, text="OK", command=lambda: (
                                root13.destroy(), root20.destroy(), self.root2.deiconify())).pack()
                        else:
                            root16.deiconify()
                            count = 0
                            count2 = 0
                            for i in range(4):
                                if D[i] == B[i]:
                                    count += 1
                            for i in range(4):
                                if D[i] in B:
                                    count2 += 1
                            N = f"{D}, Exist:, {count2}, position, {count} \n"
                            T.insert(tk.END, N)
                            T.see(tk.END)
                            root16.protocol("WM_DELETE_WINDOW", lambda: [root16.withdraw()])
                    else:
                        root14 = tk.Tk()
                        root14.title("Key incorrect!")
                        tk.Label(root14, text="Repeated digits not allowed, please enter a valid key").pack()
                        tk.Button(root14, text="OK", command=root14.destroy).pack()
                elif len(D) not in [0, 4]:
                    A.delete(0, tk.END)
                    D = ""
                    root15 = tk.Tk()
                    root15.title("Key incorrect!")
                    tk.Label(root15, text="Key is incorrect, please enter a 4 digit code").pack()
                    tk.Button(root15, text="OK", command=root15.destroy).pack()

        root20 = tk.Tk()
        root20.title("Mastermind: Level 1")
        tk.Label(root20, text="Enter The Code:", font="Arial 30 bold", justify="center").pack()
        A = tk.Entry(root20, width=15, font="Arial 15")
        A.pack()
        tk.Button(root20, text="Submit", command=I).pack()
        root16 = tk.Tk()
        root16.title("Hints")
        root16.geometry("400x500")
        T = tk.Text(root16, height=0, width=40)
        T.pack(fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(T, orient=tk.VERTICAL, command=T.yview)
        scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
        T.config(yscrollcommand=scrollbar.set)
        root16.withdraw()
        root20.protocol("WM_DELETE_WINDOW", lambda: [root20.destroy(), root16.destroy(), self.root2.deiconify()])
        root20.mainloop()


class big:
    def __init__(self):
        self.root2 = tk.Tk()
        self.root2.title("Mastermind: Level 1")
        tk.Label(self.root2, text="What Is The Key?(Numbered, 4 digits, no repeated digits)", font="Arial 20 bold",
                 justify="center").pack()
        self.C = tk.Entry(self.root2, width=15, font="Arial 15")
        self.C.pack()
        tk.Button(self.root2, text="Submit", height=1, width=5, command=lambda: self.g()).pack()
        self.root2.protocol("WM_DELETE_WINDOW", lambda: (root.deiconify(), self.root2.destroy()))
        root.mainloop()

    def g(self):
        B = self.C.get()
        if B in [""]:
            root3 = tk.Tk()
            root3.title("Key incorrect!")
            tk.Label(root3, text="oops! There is no key. Please put a key").pack()
            tk.Button(root3, text="OK", height=1, width=2, command=root3.destroy).pack()
        else:
            for i in range(len(B)):
                if B[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    root5 = tk.Tk()
                    root5.title("Key incorrect!")
                    tk.Label(root5, text="The entered key is not valid, please enter a valid key").pack()
                    tk.Button(root5, text="OK", height=1, width=2, command=root5.destroy).pack()
                    root5.mainloop()
                    break
                elif B[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    pass
            if len(B) == 4:
                l = []
                l2 = []
                l3 = []
                for i in range(len(B)):
                    if B.count(B[i]) > 1:
                        l.append(B[i])
                    else:
                        l2.append(B[i])
                    l3.append(B[i])
                if l == []:
                    root8 = tk.Toplevel(self.root2)
                    root8.title("Its 2nd player's turn!")
                    tk.Label(root8, text="Key format is correct, pass the game to second player and press ok").pack()
                    tk.Button(root8, text="OK",
                              command=lambda: [root8.destroy(), self.root2.withdraw(), s_obj := s(self.C, self.root2),
                                               s_obj.k()]).pack()
                    return B

                else:
                    root10 = tk.Tk()
                    root10.title("Key incorrect!")
                    tk.Label(root10, text="Repeated digits not allowed, please enter a valid key").pack()
                    tk.Button(root10, text="OK", command=root10.destroy).pack()
            elif len(B) not in [0, 4]:
                B = ""
                root9 = tk.Tk()
                root9.title("Key incorrect!")
                tk.Label(root9, text="Key is incorrect, please enter a 4 digit code").pack()
                tk.Button(root9, text="OK", command=root9.destroy).pack()


root = tk.Tk()
root.title("Mastermind")
tk.Label(root, text="Welcome! choose your level", font="Arial 14 bold", justify="center").pack()
tk.Button(root, text="Level 1", height=1, width=5, command=lambda: (root.withdraw(), big())).pack()
tk.Button(root, text="Level 2", height=1, width=5, command=lambda: (root.withdraw(), Lv2p1())).pack()
root.mainloop()
