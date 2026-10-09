import random

print("ハイアンドローをしましょう。")
print("表示された数字より高い(H)か低い(L)か予想し、HかLを入力してください。数字の範囲は0〜13です。")
print("また、このゲームは3回勝負です。それでは、ゲームを開始します。")

print( ) # 改行

vic_count = 0 # 勝利判定
lose_count = 0 # 敗北判定
drow_count = 0 # あいこの判定

for i in range(3):   # 3回勝負

    # 表示される数字と次に表示される数字を決める。
    num = random.randint(1, 13)
    next_num = random.randint(1,13)

    print("ラウンド", i+1)
    print(num)
    answer = input("H or L : ")
    print(next_num)

# 予想があたっていた場合
    if num < next_num and answer == "H" or num > next_num and answer == "L":
        vic_count += 1
        print("お見事。")

# 予想が外れていた場合
    elif num < next_num and answer == "L" or num > next_num and answer == "H":
        lose_count += 1
        print("残念。")

# 同数だった場合
    elif num == next_num and answer == "H" or "L":
        drow_count += 1
        print("ドロー。惜しいですね。")

# 入力されたものが指示していたものでなかった場合
    else:
        print("H か L と入力してください")

    print( )  ### 改行

if vic_count > lose_count:
    print(f"{vic_count}勝{lose_count}敗で、あなたの勝ちです。\nおめでとうございます。また、お暇なときにでも。")

elif vic_count < lose_count:
    print(f"{vic_count}勝{lose_count}敗で、あなたの負けです。\n残念な結果となってしまいましたね。再挑戦をお待ちしております。")

elif drow_count == 3:
    print("すべてドローになる方は初めてです。\n運がいいのですね、愉快な方向で。")

else:
    print(f"{vic_count}勝{lose_count}敗{drow_count}ドローで、引き分けです。\nまたどうぞ。")

