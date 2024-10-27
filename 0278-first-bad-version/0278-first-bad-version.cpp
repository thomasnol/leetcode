// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        while (left < right) {
            // int guess = (left + right) / 2;
            int guess = left + (right - left) / 2;
            bool result = isBadVersion(guess);
            if (result) {
                right = guess;
            } else {
                left = guess + 1;
            }
        }
        return right; //
    }
};