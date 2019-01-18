class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        思路：如果s长度小于等于1，直接返回s的长度；
        否则遍历整个s，利用temp保存当前无重复的字符串，
        利用stack保存所有的不重复字符串长度，
        如果当前字符不在temp中，把当前字符加入temp，
        否则把temp的长度保存在stack中，并把temp中与
        当前字符重复的字符及其之前的字符全都删除，
        把当前字符加入到temp末尾，遍历结束后，
        把temp的长度加入stack中，返回stack的最大值。
        """
        if len(s)<=1:
            return len(s)
        stack=[]
        temp=[s[0]]
        for i in range(1, len(s)):
            if s[i] not in temp:
                temp.append(s[i])
            else:
                stack.append(len(temp))
                k=temp.index(s[i])
                temp=temp[k+1:]
                temp.append(s[i])
        stack.append(len(temp))
        return max(stack)