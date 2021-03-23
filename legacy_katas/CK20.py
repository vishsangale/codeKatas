from BST import BinarySearchTree


def maxCoins(nums):
    n = len(nums)
    dp = [[0 for x in xrange(n)] for y in xrange(n)]

    for k in range(2, n + 1):
        for left in range(0, n - k):
            right = left + k
            for i in range(left + 1, right):
                dp[left][right] = max(
                    dp[left][right],
                    nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right],
                )
    return dp[0][n - 1]


a = [1, 8, 5, 6, 9, 3, 0, 2, 4, 1, 7, 1]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
c = [1, 5, 2, 3, 4, 1, 9, 10, 1]
print maxCoins(a)
print maxCoins(b)
print maxCoins(c)

t = BinarySearchTree()
for i in xrange(1, len(a) - 1):
    val = a[i - 1] * a[i] * a[i + 1]
    t.put(a[i], val)
