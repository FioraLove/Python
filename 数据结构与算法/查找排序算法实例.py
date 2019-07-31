"""
算法——查找排序相关面试题和Leetcode使用
1、给两个字符串s和t，判断t是否为s的重新排列后组成的单词。
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""


# （1）解法一：排序，O(n * logn)


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = list(s)
        tt = list(t)
        ss.sort()
        tt.sort()
        return ss == tt


"""
输入："anagram"、"nagaram"
输出：true
Runtime: 32 ms
"""


# 　　排序方法简写如下：

class Solution:
    def isAnagram(self, s, t):
        return sorted(list(s)) == sorted(list(t))


# （2）解法二：判断字母数量一致，时间复杂度O(n)


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}  # 用字典来维护字符的数量
        dict2 = {}
        for ch in s:
            dict1[ch] = dict1.get(ch, 0) + 1  # 没有就新建，有就加1
        for ch in t:
            dict2[ch] = dict2.get(ch, 0) + 1
        return dict1 == dict2


"""
输入："anagram"，"nagaram"
输出：true
Runtime: 32 ms
"""

"""
2、给定一个m * n的二维列表，查找一个数是否存在。列表有下列特性：

每一行的列表从左到右已经排序好。
每一行第一个数比上一行最后一个数大。
"""


# （1）解法一：线性查找查找，O(mn)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for line in matrix:
            if target in line:
                return True
        return False


# （2）解法二：二分查找O(logn)


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        h = len(matrix)  # 高
        if h == 0:
            return False

        w = len(matrix[0])  # 列
        if w == 0:
            return False

        left = 0
        right = w * h - 1

        while left <= right:
            mid = ((left + right)) // 2
            i = mid // w
            j = mid % w
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return False


"""
3、给定一个列表和一个整数，设计算法找到两个数的下标，使得两个数之和为给定的整数。
　　保证肯定仅有一个结果。

　　leetcode地址：https: // leetcode.com / problems / two - sum - ii - input - array - is -sorted / description /

　　例如，列表[1, 2, 5, 4]
与目标整数3，1 + 2 = 3，结果为(0, 1).

（1）方法一：通过二分查找，找到需要的数字。时间复杂度：O(nlogn)

　　首先确定第一个数，再通过给定整数确定要查找的数，通过二分查找到需要的数。
"""


class Solution:
    def binary_search(self, li, left, right, val):
        """
        二分查找
        :param li: 输入的列表
        :param val: 输入的待查找的值
        :return:
        """
        while left <= right:  # 说明候选区有值
            mid = (left + right) // 2  # 因为是下标， 因此要整除2
            if li[mid] == val:
                # 找到待查找的值返回index
                return mid
            elif li[mid] > val:
                # 待查找的值在mid左侧
                right = mid - 1  # 更新候选区
            else:  # li[mid] < val
                # 待查找的值在mid右侧
                left = mid + 1  # 更新候选区
        else:
            # 没有找到
            return None

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b >= a:
                j = self.binary_search(nums, i + 1, len(nums) - 1, b)
            else:
                j = self.binary_search(nums, 0, i - 1, b)
            if j:
                break
        return sorted([i + 1, j + 1])


"""
（2）方法二：针对已经排好序的列表

　　leetcode地址：https: // leetcode.com / problems / two - sum / description /
"""


class Solution:
    def binary_search(self, li, left, right, val):
        """
        二分查找
        :param li: 输入的列表
        :param val: 输入的待查找的值
        :return:
        """
        while left <= right:  # 说明候选区有值
            mid = (left + right) // 2  # 因为是下标， 因此要整除2
            if li[mid][0] == val:
                # 找到待查找的值返回index
                return mid
            elif li[mid][0] > val:
                # 待查找的值在mid左侧
                right = mid - 1  # 更新候选区
            else:  # li[mid] < val
                # 待查找的值在mid右侧
                left = mid + 1  # 更新候选区
        else:
            # 没有找到
            return None

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_nums = [[num, i] for i, num in enumerate(nums)]
        new_nums.sort(key=lambda x: x[0])

        for i in range(len(new_nums)):
            a = new_nums[i][0]  # 数
            b = target - a
            if b >= a:
                j = self.binary_search(new_nums, i + 1, len(new_nums) - 1, b)
            else:
                j = self.binary_search(new_nums, 0, i - 1, b)
            if j:
                break
        return sorted([new_nums[i][1], new_nums[j][1]])
