class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        print(set1, set2)
        dif1 = list(set1 - set2)
        dif2 = list(set2- set1)
        return [dif1, dif2]
    
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # nums1과 nums2의 고유 요소를 추적하기 위한 해시맵 생성
        dic1 = {}
        dic2 = {}

        # nums1의 각 요소를 해시맵에 저장
        for num in nums1:
            dic1[num] = dic1.get(num, 0) + 1

        # nums2의 각 요소를 해시맵에 저장
        for num in nums2:
            dic2[num] = dic2.get(num, 0) + 1

        # nums1에는 있지만 nums2에는 없는 요소들
        diff1 = [num for num in dic1 if num not in dic2]

        # nums2에는 있지만 nums1에는 없는 요소들
        diff2 = [num for num in dic2 if num not in dic1]

        return [diff1, diff2]
