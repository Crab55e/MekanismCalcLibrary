def Calc(name, quantity):
    if name == "塩ブロック":
        if quantity*4 >= 64:
            return {
                "塩": f"{int(quantity*4/64)}スタックと{quantity*4%64}個"
            }
        else:
            return {"塩": f"{quantity*4}個"}
    if name == "木炭ブロック":
        if quantity*9 >= 64:
            return {
                "木炭": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
            }
        else:
            return {
                "木炭": f"{quantity*9}個"
            }
    if name == "オスミウムブロック":
        if quantity*9 >= 64:
            return {
                "オスミウムインゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
            }
        else:
            return {
                "オスミウムインゴット": f"{quantity*9}個"
            }
    if name == "銅ブロック":
        if quantity*9 >= 64:
            return {
                "銅インゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
            }
        else:
            return {
                "銅インゴット": f"{quantity*9}個"
            }
    if name == "錫ブロック":
        if quantity*9 >= 64:
            return {
                "錫インゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
            }
        else:
            return {
                "錫インゴット": f"{quantity*9}個"
            }
    if name == "鉛ブロック":
        if quantity*9 >= 64:
            return {
                "鉛インゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
            }
        else:
            return {
                "鉛インゴット": f"{quantity*9}個"
            }
    if name == "ウランブロック":
        if quantity*9 >= 64:
            return {
                "ウランインゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
            }
        else:
            return {
                "ウランインゴット": f"{quantity*9}個"
            }
    if name == "鋼鉄ブロック":
        if quantity*9 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*9}個"
            }
    if name == "青銅ブロック":
        if quantity*9 >= 64:
            return {
                "青銅インゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
            }
        else:
            return {
                "青銅インゴット": f"{quantity*9}個"
            }
    if name == "精製黒曜石ブロック":
        if quantity*9 >= 64:
            return {
                "精製黒曜石インゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
            }
        else:
            return {
                "精製黒曜石インゴット": f"{quantity*9}個"
            }
    if name == "精製グロウストーンブロック":
        if quantity*9 >= 64:
            return {
                "精製グロウストーンインゴット": f"{int(quantity*9/64)}スタックと{quantity*9%64}個"
            }
        else:
            return {
                "精製グロウストーンインゴット": f"{quantity*9}個"
            }
    if name == "発展制御回路":
        if quantity*2 >= 64:
            return {
                "吹込合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*2}個",
                "基本制御回路": f"{quantity}個"
            }
    if name == "精鋭制御回路":
        if quantity*2 >= 64:
            return {
                "強化合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*2}個",
                "発展制御回路": f"{quantity}個"
            }
    if name == "究極制御回路":
        if quantity*2 >= 64:
            return {
                "原子合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*2}個",
                "精鋭制御回路": f"{quantity}個"
            }
    if name == "電解コア":
        if quantity*5 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*5%64}個",
                "オスミウムの粉": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "金の粉": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鉄の粉": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*5}個",
                "オスミウムの粉": f"{quantity*2}個",
                "金の粉": f"{quantity}個",
                "鉄の粉": f"{quantity}個"
            }
    if name == "テレポーテーションコア":
        if quantity*4 >= 64:
            return {
                "ラピスラズリ": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*4%64}個",
                "原子合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンド": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "ラピスラズリ": f"{quantity*4}個",
                "金インゴット": f"{quantity*2}個",
                "原子合金": f"{quantity*2}個",
                "ダイヤモンド": f"{quantity}個"
            }
    if name == "HDPEシート":
        if quantity*3 >= 64:
            return {
                "HDPEペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "注意": "濃縮室で濃縮した場合の数値です"
            }
        else:
            return {
                "HDPEペレット": f"{quantity*3}個",
                "注意": "濃縮室で濃縮した場合の数値です"
            }
    else:
        return "有効な値を入力してください"
    
