# shingou_action.py
from enum import Enum

# 信号の列挙型
class Shingou(Enum):
    TOMARE = 1    # とまれ
    SUSUME = 2    # すすめ
    CHUI = 3      # ちゅうい

# 信号に対応する処理を行う関数
def act_shingou(color: int) -> Shingou:
    if color == 1:
        print("とまれ")
        return Shingou.TOMARE
    elif color == 2:
        print("すすめ")
        return Shingou.SUSUME
    elif color == 3:
        print("ちゅうい")
        return Shingou.CHUI
    else:
        raise ValueError("信号機の色に対応していません")
