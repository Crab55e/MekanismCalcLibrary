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
    else:
        return "有効な値を入力してください"
    
