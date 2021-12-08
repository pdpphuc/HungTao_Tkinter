from Game_CatchApple import *

window=Tk()
window.title('Hứng táo')
window.geometry("+350+100")
icon = PhotoImage(file = "photos/apple.png")
window.iconphoto(False, icon)

canvas=Canvas(master=window, width=700, height=525, background='white')
canvas.pack()

Game_CatchApple(canvas)

window.mainloop()