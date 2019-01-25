class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        ˼·��������Ǿ�����沨��ʽ��ֵ������˼·�ǣ�����һ����ջ����������ѹջ��
        �������������ջ�е��������������㣬����������ѹջ�����ջ��ֻʣ��һ����ʱ��
        ������������������Ҫע���һ����python�еġ�/��������c���Բ�̫һ����
        ��python�У�(-1)/2=-1������c�����У�(-1)/2=0��Ҳ����c�����У�����������ȡ����
        ������С��������������python�У�������ȡ���ġ���������oj��Ĭ�ϵ�c�����е��﷨��
        ������Ҫ��������/����ʱ��ע��һ�¡�
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