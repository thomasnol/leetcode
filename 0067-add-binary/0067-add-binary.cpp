class Solution {
public:
    string addBinary(string a, string b) {
        /*
        for every digit starting from the right, process them, including the remaininder.
        */
        string ans;
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (i >= 0) sum += a[i--] - '0';
            if (j >= 0) sum += b[j--] - '0';
            if (sum >= 2) {
                carry = 1;
                sum -= 2;
            } else {
                carry = 0;
            }
            ans += to_string(sum);
        }
        if (carry == 1) ans += to_string(carry);
        reverse(ans.begin(), ans.end());
        return ans;
    }
};