/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (const i in nums) {
        let o_num = target - nums[i]
        if (nums.includes(o_num)){
            if (nums.indexOf(o_num) != i ) {
                return [i, nums.indexOf(o_num)]                 };
        };
}
};