def try_generator():
    for data in (1, 2, 3, 4, 5):
        yield data  # ここでdataが一度返却される

def main():
    for data in (x for x in try_generator()):
        print(data)  # dataを表示
        if data > 2:  # dataが2より大きければループを抜ける
            break

# main関数を実行
main()
