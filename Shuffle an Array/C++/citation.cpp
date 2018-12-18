class Solution {
    vector<int> output;
    vector<int> resnums;
public:
    Solution(vector<int> nums) {
        output = nums;
        resnums = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return resnums;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        int n = output.size();
        for(int i=0; i<n; i++){
            int j = rand()% (n-i);
            swap(output[i], output[j+i]);
        }
        return output;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 * 思路和python一样，只是rand（）的用法很迷
 */