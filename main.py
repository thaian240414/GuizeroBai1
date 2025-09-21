from guizero import App,Text


ung_dung = App(title="Hello world", width=800, height=600, bg="green yellow")

chu = Text(master= ung_dung, text="Welcome to the app")

ung_dung.display()
