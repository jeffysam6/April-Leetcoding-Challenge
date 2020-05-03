class Solution:
    def numIslands(self, graph: List[List[str]]) -> int:
   
        def cover_island(i,j):
            if(i<0 or j<0 or i>=len(graph) or j >= len(graph[0]) or graph[i][j] != '1'):
                return 

            graph[i][j] = "0"
            cover_island(i-1,j)
            cover_island(i+1,j)
            cover_island(i,j-1)
            cover_island(i,j+1)



        c = 0
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if(graph[i][j] == "1"):
                    c += 1
                    cover_island(i,j)

        return(c)

