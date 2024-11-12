"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
"""
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break
        return h_index
    
    # h랑 citations 에있는것 비교 한다음에 h>=citations[i] 면 answer + 1 이되고 최종적으로 answer 를 리턴한다. 
    # answer = 0 으로 시작해서   