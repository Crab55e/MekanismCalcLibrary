def mknsmCalc(name, quantity):
    match name:
        case "塩ブロック":
            match quantity:
                case quantity if quantity*4 >= 64:
                    result = {
                        "塩": f"{int(quantity*4/64)}スタックと{quantity*4%64}個"
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
                        "木炭": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
                    }
                    return result
                case _:
                    result = {
                        "木炭": f"{quantity*9}個"
                    }
                    return result
        case "銅ブロック":
            match quantity:
                case quantity if quantity*9 >= 64:
                    result = {
                        "銅インゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
                    }
                    return result
                case _:
                    result = {
                        "銅インゴット": f"{quantity*9}個"
                    }
                    return result
        case "錫ブロック":
            match quantity:
                case quantity if quantity*9 >= 64:
                    result = {
                        "錫インゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
                    }
                    return result
                case _:
                    result = {
                        "錫インゴット": f"{quantity*9}個"
                    }
                    return result
        case "鉛ブロック":
            match quantity:
                case quantity if quantity*9 >= 64:
                    result = {
                        "鉛インゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
                    }
                    return result
                case _:
                    result = {
                        "鉛インゴット": f"{quantity*9}個"
                    }
                    return result
        case "ウランブロック":
            match quantity:
                case quantity if quantity*9 >= 64:
                    result = {
                        "ウランインゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
                    }
                    return result
                case _:
                    result = {
                        "ウランインゴット": f"{quantity*9}個"
                    }
                    return result
        case "鋼鉄ブロック":
            match quantity:
                case quantity if quantity*9 >= 64:
                    result = {
                        "鋼鉄インゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
                    }
                    return result
                case _:
                    result = {
                        "鋼鉄インゴット": f"{quantity*9}個"
                    }
                    return result
        case "青銅ブロック":
            match quantity:
                case quantity if quantity*9 >= 64:
                    result = {
                        "青銅インゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
                    }
                    return result
                case _:
                    result = {
                        "青銅インゴット": f"{quantity*9}個"
                    }
                    return result
        case "精製黒曜石ブロック":
            match quantity:
                case quantity if quantity*9 >= 64:
                    result = {
                        "精製黒曜石インゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
                    }
                    return result
                case _:
                    result = {
                        "精製黒曜石インゴット": f"{quantity*9}個"
                    }
                    return result
        case "精製グロウストーンブロック":
            match quantity:
                case quantity if quantity*9 >= 64:
                    result = {
                        "精製グロウストーンインゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
                    }
                    return result
                case _:
                    result = {
                        "精製グロウストーンインゴット": f"{quantity*9}個"
                    }
                    return result
        case _:
            return "有効な値を入力してください"
print(mknsmCalc("塩ブロック", 20))
