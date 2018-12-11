// Forward declaration of isBadVersion API.
// ˼·��pythonһ��
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int start=1;
        int end=n;
        while(end-start>1){
            int mid=start+(end-start)/2;
            if(isBadVersion(mid)) end=mid;
            else start=mid;
        }
        if(isBadVersion(start)) return start;
        else return end;
    }
};