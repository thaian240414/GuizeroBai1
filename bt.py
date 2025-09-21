from guizero import App, Text

app = App(title="Luyện tập Bài 2", width=600, height=400, bg= "lightblue")

text = Text(master=app, text="Xin chào, tôi đang học GUIZERO",size=16,color="red")

app.display()