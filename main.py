from guizero import App, Text, TextBox, PushButton, Box

def bloqueia_janela(app:App):
    app.tk.attributes('-toolwindow', 1)
    app.tk.resizable(False, False)

app = App(title="Gerenciador MEPOUPE",bg='#EDE7DF', width='400',height='250')
bloqueia_janela(app)
ghost_box_1 = Box(app, width='fill',height=75)
box_info = Box(app, layout='grid')
email_text = Text(box_info, text="Email:", grid=[0,0], size=15, font='Times')
user_input = TextBox(box_info,grid=[1,0], width='fill')
user_input.bg = 'white'
pwd_text = Text(box_info, text="Senha:", grid=[0,1], size=15,font='Times')
pwd_input = TextBox(box_info, hide_text=True, grid=[1,1], width='fill')
pwd_input.bg = 'white'
app.display()