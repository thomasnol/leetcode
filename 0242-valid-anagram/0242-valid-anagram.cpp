class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) { return false; }
        unordered_map<char, int> letters;
        for (int i = 0; i < s.length(); i++) {
            if (!letters.contains(s[i])) {
                letters[s[i]] = 1;
            } else {
                letters[s[i]]++;
            }
        }
        for (int i = 0; i < t.length(); i++) {
            letters[t[i]]--;
            if (letters[t[i]] < 0) {
                return false;
            }
        }
        return true;
    }
};