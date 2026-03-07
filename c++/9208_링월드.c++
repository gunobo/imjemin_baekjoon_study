// c++17

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct SegTree {
    int sz, LOG;
    vector<ll> seg, lz;

    void build(const vector<ll>& xs) {
        int C = xs.size();
        sz = 1; while (sz < C) sz <<= 1;
        LOG = __lg(sz);
        seg.assign(2 * sz, 0);
        lz.assign(2 * sz, 0);
        for (int i = 0; i < C; i++) seg[sz + i] = xs[i];
        for (int i = sz - 1; i >= 1; i--) seg[i] = max(seg[2*i], seg[2*i+1]);
    }

    void push(int p) {
        if (lz[p]) {
            seg[2*p] += lz[p]; lz[2*p] += lz[p];
            seg[2*p+1] += lz[p]; lz[2*p+1] += lz[p];
            lz[p] = 0;
        }
    }

    void add0r(int r) {
        int ri = r + sz;
        for (int i = LOG; i >= 1; i--) push(ri >> i);
        for (int l = sz, rr = ri + 1; l < rr; l >>= 1, rr >>= 1) {
            if (l & 1) { seg[l]++; lz[l]++; l++; }
            if (rr & 1) { --rr; seg[rr]++; lz[rr]++; }
        }
        for (int i = 1; i <= LOG; i++) {
            int p = ri >> i;
            if (!lz[p]) seg[p] = max(seg[2*p], seg[2*p+1]);
        }
    }

    ll qmax(int l, int r) {
        int li = l + sz, ri = r + sz;
        for (int i = LOG; i >= 1; i--) { push(li >> i); push(ri >> i); }
        ll res = -1;
        for (int ll2 = li, rr = ri + 1; ll2 < rr; ll2 >>= 1, rr >>= 1) {
            if (ll2 & 1) res = max(res, seg[ll2++]);
            if (rr & 1)  res = max(res, seg[--rr]);
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    SegTree st;

    while (T--) {
        ll m; int n;
        cin >> m >> n;

        vector<ll> lx(2*n), ly(2*n);
        for (int i = 0; i < n; i++) {
            ll x, y; cin >> x >> y;
            ll a = x, b = (x <= y) ? y : y + m;
            lx[i] = a;     ly[i] = b;
            lx[n+i] = a+m; ly[n+i] = b+m;
        }

        if (n > m) { cout << "NO\n"; continue; }

        // 좌표 압축
        vector<ll> xs;
        xs.reserve(4*n);
        for (int i = 0; i < 2*n; i++) { xs.push_back(lx[i]); xs.push_back(ly[i]); }
        sort(xs.begin(), xs.end());
        xs.erase(unique(xs.begin(), xs.end()), xs.end());
        int C = xs.size();

        st.build(xs);

        // ly 기준 정렬
        vector<int> order(2*n);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int a, int b){ return ly[a] < ly[b]; });

        int sp = 0;
        bool ok = true;

        for (int ci = 0; ci < C && ok; ci++) {
            ll rv = xs[ci];

            while (sp < 2*n && ly[order[sp]] == rv) {
                int idx = order[sp++];
                int rx = (int)(lower_bound(xs.begin(), xs.end(), lx[idx]) - xs.begin());
                st.add0r(rx);
            }

            int li = (int)(lower_bound(xs.begin(), xs.end(), rv - m + 1) - xs.begin());
            if (li > ci) continue;

            if (st.qmax(li, ci) > rv + 1) ok = false;
        }

        cout << (ok ? "YES" : "NO") << "\n";
    }
}