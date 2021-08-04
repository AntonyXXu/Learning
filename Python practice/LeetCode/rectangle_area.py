# https://leetcode.com/problems/rectangle-area/

def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    a_length = ax2 - ax1
    a_height = ay2 - ay1
    b_length = bx2 - bx1
    b_height = by2 - by1

    overlapTop = min(ay2, by2)
    overlapBot = max(ay1, by1)

    overlapRight = min(ax2, bx2)
    overlapLeft = max(ax1, bx1)

    overlap_length = overlapRight - overlapLeft
    overlap_height = overlapTop - overlapBot

    if overlap_length <= 0 or overlap_height <= 0:
        return abs(a_length * a_height) + abs(b_length * b_height)
    return abs(a_length * a_height) + abs(b_length * b_height) - overlap_length * overlap_height
