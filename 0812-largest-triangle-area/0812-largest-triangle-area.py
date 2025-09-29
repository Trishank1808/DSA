class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p1,p2,p3):
            return abs(p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1]))/2
        return max(area(a, b, c) for a, b, c in combinations(points, 3))

        