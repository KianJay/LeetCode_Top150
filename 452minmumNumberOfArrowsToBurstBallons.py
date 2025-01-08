
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # 간격을 끝나는 시간 기준으로 정렬
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current_end = points[0][1]
        
        for i in range(1, len(points)):
            if points[i][0] > current_end:
                arrows += 1
                current_end = points[i][1]
        
        return arrows