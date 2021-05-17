# You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. 
# Multiple points can have the same coordinates.

# You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

# For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

# Return an array answer, where answer[j] is the answer to the jth query.

points = [[1,3],[3,3],[5,3],[2,2]]
queries = [[2,3,1],[4,3,1],[1,1,2]]

points1 = [[1,1],[2,2],[3,3],[4,4],[5,5]]
queries1 = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]

def query_in_circles(points, queries):
    res = [0] * len(queries)
    for i in range(len(queries)):
        for point in points:
            if inside(point, queries[i]):
                res[i] += 1
    return res
    

def inside(point, circle):
    radius = circle[2]
    return (circle[0] - radius <= point[0]
    and point[0] <= circle[0] + radius
    and circle[1] - radius <= point[1]
    and point[1] <= circle[1] + radius)

print(query_in_circles(points,queries))
print(query_in_circles(points1,queries1))
