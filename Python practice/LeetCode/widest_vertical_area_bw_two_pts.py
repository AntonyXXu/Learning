# Given n points on a 2D plane where points[i] = [xi, yi], 
# Return the widest vertical area between two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). 
# The widest vertical area is the one with the maximum width.

# Note that points on the edge of a vertical area are not considered included in the area.

points = [[8,7],[9,9],[7,4],[9,7]]
points1 = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
a = [[1,1],[1,2],[1,3]]
b = [[1,1],[1,1],[1,1]]

def maxWidthOfVertArea(points):
    #only thing that matters is the x axis in this case
    # brute force
    m = 0
    srt = sorted(points)
    for i in range(1,len(points)):
        if srt[i][0] - srt[i-1][0] > m:
            m = srt[i][0] - srt[i-1][0]

    return m

print(maxWidthOfVertArea(points))
print(maxWidthOfVertArea(points1))
print(maxWidthOfVertArea(a))
print(maxWidthOfVertArea(b))