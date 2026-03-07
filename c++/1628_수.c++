#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
const ll INF = 1e16;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<ll> s(n + 1), t(m + 1);
    for (int i = 1; i <= n; i++) cin >> s[i];
    for (int i = 1; i <= m; i++) cin >> t[i];

    vector<ll> dp(m + 1, INF);
    dp[0] = 0;

    for (int i = 1; i <= n; i++) {
        vector<ll> next_dp(m + 1, INF);

        int pos = lower_bound(t.begin() + 1, t.end(), s[i]) - t.begin();
        int K = 400;
        int start = max(1, min(i - K, pos - K));
        int end = min(m, max(i + (m - n) + K, pos + K));

        for (int j = start; j <= end; j++) {
            ll diff = abs(s[i] - t[j]);
            
            ll res = dp[j];
            if (dp[j-1] < res) res = dp[j-1];
            if (next_dp[j-1] < res) res = next_dp[j-1];

            if (res != INF) next_dp[j] = diff + res;
        }
        dp = move(next_dp);
    }

    cout << dp[m] << endl;

    return 0;
}