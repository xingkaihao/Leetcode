class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        思路：利用两个指针分别指向0和2，0的指针是从前往后移动，
        2的指针是从后往前移动；扫描整个nums，当前元素为1时，
        不执行操作，直接下一个；当前元素为2时，当前元素与2指针
        元素交换，并且当前指针不移动；当前元素为0时，当前元素和
        0指针元素交换，当前指针向下移一位，因为0元素指针的位置元素
        已经是扫描过的依次类推。
        """
        zero, two = -1, len(nums)
        i = 0
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[two], nums[i] = nums[i], nums[two]
            else:
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1