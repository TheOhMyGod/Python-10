import calculator, convertor

def button_click(text):
    primer = convertor.convert_expression(text)
    result = calculator.Calc(primer)
    return
