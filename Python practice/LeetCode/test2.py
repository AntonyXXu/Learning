# tomblerone
# each piece has diff sweetness (1 to 10)
# share chocolate with N friends, everyone gets whole piece
# Pieces must be consecutive
# friends take the sweetest pieces before you
# maximize the sweetness level for yourself

# -ve sweetness?
# more friends than pieces?

# k is number of people
# n is number of pieces
# n > k
c = [1, 2, 3, 3, 2, 4, 4]
c = [1, 5, 1, 10, 2, 4, 4]
c = [1, 1, 10, 1, 1, 1, 1]


def pieces(k, chocolate):
    result = 0
    for i in range(len(chocolate) - k + 1):
        left = sum(chocolate[:i+1])
        right = split(k - 1, chocolate[i+1:])
        canEat = min(left, right)
        result = max(result, canEat)
    return result


def split(k, chocolate):
    if k == 0:
        return sum[chocolate]
    result = 0
    for i in range(len(chocolate) - k + 1):
        left = sum(chocolate[:i+1])
        right = split(k - 1, chocolate[i+1:])
        canEat = min(left, right)
        result = max(result, canEat)
    return result


def calc(k, choc):
    def conditional(num):
        people = 0
        current = 0
        for piece in choc:
            current += piece
            if current >= num:
                current = 0
                people += 1
            if people >= k:
                return False
        return True
    left = 1
    right = sum(choc)

    while left < right:
        mid = left + (right - left) // 2
        if conditional(mid):
            right = mid
        else:
            left = mid + 1
    return left - 1


print(calc(3, [1, 2, 3, 3, 2, 4, 4]))
# O(n ^ k)
# O(nlogn)
