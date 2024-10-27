class Solution {
public:
    int longestPalindrome(string s) {
        // vector<int> letters(52);
        unordered_map<char, int> letters;
        int len = 0;
        int lettersRmdr = 0;
        for (char c : s) {
            letters[c]++;
            lettersRmdr++;
            if (letters[c] >= 2) {
                letters[c] -= 2;
                lettersRmdr -= 2;
                len += 2;
            }
        }
        if (lettersRmdr >= 1) len++;
        return len;
    }
};