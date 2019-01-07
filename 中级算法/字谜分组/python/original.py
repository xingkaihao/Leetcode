class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        思路：用一个字典建立索引表，键为同字母的词，
        键值为该字母的列表在返回结果中的位置index，
        遍历strs，先把元素排序并转化成元组，
        如果该元组没在字典dic中，把这个元素以列表
        的形式加入result，把元组变成字典键，对应
        的键值为该元素在result中的index，如果该元组在
        字典中，把该元素加入到result中对应的列表中，
        返回result。
        """
        flag = 0
        dic = {}
        result = []
        for i in strs:
            j = tuple(sorted(i))
            if j not in dic:
                dic[j]=flag
                flag+=1
                result.append([i])
            else:
                result[dic[j]].append(i)
        return result