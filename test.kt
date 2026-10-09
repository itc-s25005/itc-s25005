package chap17

fun main() {
    // そうたくんが掛け算を楽しく学べるプログラム作成
    // お気に入りはマリオシリーズ

    println("きみはピーチ城を守るキノピオ警備士である。")
    println("今回の訓練は籠城戦!城に立てこもって敵と戦う防衛戦だ。")
    println("きみは攻め込んできた敵の数を計算して伝える重要な役割を担っている。\n失敗は許されない。")
    println("最初は簡単かもしれないが、徐々に難しくなっていくだろう。健闘を祈る")

    var count = 0  //防衛できた回数
    var first = 1  //左側の数。前回の結果
    var phase = 1  //フェーズ番号
    val enemyList = listOf("クリボー","ノコノコ","パックンフラワー") // 出現する敵

    while (true) {
        val enemy = enemyList.random()  // enemyList からランダムで選出

        if (count % 5 == 0){  // count が 5 で割り切れたら
            println("フェーズ${phase}")  // フェーズ数を表示
        }

        var num = 0
        when(phase) {  // フェーズごとの最大出現数を決める
            1 -> num = (1..2).random()
            2 -> num = (1..3).random()
            3 -> num = (1..5).random()
            4 -> num = (1..7).random()
            else -> num = (1 .. 9).random()
        }
        val ans = first * num  // 正答

        println("${enemy}が ${first} x ${num} 体 やってきた!")
        val answer = readln().toInt()

        if (answer != ans) {  // 不正解の場合ゲーム終了
            println("終了!\n最後の答えは ${ans}\n記録は${phase}フェーズ、防衛できた回数は${count}回!")
            break
        }

        // 正解だったら次の準備
        first = ans
        count++

        if (count % 5 == 0){  //5回ごとにフェーズ数追加
            phase++
        }
    }
    when (count){  // 終了後のコメント
        0 -> println("...経験が足りなかったようだ")
        in 1..5 -> println("初めての籠城戦にしては十分だ。今後の活躍次第では昇格も見込めるぞ")
        in 6 .. 10 -> println("中々見込みのある警備士だ。よし、きみを警備士から上級警備士に昇格しよう")
        in 11 .. 15 -> println("いいね、期待以上の成果だ。そうだ、君を警備士から警備長に昇格しよう")
        in 16 .. 20 -> println("なんと!この実力で警備士とは...善は急げだ。きみを警備士から上級警備長に昇格しよう!")
        else -> println("なんて素晴らしい!すぐにでもきみを警備士から警備司令補に大幅昇格しよう!")
    }
    println("次回も期待している")
}
