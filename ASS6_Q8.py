class ThreeSum:
    def __init__(self, nums):
        self.nums = nums

    def find_three_sum(self):
        nums = sorted(self.nums)
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result

nums = [-25, -10, -7, -3, 2, 4, 8, 10]
three_sum = ThreeSum(nums)
result = three_sum.find_three_sum()

print(result)

