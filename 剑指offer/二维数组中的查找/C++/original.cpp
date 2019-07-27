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
/* �Ӷ�ά��������Ͻǿ�ʼ���ң������ǰ������target���ͷ���true��
�������������target��˵��target�����ڸ�������ߣ����������
targetС��˵��target�����ڸ��������棬�������ƣ��ﵽѭ��ֹͣ����
��û���ҵ�target��˵����������û��target������false */