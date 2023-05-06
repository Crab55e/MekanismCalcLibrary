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
        case "発展制御回路":
            match quantity:
                case quantity if  quantity*2 >= 64:
                    result = {
                        "吹込合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                        "基本制御回路": f"{int(quantity/64)スタックと{quantity%64}個}"
                    }
                    return result
                case _:
                    result = {
                        "吹込合金": f"{quantity*2}個",
                        "基本制御回路": f"{quantity}個"
                    }
                    return result
        case "精鋭制御回路": 
            match quantity:
                case quantity if quantity*2 >= 64:
                    result = {
                        "強化合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                        "発展制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
                    }
                    return result
                case _:
                    result = {
                        "強化合金": f"{quantity*2}個",
                        "発展制御回路": f"{quantity}個"
                    }
                    return result
        case "究極制御回路":
            match quantity:
                case quantity if quantity*2 >=64:
                    result = {
                        "原子合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                        "精鋭制御回路": f"{int(quantity/64)}スタックと{quantity*2%64}個"
                    }
                    return result
                case _:
                    result = {
                        "原子合金": f"{quantity*2}個",
                        "精鋭制御回路": f"{quantity}個"
                    }
                    return result
        case "電解コア":
            match quantity:
                case quantity if quantity*5 >=64:
                    result = {
                        "吹込合金": f"{int(quantity*5/64)}スタックと{quantity*5%64}個",
                        "オスミウムの粉": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                        "金の粉": f"{int(quantity/64)}スタックと{quantity%64}個",
                        "鉄の粉": f"{int(quantity/64)}スタックと{quantity%64}個"
                    }
                    return result
                case _:
                    result = {
                        "吹込合金": f"{quantity*5}個",
                        "オスミウムの粉": f"{quantity*2}個",
                        "金の粉": f"{quantity}個",
                        "鉄の粉": f"{quantity}個"
                    }
                    return result
        case "テレポーテーションコア":
            match quantity:
                case quantity if quantity*4 >=64:
                    result = {
                        "ラピスラズリ": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                        "原子合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                        "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                        "ダイヤモンド": f"{int(quantity/64)}スタックと{quantity%64}個"
                    }
                    return result
                case _:
                    result = {
                        "ラピスラズリ": f"{quantity*4}個",
                        "原子合金": f"{quantity*2}個",
                        "金インゴット": f"{quantity*2}個",
                        "ダイヤモンド": f"{quantity}個"
                    }
                    return result
        case "HDPEシート":
            match quantity:
                case quantity*3 >= 64:
                    result = {
                        "HDPEペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                        "注意": "濃縮室で濃縮した場合の数値です"
                    }
                    return result
                case _:
                    result = {
                        "HDPEペレット": f"{quantity*3}個",
                        "注意": "濃縮室で濃縮した場合の数値です"
                    }
                    return result
        case "HDPEの棒":
            match quantity:
                case quantity if quantity*4 >= 64:
                    result = {
                        "HDPEペレット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個"
                    }
                    return result
                case _:
                    result = {
                        "HDPEペレット": f"{quantity*4}個"
                    }
                    return result
        case _:
            return "有効な値を入力してください"


