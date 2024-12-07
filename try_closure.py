def test_closure(check_value):
    data = []

    def add_data(checked_value):
        if checked_value > check_value:
            data.append(checked_value)

    def get_data():
        return data

    return add_data, get_data
class DataClass(object):
    def __init__(self, checked_value):
        self.data = []
        self.checked_value = checked_value

    def add_data(self, check_value):
        if self.checked_value > check_value:
            self.data.append(check_value)

    def get_data(self):
        return self.data
if __name__ == '__main__':
    add_data, get_data = test_closure(3)

    add_data(2)
    add_data(3)
    add_data(10)

    data = get_data()
    print(data)
