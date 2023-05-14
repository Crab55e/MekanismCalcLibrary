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
    if name == "HDPEの棒":
        if quantity*4 >= 64:
            return {
                "HDPEペレット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個"
            }
        else:
            return {
                "HDPEペレット": f"{quantity*4}個"
            }
    if name == "プラ棒":
        if quantity*2 >= 64:
            return {
                "HDPEの棒": f"{int(quantity*2/64)}スタックと{quantity*2%64}個"
            }
        else:
            return {
                "HDPEの棒": f"{quantity*2}個"
            }
    if name == "核廃棄物バレル":
        if quantity*4 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "鉛インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*4}個",
                "鉛インゴット": f"{int(quantity*4)}個"
            }
    if name == "工業用アラーム":
        if quantity*6 >= 64:
            return {
                "鉛インゴット": f"{int(quantity*6/64)}スタックと{quantity*6%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "レッドストーンランプ": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鉛インゴット": f"{quantity*6}個",
                "基本制御回路": f"{quantity*2}個",
                "レッドストーンランプ": f"{quantity}個"
            }
    if name == "スキューバマスク":
        if quantity*3 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "ガラス": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*3}個",
                "ガラス": f"{quantity*2}個",
                "基本制御回路": f"{quantity}個"
            }
    if name == "潜水タンク":
        if quantity*3 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "吹込合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity/64)}スタックと{quantity%64}個",
                "化学タンク(種類不問)": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*3}個",
                "吹込合金": f"{quantity*2}個",
                "基本制御回路": f"{quantity}個",
                "化学タンク(種類不問)": f"{quantity}個"
            }
    if name == "ジェットパック":
        if quantity*3 >= 64:
            return {
                "錫インゴット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "鋼鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity/64)}スタックと{quantity%64}個",
                "化学タンク": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "錫インゴット": f"{quantity*3}個",
                "鋼鉄インゴット": f"{quantity*2}個",
                "基本制御回路": f"{quantity}個",
                "化学タンク": f"{quantity}個"
            }
    if name == "装甲ジェットパック":
        if quantity*2 >= 64:
            return {
                "ダイヤモンドの粉": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "青銅インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ブロック": f"{int(quantity/64)}スタックと{quantity%64}個",
                "ジェットパック": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "ダイヤモンドの粉": f"{quantity*2}個",
                "青銅インゴット": f"{quantity*2}個",
                "鋼鉄ブロック": f"{quantity}個",
                "ジェットパック": f"{quantity}個"
            }
    if name == "フリーランナー":
        if quantity*2 >= 64:
            return {
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "吹込合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "エネルギータブレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個"
            }
        else:
            return {
                "基本制御回路": f"{quantity*2}個",
                "吹込合金": f"{quantity*2}個",
                "エネルギータブレット": f"{quantity*2}個"
            }
    if name == "原子分解機":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "原子合金": f"{int(quantity/64)}スタックと{quantity%64}個",
                "精製黒曜石インゴット": f"{int(quantity/64)}スタックと{quantity%64}個",
                "エネルギータブレット": f"{int(quantity/64)}スタックと{quantity%64}個",
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "原子合金": f"{quantity}個",
                "精製黒曜石インゴット": f"{quantity}個",
                "エネルギータブレット": f"{quantity}個"
            }
    if name == "エレクトリックボウ":
        if quantity*3 >= 64:
            return{
                "糸": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "吹込合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "エネルギータブレット": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "糸": f"{quantity*3}個",
                "吹込合金": f"{quantity*2}個",
                "エネルギータブレット": f"{quantity}個"
            }
    if name == "火炎放射器":
        if quantity*4 >= 64:
            return {
                "錫インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "青銅インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "火打石と打ち金": f"{int(quantity/64)}スタックと{quantity%64}個",
                "発展制御回路": f"{int(quantity/64)}スタックと{quantity%64}個",
                "化学タンク(種類不問)": f"{int(quantity/64)}スタックと{quantity%64}個",
            }
        else:
            return {
                "錫インゴット": f"{quantity*4}個",
                "青銅インゴット": f"{quantity*2}個",
                "火打石と打ち金": f"{quantity}個",
                "発展制御回路": f"{quantity}個",
                "化学タンク": f"{quantity}個"
                }
    if name == "エネルギータブレット":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "金インゴット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "吹込合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "金インゴット": f"{quantity*3}個",
                "吹込合金": f"{quantity*2}個"
            }
    if name == "コンフィギュレーター":
        if quantity*2 >= 64:
            return {
                "吹込合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ラピスラズリ": f"{int(quantity/64)}スタックと{quantity%64}個",
                "エネルギータブレット": f"{quantity/64}スタックと{quantity%64}個",
                "棒": f"{quantity/64}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*2}個",
                "ラピスラズリ": f"{quantity}個",
                "エネルギータブレット": f"{quantity}個",
                "棒": f"{quantity}個"
            }
    if name == "ネットワークリーダー":
        if quantity*2 >= 64:
            return {
                "吹込合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ガラス": f"{int(quantity/64)}スタックと{quantity%64}個",
                "エネルギータブレット": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鋼鉄インゴット": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*2}個",
                "ガラス": f"{quantity}個",
                "エネルギータブレット": f"{quantity}個",
                "鋼鉄インゴット": f"{quantity}個"
            }
    if name == "鉱石辞書":
        if quantity >= 64:
            return {
                "基本制御回路": f"{quantity/64}スタックと{quantity%64}個",
                "本": f"{quantity/64}スタックと{quantity%64}個"
            }
        else:
            return {
                "基本制御回路": f"{quantity}個",
                "本": f"{quantity}個"
            }
    if name == "ポータブルテレポーター":
        if quantity*2 >= 64:
            return {
                "エネルギータブレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "テレポーテーションコア": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "エネルギータブレット": f"{quantity*2}個",
                "基本制御回路": f"{quantity*2}個",
                "テレポーテーションコア": f"{quantity}個"
            }
    if name == "設定カード":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "基本制御回路": f"{quantity}個"
            }
    if name == "クラフトレシピ":
        if quantity >= 64:
            return {
                "基本制御回路": f"{int(quantity/64)}スタックと{quantity%64}個",
                "紙": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "基本制御回路": f"{quantity}個",
                "紙": f"{quantity}個"
            }
    if name == "弾性波解析器":
        if quantity*7 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*7/64)}スタックと{quantity*7%64}個",
                "ラピスラズリ": f"{int(quantity/64)}スタックと{quantity%64}個",
                "エネルギータブレット": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*7}個",
                "ラピスラズリ": f"{quantity}個",
                "エネルギータブレット": f"{quantity}個"
            }
    if name == "計量スポイト":
        if quantity*5 >= 64:
            return {
                "板ガラス": f"{int(quantity*5)}スタックと{quantity%64}個",
                "オスミウムインゴット": f"{int(quantity/64)}個"
            }
        else:
            return {
                "板ガラス": f"{quantity*5}個",
                "オスミウムインゴット": f"{quantity}個"
            }
    if name == "ガイガーカウンター":
        if quantity*4 >= 64:
            return {
                "鉛インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鉛インゴット": f"{quantity*4}個",
                "基本制御回路": f"{quantity}個"
            }
    if name == "線量計":
        if  quantity*4 >= 64:
            return {
                "鉛インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "レッドストーンダスト": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鉛インゴット": f"{quantity*4}個",
                "レッドストーンダスト": f"{quantity}個"
            }
    if name == "キャンティーン":
        if quantity*4 >= 64:
            return {
                "錫インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ボウル": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "錫インゴット": f"{quantity*4}個",
                "ボウル": f"{quantity}個"
            }
    if name == "防護マスク":
        if quantity*5 >= 64:
            return {
                "鉛インゴット": f"{int(quantity*5/64)}スタックと{quantity*5%64}個",
                "橙色の染料": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鉛インゴット": f"{quantity*5}個",
                "橙色の染料": f"{quantity}個"
            }
    if name == "防護ガウン":
        if quantity*8 >= 64:
            return {
                "鉛インゴット": f"{int(quantity*8/64)}スタックと{quantity*8%64}個",
                "橙色の染料": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鉛インゴット": f"{quantity*8}個",
                "橙色の染料": f"{quantity}個"
            }
    if name == "防護パンツ":
        if quantity*7 >= 64:
            return {
                "鉛インゴット": f"{int(quantity*7/64)}スタックと{quantity*7%64}個",
                "橙色の染料": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鉛インゴット": f"{quantity*7}個",
                "橙色の染料": f"{quantity}個"
            }
    if name == "防護ブーツ":
        if quantity*4 >= 64:
            return {
                "鉛インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "黒色の染料": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鉛インゴット": f"{quantity*4}個",
                "黒色の染料": f"{quantity}個"
            }
    if name == "MekaSuitヘルメット":
        if quantity*4 >= 64:
            return {
                "HDPEシート": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ポロニウムペレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "究極制御回路": f"{int(quantity/64)}スタックと{quantity%64}個",
                "ネザライトのヘルメット": f"{int(quantity/64)}スタックと{quantity%64}個",
                "基本インダクションセル": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "HDPEシート": f"{quantity*4}個",
                "ポロニウムペレット": f"{quantity*2}個",
                "究極制御回路": f"{quantity}個",
                "ネザライトのヘルメット": f"{quantity}個",
                "基本インダクションセル": f"{quantity}個"
            }
    if name == "MekaSuitボディアーマー":
        if quantity*4 >= 64:
            return {
                "HDPEシート": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ポロニウムペレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "究極制御回路": f"{int(quantity/64)}スタックと{quantity%64}個",
                "ネザライトのチェストプレート": f"{int(quantity/64)}スタックと{quantity%64}個",
                "基本インダクションセル": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "HDPEシート": f"{quantity*4}個",
                "ポロニウムペレット": f"{quantity*2}個",
                "究極制御回路": f"{quantity}個",
                "ネザライトのチェストプレート": f"{quantity}個",
                "基本インダクションセル": f"{quantity}個"
            }
    if name == "MekaSuitパンツ":
        if quantity*4 >= 64:
            return {
                "HDPEシート": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ポロニウムペレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "究極制御回路": f"{int(quantity/64)}スタックと{quantity%64}個",
                "ネザライトのレギンス": f"{int(quantity/64)}スタックと{quantity%64}個",
                "基本インダクションセル": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "HDPEシート": f"{quantity*4}個",
                "ポロニウムペレット": f"{quantity*2}個",
                "究極制御回路": f"{quantity}個",
                "ネザライトのレギンス": f"{quantity}個",
                "基本インダクションセル": f"{quantity}個"
            }
    if name == "MekaSuitブーツ":
        if quantity*4 >= 64:
            return {
                "HDPEシート": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ポロニウムペレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "究極制御回路": f"{int(quantity/64)}スタックと{quantity%64}個",
                "ネザライトのブーツ": f"{int(quantity/64)}スタックと{quantity%64}個",
                "基本インダクションセル": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "HDPEシート": f"{quantity*4}個",
                "ポロニウムペレット": f"{quantity*2}個",
                "究極制御回路": f"{quantity}個",
                "ネザライトのブーツ": f"{quantity}個",
                "基本インダクションセル": f"{quantity}個"
            }
    if name == "Meka-Tool":
        if quantity*2 >= 64:
            return {
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "HDPEシート": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ポロニウムペレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "コンフィギュレーター": f"{int(quantity/64)}スタックと{quantity%64}個",
                "原子分解機": f"{int(quantity/64)}スタックと{quantity%64}個",
                "基本インダクションセル": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "究極制御回路": f"{quantity*2}個",
                "HDPEシート": f"{quantity*2}個",
                "ポロニウムペレット": f"{quantity*2}個",
                "コンフィギュレーター": f"{quantity}個",
                "原子分解機": f"{quantity}個",
                "基本インダクションセル": f"{quantity}個"
            }
    if name == "改造ステーション": 
        if quantity*4 >= 64:
            return {
                "HDPEシート": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "チェスト": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個",
                "ポロニウムペレット": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "HDPEシート": f"{int(quantity*4)}個",
                "究極制御回路": f"{int(quantity*2)}個",
                "チェスト": f"{int(quantity)}個",
                "鋼鉄ケーシング": f"{int(quantity)}個",
                "ポロニウム": f"{int(quantity)}個"
            }
    if name == "モジュールベース":
        if quantity%2 == 0:
            if quantity*4 >= 64:
                return {
                    "青銅塊": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                    "錫インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                    "HDPEシート": f"{int(quantity/64)}スタックと{quantity%64}個"
                }
            else:
                return {
                    "青銅塊": f"{quantity*4}個",
                    "錫インゴット": f"{quantity*4}個",
                    "HDPEシート": f"{quantity}個"
                }
        else:
            return "有効な値を入力してください(2n個)"
    if name == "栄養駐車ユニット":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ポロニウムペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "キャンティーン": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "ポロニウムペレット": f"{quantity*3}個",
                "キャンティーン": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "ジェットパックユニット": 
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ポロニウムペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "ジェットパック": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "ポロニウムペレット": f"{quantity*3}個",
                "ジェットパック": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "視界強化ユニット":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ポロニウムペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "エメラルド": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "ポロニウムペレット": f"{quantity*3}個",
                "エメラルド": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "太陽光再充電ユニット":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ポロニウムペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "発展型太陽光発電機": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "ポロニウムペレット": f"{quantity*3}個",
                "発展型太陽光発電機": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "攻撃力増強ユニット":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "HDPEシート": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "鉄の剣": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "HDPEシート": f"{quantity*3}個",
                "鉄の剣": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "油圧式推進ユニット": 
        if quantity*3 >= 64:
            return {
                "ポロニウムペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "強化合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "エネルギータブレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "フリーランナー": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "ポロニウムペレット": f"{quantity*3}個",
                "強化合金": f"{quantity*2}個",
                "エネルギータブレット": f"{quantity*2}個",
                "フリーランナー": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "機関式推進ユニット":
        if quantity*3 >= 64:
            return {
                "ポロニウムペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "強化合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "エネルギータブレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンドのレギンス": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
    if name == "線計量ユニット":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "HDPEシート": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "線計量": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "HDPEシート": f"{quantity*3}個",
                "線計量": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "採掘漸増ユニット":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "HDPEシート": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "鉄のツルハシ": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "HDPEシート": f"{quantity*3}個",
                "鉄のツルハシ": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "電解呼吸ユニット":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "HDPEシート": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "電解コア": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "HDPEシート": f"{quantity*3}個",
                "電解コア": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "重力変調ユニット":
        if quantity*3 >= 64:
            return {
                "反物質ペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "原子合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "究極インダクションプロバイダ": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ネザースター": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "反物質ペレット": f"{quantity*3}個",
                "原子合金": f"{quantity*2}個",
                "究極インダクションプロバイダ": f"{quantity*2}個",
                "ネザースター": f"{quantity}個",
                "mモジュールベース": f"{quantity}個"
            }
    if name == "鉱脈採掘ユニット":
        if quantity*3 >= 64:
            return {
                "ポロニウムペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "強化合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンドのツルハシ": f"{int(quantity/64)}スタックと{quantity%64}個",
                "ダイヤモンドの斧": f"{int(quantity/64)}スタックと{quantity%64}個",
                "ダイヤモンドのシャベル": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "ポロニウムペレット": "{quantity*3}個",
                "強化合金": f"{quantity*2}個",
                "ダイヤモンドのツルハシ": f"{quantity}個",
                "ダイヤモンドの斧": f"{quantity}個",
                "ダイヤモンドのシャベル": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "耕作ユニット":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "HDPEシート": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "鉄のクワ": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "HDPEシート": f"{quantity*3}個",
                "鉄のクワ": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "テレポートユニット":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "反物質ペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "テレポーテーションコア": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "反物質ペレット": f"{quantity*3}個",
                "テレポーテーションコア": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "電力配分ユニット":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ポロニウムペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "基本インダクションプロバイダ": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "ポロニウムペレット": f"{quantity*3}個",
                "基本インダクションプロバイダ": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "エネルギーユニット":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "HDPEシート": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "基本インダクションセル": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
    if name == "シルクタッチユニット":
        if quantity*3 >= 64:
            return {
                "ポロニウムペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "強化合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンドのツルハシ": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精製グロウストーンブロック": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "ポロニウムペレット": f"{quantity*3}個",
                "強化合金": f"{quantity*2}個",
                "ダイヤモンドのツルハシ": f"{quantity*2}個",
                "精製グロウストーンブロック": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "放射線防護ユニット":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "HDPEシート": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "鉛ブロック": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{quantity/64}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "HDPEシート": f"{quantity*3}個",
                "鉛ブロック": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "磁気誘導ユニット":
        if quantity*3 >= 64:
            return {
                "ポロニウムペレット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "強化合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鉄格子": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "ポロニウムペレット": f"{quantity*3}個",
                "強化合金": f"{quantity*2}個",
                "精鋭制御回路": f"{quantity*2}個",
                "鉄格子": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "呼吸浄化ユニット":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ポロニウムペレット": f"{int(quantity*2/64)}スタックと{quantity*2/64}個",
                "防護マスク": f"{int(quantity/64)}スタックと{quantity%64}個",
                "スキューバマスク": f"{int(quantity/64)}スタックと{quantity%64}個",
                "モジュールベース": f"{int(quantity/64)}スタックと{quantity%64}個",
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "ポロニウムペレット": f"{quantity*2}個",
                "防護マスク": f"{quantity}個",
                "スキューバマスク": f"{quantity}個",
                "モジュールベース": f"{quantity}個"
            }
    if name == "基本エネルギーキューブ":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "エネルギータブレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "鉄インゴット": f"{quantity*2}個",
                "エネルギータブレット": f"{quantity}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "発展エネルギーキューブ":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "オスミウムインゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "エネルギータブレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本エネルギーキューブ": f"{int(quantity/64)}スタックと{quantity%64}個",
                }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "オスミウムインゴット": f"{quantity*2}個",
                "エネルギータブレット": f"{quantity*2}個",
                "基本エネルギーキューブ": f"{quantity}個"
            }
    if name == "精鋭エネルギーキューブ":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "エネルギータブレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展エネルギーキューブ": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "金インゴット": f"{quantity*2}個",
                "エネルギータブレット": f"{quantity*2}個",
                "発展エネルギーキューブ": f"{quantity}個"
            }
    if name == "究極エネルギーキューブ":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ダイヤモンド": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "エネルギータブレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭エネルギーキューブ": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "ダイヤモンド": f"{quantity*2}個",
                "エネルギータブレット": f"{quantity*2}個",
                "精鋭エネルギーキューブ": f"{quantity}個"
            }
    if name == "基本流体タンク":
        if quantity*4 >= 64:
            return {
                "鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
            }
        else:
            return {
                "鉄インゴット": f"{quantity*4}個",
                "レッドストーンダスト": f"{quantity*4}個"
            }
    if name == "発展流体タンク":
        if quantity*4 >= 64:
            return {
                "鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
            }
        else:
            return {
                "鉄インゴット": f"{quantity*4}個",
                "吹込合金": f"{quantity*4}個"
            }
    if name == "精鋭流体タンク":
        if quantity*4 >= 64:
            return {
                "鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
            }
        else:
            return {
                "鉄インゴット": f"{quantity*4}個",
                "強化合金": f"{quantity*4}個"
            }
    if name == "究極流体タンク":
        if quantity*4 >= 64:
            return {
                "鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
            }
        else:
            return {
                "鉄インゴット": f"{quantity*4}個",
                "原子合金": f"{quantity*4}個"
            }
    if name == "基本化学タンク":
        if quantity*4 >= 64:
            return {
                "オスミウムインゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個"
            }
        else:
            return {
                "オスミウムインゴット": f"{quantity*4}個",
                "レッドストーンダスト": f"{quantity*4}個"
            }
    if name == "発展化学タンク":
        if quantity*4 >= 64:
            return {
                "オスミウムインゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個"
            }
        else:
            return {
                "オスミウムインゴット": f"{quantity*4}個",
                "吹込合金": f"{quantity*4}個"
            }
    if name == "精鋭化学タンク":
        if quantity*4 >= 64:
            return {
                "オスミウムインゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個"
            }
        else:
            return {
                "オスミウムインゴット": f"{quantity*4}個",
                "強化合金": f"{quantity*4}個"
            }
    if name == "究極化学タンク":
        if quantity*4 >= 64:
            return {
                "オスミウムインゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個"
            }
        else:
            return {
                "オスミウムインゴット": f"{quantity*4}個",
                "原子合金": f"{quantity*4}個"
            }
    if name == "基本ビン":
        if quantity*5 >= 64:
            return {
                "丸石": f"{int(quantity*5%64)}スタックと{quantity*5%64}個",
                "レッドストーンダスト": f"{int(quantity*2%64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "丸石": f"{quantity*5}個",
                "レッドストーンダスト": f"{quantity*2}個",
                "基本制御回路": f"{quantity}個"
            }
    if name == "発展ビン":
        if quantity*5 >= 64:
            return {
                "丸石": f"{int(quantity*5%64)}スタックと{quantity*5%64}個",
                "吹込合金": f"{int(quantity*2%64)}スタックと{quantity*2%64}個",
                "発展制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "丸石": f"{quantity*5}個",
                "吹込合金": f"{quantity*2}個",
                "発展制御回路": f"{quantity}個"
            }
    if name == "精鋭ビン":
        if quantity*5 >= 64:
            return {
                "丸石": f"{int(quantity*5%64)}スタックと{quantity*5%64}個",
                "強化合金": f"{int(quantity*2%64)}スタックと{quantity*2%64}個",
                "精鋭制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "丸石": f"{quantity*5}個",
                "強化合金": f"{quantity*2}個",
                "精鋭制御回路": f"{quantity}個"
            }
    if name == "究極ビン":
        if quantity*5 >= 64:
            return {
                "丸石": f"{int(quantity*5%64)}スタックと{quantity*5%64}個",
                "原子合金": f"{int(quantity*2%64)}スタックと{quantity*2%64}個",
                "究極制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "丸石": f"{quantity*5}個",
                "原子合金": f"{quantity*2}個",
                "究極制御回路": f"{quantity}個"
            }
    if name == "充電パッド":
        if quantity*3 >= 64:
            return {
                "磨かれたブラックストーンの感圧版": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "鋼鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "エネルギータブレット": f"{int(quantity/64)}スタックと{quantity%64}個",
            }
        else:
            return {
                "磨かれたブラックストーンの感圧版": f"{quantity*3}個",
                "鋼鉄インゴット": f"{quantity*2}個",
                "エネルギータブレット": f"{quantity}個"
            }
    if name == "セキュリティーデスク":
        if quantity*4 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ガラス": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個",
                "テレポーテーションコア": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity*2}個",
                "ガラス": f"{quantity}個",
                "鋼鉄ケーシング": f"{quantity}個",
                "テレポーテーション": f"{quantity}個"
            }
    if name == "パーソナルチェスト":
        if quantity*5 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*5/64)}スタックと{quantity*5%64}個",
                "チェスト": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ガラス": f"{int(quantity/64)}スタックと{quantity%64}個",
                "基本制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*5}個",
                "チェスト": f"{quantity*2}個",
                "ガラス": f"{quantity}個",
                "基本制御回路": f"{quantity}個"
            }
    if name == "量子もつれ転送機":
        if quantity*4 >= 64:
            return {
                "精製黒曜石インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "原子合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "テレポーテーションコア": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "精製黒曜石インゴット": f"{quantity*4}個",
                "原子合金": f"{quantity*2}個",
                "究極制御回路": f"{quantity*2}個",
                "テレポーテーションコア": f"{quantity}個"
            }
    if name == "薪木ストーブ":
        if quantity*5 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*5/64)}スタックと{quantity*5%64}個",
                "かまど": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*5}個",
                "かまど": f"{quantity*2}個",
                "基本制御回路": f"{quantity}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "段ボール箱":
        if quantity*4 >= 64:
            return {
                "おがくず": f"{int(quantity*4/64)}スタックと{quantity*4%64}個"
            }
        else:
            return {
                "おがくず": f"{quantity*4}個"
            }
    if name == "ロビット":
        if quantity*2 >= 64:
            return {
                "精製黒曜石インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "エネルギータブレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄インゴット": f"{int(quantity/64)}スタックと{quantity%64}個",
                "原子合金": f"{int(quantity/64)}スタックと{quantity%64}個",
                "パーソナルチェスト": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "精製黒曜石インゴット": f"{quantity*2}個",
                "エネルギータブレット": f"{quantity*2}個",
                "鋼鉄インゴット": f"{quantity}個",
                "原子合金": f"{quantity}個",
                "パーソナルチェスト": f"{quantity}個"
            }
    if name == "鋼鉄ケーシング":
        if quantity*4 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ガラス": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "オスミウムインゴット": f"{int(quantity/64)}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*4}個",
                "ガラス": f"{quantity*4}個",
                "オスミウムインゴット": f"{quantity}個"
            }
    if name == "冶金吹込機":
        if quantity*4 >= 64:
            return {
                "鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "レッドストーンダスト": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "かまど": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "オスミウムインゴット": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鉄インゴット": f"{quantity*4}個",
                "レッドストーンダスト": f"{quantity*2}個",
                "かまど": f"{quantity*2}個",
                "オスミウムインゴット": f"{quantity}個"
            }
    if name == "濃縮室":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "鉄インゴット": f"{quantity*2}個",
                "基本制御回路": f"{quantity*2}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "電動精錬機":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ガラス": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "ガラス": f"{quantity*2}個",
                "基本制御回路": f"{quantity*2}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "粉砕機":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*3%64}個",
                "マグマ入りバケツ": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "マグマ入りバケツ": f"{quantity*2}個",
                "基本制御回路": f"{quantity*2}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "精密製材機":
        if quantity*4 >= 64:
            return {
                "鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "吹込合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鉄インゴット": f"{quantity*4}個",
                "吹込合金": f"{quantity*2}個",
                "基本制御回路": f"{quantity*2}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "定式組み立て機":
        if quantity*4 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "作業台": f"{int(quantity/64)}スタックと{quantity%64}個",
                "チェスト": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "作業台": f"{quantity}個",
                "チェスト": f"{quantity}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "オスミウム圧縮機":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "バケツ": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "バケツ": f"{quantity*2}個",
                "発展制御回路": f"{quantity*2}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "浄化室":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "オスミウムインゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "濃縮室": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "オスミウムインゴット": f"{quantity*2}個",
                "発展制御回路": f"{quantity*2}個",
                "濃縮室": f"{quantity}個"
            }
    if name == "結合機":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "丸石": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity*2}個",
                "丸石": f"{quantity*2}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "回転式流体凝縮器":
        if quantity*4 >= 64:
            return {
                "ガラス": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "化学タンク(種類不問)": f"{int(quantity/64)}スタックと{quantity%64}個",
                "基本流体タンク": f"{int(quantity/64)}スタックと{quantity%64}個",
                "エネルギータブレット": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "ガラス": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "化学タンク(種類不問)": f"{quantity}個",
                "基本流体タンク": f"{quantity}個",
                "エネルギータブレット": f"{quantity}個"
            }
    if name == "電気分解機":
        if quantity*4 >= 64:
            return {
                "鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "吹込合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "レッドストーンダスト": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "電解コア": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鉄インゴット": f"{quantity*4}個",
                "吹込合金": f"{quantity*2}個",
                "レッドストーンダスト": f"{quantity*2}個",
                "電解コア": f"{quantity}個"
            }
    if name == "化学酸化機":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "パーソナルチェスト": f"{int(quantity/64)}スタックと{quantity%64}個",
                "化学タンク(種類不問)": f"{int(quantity/64)}スタックと{quantity%64}個",
                "ダイナミックタンク": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "パーソナルチェスト": f"{quantity}個",
                "化学タンク(種類不問)": f"{quantity}個",
                "ダイナミックタンク": f"{quantity}個"
            }
    if name == "化学混成機":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "化学タンク(種類不問)": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイナミックタンク": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "化学タンク(種類不問)": f"{quantity*2}個",
                "ダイナミックタンク": f"{quantity}個"
            }
    if name == "化学注入室":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "浄化室": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity*2}個",
                "金インゴット": f"{quantity*2}個",
                "浄化室": f"{quantity}個"
            }
    if name == "化学溶解機":
        if quantity*4 >= 64:
            return {
                "精製黒曜石インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "化学タンク(種類不問)": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ケーシング": f"{int(quantity)}スタックと{quantity%64}個"
            }
        else:
            return {
                "精製黒曜石インゴット": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "化学タンク(種類不問)": f"{quantity*2}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "化学洗浄機":
        if quantity*4 >= 64:
            return {
                "精製黒曜石インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "流体タンク(種類不問)": f"{int(quantity/64)}スタックと{quantity%64}個",
                "化学タンク(種類不問)": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鋼鉄ケーシング": f"{int(quantity)}スタックと{quantity%64}個"
            }
        else:
            return {
                "精製黒曜石インゴット": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "流体タンク(種類不問)": f"{quantity}個",
                "化学タンク(種類不問)": f"{quantity}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "化学結晶化装置":
        if quantity*4 >= 64:
            return {
                "精製黒曜石インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "蛍石": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "精製黒曜石インゴット": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "蛍石": f"{quantity*2}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "加圧反応室":
        if quantity*2 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "化学タンク(種類不問)": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "吹込合金": f"{int(quantity/64)}スタックと{quantity%64}個",
                "濃縮室": f"{int(quantity/64)}スタックと{quantity%64}個",
                "ダイナミックタンク": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*2}個",
                "基本制御回路": f"{quantity*2}個",
                "化学タンク(種類不問)": f"{quantity*2}個",
                "吹込合金": f"{quantity}個",
                "濃縮室": f"{quantity}個",
                "ダイナミックタンク": f"{quantity}個"
            }
    if name == "抵抗型発熱機":
        if quantity*4 >= 64:
            return {
                "錫インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "レッドストーンダスト": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個",
                "エネルギータブレット": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "錫インゴット": f"{quantity*4}個",
                "レッドストーンダスト": f"{quantity*3}個",
                "鋼鉄ケーシング": f"{quantity}個",
                "エネルギータブレット": f"{quantity}個"
            }
    if name == "栄養液化機":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ボウル": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ケーシング": f"{quantity/64}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "ボウル": f"{quantity*2}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "電動ポンプ":
        if quantity*3 >= 64:
            return {
                "オスミウムインゴット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "吹込合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "バケツ": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "オスミウムインゴット": f"{quantity*3}個",
                "吹込合金": f"{quantity*2}個",
                "バケツ": f"{quantity}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "流体再供給機":
        if quantity*6 >= 64:
            return {
                "錫インゴット": f"{int(quantity*6/64)}スタックと{quantity*6%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ケーシング": f"{int(quantity)}スタックと{quantity}個"
            }
        else:
            return {
                "錫インゴット": f"{quantity*6}個",
                "基本制御回路": f"{quantity*2}個",
                "鋼鉄ケーシング" : f"{quantity}個"
            }
    if name == "弾性波発振装置":
        if quantity*5 >= 64:
            return {
                "錫インゴット": f"{int(quantity*5/64)}スタックと{quantity*5%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ラピスラズリ": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "錫インゴット": f"{quantity*5}個",
                "基本制御回路": f"{quantity*2}個",
                "ラピスラズリ": f"{quantity}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "レーザー":
        if quantity*3 >= 64:
            return {
                "強化合金": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "エネルギータブレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンド": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*3}個",
                "エネルギータブレット": f"{quantity*2}個",
                "ダイヤモンド": f"{quantity}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "レーザー増幅器":
        if quantity*7 >= 64:
            return {
                "鋼鉄ケーシング": f"{int(quantity*7/64)}スタックと{quantity*7%64}個",
                "ダイヤモンド": f"{int(quantity/64)}スタックと{quantity%64}個",
                "基本エネルギーキューブ": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄ケーシング": f"{quantity*7}個",
                "ダイヤモンド": f"{quantity}個",
                "基本エネルギーキューブ": f"{quantity}個"
            }
    if name == "レーザートラクタービーム":
        if quantity >= 64:
            return {
                "レーザー増幅器": f"{int(quantity/64)}スタックと{quantity%64}個",
                "パーソナルチェスト": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レーザー増幅器": f"{quantity}個",
                "パーソナルチェスト": f"{quantity}個"
            }
    if name == "デジタルマイナー":
        if quantity*2 >= 64:
            return {
                "原子合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "物流ソーター": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "テレポーテーションコア": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity/64)}スタックと{quantity%64}個",
                "ロビット": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*2}個",
                "物流ソーター": f"{quantity*2}個",
                "テレポーテーションコア": f"{quantity*2}個",
                "基本制御回路": f"{quantity}個",
                "ロビット": f"{quantity}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "鉱石統合器":
        if quantity*4 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "板ガラス": f"{int(quantity/64)}スタックと{quantity%64}個",
                "チェスト": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鉱石辞書": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄ケーシング": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "板ガラス": f"{quantity}個",
                "チェスト": f"{quantity}個",
                "鉱石辞書": f"{quantity}個"
            }
    if name == "太陽中性子反応機":
        if quantity*3 >= 64:
            return {
                "青銅インゴット": f"{int(quantity*3/64)}スタックと{quantity*3%64}個",
                "強化合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "HDPEシート": f"{int(quantity/64)}スタックと{quantity%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "青銅インゴット": f"{quantity*3}個",
                "強化合金": f"{quantity*2}個",
                "精鋭制御回路": f"{quantity*2}個",
                "HDPEシート": f"{quantity}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "同位体遠心分離機":
        if quantity*6 >= 64:
            return {
                "鉛インゴット": f"{int(quantity*6/64)}スタックと{quantity*6%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本化学タンク": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鉛インゴット": f"{quantity*6}個",
                "究極制御回路": f"{quantity*2}個",
                "基本化学タンク": f"{quantity}個"
            }
    if name == "反陽子核合成機":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "反物質ペレット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "反物質ペレット": f"{quantity*2}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "基本吹込ファクトリー":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "冶金吹込み機": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "鉄インゴット": f"{quantity*2}個",
                "冶金吹込み機": f"{quantity}個"
            }
    if name == "基本精錬ファクトリー":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "電動精錬機": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "鉄インゴット": f"{quantity*2}個",
                "電動精錬機": f"{quantity}個"
            }
    if name == "基本濃縮ファクトリー":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "濃縮室": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "鉄インゴット": f"{quantity*2}個",
                "濃縮室": f"{quantity}個"
            }
    if name == "基本粉砕ファクトリー":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "粉砕機": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "鉄インゴット": f"{quantity*2}個",
                "粉砕機": f"{quantity}個"
            }
    if name == "基本圧縮ファクトリー":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "オスミウム圧縮機": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "鉄インゴット": f"{quantity*2}個",
                "オスミウム圧縮機": f"{quantity}個"
            }
    if name == "基本結合ファクトリー":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "結合機": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "鉄インゴット": f"{quantity*2}個",
                "結合機": f"{quantity}個"
            }
    if name == "基本浄化ファクトリー":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "浄化室": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "鉄インゴット": f"{quantity*2}個",
                "浄化室": f"{quantity}個"
            }
    if name == "基本注入ファクトリー":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "化学注入室": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "鉄インゴット": f"{quantity*2}個",
                "化学注入室": f"{quantity}個"
            }
    if name == "基本製材ファクトリー":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精密製材機": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "基本制御回路": f"{quantity*2}個",
                "鉄インゴット": f"{quantity*2}個",
                "精密製材機": f"{quantity}個"
            }
    if name == "発展吹込ファクトリー":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "オスミウムインゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本吹込ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "発展制御回路": f"{quantity*2}個",
                "オスミウムインゴット": f"{quantity*2}個",
                "基本吹込ファクトリー": f"{quantity}個"
            }
    if name == "発展精錬ファクトリー":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "オスミウムインゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本精錬ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "発展制御回路": f"{quantity*2}個",
                "オスミウムインゴット": f"{quantity*2}個",
                "基本精錬ファクトリー": f"{quantity}個"
            }
    if name == "発展濃縮ファクトリー":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "オスミウムインゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本濃縮ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "発展制御回路": f"{quantity*2}個",
                "オスミウムインゴット": f"{quantity*2}個",
                "基本濃縮ファクトリー": f"{quantity}個"
            }
    if name == "発展粉砕ファクトリー":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "オスミウムインゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本粉砕ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "発展制御回路": f"{quantity*2}個",
                "オスミウムインゴット": f"{quantity*2}個",
                "基本粉砕ファクトリー": f"{quantity}個"
            }
    if name == "発展圧縮ファクトリー":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "オスミウムインゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本圧縮ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "発展制御回路": f"{quantity*2}個",
                "オスミウムインゴット": f"{quantity*2}個",
                "基本圧縮ファクトリー": f"{quantity}個"
            }
    if name == "発展結合ファクトリー":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "オスミウムインゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本結合ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "発展制御回路": f"{quantity*2}個",
                "オスミウムインゴット": f"{quantity*2}個",
                "基本結合ファクトリー": f"{quantity}個"
            }
    if name == "発展浄化ファクトリー":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "オスミウムインゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本浄化ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "発展制御回路": f"{quantity*2}個",
                "オスミウムインゴット": f"{quantity*2}個",
                "基本浄化ファクトリー": f"{quantity}個"
            }
    if name == "発展注入ファクトリー":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "オスミウムインゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本注入ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "発展制御回路": f"{quantity*2}個",
                "オスミウムインゴット": f"{quantity*2}個",
                "基本注入ファクトリー": f"{quantity}個"
            }
    if name == "発展製材ファクトリー":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "オスミウムインゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本製材ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "発展制御回路": f"{quantity*2}個",
                "オスミウムインゴット": f"{quantity*2}個",
                "基本製材ファクトリー": f"{quantity}個"
            }
    if name == "精鋭吹込ファクトリー":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展吹込ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity*2}個",
                "金インゴット": f"{quantity*2}個",
                "発展吹込ファクトリー": f"{quantity}個"
            }
    if name == "精鋭精錬ファクトリー":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展精錬ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity*2}個",
                "金インゴット": f"{quantity*2}個",
                "発展精錬ファクトリー": f"{quantity}個"
            }
    if name == "精鋭濃縮ファクトリー":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展濃縮ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity*2}個",
                "金インゴット": f"{quantity*2}個",
                "発展濃縮ファクトリー": f"{quantity}個"
            }
    if name == "精鋭粉砕ファクトリー":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展粉砕ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity*2}個",
                "金インゴット": f"{quantity*2}個",
                "発展粉砕ファクトリー": f"{quantity}個"
            }
    if name == "精鋭圧縮ファクトリー":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展圧縮ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity*2}個",
                "金インゴット": f"{quantity*2}個",
                "発展圧縮ファクトリー": f"{quantity}個"
            }
    if name == "精鋭結合ファクトリー":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展結合ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity*2}個",
                "金インゴット": f"{quantity*2}個",
                "発展結合ファクトリー": f"{quantity}個"
            }
    if name == "精鋭浄化ファクトリー":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展浄化ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity*2}個",
                "金インゴット": f"{quantity*2}個",
                "発展浄化ファクトリー": f"{quantity}個"
            }
    if name == "精鋭注入ファクトリー":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展注入ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity*2}個",
                "金インゴット": f"{quantity*2}個",
                "発展注入ファクトリー": f"{quantity}個"
            }
    if name == "精鋭製材ファクトリー":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展製材ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity*2}個",
                "金インゴット": f"{quantity*2}個",
                "発展製材ファクトリー": f"{quantity}個"
            }
    if name == "究極吹込ファクトリー":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンド": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭吹込ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "ダイヤモンド": f"{quantity*2}個",
                "精鋭吹込ファクトリー": f"{quantity}個"
            }
    if name == "究極精錬ファクトリー":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンド": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭精錬ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "ダイヤモンド": f"{quantity*2}個",
                "精鋭精錬ファクトリー": f"{quantity}個"
            }
    if name == "究極濃縮ファクトリー":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンド": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭濃縮ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "ダイヤモンド": f"{quantity*2}個",
                "精鋭濃縮ファクトリー": f"{quantity}個"
            }
    if name == "究極粉砕ファクトリー":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンド": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭粉砕ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "ダイヤモンド": f"{quantity*2}個",
                "精鋭粉砕ファクトリー": f"{quantity}個"
            }
    if name == "究極圧縮ファクトリー":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンド": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭圧縮ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "ダイヤモンド": f"{quantity*2}個",
                "精鋭圧縮ファクトリー": f"{quantity}個"
            }
    if name == "究極結合ファクトリー":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンド": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭結合ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "ダイヤモンド": f"{quantity*2}個",
                "精鋭結合ファクトリー": f"{quantity}個"
            }
    if name == "究極浄化ファクトリー":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンド": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭浄化ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "ダイヤモンド": f"{quantity*2}個",
                "精鋭浄化ファクトリー": f"{quantity}個"
            }
    if name == "究極注入ファクトリー":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンド": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭注入ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "ダイヤモンド": f"{quantity*2}個",
                "精鋭注入ファクトリー": f"{quantity}個"
            }
    if name == "究極製材ファクトリー":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ダイヤモンド": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭製材ファクトリー": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "究極制御回路": f"{quantity*2}個",
                "ダイヤモンド": f"{quantity*2}個",
                "精鋭製材ファクトリー": f"{quantity}個"
            }
    if name == "スピードアップグレード":
        if quantity*2 >= 64:
            return {
                "吹込合金": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "ガラス": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "オスミウムの粉": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*2}個",
                "ガラス": f"{quantity*2}個",
                "オスミウムの粉": f"{quantity}個",
            }
    if name == "エネルギーアップグレード":
        if quantity*2 >= 64:
            return {
                "吹込合金": f"{int(quantity*2)}スタックと{quantity*2%64}個",
                "ガラス": f"{int(quantity*2)}スタックと{quantity*2%64}個",
                "金の粉": f"{int(quantity)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*2}個",
                "ガラス": f"{quantity*2}個",
                "金の粉": f"{quantity}個"
            }
    if name == "フィルターアップグレード":
        if quantity*2 >= 64:
            return {
                "吹込合金": f"{int(quantity*2)}スタックと{quantity*2%64}個",
                "ガラス": f"{int(quantity*2)}スタックと{quantity*2%64}個",
                "錫の粉": f"{int(quantity)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*2}個",
                "ガラス": f"{quantity*2}個",
                "錫の粉": f"{quantity}個"
            }
    if name == "消音アップグレード":
        if quantity*2 >= 64:
            return {
                "吹込合金": f"{int(quantity*2)}スタックと{quantity*2%64}個",
                "ガラス": f"{int(quantity*2)}スタックと{quantity*2%64}個",
                "鋼鉄の粉": f"{int(quantity)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*2}個",
                "ガラス": f"{quantity*2}個",
                "鋼鉄の粉": f"{quantity}個"
            }
    if name == "ガスアップグレード":
        if quantity*2 >= 64:
            return {
                "吹込合金": f"{int(quantity*2)}スタックと{quantity*2%64}個",
                "ガラス": f"{int(quantity*2)}スタックと{quantity*2%64}個",
                "鉄の粉": f"{int(quantity)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*2}個",
                "ガラス": f"{quantity*2}個",
                "鉄の粉": f"{quantity}個"
            }
    if name == "アンカーアップグレード":
        if quantity*2 >= 64:
            return {
                "吹込合金": f"{int(quantity*2)}スタックと{quantity*2%64}個",
                "ガラス": f"{int(quantity*2)}スタックと{quantity*2%64}個",
                "ダイヤモンドの粉": f"{int(quantity)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*2}個",
                "ガラス": f"{quantity*2}個",
                "ダイヤモンの粉": f"{quantity}個"
            }
    if name == "基本ティアインストーラー":
        if quantity*4 >= 64:
            return {
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "鉄インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "基本制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "木材": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "レッドストーンダスト": f"{quantity*4}個",
                "鉄インゴット": f"{quantity*2}個",
                "基本制御回路": f"{quantity*2}個",
                "木材": f"{quantity}個"
            }
    if name == "発展ティアインストーラー":
        if quantity*4 >= 64:
            return {
                "吹込合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "オスミウムインゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "木材": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "吹込合金": f"{quantity*4}個",
                "オスミウムインゴット": f"{quantity*2}個",
                "発展制御回路": f"{quantity*2}個",
                "木材": f"{quantity}個"
            }
    if name == "精鋭ティアインストーラー":
        if quantity*4 >= 64:
            return {
                "強化合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "金インゴット": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "精鋭制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "木材": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "強化合金": f"{quantity*4}個",
                "金インゴット": f"{quantity*2}個",
                "精鋭制御回路": f"{quantity*2}個",
                "木材": f"{quantity}個"
            }
    if name == "究極ティアインストーラー":
        if quantity*4 >= 64:
            return {
                "原子合金": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ダイヤモンド": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "究極制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "木材": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "原子合金": f"{quantity*4}個",
                "ダイヤモンド": f"{quantity*2}個",
                "究極制御回路": f"{quantity*2}個",
                "木材": f"{quantity}個"
            }
    if name == "テレポーター":
        if quantity*4 >= 64:
            return {
                "基本制御回路": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "鋼鉄ケーシング": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "テレポーテーションコア": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "基本制御回路": f"{quantity*4}個",
                "鋼鉄ケーシング": f"{quantity*4}個",
                "テレポーテーションコア": f"{quantity}個"
            }
    if name == "テレポーターフレーム":
        if quantity*8 >= 64:
            return {
                "精製黒曜石インゴット": f"{int(quantity*8/64)}スタックと{quantity*8%64}個",
                "精製グロウストーンインゴット": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "精製黒曜石インゴット": f"{quantity*8}個",
                "精製グロウストーンインゴット": f"{quantity}個"
            }
    if name == "構造用ガラス":
        if quantity*4 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "ガラス": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "構造用ガラス": f"{quantity*4}個",
                "ガラス": f"{quantity}個"
            }
    if name == "ダイナミックタンク":
        if quantity*4 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "バケツ": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*4}個",
                "バケツ": f"{quantity}個"
            }
    if name == "ダイナミックバルブ":
        if quantity*4 >= 64:
            return {
                "ダイナミックタンク": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "基本制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "ダイナミックタンク": f"{quantity*4}個",
                "基本制御回路": f"{quantity}個"
            }
    if name == "ボイラーケーシング":
        if quantity*4 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "鉄インゴット": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*4}個",
                "鉄インゴット": f"{quantity}個"
            }
    if name == "ボイラーバルブ":
        if quantity*4 >= 64:
            return {
                "ボイラーケーシング": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "発展制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "ボイラーケーシング": f"{quantity*4}個",
                "発展制御回路": f"{quantity}個"
            }
    if name == "加熱素子":
        if quantity*4 >= 64:
            return {
                "銅インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "レッドストーンダスト": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "鋼鉄ケーシング": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "銅インゴット": f"{quantity*4}個",
                "レッドストーンダスト": f"{quantity*4}個",
                "鋼鉄ケーシング": f"{quantity}個"
            }
    if name == "圧力分散機":
        if quantity*4 >= 64:
            return {
                "鉄格子": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "鋼鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "吹込合金": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鉄格子": f"{quantity*4}個",
                "鋼鉄インゴット": f"{quantity*4}個",
                "吹込合金": f"{quantity}個"
            }
    if name == "加温蒸発濃縮ブロック":
        if quantity*4 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "銅インゴット": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*4}個",
                "銅インゴット": f"{quantity}個"
            }
    if name == "加温蒸発濃縮コントローラー":
        if quantity*5 >= 64:
            return {
                "加温蒸発濃縮ブロック": f"{int(quantity*5/64)}スタックと{quantity*5%64}個",
                "発展制御回路": f"{int(quantity*2/64)}スタックと{quantity*2%64}個",
                "板ガラス": f"{int(quantity/64)}スタックと{quantity%64}個",
                "バケツ": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "加温蒸発濃縮ブロック": f"{quantity*5}個",
                "発展制御回路": f"{quantity*2}個",
                "板ガラス": f"{quantity}個",
                "バケツ": f"{quantity}個"
            }
    if name == "加温蒸発濃縮バレル":
        if quantity*4 >= 64:
            return {
                "加温蒸発濃縮ブロック": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "発展制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "加温蒸発濃縮ブロック": f"{quantity*4}個",
                "発展制御回路": f"{quantity}個"
            }
    if name == "インダクションケーシング":
        if quantity%4 != 0:
            if quantity*4 >= 64:
                return {
                    "鋼鉄インゴット": f"{int((quantity*4+(4-quantity*4%4))/64)}スタックと{(quantity*4+(4-quantity*4%4))%64}個",
                    "エネルギータブレット": f"{int((quantity+(4-quantity%4))/64)}スタックと{(quantity+(4-quantity%4))%64}個"
                }
            else:
                return {
                    "鋼鉄インゴット": f"{quantity*4+(4-quantity*4%4)}個",
                    "エネルギータブレット": f"{quantity+(4-quantity%4)}個"
                }
        if quantity*4 >= 64:
            return {
                "鋼鉄インゴット": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "エネルギータブレット": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "鋼鉄インゴット": f"{quantity*4}個",
                "エネルギータブレット": f"{quantity}個"
            }
    if name == "インダクションポート":
        if quantity%2 != 0:
            if quantity*4 >= 64:
                return {
                    "インダクションケーシング": f"{int((quantity*4+(2-quantity*4%2))/64)}スタックと{(quantity*4+(2-quantity*4%2))%64}個",
                    "精鋭制御回路": f"{int((quantity+(2-quantity%2))/64)}スタックと{(quantity+(2-quantity%2))%64}個"
                }
            else:
                return {
                    "インダクションケーシング": f"{quantity*4}個",
                    "精鋭制御回路": f"{quantity}個"
                }
        if quantity*4 >= 64:
            return {
                "インダクションケーシング": f"{int(quantity*4/64)}スタックと{quantity*4%64}個",
                "精鋭制御回路": f"{int(quantity/64)}スタックと{quantity%64}個"
            }
        else:
            return {
                "インダクションケーシング": f"{quantity*4}個",
                "精鋭制御回路": f"{quantity}個"
            }
    else:
        return "有効な値を入力してください"

