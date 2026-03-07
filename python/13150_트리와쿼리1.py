import sys
input = sys.stdin.readline

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    def rd(): nonlocal idx; v=data[idx]; idx+=1; return int(v)

    N = rd()
    edge_u = [0]*N; edge_v = [0]*N; edge_w = [0]*N
    adj = [[] for _ in range(N+1)]

    for i in range(1, N):
        u,v,w = rd(),rd(),rd()
        edge_u[i]=u; edge_v[i]=v; edge_w[i]=w
        adj[u].append((v,i)); adj[v].append((u,i))

    parent=[0]*(N+1); depth=[0]*(N+1); subtree=[1]*(N+1)
    heavy=[-1]*(N+1); parent_edge=[0]*(N+1)

    # iterative post-order DFS
    order=[]; visited=[False]*(N+1)
    stack=[(1,0,False)]
    while stack:
        u,p,done = stack.pop()
        if done:
            order.append(u)
            if p:
                subtree[p]+=subtree[u]
                if heavy[p]==-1 or subtree[u]>subtree[heavy[p]]:
                    heavy[p]=u
            continue
        if visited[u]: continue
        visited[u]=True
        stack.append((u,p,True))
        for v,ei in adj[u]:
            if not visited[v]:
                parent[v]=u; depth[v]=depth[u]+1; parent_edge[v]=ei
                stack.append((v,u,False))

    # HLD pos 배정: heavy child를 연속으로
    head=[0]*(N+1); pos=[0]*(N+1); cur=[0]
    stack=[(1,1)]
    while stack:
        u,h=stack.pop()
        head[u]=h; pos[u]=cur[0]; cur[0]+=1
        # light children 먼저 push (나중에 처리)
        for v,ei in adj[u]:
            if v!=parent[u] and v!=heavy[u]:
                stack.append((v,v))
        # heavy child 나중에 push -> 먼저 처리 (LIFO)
        if heavy[u]!=-1:
            stack.append((heavy[u],h))

    # 세그먼트 트리
    SIZE=1
    while SIZE<N: SIZE<<=1
    seg=[0]*(2*SIZE)

    def update(p,val):
        p+=SIZE; seg[p]=val; p>>=1
        while p: seg[p]=max(seg[2*p],seg[2*p+1]); p>>=1

    def query(l,r):
        res=0; l+=SIZE; r+=SIZE+1
        while l<r:
            if l&1: res=max(res,seg[l]); l+=1
            if r&1: r-=1; res=max(res,seg[r])
            l>>=1; r>>=1
        return res

    edge_pos=[0]*N
    for i in range(1,N):
        u,v=edge_u[i],edge_v[i]
        child = v if depth[v]>depth[u] else u
        edge_pos[i]=pos[child]
        update(pos[child], edge_w[i])

    def path_max(u,v):
        res=0
        while head[u]!=head[v]:
            if depth[head[u]]<depth[head[v]]: u,v=v,u
            res=max(res, query(pos[head[u]], pos[u]))
            u=parent[head[u]]
        if u==v: return res
        if depth[u]>depth[v]: u,v=v,u
        res=max(res, query(pos[u]+1, pos[v]))
        return res

    M=rd(); out=[]
    for _ in range(M):
        t=rd()
        if t==1:
            i,c=rd(),rd(); edge_w[i]=c; update(edge_pos[i],c)
        else:
            u,v=rd(),rd(); out.append(path_max(u,v))

    sys.stdout.write('\n'.join(map(str,out))+('\n' if out else ''))

main()