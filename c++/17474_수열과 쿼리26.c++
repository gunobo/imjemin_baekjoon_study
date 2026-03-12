/*
 * Segment Tree Beats (Ji 세그먼트 트리)
 *
 * 지원 연산:
 *   chmin(l, r, x) : A[i] = min(A[i], x)  for l<=i<=r
 *   qmax (l, r)    : max(A[l..r])
 *   qsum (l, r)    : sum(A[l..r])
 *
 * 각 노드가 저장하는 값:
 *   max1   : 구간 최댓값
 *   max2   : max1 미만인 값 중 최댓값  (-INF if 없음)
 *   cntMax : max1 개수
 *   sum    : 구간 합
 *   lazy   : 아직 내리지 않은 chmin 값  (INF = 없음)
 *
 * chmin(x) 처리 규칙:
 *   x >= max1            → 아무 변화 없음 (break)
 *   max2 < x < max1      → max1 원소만 x로 교체 → O(1) 갱신 후 lazy 저장
 *   x <= max2            → 자식 양쪽으로 내려가야 함
 *
 * 시간복잡도: O((N+M) log² N)  (势函数 증명)
 * 메모리:     각 Node 40B × 4N ≒ 160MB  (N=10^6 기준)
 */

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

static const ll INF = (ll)4e18;

// ── 노드 구조체 ─────────────────────────────────────────────────────
struct Node {
    ll  max1;    // 구간 최댓값
    ll  max2;    // 두 번째 최댓값 (max1 미만, 없으면 -INF)
    ll  sum;     // 구간 합
    int cntMax;  // max1 개수
    ll  lazy;    // 내려야 할 chmin  (INF = 없음)
};

// ── Segment Tree Beats ──────────────────────────────────────────────
struct SegBeats {
    int      n;
    vector<Node> t;

    // ── 빌드 ──────────────────────────────────────────────────────
    void build(vector<ll>& a, int v, int l, int r) {
        t[v].lazy = INF;
        if (l == r) {
            t[v].max1   = a[l];
            t[v].max2   = -INF;
            t[v].sum    = a[l];
            t[v].cntMax = 1;
            return;
        }
        int mid = (l + r) / 2;
        build(a, 2*v,   l,     mid);
        build(a, 2*v+1, mid+1, r);
        pull(v);
    }
    void init(vector<ll>& a) {
        n = (int)a.size() - 1;   // 1-indexed
        t.resize(4 * n + 4);
        build(a, 1, 1, n);
    }

    // ── pull-up: 자식 → 부모 ──────────────────────────────────────
    void pull(int v) {
        Node& L = t[2*v]; Node& R = t[2*v+1]; Node& V = t[v];
        V.sum = L.sum + R.sum;
        if (L.max1 == R.max1) {
            V.max1   = L.max1;
            V.cntMax = L.cntMax + R.cntMax;
            V.max2   = max(L.max2, R.max2);
        } else if (L.max1 > R.max1) {
            V.max1   = L.max1;
            V.cntMax = L.cntMax;
            V.max2   = max(L.max2, R.max1);
        } else {
            V.max1   = R.max1;
            V.cntMax = R.cntMax;
            V.max2   = max(L.max1, R.max2);
        }
    }

    // ── chmin을 노드 v에 직접 적용 (max2 < x < max1 조건 만족 시) ──
    void applyChmin(int v, ll x) {
        if (x >= t[v].max1) return;
        // max1인 원소만 x로 바뀜 → sum 조정, max1 갱신
        t[v].sum  -= (t[v].max1 - x) * (ll)t[v].cntMax;
        t[v].max1  = x;
        // 자식에게 내려야 할 lazy 갱신 (더 작은 값으로)
        t[v].lazy  = min(t[v].lazy, x);
    }

    // ── lazy push-down: 부모 → 자식 ──────────────────────────────
    void push(int v) {
        if (t[v].lazy < INF) {
            applyChmin(2*v,   t[v].lazy);
            applyChmin(2*v+1, t[v].lazy);
            t[v].lazy = INF;
        }
    }

    // ── range chmin [l, r] x ──────────────────────────────────────
    void chmin(int v, int nl, int nr, int l, int r, ll x) {
        if (l > nr || r < nl || x >= t[v].max1) return;   // break 조건
        if (l <= nl && nr <= r && x > t[v].max2) {        // tag 조건
            applyChmin(v, x);
            return;
        }
        push(v);
        int mid = (nl + nr) / 2;
        chmin(2*v,   nl,    mid, l, r, x);
        chmin(2*v+1, mid+1, nr,  l, r, x);
        pull(v);
    }

    // ── range max query [l, r] ────────────────────────────────────
    ll qmax(int v, int nl, int nr, int l, int r) {
        if (l > nr || r < nl) return -INF;
        if (l <= nl && nr <= r) return t[v].max1;
        push(v);
        int mid = (nl + nr) / 2;
        return max(qmax(2*v,   nl,    mid, l, r),
                   qmax(2*v+1, mid+1, nr,  l, r));
    }

    // ── range sum query [l, r] ────────────────────────────────────
    ll qsum(int v, int nl, int nr, int l, int r) {
        if (l > nr || r < nl) return 0LL;
        if (l <= nl && nr <= r) return t[v].sum;
        push(v);
        int mid = (nl + nr) / 2;
        return qsum(2*v,   nl,    mid, l, r)
             + qsum(2*v+1, mid+1, nr,  l, r);
    }

    // ── public interface ──────────────────────────────────────────
    void chmin(int l, int r, ll x) { chmin(1, 1, n, l, r, x); }
    ll   qmax (int l, int r)       { return qmax(1, 1, n, l, r); }
    ll   qsum (int l, int r)       { return qsum(1, 1, n, l, r); }
};

// ── main ────────────────────────────────────────────────────────────
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;
    vector<ll> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];

    SegBeats seg;
    seg.init(a);

    int m; cin >> m;
    while (m--) {
        int t; cin >> t;
        if (t == 1) {
            int l, r; ll x; cin >> l >> r >> x;
            seg.chmin(l, r, x);
        } else if (t == 2) {
            int l, r; cin >> l >> r;
            cout << seg.qmax(l, r) << "\n";
        } else {
            int l, r; cin >> l >> r;
            cout << seg.qsum(l, r) << "\n";
        }
    }
}