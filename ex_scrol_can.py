import tkinter as tk
from tkinter import Frame, Canvas, Scrollbar, Button

global size_x, size_y, canvas1, canvas2, block1, block2
size_x = size_y = 150
block1 = block2 = ''


def onscroll(axis, *args):
    global canvas1, canvas2
    print(f'axis: {axis} and args are {[*args]}                           ',
          end='\r')
    if axis == 'x-axis':
        canvas1.xview(*args)
        canvas2.xview(*args)
    elif axis == 'y-axis':
        canvas1.yview(*args)
        canvas2.yview(*args)

    else:
        assert False, f"axis {axis} is incorrect, use 'x-axis' or 'y-axis'"


def onresize(enlarge, *args):
    global size_x, size_y
    print(f'enlarge: {enlarge} and args are {[*args]}                    ',
          end='\r')
    if enlarge:
        size_x *= 1.1
        size_y *= 1.1
    else:
        size_x /= 1.1
        size_y /= 1.1


def main():
    global canvas1, canvas2, block1, block2
    root = tk.Tk()
    frame1 = Frame(root, bg='grey')
    frame1.grid(row=0, column=0)
    frame2 = Frame(root, bg='grey')
    frame2.grid(row=0, column=1)
    frame3 = Frame(root, bg='grey')
    frame3.grid(row=0, column=2)

    yscrollbar = Scrollbar(frame3, orient='vertical',
                           command=lambda *args: onscroll('y-axis', *args))
    yscrollbar.pack(side='right', fill='y', expand='yes')
    xscrollbar = Scrollbar(frame3, orient='horizontal',
                           command=lambda *args: onscroll('x-axis', *args))
    xscrollbar.pack(side='bottom', fill='x', expand='yes')

    reduce_button = Button(frame3, text='reduce ',
                           command=lambda *args: onresize(False, *args))
    reduce_button.pack(side='right', anchor='ne')
    enlarge_button = Button(frame3, text='enlarge',
                            command=lambda *args: onresize(True, *args))
    enlarge_button.pack(side='right', anchor='ne')

    canvas1 = Canvas(frame1, width=200, height=200, bg="blue",
                     scrollregion=(0, 0, 500, 500),
                     yscrollcommand=yscrollbar.set,
                     xscrollcommand=xscrollbar.set)
    canvas1.pack(side='right')
    canvas2 = Canvas(frame2, width=200, height=200, bg="yellow",
                     scrollregion=(0, 0, 500, 500),
                     yscrollcommand=yscrollbar.set,
                     xscrollcommand=xscrollbar.set)
    canvas2.pack()

    canvas3 = Canvas(frame3, width=200, height=200, bg='pink')
    canvas3.pack()

    while True:
        canvas1.delete(block1)
        canvas2.delete(block2)
        block1 = canvas1.create_rectangle(100, 100, size_x, size_y,
                                          fill='orange')
        block2 = canvas2.create_rectangle(100, 100, size_x, size_y,
                                          fill='blue')
        root.update()

    root.mainloop()


if __name__ == "__main__":
    main()