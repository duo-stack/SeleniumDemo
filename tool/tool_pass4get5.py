def tool_pass4get5(target_float: float, target_length: int = 2):
    num2part = str(target_float).split('.')
    if (len(num2part) > 1) and (len(num2part[1]) > target_length + 1):
        num2part[1] = num2part[1][: target_length + 1]
        symbol = "-" if num2part[0][0] == "-" else "+"
        if symbol == "-":
            num2part[0] = num2part[0][1:]
        num2part[1] = '1' + num2part[1]
        if eval(num2part[1][-1]) >= 5:
            num2part[1] = str(eval(num2part[1][: -1]) + 1)
            if num2part[1][0] == '2':
                num2part[0] = str(eval(num2part[0]) + 1)
                num2part[1] = '0'
            else:
                num2part[1] = num2part[1][1:]
        else:
            num2part[1] = num2part[1][1: -1]
        if len(num2part[1]) == 0:
            num2part[1] = '0'
        result = eval(symbol + num2part[0] + '.' + num2part[1])
    else:
        result = target_float
    if target_length == 0:
        return int(result)
    else:
        if type(result) is int:
            return float(result)
        return result


if __name__ == "__main__":
    print(tool_pass4get5(3190.0499999999997))
