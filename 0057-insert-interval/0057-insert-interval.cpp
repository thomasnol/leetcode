class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res {};
        for (int v; v < intervals.size(); v++) {
            // newInterval fully before intervals[v]
            if (newInterval[1] < intervals[v][0]) {
                res.push_back(newInterval);
                for (int j = v; j < intervals.size(); j++) {
                    res.push_back(intervals[j]);
                }
                return res;
            }
            // newInterval starts after v ends
            else if (newInterval[0] > intervals[v][1]) {
                res.push_back(intervals[v]);
            // some kind of collision
            } else {
                newInterval[0] = min(newInterval[0], intervals[v][0]);
                newInterval[1] = max(newInterval[1], intervals[v][1]);
            }
        }
        res.push_back(newInterval);
        return res;
    }
};