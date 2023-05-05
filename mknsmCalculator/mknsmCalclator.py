def mknsmCalc(name, quantity):
    match name:
        case "塩ブロック":
            match quantity:
                case quantity if quantity*4 > 64:
                    result = {
                        "塩": quantity*4
                    }
                    return result
                case _:
                    result = {
                        "塩": quantity*4
                    }
                    return result
        