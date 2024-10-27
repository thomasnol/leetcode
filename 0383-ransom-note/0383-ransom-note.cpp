class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> letters(26);
        for (char& c : magazine) {
            letters[c - 'a']++;
        }
        for (char& c : ransomNote) {
            if (letters[c - 'a'] <= 0) return false;
            letters[c - 'a']--;
        }
        return true;
        // unordered_map<char, int> letters;
        // for (char c : magazine) {
        //     letters[c]++;
        // }
        // for (char c : ransomNote) {
        //     if (letters[c] <= 0) return false;
        //     letters[c]--;
        // }
        // return true;
    }
};