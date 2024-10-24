class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) { return -1; }
        int left = 0;
        int right = nums.size() - 1;
        int index;
        /*
        step size = .25*arraylength
        find middle index, compare val with target:
        if val lower than target, set next index to 75th and continue, with range 50-100th
        */
        while (left <= right) {
            index = (left + right) / 2;
            if (nums[index] == target) {
                return index;
            } else if (nums[index] < target) {
                left = index + 1;
            } else {
                right = index - 1;
            }
        }
        return -1;
    }
};