# try_lambda.py

from typing import List, Callable

# 処理を実行する関数
def execute_param_fn(args: List[int], hosei: int, fn: Callable[[int, int], int]) -> int:
    # 引数の関数をargsの最大値または最小値とhoseiを使って呼び出す
    return fn(max(args), hosei)  # max(args) と hosei を引数にラムダ関数を呼び出す

# ラムダ関数の定義と関数の実行例
if __name__ == "__main__":
    # ラムダ関数1: 最大値に補正値を加える
    lambda1 = lambda a, b: a + b

    # ラムダ関数2: 最小値から補正値を引く
    lambda2 = lambda a, b: a - b

    # execute_param_fnを呼び出し
    result1 = execute_param_fn([1, 2, 3], 4, lambda1)  # 最大値+補正値
    result2 = execute_param_fn([1, 2, 3], 4, lambda2)  # 最小値-補正値

    # 結果を出力
    print(result1)  # 結果: 7
    print(result2)  # 結果: -3
