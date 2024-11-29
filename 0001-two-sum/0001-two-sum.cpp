// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         unordered_map<int, int>m;
//         for(int i = 0; i < nums.size(); i++){
//             if(m.count(target - nums[i])) return {m[target - nums[i]], i};
//             m[nums[i]] = i;
//         }
//         return {0,1};
//     }  
// };

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int>m;
        int n = nums.size();
        vector<int> v;
        for(int i = 0; i < n; i++){
            int tg = target - nums[i];
            // if(m.count(tg)) {
            if(m.find(tg)!=m.end()) {
                v.push_back(i);
                v.push_back(m[tg]);
                // return {m[tg], i};
                break;
            }
            m[nums[i]] = i;
        }
        return v;
    }  
};