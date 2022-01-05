class Counter:
    def start(self, start_value=0):
        self.value = start_value

    def up_counter(self):
        self.value += 1

    def down_counter(self):
        self.value -= 1

    def show_counter(self):
        print(f'count={self.value}')

    def clear_all(self):
        self.value = 0
