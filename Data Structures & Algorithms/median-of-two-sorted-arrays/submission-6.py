class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_kth(nums1, nums2, k):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]
            
            m1, m2 = len(nums1) // 2, len(nums2) // 2
            
            if m1 + m2 < k:
                if nums1[m1] < nums2[m2]:
                    return find_kth(nums1[m1 + 1:], nums2, k - m1 - 1)
                else:
                    return find_kth(nums1, nums2[m2 + 1:], k - m2 - 1)
            else:
                if nums1[m1] < nums2[m2]:
                    return find_kth(nums1, nums2[:m2], k)
                else:
                    return find_kth(nums1[:m1], nums2, k)

        total_length = len(nums1) + len(nums2)
        median = total_length // 2
        if total_length % 2 == 0:
            return (find_kth(nums1, nums2, median - 1) + find_kth(nums1, nums2, median)) / 2
        else:
            return find_kth(nums1, nums2, median)
