def mknsmCalc(name, quantity):
    result = {}
    match name:
        case "塩ブロック":
            result = {
                "塩": quantity*4
            }
            return result
        case "木炭ブロック":
            result = {
                "木炭": quantity*9
            }
            return result
        case "オスミウムブロック":
            result = {
                "オスミウム": quantit*9
            }
            return result
        case "銅ブロック":
            result = {
                "銅": quantity*9
            }
            return result
        case "錫ブロック":
            result = {
                "錫": quantity*9
            }
            return result

