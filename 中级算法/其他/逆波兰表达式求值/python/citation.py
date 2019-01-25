class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        思路：这道题是经典的逆波兰式求值。具体思路是：开辟一个空栈，遇到数字压栈，
        遇到运算符弹出栈中的两个数进行运算，并将运算结果压栈，最后栈中只剩下一个数时，
        就是所求结果。这里需要注意的一点是python中的’/’除法和c语言不太一样。
        在python中，(-1)/2=-1，而在c语言中，(-1)/2=0。也就是c语言中，除法是向零取整，
        即舍弃小数点后的数。而在python中，是向下取整的。而这道题的oj是默认的c语言中的语法，
        所以需要在遇到’/’的时候注意一下。
        """
        if len(tokens) == 0:
            return 0
        stack = [] 
        operator = set(["+", "-", "*", "/"])
        for token in tokens:
            if token not in operator:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+": res = first + second 
                elif token == "-": res = first - second 
                elif token == "*": res = first * second 
                elif token == "/": 
                    if first * second > 0:
                        res = first / second 
                    else:
                        res = - (abs(first) / abs(second))
                stack.append(res)
        return stack[0]