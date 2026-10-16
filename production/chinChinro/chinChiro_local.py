import random


def roll_dice():
    """
    サイコロを3つ振る。
    約1%（1/100）の確率で通常ありえない「7」が出るイカサマダイス。
    """
    dice = []
    for _ in range(3):
        # 1%の確率で 7、残り99%の確率で 1〜6
        if random.random() < 0.01:
            dice.append(7)
        else:
            dice.append(random.randint(1, 6))

    return sorted(dice)


def evaluate_hand(dice):
    """
    出目(dice)から役と強度を判定する
    """
    d1, d2, d3 = dice

    # 特殊役：7が含まれる場合
    if d1 == d2 == d3 == 7:
        return ("スリーセブン (超特大勝ち)", 999)

    # 1. ピンゾロ（1, 1, 1）
    if dice == [1, 1, 1]:
        return ("ピンゾロ (5倍勝ち)", 100)

    # 2. ゾロ目（2~6のゾロ目）
    if d1 == d2 == d3:
        return (f"{d1}のゾロ目 (3倍勝ち)", 90 + d1)

    # 3. シゴロ（4, 5, 6）
    if dice == [4, 5, 6]:
        return ("シゴロ (2倍勝ち)", 80)

    # 4. ヒフミ（1, 2, 3）
    if dice == [1, 2, 3]:
        return ("ヒフミ (2倍負け)", 0)

    # 5. 通常の目（2つが同じ数字で、残りの1つが出目になる）
    if d1 == d2:
        return (f"{d3}の目", 10 + d3)
    if d2 == d3:
        return (f"{d1}の目", 10 + d1)

    # 6. 役なし（目なし）
    return ("目なし", 1)


def play_chinchiro():
    print("=== チンチロリン（裏モード・7出現） ===")
    print("※[Enter]でサイコロを振ります。 [q] を入力すると終了します。")

    count = 1
    while True:
        user_input = (
            input(
                f"\n[{count}回目] Enterキーを押して振る (qで終了): "
            )
            .strip()
            .lower()
        )

        if user_input == "q":
            print("\nゲームを終了します。お疲れ様でした！")
            break

        dice = roll_dice()
        hand_name, score = evaluate_hand(dice)

        print(f"出目: {dice} ➔ 結果: 【{hand_name}】")
        count += 1


if __name__ == "__main__":
    play_chinchiro()
