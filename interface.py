from tkinter import *
from tkinter import messagebox, ttk
from requests import get

def ConsultarCEP():
    global CEP, request
    requestExists = False
    CEP = CaixaEntry.get("1.0", END)
    CEP = str(CEP).strip()
    try:
        request = get(f'https://cep.awesomeapi.com.br/json/{CEP}').json()
        requestExists = True
    except:
        messagebox.showerror('ERRO!', 'CEP inválido. Por favor, digite um CEP válido.')
        apagarDados()
    finally:
        if requestExists is True:
            if 'status' in request:
                messagebox.showerror('ERRO!', 'CEP inválido. Por favor, digite um CEP válido.')
                apagarDados()
            else:
                global endereco, bairro, municipio_estado, ddd, cidade_ibge
                endereco = request['address']
                bairro = request['district']
                municipio_estado = f"{request['city']} - {request['state']}".lstrip().rstrip()
                ddd = request['ddd']
                cidade_ibge = request['city_ibge']

def copy_button(value):
    app.clipboard_clear()
    app.clipboard_append(value)
    app.update()

def apagarDados():
    CaixaCEP.config(state=NORMAL)
    CaixaEndereco.config(state=NORMAL)
    CaixaBairro.config(state=NORMAL)
    CaixaMunicipioEstado.config(state=NORMAL)
    CaixaDDD.config(state=NORMAL)
    CaixaCodIBGE.config(state=NORMAL)
    CaixaCEP.delete('1.0', END)
    CaixaEndereco.delete('1.0', END)
    CaixaBairro.delete('1.0', END)
    CaixaMunicipioEstado.delete('1.0', END)
    CaixaDDD.delete('1.0', END)
    CaixaCodIBGE.delete('1.0', END)
    CaixaCEP.config(state=DISABLED)
    CaixaEndereco.config(state=DISABLED)
    CaixaBairro.config(state=DISABLED)
    CaixaMunicipioEstado.config(state=DISABLED)
    CaixaDDD.config(state=DISABLED)
    CaixaCodIBGE.config(state=DISABLED)

# Passagem de dados para a tela de consulta de CEP
def CEPoutput():
    CaixaCEP.config(state=NORMAL)
    text = CaixaCEP.get('1.0', END)
    text = ''.join(CEP)
    CaixaCEP.delete('1.0', END)
    CaixaCEP.insert(END, str(text))
    CaixaCEP.config(state=DISABLED)

def EnderecoOutput():
    CaixaEndereco.config(state=NORMAL)
    endereco = request['address']
    text = CaixaEndereco.get('1.0', END)
    text = ''.join(endereco)
    CaixaEndereco.delete('1.0', END)
    CaixaEndereco.insert(END, str(text))
    CaixaEndereco.config(state=DISABLED)

def BairroOutput():
    CaixaBairro.config(state=NORMAL)
    bairro = request['district']
    text = CaixaBairro.get('1.0', END)
    text = ''.join(bairro)
    CaixaBairro.delete('1.0', END)
    CaixaBairro.insert(END, str(text))
    CaixaBairro.config(state=DISABLED)

def MunicipioEstadoOutput():
    CaixaMunicipioEstado.config(state=NORMAL)
    municipio_estado = f"{request['city']} - {request['state']}".lstrip().rstrip()
    text = CaixaMunicipioEstado.get('1.0', END)
    text = ''.join(municipio_estado)
    CaixaMunicipioEstado.delete('1.0', END)
    CaixaMunicipioEstado.insert(END, str(text))
    CaixaMunicipioEstado.config(state=DISABLED)

def DDDoutput():
    CaixaDDD.config(state=NORMAL)
    ddd = request['ddd']
    text = CaixaDDD.get('1.0', END)
    text = ''.join(ddd)
    CaixaDDD.delete('1.0', END)
    CaixaDDD.insert(END, str(text))
    CaixaDDD.config(state=DISABLED)

def CodIBGEoutput():
    CaixaCodIBGE.config(state=NORMAL)
    cidade_ibge = request['city_ibge']
    text = CaixaCodIBGE.get('1.0', END)
    text = ''.join(cidade_ibge)
    CaixaCodIBGE.delete('1.0', END)
    CaixaCodIBGE.insert(END, str(text))
    CaixaCodIBGE.config(state=DISABLED)

def GeneralOutput():
    ConsultarCEP()
    CEPoutput()
    EnderecoOutput()
    BairroOutput()
    MunicipioEstadoOutput()
    DDDoutput()
    CodIBGEoutput()

app = Tk()
app.title('Consultor de CEP')
app.geometry('350x465')
app.resizable(False, False)
app.configure(background='#b9b9c9')

backgroundColor = '#b9b9c9'
copyButtonX = 300

Titulo = Label(app, text='Consultor de CEP', bg=backgroundColor, fg='black', font=('Arial', 20))
Titulo.place(x=68, y=10)

separator = ttk.Separator(app, orient='horizontal')
separator.pack(fill='x', pady=52)

TextoCX1 = Label(app, text='Digite o CEP: ', background=backgroundColor, fg='black', font=('Arial', 12))
TextoCX1.place(x=10, y=60)

CaixaEntry = Text(app, width=25, height=1, font=('Arial', 12))
CaixaEntry.place(x=10, y=85)

BotaoEnviar = Button(app, text='Consultar', width=9, height=1, bg='#26992a', command=ConsultarCEP)
BotaoEnviar.place(x=245, y=83)

OBS = Label(app, text='OBS: Digite somente os números do CEP', background=backgroundColor, fg='black', font=('Arial', 9))
OBS.place(x=10, y=115)

# DADOS OBTIDOS
TextoCEP = Label(app, text='CEP', background=backgroundColor, fg='#009', font=('Arial', 11))
TextoCEP.place(x=10, y=150)

CaixaCEP =  Text(app, width=34, height=1, font=('Arial', 11))
CaixaCEP.place(x=10, y=175)

photo = PhotoImage(file="C:/Users/macie/OneDrive/Área de Trabalho/Projetos/Projetos - Python/Projetos com uso de API e Interface Grafica/Consulta de CEP/imagens/logoCopiarEColar.png")

CoppyButtonCEP = Button(app, text='Copiar', width=25, height=25, image=photo, bg='#969997', command=lambda: copy_button(CEP.strip()))
CoppyButtonCEP.place(x=copyButtonX, y=170)

TextoEndereco = Label(app, text='Endereço', background=backgroundColor, fg='#009', font=('Arial', 11))
TextoEndereco.place(x=10, y=200)

CaixaEndereco =  Text(app, width=34, height=1, font=('Arial', 11))
CaixaEndereco.place(x=10, y=225)

CoppyButtonEndereco = Button(app, text='Copiar', width=25, height=25, image=photo, bg='#969997', command=lambda: copy_button(endereco.strip()))
CoppyButtonEndereco.place(x=copyButtonX, y=220)

TextoBairro = Label(app, text='Bairro', background=backgroundColor, fg='#008', font=('Arial', 11))
TextoBairro.place(x=10, y=250)

CaixaBairro =  Text(app, width=34, height=1, font=('Arial', 11))
CaixaBairro.place(x=10, y=275)

CoppyButtonBairro = Button(app, text='Copiar', width=25, height=25, image=photo, bg='#969997', command=lambda: copy_button(bairro.strip()))
CoppyButtonBairro.place(x=copyButtonX, y=270)

TextoMunicipioEstado = Label(app, text='Munícipio e Estado', background=backgroundColor, fg='#009', font=('Arial', 11))
TextoMunicipioEstado.place(x=10, y=300)

CaixaMunicipioEstado =  Text(app, width=34, height=1, font=('Arial', 11))
CaixaMunicipioEstado.place(x=10, y=325)

CoppyButtonMunicipioEstado = Button(app, text='Copiar', width=25, height=25, image=photo, bg='#969997', command=lambda: copy_button(municipio_estado.lstrip().rstrip()))
CoppyButtonMunicipioEstado.place(x=copyButtonX, y=320)

TextoDDD = Label(app, text='DDD', background=backgroundColor, fg='#009', font=('Arial', 11))
TextoDDD.place(x=10, y=350)

CaixaDDD =  Text(app, width=34, height=1, font=('Arial', 11))
CaixaDDD.place(x=10, y=375)

CoppyButtonDDD = Button(app, text='Copiar', width=25, height=25, image=photo, bg='#969997', command=lambda: copy_button(ddd.strip()))
CoppyButtonDDD.place(x=copyButtonX, y=370)

TextoCodIBGE = Label(app, text='Código de Cidade do IBGE', background=backgroundColor, fg='#009', font=('Arial', 11))
TextoCodIBGE.place(x=10, y=400)

CaixaCodIBGE =  Text(app, width=34, height=1, font=('Arial', 11))
CaixaCodIBGE.place(x=10, y=425)

CoppyButtonCodIBGE = Button(app, text='Copiar', width=25, height=25, image=photo, bg='#969997', command=lambda: copy_button(cidade_ibge.strip()))
CoppyButtonCodIBGE.place(x=copyButtonX, y=420)

BotaoEnviar.configure(command=GeneralOutput)

app.mainloop()