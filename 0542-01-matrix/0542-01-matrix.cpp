class Solution {
public:
    /*
    proceed through finding closest 0 for every member of the grid.
    store the value in the output
    if the distance between cur and distance is >= distance from any of the squares within range from cur to target, then 

    if (current path travelled > stored value in output + 1): return and store value in output 
    */
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int mRows = mat.size();
        int mCols = mat[0].size();
        queue<pair<int,int>> q;
        for (int i = 0; i < mRows; ++i) {
            for (int j = 0; j < mCols; ++j) {
                if (mat[i][j] == 0) q.emplace(i, j);
                else mat[i][j] = -1; // Mark ones as unvisited
            }
        }
        // vector<int> DIR = {0,1,2,3};
        vector<vector<int>> dirs = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();

            // for (vector<int> DIR : directions) {
            for (int i = 0; i < 4; ++i) {
                int nRow = r + dirs[i][0];
                int nCol = c + dirs[i][1];
                // int nRow = r + (DIR[i]%2 - DIR[i]/2);
                // int nCol = c + (0-DIR[i]/2 + 1 - DIR[i]%2);

                if (nRow < 0 || nRow == mRows || nCol < 0 || nCol == mCols || mat[nRow][nCol] != -1) continue;
                mat[nRow][nCol] = mat[r][c] + 1;
                q.emplace(nRow, nCol);
            }
        }
        return mat;
    }
};