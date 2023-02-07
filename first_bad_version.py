def isBadVersion(version: int) -> bool:
    if version == 4:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                if not isBadVersion(mid - 1):
                    return mid
                right = mid - 1



s = Solution()
print(s.firstBadVersion(5))
