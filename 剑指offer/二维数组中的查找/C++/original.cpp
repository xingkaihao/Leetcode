class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        int rows = array.size();
        if(rows != 0){
            int columns = array[0].size();
            int row = 0;
            int column = columns - 1;
            while(row < rows && column >= 0){
                if(array[row][column] == target){
                    return true;
                }
                else if(array[row][column] > target)
                    column--;
                else
                   row++;
            }
        }
        return false;
    }
};
/* 从二维数组的右上角开始查找，如果当前数等于target，就返回true，
否则，如果该数比target大，说明target可能在该数的左边，如果该数比
target小，说明target可能在该数的下面，依次类推，达到循环停止条件
还没有找到target，说明该数组中没有target，返回false */