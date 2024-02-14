class Unit:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def __len__(self):
        return self.length
    def append_begin(self, data):
        new_unit = Unit(data)
        new_unit.next = self.head
        self.head = new_unit
        self.length += 1
    def append_end(self, data):
        new_node = Unit(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        self.length += 1
    def remove_first(self):
        if not self.head:
            raise ValueError('Связанный список пуст')
        self.head = self.head.next
        self.length -= 1
    def remove_last(self):
        if not self.head:
            raise ValueError('Связанный список пуст')
        if not self.head.next:
            self.head = None
        else:
            second_last = self.head
            while second_last.next.next:
                second_last = second_last.next
            second_last.next = None
        self.length -= 1
    def remove_first_value(self, value):
        if not self.head:
            raise ValueError('Связанный список пуст')
        if self.head.data == value:
            self.head = self.head.next
            self.length -= 1
            return 
        actual = self.head
        while actual.next:
            if actual.next.data == value:
                actual.next = actual.next.next
                self.length -= 1
                return
            actual = actual.next
        raise ValueError('Значение не найдено')
    def remove_last_value(self, value):
        if not self.head:
            raise ValueError('Связанный список пуст')
        if self.head.data == value:
            self.head = self.head.next
            self.length -= 1
            return
        actual = self.head
        while actual.next:
            if actual.next.data == value and not actual.next.next:
                actual.next = None
                self.length -= 1
                return
            if actual.next.data == value:
                actual.next = actual.next.next
                self.length -= 1
                return
            actual = actual.next
        raise ValueError('Значение не найдено')
    def remove_at(self, index):
        if index < 0 or index >= self.length:
            raise ValueError('Invalid index')
        if index == 0:
            self.head = self.head.next
        else:
            actual = self.head
            for _ in range(index - 1):
                actual = actual.next
            actual.next = actual.next.next
        self.length -= 1

