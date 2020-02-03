def find_pivot(arr, l, r):
    if r == l + 1 and arr[l] > arr[r] :
        return r
    l_n, r_n = arr[l], arr[r]
    if l_n > r_n:
        m = (l + r) // 2
        if l_n > arr[m]:
            return find_pivot(arr, l, m)
        else:
            return find_pivot(arr, m, r)
    else:
        return 0

# more elegent solution from LC
class Solution:
    def findMin(self, nums) -> int:
        if not nums:
            return

        frnt, rear = 0, len(nums) - 1
        # rotated before the first num or after the last num
        # equals to No rotation.
        if nums[frnt] <= nums[rear]:
            return nums[frnt]
        while frnt < rear - 1:
            mid = (frnt + rear) // 2

            if nums[0] < nums[mid]:
                frnt = mid
            else:
                rear = mid
        return min(nums[frnt], nums[rear])


if __name__ == '__main__':
    arr = [0,1,2,4,5,6,7,9]
    print(find_pivot(arr, 0, len(arr)-1))