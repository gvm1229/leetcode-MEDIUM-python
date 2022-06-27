from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue

            # The code from this point on automatically assumes "order of the pair (i & i+1)" != "non-decreasing".
            if changed:
                return False  # already changed a value, cannot do it twice.

            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]

            changed = True

        return True


p1 = Solution()
print(p1.checkPossibility([4, 2, 3]))       # Expected output: True
print(p1.checkPossibility([4, 2, 1]))       # Expected output: False
print(p1.checkPossibility([5, 7, 1, 8]))    # Expected output: True
print(p1.checkPossibility([3, 4, 2, 3]))    # Expected output: False