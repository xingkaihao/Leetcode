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
/* ˼·����һ��vector temp�����ͬ��ĸ�Ĵʣ���������strs����Ԫ�����򣬱���temp��
 * �ж�temp���Ƿ��и���ͬ��ĸ�Ĵʣ�����У������Ԫ�ؼ���result�ж�Ӧ��vector�У�
 * ���û�У���һ��flag��ǣ������Ԫ�ص�ԭ�ͺ��������ַ����ֱ����result��temp�У�
 * ����result��
 */