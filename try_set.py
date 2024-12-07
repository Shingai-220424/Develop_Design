import random
import time

# 0～1億の間のランダムな整数要素を持つ100万個の要素のリストを内包表記で作成
a = [random.randint(0, 100000000) for _ in range(1000000)]

# 0～1億の間のランダムな整数要素を持つ100個のリストを作成
checked_list = [random.randint(0, 100000000) for _ in range(100)]

# リストaをセットに変換
a_set = set(a)

# チェック開始前の時刻を記録
start_time = time.time()

# checked_listの各要素がa_setに存在するかどうかをチェック
for temp in checked_list:
    if temp in a_set:
        print(f'temp:{temp} in a_set')

# チェックにかかった時間を表示
end_time = time.time()
print(f'チェックにかかった時間: {end_time - start_time}秒')
