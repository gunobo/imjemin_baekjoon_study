import sys

# 재귀 깊이 제한 설정
sys.setrecursionlimit(3000)

def solve():
    dna = sys.stdin.readline().strip()
    n = len(dna)
    m = int(sys.stdin.readline())
    
    codon_table = {}
    for _ in range(m):
        c, a = sys.stdin.readline().split()
        codon_table[c] = a
    
    # 아미노산 종류별로 가능한 코돈 리스트 저장
    amino_to_codons = {}
    for c, a in codon_table.items():
        if a not in amino_to_codons:
            amino_to_codons[a] = []
        amino_to_codons[a].append(c)
        
    amino_list = list(amino_to_codons.keys())
    mod = 1000000007

    # 다음 뉴클레오타이드 위치 미리 계산 (A, C, G, T)
    next_idx = [[-1] * 4 for _ in range(n + 1)]
    char_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    
    for i in range(n - 1, -1, -1):
        for j in range(4):
            next_idx[i][j] = next_idx[i+1][j]
        next_idx[i][char_map[dna[i]]] = i

    memo = [-1] * (n + 1)

    def get_count(curr):
        if curr >= n:
            return 0
        if memo[curr] != -1:
            return memo[curr]
        
        total = 0
        
        # 각 아미노산에 대해
        for amino in amino_list:
            # 해당 아미노산을 만들 수 있는 가장 빠른 위치 찾기
            min_pos = float('inf')
            for codon in amino_to_codons[amino]:
                # 코돈의 첫 번째 문자
                p1 = next_idx[curr][char_map[codon[0]]]
                if p1 == -1 or p1 + 1 >= n: continue
                # 두 번째 문자
                p2 = next_idx[p1 + 1][char_map[codon[1]]]
                if p2 == -1 or p2 + 1 >= n: continue
                # 세 번째 문자
                p3 = next_idx[p2 + 1][char_map[codon[2]]]
                if p3 != -1:
                    min_pos = min(min_pos, p3)
            
            if min_pos != float('inf'):
                # (이 아미노산 하나만 있는 경우 1) + (이후에 더 붙는 경우)
                total = (total + 1 + get_count(min_pos + 1)) % mod
                
        memo[curr] = total
        return total

    print(get_count(0))

solve()