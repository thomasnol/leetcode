class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int num = 0;
        int freq = 0;
        for (int n : nums) {
            if (n == num) {
                freq++;
            } else {
                if (freq >= 1) {
                    freq--;
                } else {
                    num = n;
                    freq = 1;
                }
            }
        }
        return num;
        // unordered_map<int, int> map;
        // int cMax = 0;
        // int majNum = 0;
        // for (int n : nums) {
        //     map[n]++;
        //     if (map[n] > cMax) {
        //         cMax = map[n];
        //         majNum = n;
        //     }
        // }
        // return majNum;
    }
};