class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        思路：输入是一个二维数组，"0" 代表是水 "1"代表是陆地  （注意里面存的是字符串，很坑 我调了半天才发现）
　　
　　从左上角(0, 0)开始 遍历所有位置 一直到右下角 (m, n)， 这个过程中 
　　　　如果发现当前位置是"1"， 先把这个位置标记为查询过，
　　　　然后递归查看当前位置的上下左右四个位置，把是"1"的标记遍历过，再查看这个位置的上下左右
　　
　　实际上是一个循环 套了一个递归来实现。
　　当发现一个陆地 就计数器自增1 然后和这个陆地相连的所有陆地都标记为已经查找过

　　小技巧：
　　　　遍历图的时候，边界位置要留意，左边没有左侧，上边没有上侧，右边没有右侧，下边没有下侧， 
　　　　　　可以写分支判断如果是边界就不遍历外侧。
　　　　我选择的办法是，在图的外侧增加一圈"0", 相当于扩大了整个图，
　　　　　　这样在递归陆地的过程中会节省了判断，并且不用考虑超出范围的问题。
        '''
        # 如果是空图 返回没有陆地
        if not grid:
            return 0
        # 把原图改变一下  四周加上一圈"0" 防止出界 方便遍历
        w, h = len(grid[0]), len(grid)
        new_grid = [["0" for i in range(w + 2)]]
        for g in grid:
            new_grid.append(["0"] + g + ["0"])
        new_grid.append(["0" for i in range(w + 2)])
        
        num = 0 # 记录陆地数量
        
        # 遍历除了周围的"0" 中间的部分
        for i in range(1, h+1):
            for j in range(1, w+1):
                if new_grid[i][j] == "1":   # 如果是陆地 就进入深度遍历
                    num += 1
                    self.deep_search(i, j, new_grid)
        
        return num
    
    
    def deep_search(self, i, j, grid):
        """如果当前是陆地，把当前结点标记遍历过，并分别看左右上下四个位置"""
        if grid[i][j] == "0":
            return 
        grid[i][j] = "0"
        self.deep_search(i-1,j,grid)
        self.deep_search(i,j-1,grid)
        self.deep_search(i,j+1,grid)
        self.deep_search(i+1,j,grid)