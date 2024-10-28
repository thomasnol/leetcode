class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for (int n : nums) {
            if (s.contains(n)) return true;
            else s.insert(n);
        }
        return false;
    }
};