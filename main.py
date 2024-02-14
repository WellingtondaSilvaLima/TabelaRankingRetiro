from tkinter import *

def somando(pontos, recebe, pontos_equipe, novos_pontos, equipe):
    try:
        provas = recebe.get()
        somar = int(pontos_equipe) + int(provas)
        pontos['text'] = str(somar)
        recebe.delete(0, END)

        gravando(str(somar), novos_pontos, equipe)
    except:
        pop = Toplevel(janela)
        pop.title('Erro')
        pop.geometry('250x100+500+200')
        pop.configure(bg=cor_fundo, padx=10, pady=15)
        Label(pop, text='Pontos errados.', font='Times 18', bg=cor_fundo, fg='#fff').pack()

def gravando(pontos, novos_pontos, equipe):
    for item in novos_pontos:
        try:
            if equipe in item:
                item[1] = pontos
                # Fazendo o tratamento
                aguia = f'{novos_pontos[0][0]}*{novos_pontos[0][1]}/'
                touro = f'{novos_pontos[1][0]}*{novos_pontos[1][1]}/'
                leao = f'{novos_pontos[2][0]}*{novos_pontos[2][1]}'
                novos_pontos = aguia + touro + leao
                
                with open('ranking.txt', 'w') as arquivo:
                    arquivo.write(novos_pontos)
        except:
            pop = Toplevel(janela)
            pop.title('Erro')
            pop.geometry('50x50+500+200')
            pop.configure(bg=cor_fundo, padx=10, pady=15)
            Label(pop, text='Pontos errados.', font='Times 18', bg=cor_fundo, fg='#fff').pack()

# Ler o arquivo de ranking---------------------
with open('ranking.txt', 'r') as arquivo:
    pontos = arquivo.read()

pontos = pontos.split('/')

novos_pontos = []
for item in pontos:
    novos_pontos.append(item.split('*'))
#-----------------------------------------------

janela = Tk()

janela.title('Ranking Retiro')

janela.iconbitmap(bitmap='images/4.ico')

cor_fundo = '#000000'
janela.geometry('600x470+400+100')
janela.configure(bg=cor_fundo, padx=10, pady=15)
janela.resizable(False, False)

titulo = Label(janela, text='Igreja: O Evangelho Visível',
               bg=cor_fundo, fg='#fff',
               font='Sans 20 bold', pady=20)
titulo.grid(column=1, row=0, columnspan=2)


images = [f'images/1.png', f'images/2.png', f'images/3.png']
img_1 = PhotoImage(file=images[0])
Label(janela, image=img_1, bg=cor_fundo).grid(column=0, row=1, pady=20)
# Tornar Dinâmico
pontos_1 = Label(janela, text=novos_pontos[0][1],
                        bg=cor_fundo, fg='#fff',
                        font='Comics 16')
pontos_1.grid(column=1, row=1, pady=20)

recebe_1 = Entry(janela, width=10, justify='center', font='Comics 14')
recebe_1.grid(column=2, row=1, pady=20)

# Colocar uma ação
try:
    btn_soma_1 = Button(janela, text='Somar', anchor=CENTER, width=10,
                        font='Comics 14',
                        command=lambda: somando(pontos_1, recebe_1,
                                                novos_pontos[0][1],
                                                novos_pontos, 'Aguia'))
    btn_soma_1.grid(column=3, row=1, pady=20)
except:
    pop = Toplevel(janela)
    pop.title('Erro')
    pop.geometry('50x50+500+200')
    pop.configure(bg=cor_fundo, padx=10, pady=15)
    Label(pop, text='Pontos errados.', font='Times 18', bg=cor_fundo, fg='#fff').pack()


img_2 = PhotoImage(file=images[1])
Label(janela, image=img_2, bg=cor_fundo).grid(column=0, row=2, pady=20)
# Tornar Dinâmico
pontos_2 = Label(janela, text=novos_pontos[1][1],
                        bg=cor_fundo, fg='#fff',
                        font='Comics 16')
pontos_2.grid(column=1, row=2, pady=20)

recebe_2 = Entry(janela, width=10, justify='center', font='Comics 14')
recebe_2.grid(column=2, row=2, pady=20)

# Colocar uma ação
try:
    btn_soma_2 = Button(janela, text='Somar', anchor=CENTER, width=10,
                    font='Comics 14',
                    command=lambda: somando(pontos_2, recebe_2,
                                                novos_pontos[1][1],
                                                novos_pontos, 'Touro'))
    btn_soma_2.grid(column=3, row=2, pady=20)
except:
    pop = Toplevel(janela)
    pop.title('Erro')
    pop.geometry('50x50+500+200')
    pop.configure(bg=cor_fundo, padx=10, pady=15)
    Label(pop, text='Pontos errados.', font='Times 18', bg=cor_fundo, fg='#fff').pack()


img_3 = PhotoImage(file=images[2])
Label(janela, image=img_3, bg=cor_fundo).grid(column=0, row=3, pady=20)
# Tornar Dinâmico
pontos_3 = Label(janela, text=novos_pontos[2][1],
                        bg=cor_fundo, fg='#fff',
                        font='Comics 16')
pontos_3.grid(column=1, row=3, pady=20)

recebe_3 = Entry(janela, width=10, justify='center', font='Comics 14')
recebe_3.grid(column=2, row=3, pady=20)

# Colocar uma ação
try:
    btn_soma_3 = Button(janela, text='Somar', anchor=CENTER, width=10,
                    font='Comics 14',
                    command=lambda: somando(pontos_3, recebe_3,
                                                novos_pontos[2][1],
                                                novos_pontos, 'Leao'))
    btn_soma_3.grid(column=3, row=3, pady=20)
except:
    pop = Toplevel(janela)
    pop.title('Erro')
    pop.geometry('50x50+500+200')
    pop.configure(bg=cor_fundo, padx=10, pady=15)
    Label(pop, text='Pontos errados.', font='Times 18', bg=cor_fundo, fg='#fff').pack()


janela.mainloop()
