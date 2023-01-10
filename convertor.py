def convert_expression(text):
    result = []
    digit = ""
    while text[0] == '-':
        text = '0' + text
    for symbol in str(text):
        if symbol.isdigit():
            digit += symbol
        else:
            result.append(float(digit))
            digit = ""
            result.append(symbol) 
    else:
        if digit:
            result.append(float(digit))
    print(result)
    while ',' in result:
        i = result.index(',')
        result[i] = '.'
    while '.' in result:
        i = result.index('.')
        decimal_num = str(int(result[i-1])) + result[i] + str(int(result[i+1]))
        result = result[:i - 1] + [float(decimal_num)] + result[i + 2:]
    print(result)
    return result
