class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        思路：res用来存放结果，minus用来存放nums中的负数，plus用来存放nums中的非负数，
        一个for循环用来构建minus、plus，并建立字典，字典的键为nums中的元素，键值为该元素
        在nums中的数。对minus和plus进行set()操作，分别赋值给m和p。用一个if判断是否可以有
        [0,0,0]的情况。用两个嵌套的for循环遍历m和p，temp表示第三个需要的数字，当这个数字在字典中，
        并且满足如果下条件：
        如果temp是i和j中的一个，这个元素在nums中的数量要大于1；或者temp<i或者temp>j
        这个是为了避免出现副本。
        满足条件的nums添加到res中，返回res。
        """
        res, minus, plus, count = [], [], [], {}
        for num in nums:
            count[num] = count.get(num, 0)+1
            if num < 0:
                minus.append(num)
            else:
                plus.append(num)
        m, p = set(minus), set(plus)
        if 0 in count and count[0] >= 3:
            res.append([0, 0, 0])
        for i in m:
            for j in p:
                temp = -i - j
                if temp in count and (temp < i or temp > j or (temp in {i, j} and count[temp] > 1)):
                    res.append([i, j, temp])
        return res
