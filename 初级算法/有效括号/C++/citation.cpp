class Solution {
public:
    bool isValid(string s) {
        stack<char> symbols;
        for(int i = 0; i < s.size(); i++){
            if(s[i] == '(' || s[i] == '[' || s[i] == '{')
                symbols.push(s[i]);
            else{
                if(symbols.size() == 0)
                    return false;

                char match;
                switch(s[i]){
                    case ')':
                        match = '(';
                        break;
                    case ']':
                        match = '[';
                        break;
                    case '}':
                        match = '{';
                        break;
                }
                char c = symbols.top();
                symbols.pop();

                if(c != match)
                    return false;
            }

        }
        if(symbols.size() != 0)
            return false;

        return true;
    }
};
/* ��������s�����Ԫ��Ϊ�����ţ���ѹ��ջ�У�������������ţ�����ջ��û��Ԫ�أ���False
 * ���Ԫ��Ϊ�����ţ��Ѷ�Ӧ��ƥ�����Ÿ�ֵ��match�����match��ջ����Ԫ����ȣ�ɾ��ջ��Ԫ�أ�
 * ������ѭ�����������ȣ���false�����������s��û��false����Ϊtrue��
 */