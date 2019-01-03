class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) return 0;
        int m = haystack.size(), n = needle.size();
        if (m < n) return -1;
        for (int i = 0; i <= m - n; ++i) {
            int j = 0;
            for (j = 0; j < n; ++j) {
                if (haystack[i + j] != needle[j]) break;
            }
            if (j == n) return i;
        }
        return -1;
    }
};
/* 利用两层嵌套循环，利用haystack的字符去匹配needle中的字符，
如果和needle中第一个字符匹配，就匹配needle中下一个字符，
如果不匹配，就用haystack中下一个字符匹配needle中第一个字符，
依次类推*/