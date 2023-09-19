i = 0
a = 0
b = 0

def on_pin_pressed_p0():
    global i
    if i >= 1:
        i += 1
        basic.show_number(a - b)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global a, b
    if i == 0:
        a += 0 - 1
        basic.show_number(a)
    elif i == 1:
        b += 0 - 1
        basic.show_number(b)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    global i
    if i >= 1:
        i += 1
        basic.show_number(a / b)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    global i
    i += 1
    if i >= 2:
        basic.show_number(a + b)
    else:
        basic.show_number(0)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global a, b
    if i == 0:
        a += 1
        basic.show_number(a)
    elif i == 1:
        b += 1
        basic.show_number(b)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global i
    if i >= 1:
        i += 1
        basic.show_number(a * b)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
