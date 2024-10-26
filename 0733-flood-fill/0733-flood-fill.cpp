class Solution {
public:
    void dfs(vector<vector<int>>& image, int sr, int sc, int oColor, int color) {
        if (sr<0 || sr >= image.size() || sc<0 || sc>=image[0].size() || image[sr][sc] != oColor || image[sr][sc] == color) {
            return;
        }
        image[sr][sc] = color;
        dfs(image, sr+1, sc, oColor, color);
        dfs(image, sr-1, sc, oColor, color);
        dfs(image, sr, sc+1, oColor, color);
        dfs(image, sr, sc-1, oColor, color);
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int oColor = image[sr][sc];
        dfs(image, sr, sc, oColor, color);
        return image;
    }
};