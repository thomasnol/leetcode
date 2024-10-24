class Solution {
public:
    bool isPalindrome(string s) {
        int i1 = 0;
        int i2 = s.length() - 1;
        while (i1 < i2) {
            if (!isalnum(s[i1])) {
                i1++;
            } else if (!isalnum(s[i2])) {
                i2--;
            } else if (tolower(s[i1]) != tolower(s[i2])) {
                return false;
            } else {
                i1++;
                i2--;
            }
        }
        return true;
    }
};