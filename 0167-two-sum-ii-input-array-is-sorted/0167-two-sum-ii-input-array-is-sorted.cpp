class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;
        while (l < r) {
            int tsum = numbers[l] + numbers[r];

            if (tsum > target) {
                r--;
            } else if (tsum < target) {
                l++;
            } else {
                return {l + 1, r + 1};
            }
        }
        return {};
    }
};
