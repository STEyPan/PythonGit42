class Stack:
    __stack = list()

    def __init__(self, stack = list()):

        self.__stack = stack

    def __del__(self):
        pass

    def push_item(self, item):
        self.__stack.append(item)
        return self.__stack

    def pop_item(self):
        del_elem = self.__stack.pop()
        return del_elem

    def top_item(self):
        if self.__stack:
            return self.__stack[-1]

        return self.__stack

    def size_stack(self):
        return len(self.__stack)

    def __getitem__(self, index):
        return self.__stack[index]

    def __delitem__(self, key):
        return self.__stack.pop(key)

    def __setitem__(self, key, value):
        if key > len(self.__stack):
            while key != len(self.__stack):
                self.__stack.append(0)
        elif key < 0:
            return
        self.__stack.append(value)

    def __contains__(self, target):
        for elem in self.__stack:
            if elem == target:
                return True

        return False

    def indexOf(self, target):
        return self.__stack.index(target)

    def countOf(self, target):
        return self.__stack.count(target)