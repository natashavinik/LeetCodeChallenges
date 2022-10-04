class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int need = target - nums[i];
            if (map.containsKey(need)) {
                return new int[] {map.get(need), i};
            }
            map.put(nums[i], i);
        }
    return null;}
}




//    n_dict = {}
        
//         for i in range(len(nums)):
//             need = target - nums[i]
//             if need in n_dict:
//                 return (n_dict[need], i)
//             n_dict[nums[i]] = i