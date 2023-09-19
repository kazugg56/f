let i = 0
let a = 0
let b = 0
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {

    if (i >= 1) {
        i += 1
        basic.showNumber(a - b)
    }

})
input.onButtonPressed(Button.A, function on_button_pressed_a() {

    if (i == 0) {
        a += 0 - 1
        basic.showNumber(a)
    } else if (i == 1) {
        b += 0 - 1
        basic.showNumber(b)
    }

})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {

    if (i >= 1) {
        i += 1
        basic.showNumber(a / b)
    }

})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {

    i += 1
    if (i >= 2) {
        basic.showNumber(a + b)
    } else {
        basic.showNumber(0)
    }

})
input.onButtonPressed(Button.B, function on_button_pressed_b() {

    if (i == 0) {
        a += 1
        basic.showNumber(a)
    } else if (i == 1) {
        b += 1
        basic.showNumber(b)
    }

})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {

    if (i >= 1) {
        i += 1
        basic.showNumber(a * b)
    }

})

