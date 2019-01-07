class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        vector<string> temp;
        string s;
        int flag;
        for(int i=0; i<strs.size(); i++){
            s=strs[i];
            sort(s.begin(), s.end());
            flag=0;
            for(int j=0; j<temp.size(); j++){
                if(temp[j]==s){
                    cout<<i;
                    result[j].push_back(strs[i]);
                    flag = 1;
                    break;
                }
            }
            if(flag==0){
                temp.push_back(s);
                result.push_back({strs[i]});
            }
        }
        return result;
    }
};
/* 思路：用一个vector temp存放相同字母的词，遍历整个strs，把元素排序，遍历temp，
 * 判断temp中是否有该相同字母的词，如果有，把这个元素加入result中对应的vector中，
 * 如果没有，用一个flag标记，把这个元素的原型和排序后的字符串分别加入result和temp中，
 * 返回result。
 */