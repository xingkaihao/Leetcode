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
/* 遍历整个s，如果元素为左括号，就压入栈中，如果不是左括号，并且栈中没有元素，则False
 * 如果元素为右括号，把对应的匹配括号赋值给match，如果match和栈定的元素相等，删除栈顶元素，
 * 并继续循环，如果不相等，则false，如果遍历完s还没有false，则为true。
 */