def mknsmCalc(name, quantity):
    match name:
        case "塩ブロック":
            match quantity:
                case quantity if quantity*4 > 64:
                    result = {
                        "塩": f"{int(quantity*4/64)}スタックと{quantity%64}個"
                    }
                    return result
                case _:
                    result = {
                        "塩": f"{quantity*4}個"
                    }
                    return result

