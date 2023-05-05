def mknsmCalc(name, quantity):
    match name:
        case "塩ブロック":
            match quantity:
                case quantity if quantity*4 >= 64:
                    result = {
                        "塩": f"{int(quantity*4/64)}スタックと{quantity*4-64*int(quantity*4/64)}個"
                    }
                    return result
                case _:
                    result = {
                        "塩": f"{quantity*4}個"
                    }
                    return result
        case "木炭ブロック":
            match quantity:
                case quantity if quantity*9 >= 64:
                    result = {
                        "木炭": f"{int(quantity*9/64)}スタックと{quantity*9-64*int(quantity*9/64)}個"
                    }
                    return result
                case _:
                    result = {
                        "木炭": f"{quantity*9}個"
                    }
        case _:
            return "有効な値を入力してください"
        
print(mknsmCalc("塩ブロック", 17))
print(mknsmCalc("塩ブロック", 15))
print(mknsmCalc("木炭ブロック", 17))
print(mknsmCalc("木炭ブロック", 15))
print(mknsmCalc("例外", 17))
