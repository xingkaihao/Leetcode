
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()<2) return 0;
        int min_price = prices[0];
        int max_profile = 0;
        for(int i=0; i<prices.size(); ++i){
            if(min_price > prices[i]) min_price=prices[i];
            if(max_profile < (prices[i]-min_price)){
                max_profile = prices[i]-min_price; 
            } 
        }
        return max_profile;
    }
};
//思路和python一样