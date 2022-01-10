CONFORM_DICT = {'}': '{',
                ')': '(',
                ']': '['}


class My_Stack():

    def __init__(self, a):
        if type(a) == type('string'):
            self.s_list = list(a)
        else:
            self.s_list = a

    def isEmpty(self):
        print('test isEmpty ')
        return len(self.s_list) == 0

    def push(self, a):
        self.s_list.append(a)

    def __str__(self):
        s_len = len(self.s_list)
        s_str = '['
        for i in range(0, s_len):
            s_str += str(self.s_list[i])
            if i != s_len - 1:
                s_str += ', '
            else:
                s_str += ']'
        return s_str

    def pop(self):
        if len(self.s_list) == 0:
            return ValueError
        else:
            self.s_list.pop(self.size() - 1)
            return self.peek()

    def size(self):
        return len(self.s_list)

    def peek(self):
        if len(self.s_list) == 0:
            return None
        else:
            return self.s_list[-1]


def test_string(test_str):
    st = My_Stack([])
    print(test_str)
    test_str_list = list(test_str)
    for el in test_str_list:
        if el not in CONFORM_DICT:
            st.push(el)

        else:
            if st.peek() == CONFORM_DICT[el]:
                st.pop()
            else:
                print('!!!Несбалансированная последовательность!!!')
                return False
    print('Сбалансированная последовательность')
    return True


if __name__ == "__main__":
    # test_str = '(((([{}]))))'
    # test_str = '[([])((([[[]]])))]{()}'
    # test_str = '{{[()]}}'
    # test_str = '}{}'
    # test_str = '{{[(])]}}'
    test_str = '[[{())}]'
    print()
    test_string(test_str)
