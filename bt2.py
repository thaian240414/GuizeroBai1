from guizero import App,Text

app = App(title="Hộp thoại của tôi",bg="#FFFFFB")

text = Text(master= app, text="Thái An", color="#E98D9E")

text1 = Text(master=app,text="Học GUI thật thú vị!", color="#C13346")

app.display()