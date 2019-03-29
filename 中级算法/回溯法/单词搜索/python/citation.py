class Solution:
#1.通过search函数的参数x, y记录当前搜索的位置，同时遍历上下左右方向，进入下一个位置。进入时要考虑下个位置是否符合标准。（详细解释见代码）
#2.已搜索过的位置记为true,防止递归无法终止。搜索完后重新标记为false。
    def __init__(self):
        self.pos = list()
        self.n = self.m = 0 #用来储存行和列的数目
        self.flag = False #用来标志最终结果
        self.l = 0   #单词长度
        self.target = "" #目标要构建的单词
        self.direction = [[1,0],[-1,0],[0,1],[0,-1]] #可以选的方向
    def search(self, board, x, y, s):
        if s == self.target: self.flag = True; return #如果构建中的字符串达到目标要构建的单词
        if len(s) >= self.l: return#如果构建的字符的长度大了，就返回，防止无限增加
        self.pos[x][y] = True#把当前位置标记为已搜索，防止再次搜索。
        for d in self.direction:#遍历所有方向，上下左右
            if 0 <= x+d[0] <= self.n-1 and 0 <= y+d[1] <= self.m-1 and not self.pos[x+d[0]][y+d[1]] and board[x+d[0]][y+d[1]] == self.target[len(s)]:#只有当下个节点没有超过边界并且没有被访问过并且是下一个必须的组成单词的下一个字母时，我们才调用递归
                self.search(board, x+d[0], y+d[1], s+board[x+d[0]][y+d[1]])#构建中的单词需要加上下一个字母，同时更新位置
                if self.flag: return#如果找到了该单词，直接返回
        self.pos[x][y] = False#把当前标为未访问
 
    def exist(self, board, word):
        self.n = len(board)    #储存行数
        if self.n == 0: return False
        self.m = len(board[0]) #储存列数
        if self.m == 0: return False
        self.l = len(word)     #储存单词长度
        if self.l == 0 or self.l > self.n*self.m: return False #如果当前单词比所有字母连一起还长
        self.target = word     #储存目标单词
        self.pos = [[False for col in range(self.m)] for row in range(self.n)] #构建一个检测有没有被访问的表
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == word[0]:#如果当前字母等于第一个字母，开始递归
                    self.search(board,i,j,board[i][j])
 
        return self.flag#返回最终结果