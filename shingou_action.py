
from enum import Enum
import sys
# 信号の列挙型
class Shingou(Enum):
    RED = 1    # とまれ
    BLUE = 2    # すすめ
    YELLOW = 3      # ちゅうい

# 信号に対応する処理を行う関数
def act_shingou(color: int) -> Shingou:
    if color == 1:
        print("とまれ")
        return Shingou.RED
    elif color == 2:
        print("すすめ")
        return Shingou.BLUE
    elif color == 3:
        print("ちゅうい")
        return Shingou.YELLOW
    else:
        raise ValueError("信号機の色に対応していません")

try:
    color_input = int(sys.argv[1])
    act_shingou(color_input)
except ValueError as e:
    print(f"エラー：{e}")
