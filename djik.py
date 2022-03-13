import sys
class Graph():
    def __init__(self, ver):
        self.V = ver
        self.graph = [[0 for column in range(ver)] for row in range(ver)]
  
    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        try:
            dist = [sys.maxsize]*self.V
            dist[src] = 0
            sptSet = [False] * self.V
            for cout in range(self.V):
                x = self.minDistance(dist, sptSet)
                sptSet[x] = True
                for y in range(self.V):
                    if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                            dist[y] = dist[x] + self.graph[x][y]
    
            return dist
        except:
            return [-1]*self.V
 
if __name__ == "__main__":
    n = int(input())
    g=Graph(n)
    k=[[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        temp = list(map(int,input().split(" ")))
        for j in temp:
            k[i][j-1]=1
    result = list(map(int,input().split(" ")))
    g.graph = k
    d = g.dijkstra(result[0]-1)
    print(d[result[1]-1])
    