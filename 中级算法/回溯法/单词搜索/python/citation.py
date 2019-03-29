class Solution:
#1.ͨ��search�����Ĳ���x, y��¼��ǰ������λ�ã�ͬʱ�����������ҷ��򣬽�����һ��λ�á�����ʱҪ�����¸�λ���Ƿ���ϱ�׼������ϸ���ͼ����룩
#2.����������λ�ü�Ϊtrue,��ֹ�ݹ��޷���ֹ������������±��Ϊfalse��
    def __init__(self):
        self.pos = list()
        self.n = self.m = 0 #���������к��е���Ŀ
        self.flag = False #������־���ս��
        self.l = 0   #���ʳ���
        self.target = "" #Ŀ��Ҫ�����ĵ���
        self.direction = [[1,0],[-1,0],[0,1],[0,-1]] #����ѡ�ķ���
    def search(self, board, x, y, s):
        if s == self.target: self.flag = True; return #��������е��ַ����ﵽĿ��Ҫ�����ĵ���
        if len(s) >= self.l: return#����������ַ��ĳ��ȴ��ˣ��ͷ��أ���ֹ��������
        self.pos[x][y] = True#�ѵ�ǰλ�ñ��Ϊ����������ֹ�ٴ�������
        for d in self.direction:#�������з�����������
            if 0 <= x+d[0] <= self.n-1 and 0 <= y+d[1] <= self.m-1 and not self.pos[x+d[0]][y+d[1]] and board[x+d[0]][y+d[1]] == self.target[len(s)]:#ֻ�е��¸��ڵ�û�г����߽粢��û�б����ʹ���������һ���������ɵ��ʵ���һ����ĸʱ�����ǲŵ��õݹ�
                self.search(board, x+d[0], y+d[1], s+board[x+d[0]][y+d[1]])#�����еĵ�����Ҫ������һ����ĸ��ͬʱ����λ��
                if self.flag: return#����ҵ��˸õ��ʣ�ֱ�ӷ���
        self.pos[x][y] = False#�ѵ�ǰ��Ϊδ����
 
    def exist(self, board, word):
        self.n = len(board)    #��������
        if self.n == 0: return False
        self.m = len(board[0]) #��������
        if self.m == 0: return False
        self.l = len(word)     #���浥�ʳ���
        if self.l == 0 or self.l > self.n*self.m: return False #�����ǰ���ʱ�������ĸ��һ�𻹳�
        self.target = word     #����Ŀ�굥��
        self.pos = [[False for col in range(self.m)] for row in range(self.n)] #����һ�������û�б����ʵı�
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == word[0]:#�����ǰ��ĸ���ڵ�һ����ĸ����ʼ�ݹ�
                    self.search(board,i,j,board[i][j])
 
        return self.flag#�������ս��