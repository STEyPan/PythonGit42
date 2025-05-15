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
