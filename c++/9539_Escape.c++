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

        // BFS from 1 to find parent array + order
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

        // Reconstruct path 1 -> t
        vector<int> path;
        for (int v = t; v != 0; v = par[v]) path.push_back(v);
        reverse(path.begin(), path.end());
        set<int> path_set(path.begin(), path.end());
        int K = path.size();

        // Bottom-up DP for off-path nodes:
        //   si_gain[v] = optimal HP gain visiting v's subtree (with enough HP)
        //   si_need[v] = min HP at v's entry to achieve si_gain[v]
        //   sorted_ch[v] = profitable children sorted by ENTRY COST ascending
        //                  (entry cost = max(0, -val[child]))
        vector<ll> si_gain(n+1, 0), si_need(n+1, 0);
        vector<vector<pair<ll,int>>> sorted_ch(n+1);

        for (int i = (int)bfs_order.size()-1; i >= 0; i--) {
            int v = bfs_order[i];
            if (path_set.count(v)) continue;

            // Collect profitable children, sorted by si_need for DP
            vector<pair<ll,int>> ch_dp;
            for (int u : adj[v]) {
                if (u == par[v] || path_set.count(u)) continue;
                if (si_gain[u] > 0) ch_dp.push_back({si_need[u], u});
            }
            sort(ch_dp.begin(), ch_dp.end());

            // Compute si_need, si_gain using si_need-sorted order
            ll need = max(0LL, -val[v]);
            ll running = need + val[v];
            for (auto& [cn, c] : ch_dp) {
                if (running < cn) { need += cn - running; running = cn; }
                running += si_gain[c];
            }
            si_need[v] = need;
            si_gain[v] = val[v];
            for (auto& [cn, c] : ch_dp) si_gain[v] += si_gain[c];

            // Build runtime sorted_ch by entry cost (for partial_gain)
            vector<pair<ll,int>> ch_ec;
            for (auto& [cn, c] : ch_dp)
                ch_ec.push_back({max(0LL, -val[c]), c});
            sort(ch_ec.begin(), ch_ec.end());
            sorted_ch[v] = ch_ec;
        }

        // partial_gain(v, H): best gain achievable entering v with HP=H
        // Uses entry cost to determine which children can be visited
        function<ll(int, ll)> partial_gain = [&](int v, ll H) -> ll {
            ll running = H + val[v];
            ll gain = val[v];
            for (auto& [ec, c] : sorted_ch[v]) {
                if (running < ec) break;  // sorted by entry cost; all later also fail
                ll pg = partial_gain(c, running);
                if (pg > 0) { running += pg; gain += pg; }
            }
            return gain;
        };

        // PQ: (HP threshold to try visiting, node)
        // Nodes are pushed with entry cost initially.
        // If partial_gain is unprofitable now, pushed back with si_need threshold
        // (guaranteeing full gain when that threshold is met).
        using T2 = pair<ll, int>;
        priority_queue<T2, vector<T2>, greater<T2>> pq;
        set<int> in_pq;

        auto try_push = [&](int node, ll threshold) {
            if (si_gain[node] <= 0 || in_pq.count(node)) return;
            in_pq.insert(node);
            pq.push({threshold, node});
        };

        auto unlock_at = [&](int pi) {
            int v = path[pi];
            int prev_v = (pi > 0) ? path[pi-1] : -1;
            int next_v = (pi+1 < K) ? path[pi+1] : -1;
            for (int u : adj[v]) {
                if (u == prev_v || u == next_v || path_set.count(u)) continue;
                try_push(u, max(0LL, -val[u]));
            }
        };

        ll hp = 0;
        bool ok = true;

        auto use_pq = [&]() {
            while (!pq.empty()) {
                auto [need, node] = pq.top();
                if (need > hp) break;
                pq.pop();
                in_pq.erase(node);

                ll pg = partial_gain(node, hp);
                if (pg < 0 || (pg == 0 && val[node] < 0)) {
                    // Not profitable at current HP; re-queue at si_need threshold
                    if (hp < si_need[node]) {
                        in_pq.insert(node);
                        pq.push({si_need[node], node});
                    }
                    continue;
                }
                hp += val[node];
                for (auto& [ec, c] : sorted_ch[node])
                    try_push(c, max(0LL, -val[c]));
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