import random

print("ゲームを開始します。")
print("表示された数字より高い(H)か低い(L)か予想し、HかLを入力してください。数字の範囲は0〜13です。")

for i in range(3):   ### 3回勝負

    ### 表示される数字と次に表示される数字を決める。
    num = random.randint(1, 13)
    next_num = random.randint(1,13)

    print("ラウンド", i+1)
    print(num)
    answer = input("H or L : ")
    print(next_num)

### 予想があたっていた場合
    if num < next_num and answer == "H" or num > next_num and answer == "L":
        print("お見事。")

### 予想が外れていた場合
    elif num < next_num and answer == "L" or num > next_num and answer == "H":
        print("残念。")

### 同数だった場合
    elif num == next_num and answer == "H" or "L":
        print("ドロー。惜しいですね。")

### 入力されたものが指示していたものでなかった場合
    else:
        print("H か L と入力してください")

    print( )  ### 改行





