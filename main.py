import tkinter as tk


def set_brush_color(event):
    global brush_color

    brush_color = brush_color_var.get()


def set_brush_size(event):
    global brush_size
    brush_size = scale_brush_size.get()


def canvas_clear():
    canvas.delete('all')


def paint(event):
    pos = event.x - brush_size, event.y - brush_size, event.x + brush_size, event.y + brush_size
    canvas.create_oval(*pos, fill=brush_color, outline=brush_color)

root = tk.Tk()
root.geometry()
root['bg'] = '#282C34'
root.title('Paint')

canvas_width = 600
canvas_height = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=3, column=0, columnspan=10)
canvas.bind("<B1-Motion>", paint)

btn_canvas_clear = tk.Button(root, text="Clear", command=canvas_clear)
btn_canvas_clear.grid(row=0, column=0, stick='wens')

scale_brush_size = tk.Scale(root, orient=tk.HORIZONTAL, from_=2, to= 30)
scale_brush_size.grid(row=0, column=1, columnspan=2, stick='wens')
scale_brush_size.bind('<Leave>', set_brush_size)

frame_color = tk.Frame(root)
frame_color.grid(row=0, column=3, columnspan=3, rowspan=2, stick='wens')
frame_color.bind('<Leave>', set_brush_color)

brush_color_var = tk.StringVar()
brush_color_var.set('black')
color_red = tk.Radiobutton(frame_color, bg='red', variable=brush_color_var, value='red').grid(row=0, column=0, stick='wens')
color_green = tk.Radiobutton(frame_color, bg='green', variable=brush_color_var, value='green').grid(row=0, column=1, stick='wens')
color_blue = tk.Radiobutton(frame_color, bg='blue', variable=brush_color_var, value='blue').grid(row=0, column=2, stick='wens')
color_white = tk.Radiobutton(frame_color, bg='white', variable=brush_color_var, value='white').grid(row=1, column=0, stick='wens')
color_black = tk.Radiobutton(frame_color, bg='black', variable=brush_color_var, value='black').grid(row=1, column=1, stick='wens')
color_gray = tk.Radiobutton(frame_color, bg='gray', variable=brush_color_var, value='gray').grid(row=1, column=2, stick='wens')



brush_size = scale_brush_size.get()
brush_color = brush_color_var.get()

root.mainloop()

