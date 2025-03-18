from pathlib import Path
from tkinter import Tk, Canvas, Label, PhotoImage, Entry

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/jezzzcan/Desktop/TT2_Brainboard/Tkinter-Designer-master/seleccionarCarpeta/build/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_enter(label, hover_image):
    label.config(image=hover_image)

def on_leave(label, normal_image):
    label.config(image=normal_image)

def on_click(label, pressed_image):
    label.config(image=pressed_image)

def create_label(x, y, normal, hover, pressed, command):
    normal_image = PhotoImage(file=relative_to_assets(normal))
    hover_image = PhotoImage(file=relative_to_assets(hover))
    pressed_image = PhotoImage(file=relative_to_assets(pressed))
    
    label = Label(window, image=normal_image, borderwidth=0, highlightthickness=0, bg="#FFFFFF")
    label.image = normal_image
    label.place(x=x, y=y)
    
    label.bind("<Enter>", lambda event: on_enter(label, hover_image))
    label.bind("<Leave>", lambda event: on_leave(label, normal_image))
    label.bind("<ButtonPress-1>", lambda event: on_click(label, pressed_image))
    label.bind("<ButtonRelease-1>", lambda event: command())
    
    return label

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
canvas.create_image(74.0, 51.0, image=image_image_2)

canvas.create_text(
    75.0, 110.0,
    anchor="nw",
    text="Selecciona una carpeta para \n guardar/cargar creaciones:",
    fill="#FFFFFF",
    font=("Inter Black", 40 * -1)
)

canvas.create_text(
    49.0, 312.0,
    anchor="nw",
    text="Carpeta seleccionada:",
    fill="#FFFFFF",
    font=("Inter Black", 24 * -1)
)

# Crear labels en lugar de botones
create_label(36.0, 227.0, "button_1.png", "button_1_hover.png", "button_1_pressed.png", lambda: print("button_1 clicked"))
create_label(335.0, 227.0, "button_2.png", "button_2_hover.png", "button_2_pressed.png", lambda: print("button_2 clicked"))
create_label(233.0, 419.0, "button_3.png", "button_3_hover.png", "button_3_pressed.png", lambda: print("button_3 clicked"))

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(324.0, 380.5, image=entry_image_1)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(x=76.5, y=365.0, width=495.0, height=30.0)

window.resizable(False, False)
window.mainloop()