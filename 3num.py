nums = [-2,-7,-11,-8,9,-7,-8,-15,10,4,3,9,8,11,1,12,-6,-14,-2,-1,-7,-13,-11,-15,11,-2,7,-4,12,7,-3,-5,7,-7,3,2,1,10,2,-12,-1,12,12,-8,9,-9,11,10,14,-6,-6,-8,-3,-2,14,-15,3,-2,-4,1,-9,8,11,5,-14,-1,14,-6,-14,2,-2,-8,-9,-13,0,7,-7,-4,2,-8,-2,11,-9,2,-13,-10,2,5,4,13,13,2,-1,10,14,-8,-14,14,2,10]
nums = sorted(nums)

all_list = []
for i in range(len(nums)):
    if nums[i] > 0:
        break
    j = i + 1
    k = len(nums) - 1
    if nums[i] == nums[j] == nums[k] == 0:
        all_list.append((0, 0, 0))
        continue
    while j < k:
        if nums[i] + nums[j] + nums[k] > 0:
            k -= 1
        elif nums[i] + nums[j] + nums[k] < 0:
            j += 1
        else:
            all_list.append((nums[i], nums[j], nums[k]))
            k -= 1
            j += 1

all_list = list(set(all_list))
all_list = list(map(lambda x: list(x), all_list))
print()

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            HL = self.maxDepth(root.left)
            HR = self.maxDepth(root.right)
            return max(HL, HR) + 1
        else:
            return 0