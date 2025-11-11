INF=9999999
def prims_algorithm(graph,V):
    selected=[False]*V
    no_edge=0
    selected[0]=True
    total_cost=0
    print("Edges in delivery root")
    
    while no_edge<V-1:
        minimum=INF
        x=0
        y=0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if (not selected[j]) and graph[i][j]!=0:
                        if minimum>graph[i][j]:
                            minimum=graph[i][j]
                            x=i
                            y=j
        print(f"{chr(65+x)}-->{chr(65+y)}:{graph[x][y]} min")
        total_cost+=graph[x][y]
        selected[y]=True
        no_edge+=1
    print(f"\nminimum total delivery time:{total_cost} minutes\n")
        
def main():
    while True:
        print("1.input graph and find minimum delivery time")
        print("2.Exit")
        
        choice=input("Enter your choice:")
        
        if choice=="1":
            V=int(input("Enter number of delivery locations"))
            print("Enter adjacency matrix:")
            graph=[]
            for i in range(V):
                row=list(map(int,input(f"row{i+1}:").split()))
                graph.append(row)
            prims_algorithm(graph,V)
        elif choice=="2":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
            
main()
