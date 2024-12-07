import argparse
from enum import Enum

# 進行状況を示すEnum (列挙型)
class Status(Enum):
    INIT = '初期化'
    PROCESSING = '処理中'
    COMPLETE = '完了'

# ジェネレータを使って数値リストのフィルタリング
def number_generator(nums, threshold):
    for num in nums:
        if num > threshold:
            yield num

# クロージャで状態を保持する関数
def create_filter(threshold):
    # フィルタリングをクロージャで保持
    return lambda nums: [num for num in nums if num > threshold]

# メイン処理
def main():
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description="数値リストの処理ツール")
    parser.add_argument('--numbers', type=str, required=True, help="カンマ区切りの数値リスト")
    parser.add_argument('--threshold', type=int, required=True, help="フィルタの閾値")
    parser.add_argument('--operation', type=str, choices=['filter', 'add'], required=True, help="操作の種類")
    args = parser.parse_args()

    # 数値のリストを整数に変換
    nums = list(map(int, args.numbers.split(',')))

    # 状態を表示
    print(f"ステータス: {Status.INIT.value}")

    # 進行状況を処理
    print(f"ステータス: {Status.PROCESSING.value}")
    
    if args.operation == 'filter':
        # ラムダ式とジェネレータを使ってフィルタリング
        filter_func = create_filter(args.threshold)
        filtered_numbers = filter_func(nums)
        
        # 結果をセットに変換して重複を排除
        result = set(filtered_numbers)
        print(f"フィルタリング後の結果: {result}")

    elif args.operation == 'add':
        # 数値を加算する操作
        added_numbers = [num + 10 for num in nums]
        
        # 結果をセットに変換して重複を排除
        result = set(added_numbers)
        print(f"加算後の結果: {result}")

    # 処理完了
    print(f"ステータス: {Status.COMPLETE.value}")

if __name__ == "__main__":
    main()
