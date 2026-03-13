#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while (T--) {
        int n, t; cin >> n >> t;
        vector<ll> val(n+1);
        for (int i = 1; i <= n; i++) cin >> val[i];
        vector<vector<int>> adj(n+1);
        for (int i = 0; i < n-1; i++) {
            int a, b; cin >> a >> b;
            adj[a].push_back(b); adj[b].push_back(a);
        }

        vector<int> par(n+1, -1); par[1] = 0;
        vector<int> bfs_order;
        {
            queue<int> q; q.push(1);
            while (!q.empty()) {
                int v = q.front(); q.pop();
                bfs_order.push_back(v);
                for (int u : adj[v])
                    if (par[u] == -1) { par[u] = v; q.push(u); }
            }
        }

        vector<int> path;
        for (int v = t; v != 0; v = par[v]) path.push_back(v);
        reverse(path.begin(), path.end());
        set<int> path_set(path.begin(), path.end());
        int K = path.size();

        vector<ll> si_gain(n+1, 0), si_need(n+1, 0);
        // pg0[v] = partial_gain(v, 0): gain when entering v with HP=0
        //   = LLONG_MIN if entry_cost[v] > 0 (can't enter)
        //   = val[v] + sum of max(0, pg0[c]) for c where entry_cost[c]=0
        //   Note: entry_cost[v]=max(0,-val[v])=0 iff val[v]>=0
        vector<ll> pg0(n+1, LLONG_MIN);
        vector<vector<int>> children(n+1); // profitable off-path children (for unlock)

        for (int i = (int)bfs_order.size()-1; i >= 0; i--) {
            int v = bfs_order[i];
            if (path_set.count(v)) continue;

            vector<pair<ll,int>> ch_dp;
            for (int u : adj[v]) {
                if (u == par[v] || path_set.count(u)) continue;
                if (si_gain[u] > 0) ch_dp.push_back({si_need[u], u});
            }
            sort(ch_dp.begin(), ch_dp.end());

            ll need = max(0LL, -val[v]);
            ll running = need + val[v];
            for (auto& [cn, c] : ch_dp) {
                if (running < cn) { need += cn - running; running = cn; }
                running += si_gain[c];
            }
            si_need[v] = need;
            si_gain[v] = val[v];
            for (auto& [cn, c] : ch_dp) {
                si_gain[v] += si_gain[c];
                children[v].push_back(c);
            }

            // pg0[v]: gain when entering v with HP=0
            if (val[v] >= 0) {
                // entry_cost=0, can enter with HP=0
                ll g = val[v];
                for (auto& [cn, c] : ch_dp) {
                    // only children reachable with HP=val[v]+... 
                    // with entry HP=0, after visiting v: running HP = val[v]
                    // but we need to compute this greedily by entry cost
                    // Actually pg0[v] considers entry with H=0, so after v: H'=0+val[v]=val[v]>=0
                    // children with entry_cost[c] <= val[v] are reachable
                    // This recursion is complex. Simple bound: only free children (entry=0 = val[c]>=0)
                    if (val[c] >= 0 && pg0[c] != LLONG_MIN) {
                        // can visit c with running HP = current running
                        // for simplicity, use pg0 of val>=0 children
                        g += max(0LL, pg0[c]);
                    }
                }
                pg0[v] = g;
            } else {
                pg0[v] = LLONG_MIN; // can't enter with HP=0
            }
        }

        // si_thr[v]: min HP to guarantee net gain >= 0 from visiting v
        // val[v]>=0: 0
        // val[v]<0: check if entering with H=entry_cost gives net>0
        //   H=entry_cost, hp_after=0. Free children (val[c]>=0) reachable with hp=0.
        //   free_gain = sum of pg0[c] for c with val[c]>=0
        //   if free_gain > |val[v]|: si_thr = entry_cost
        //   else: si_thr = si_need[v]
        auto get_thr = [&](int v) -> ll {
            if (val[v] >= 0) return 0LL;
            ll entry = -val[v];
            ll free_gain = 0;
            for (int c : children[v]) {
                if (val[c] >= 0 && pg0[c] != LLONG_MIN)
                    free_gain += max(0LL, pg0[c]);
            }
            return (free_gain > entry) ? entry : si_need[v];
        };

        using T2 = pair<ll, int>;
        priority_queue<T2, vector<T2>, greater<T2>> pq;
        vector<bool> visited(n+1, false);

        auto try_push = [&](int node) {
            if (si_gain[node] <= 0 || visited[node]) return;
            pq.push({get_thr(node), node});
        };

        auto unlock_at = [&](int pi) {
            int v = path[pi];
            int prev_v = (pi > 0) ? path[pi-1] : -1;
            int next_v = (pi+1 < K) ? path[pi+1] : -1;
            for (int u : adj[v]) {
                if (u == prev_v || u == next_v || path_set.count(u)) continue;
                try_push(u);
            }
        };

        ll hp = 0;
        bool ok = true;

        auto use_pq = [&]() {
            while (!pq.empty()) {
                auto [need, node] = pq.top();
                if (need > hp) break;
                pq.pop();
                if (visited[node]) continue;
                visited[node] = true;
                hp += val[node];
                for (int c : children[node]) try_push(c);
            }
        };

        for (int i = 0; i < K; i++) {
            use_pq();
            hp += val[path[i]];
            if (hp < 0) { ok = false; break; }
            unlock_at(i);
            use_pq();
        }

        cout << (ok ? "escaped" : "trapped") << "\n";
    }
}