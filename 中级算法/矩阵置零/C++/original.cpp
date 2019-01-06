class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int row=matrix.size();
        int column=matrix[0].size();
        vector<int> row1, column1;
        for(int i=0; i<row; i++){
            for(int l=0; l<column; l++){
                if(matrix[i][l]==0){
                    row1.push_back(i);
                    column1.push_back(l);
                }
            }
        }
        if(row1.empty()) return;
        sort(row1.begin(), row1.end());
        sort(column1.begin(), column1.end());
        vector<int> row11;
        row11.push_back(row1[0]);
        for(int c=1; c<row1.size(); c++){
            if(row1[c]!=row1[c-1]) row11.push_back(row1[c]);
        }
        int m=0;
        for(int j=0; j<row; j++){
            if(row11[m]==j){
                for(int n=0; n<column; n++){
                    matrix[j][n]=0;
                }
                m+=1;
            }
            else{
                for(int k=0; k<column1.size(); k++){
                    matrix[j][column1[k]]=0;
                }
            }
        }
    }
};
/* ˼·���ȱ���һ��matrix������0Ԫ�ص�λ�ã���������row1�У���������column1�У�
 * ���row1Ϊ�գ���û��0Ԫ�أ���������򡣷��򣬰�row1��column1���򣬲�ɾ��row1
 * �еĸ�����֮�����matrix�������row1�е��У���������0��������ǣ��Ͱ�column��
 * ������0��
 */