def Calc(expression):
    result = 0
    while '/' in expression:
        i = expression.index('/')
        result = expression[i-1] / expression[i+1]
        # del expression[i+1], expression[i], expression[i-1]
        # expression.insert(i-1,a)
        expression = expression[:i - 1] + [result] + expression[i + 2:]
    while '*' in expression:
        i = expression.index('*')
        result = expression[i-1] * expression[i+1]
        # del expression[i+1], expression[i], expression[i-1]
        # expression.insert(i-1,a) 
        expression = expression[:i - 1] + [result] + expression[i + 2:]
    while '-' in expression:
        i = expression.index('-')
        result = expression[i-1] - expression[i+1]
        # del expression[i+1], expression[i], expression[i-1]
        # expression.insert(i-1,a)
        expression = expression[:i - 1] + [result] + expression[i + 2:]
    while '+' in expression:
        i = expression.index('+')
        result = expression[i-1] + expression[i+1]
        # del expression[i+1], expression[i], expression[i-1]
        # expression.insert(i-1,a)
        expression = expression[:i - 1] + [result] + expression[i + 2:]
    
    return result
