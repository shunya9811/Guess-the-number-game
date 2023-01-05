import random, math

# 入力
def inputMin():
    min_num = input("最小数を入力してください>") 
    if not isInt(min_num):
        return inputMin()
    return int(min_num)

def inputMax(min_num):
    max_num = input("最大数を入力してください>")
    if not isInt(max_num):
        return inputMax(min_num)
    if min_num >= int(max_num):
        print("最小数より大きい整数を入力してください")
        return inputMax(min_num)
    return int(max_num)

def inputGuess(min_num, max_num):
    guess = input("回答>")
    if not isInt(guess):
        return inputGuess(min_num, max_num)
    if min_num > int(guess) or max_num < int(guess):
        print(str(min_num) + "から" + str(max_num) + "までの整数が有効です")
        return inputGuess(min_num, max_num)
    return int(guess)

# 入力チェック
def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        print("整数を入力してください")
        return False

# ゲーム
def guess(min_num, max_num, answer):
    print("それでは" + str(min_num) + "から" + str(max_num) + "までの、私が決めた数字を当ててください")

    # 二分探索できる回数だけ猶予を与える
    diff = abs(max_num - min_num)
    count = int(math.log2(diff)) + 2

    for i in range(1, count):
        guess = inputGuess(min_num, max_num)
        if compare(answer, guess):
            print("正解だよ!!私が決めた数字は" + str(answer) + "だよ。" + str(i) + "回目で当たったね")
            return 
        else:
            continue
    
    print("残念でした。当たらなかったね。答えは" + str(answer) + "だよ!またチャレンジしてみて")

def compare(answer, guess):
    if guess > answer:
        print(str(guess) + "は大きすぎるよ")
        return False
    elif guess < answer:
        print(str(guess) + "は小さすぎるよ")
        return False
    else:
        return True

def main():
    print("これから設定する最小数と最大数の中で、私が決めた数字を当ててください")
    min_num = inputMin()
    max_num = inputMax(min_num)
    answer = random.randint(min_num, max_num)
    guess(min_num, max_num, answer)

if __name__ == "__main__":
    main()