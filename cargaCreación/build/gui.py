from pathlib import Path
from tkinter import Tk, Canvas, Label, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/jezzzcan/Desktop/TT2_Brainboard/Tkinter-Designer-master/cargaCreación/build/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_enter(event):
    event.widget.config(image=event.widget.hover_img)

def on_leave(event):
    event.widget.config(image=event.widget.normal_img)

def on_click(event, button_name):
    print(f"{button_name} presionado")
    event.widget.config(image=event.widget.pressed_img)

window = Tk()
window.geometry("640x480")
window.configure(bg="#FFFFFF")

window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 640
window_height = 480
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=480,
    width=640,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(320.0, 240.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
canvas.create_image(58.0, 50.0, image=image_image_2)

canvas.create_text(
    43.0, 92.0, anchor="nw", text="Selecciona una creación \n guardada:",
    fill="#FFFFFF", font=("Inter Black", 40 * -1)
)

def create_label(x, y, normal, hover, pressed, name):
    normal_img = PhotoImage(file=relative_to_assets(normal))
    hover_img = PhotoImage(file=relative_to_assets(hover))
    pressed_img = PhotoImage(file=relative_to_assets(pressed))
    
    label = Label(window, image=normal_img, borderwidth=0, highlightthickness=0, bg="#FFFFFF")
    
    # Guardar referencias dentro del Label
    label.normal_img = normal_img  
    label.hover_img = hover_img  
    label.pressed_img = pressed_img  

    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)
    label.bind("<ButtonPress-1>", lambda e: on_click(e, name))  # Pasar el nombre del botón
    label.bind("<ButtonRelease-1>", on_leave)  # Volver al estado normal al soltar

    label.place(x=x, y=y)
    return label

# Crear botones con imágenes de estado
create_label(94, 212, "button_1.png", "button_1_hover.png", "button_1_pressed.png", "Botón 1")
create_label(418, 368, "button_2.png", "button_2_hover.png", "button_2_pressed.png", "Botón 2")

window.resizable(False, False)
window.mainloop()