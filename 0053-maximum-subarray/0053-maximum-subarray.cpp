class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // sliding window
        int curSum = 0;
        int curMax = nums[0];
        for (int n : nums) {
            if (curSum < 0) curSum = 0;            
            curSum += n;
            curMax = max(curSum, curMax);
        }
        return curMax;
    }
};