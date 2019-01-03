class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        思路：把每种括号配对建立字典a，键为后半个括号，
        键值是前半个括号，遍历s， 如果元素不为后半个括号，
        就把元素加入到l中，如果元素为后半个括号且与l最后一个元素配对，
        也就是与a中对应的键值相等，则把l中最后一个元素删除，
        遍历结束，查看l的长度是否为1。
        注意：l初始值为[None]，也就是初始长度为1。
        """
        a = {')':'(', ']':'[', '}':'{'}
        l = [None]
        for i in s:
            if i in a and a[i] == l[-1]:
                l.pop()
            else:
                l.append(i)
        return len(l)==1