class Solution:
    def minPathSum(self, graph: List[List[int]]) -> int:
        
        answer = [ [0]*len(graph[0]) for i in range(len(graph))]


        for i in range(len(graph)):
            for j in range(len(graph[0])):

                answer[i][j] = graph[i][j]

                if(i>0 and j >0):
                    answer[i][j] += min(answer[i-1][j],answer[i][j-1])

                elif(i==0 and j!=0):
                    answer[i][j] += answer[i][j - 1]

                elif(j == 0 and i!= 0):
                    answer[i][j] += answer[i-1][j]



        return (answer[-1][-1])


        