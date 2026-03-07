#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

const int INF = 2e9 + 7;

// 삭제 가능한 힙 (최적화)
struct MaxHeap {
    priority_queue<int> a, b;
    void ins(int x) { if (x != -INF) a.push(x); }
    void del(int x) { if (x != -INF) b.push(x); }
    void normalize() { while (!b.empty() && !a.empty() && a.top() == b.top()) { a.pop(); b.pop(); } }
    int top() { normalize(); return a.empty() ? -INF : a.top(); }
};

struct MinHeap {
    priority_queue<int, vector<int>, greater<int>> a, b;
    void ins(int x) { if (x != INF) a.push(x); }
    void del(int x) { if (x != INF) b.push(x); }
    void normalize() { while (!b.empty() && !a.empty() && a.top() == b.top()) { a.pop(); b.pop(); } }
    int top() { normalize(); return a.empty() ? INF : a.top(); }
};

struct Node {
    Node *ch[2], *p;
    long long val, sum_p, sum_v;
    int min_p, max_p, min_v, max_v;
    int sz_p, sz_v;
    bool rev;

    // lp: 경로용 Lazy, lv: 가상 자식용 Lazy
    int lp_set, lv_set;
    long long lp_add, lv_add;

    MinHeap v_min; MaxHeap v_max;

    Node(int v) {
        ch[0] = ch[1] = p = nullptr;
        val = sum_p = v; min_p = max_p = v;
        sz_p = 1; sum_v = 0; sz_v = 0;
        min_v = INF; max_v = -INF;
        lp_set = lv_set = INF; lp_add = lv_add = 0;
        rev = false;
    }

    bool is_root() { return !p || (p->ch[0] != this && p->ch[1] != this); }

    // 경로 업데이트 (Preferred Edge)
    void apply_p(int s, long long a) {
        if (s != INF) {
            val = s; sum_p = (long long)s * sz_p;
            min_p = max_p = s; lp_set = s; lp_add = 0;
        }
        if (a != 0) {
            val += a; sum_p += a * sz_p;
            min_p += (int)a; max_p += (int)a; lp_add += a;
        }
    }

    // 가상 자식(서브트리) 업데이트 핵심
    void apply_v(int s, long long a) {
        if (s != INF) {
            min_v = max_v = s; sum_v = (long long)s * sz_v;
            lv_set = s; lv_add = 0;
        }
        if (a != 0) {
            if (min_v != INF) min_v += (int)a;
            if (max_v != -INF) max_v += (int)a;
            sum_v += a * sz_v; lv_add += a;
        }
    }

    void push_up() {
        sz_p = 1 + (ch[0] ? ch[0]->sz_p : 0) + (ch[1] ? ch[1]->sz_p : 0);
        sum_p = val + (ch[0] ? ch[0]->sum_p : 0) + (ch[1] ? ch[1]->sum_p : 0);
        min_p = max_p = (int)val;
        if (ch[0]) { min_p = min(min_p, ch[0]->min_p); max_p = max(max_p, ch[0]->max_p); }
        if (ch[1]) { min_p = min(min_p, ch[1]->min_p); max_p = max(max_p, ch[1]->max_p); }
        min_v = v_min.top();
        max_v = v_max.top();
    }

    void push_down() {
        if (rev) {
            if (ch[0]) { swap(ch[0]->ch[0], ch[0]->ch[1]); ch[0]->rev ^= 1; }
            if (ch[1]) { swap(ch[1]->ch[0], ch[1]->ch[1]); ch[1]->rev ^= 1; }
            rev = false;
        }
        if (lp_set != INF || lp_add != 0) {
            if (ch[0]) ch[0]->apply_p(lp_set, lp_add);
            if (ch[1]) ch[1]->apply_p(lp_set, lp_add);
            lp_set = INF; lp_add = 0;
        }
    }
};



void rotate(Node* x) {
    Node* y = x->p; Node* z = y->p;
    int k = (y->ch[1] == x);
    if (!y->is_root()) z->ch[z->ch[1] == y] = x;
    x->p = z; y->ch[k] = x->ch[k ^ 1];
    if (x->ch[k ^ 1]) x->ch[k ^ 1]->p = y;
    x->ch[k ^ 1] = y; y->p = x;
    y->push_up(); x->push_up();
}

void splay(Node* x) {
    static Node* stk[100005]; int top = 0; stk[++top] = x;
    for (Node* i = x; !i->is_root(); i = i->p) stk[++top] = i->p;
    while (top) stk[top--]->push_down();
    while (!x->is_root()) {
        Node* y = x->p; Node* z = y->p;
        if (!y->is_root()) (y->ch[1] == x) ^ (z->ch[1] == y) ? rotate(x) : rotate(y);
        rotate(x);
    }
}

void access(Node* x) {
    Node* last = nullptr;
    for (Node* y = x; y; y = y->p) {
        splay(y);
        if (y->ch[1]) {
            y->v_min.ins(min(y->ch[1]->min_p, y->ch[1]->min_v));
            y->v_max.ins(max(y->ch[1]->max_p, y->ch[1]->max_v));
            y->sum_v += (y->ch[1]->sum_p + y->ch[1]->sum_v);
            y->sz_v += y->ch[1]->sz_p + y->ch[1]->sz_v;
        }
        if (last) {
            y->v_min.del(min(last->min_p, last->min_v));
            y->v_max.del(max(last->max_p, last->max_v));
            y->sum_v -= (last->sum_p + last->sum_v);
            y->sz_v -= last->sz_p + last->sz_v;
        }
        y->ch[1] = last; y->push_up(); last = y;
    }
    splay(x);
}

void make_root(Node* x) { access(x); swap(x->ch[0], x->ch[1]); x->rev ^= 1; }
Node* find_root(Node* x) { access(x); while (x->ch[0]) { x->push_down(); x = x->ch[0]; } splay(x); return x; }

void link(Node* x, Node* y) {
    make_root(x); access(y); x->p = y;
    y->v_min.ins(min(x->min_p, x->min_v));
    y->v_max.ins(max(x->max_p, x->max_v));
    y->sum_v += (x->sum_p + x->sum_v);
    y->sz_v += x->sz_p + x->sz_v;
    y->push_up();
}

void cut(Node* x) {
    access(x);
    if (x->ch[0]) { x->ch[0]->p = nullptr; x->ch[0] = nullptr; x->push_up(); }
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);
    int N, M; cin >> N >> M;
    vector<pair<int, int>> edges(N - 1);
    for (int i = 0; i < N - 1; i++) cin >> edges[i].first >> edges[i].second;
    vector<Node*> nodes(N + 1);
    for (int i = 1; i <= N; i++) { int v; cin >> v; nodes[i] = new Node(v); }
    for (auto& e : edges) link(nodes[e.first], nodes[e.second]);
    int r; cin >> r; Node* cur_root = nodes[r]; make_root(cur_root);

    while (M--) {
        int op, x, y, z; cin >> op;
        if (op == 0) { cin >> x >> y; access(nodes[x]); nodes[x]->val = y; nodes[x]->push_up(); }
        else if (op == 1) { cin >> x; cur_root = nodes[x]; make_root(cur_root); }
        else if (op == 2) { cin >> x >> y >> z; make_root(nodes[x]); access(nodes[y]); nodes[y]->apply_p(z, 0); make_root(cur_root); }
        else if (op == 3) { cin >> x; access(nodes[x]); cout << min((int)nodes[x]->val, nodes[x]->min_v) << "\n"; }
        else if (op == 4) { cin >> x; access(nodes[x]); cout << max((int)nodes[x]->val, nodes[x]->max_v) << "\n"; }
        else if (op == 5) { cin >> x >> y; access(nodes[x]); nodes[x]->val += y; nodes[x]->push_up(); }
        else if (op == 6) { cin >> x >> y >> z; make_root(nodes[x]); access(nodes[y]); nodes[y]->apply_p(INF, z); make_root(cur_root); }
        else if (op == 7) { cin >> x >> y; make_root(nodes[x]); access(nodes[y]); cout << nodes[y]->min_p << "\n"; make_root(cur_root); }
        else if (op == 8) { cin >> x >> y; make_root(nodes[x]); access(nodes[y]); cout << nodes[y]->max_p << "\n"; make_root(cur_root); }
        else if (op == 9) {
            cin >> x >> y; make_root(cur_root); if (find_root(nodes[y]) == nodes[x]) continue;
            access(nodes[x]); splay(nodes[x]);
            if (nodes[x]->ch[0]) { nodes[x]->ch[0]->p = nullptr; nodes[x]->ch[0] = nullptr; nodes[x]->push_up(); }
            link(nodes[x], nodes[y]); make_root(cur_root);
        }
        else if (op == 10) { cin >> x >> y; make_root(nodes[x]); access(nodes[y]); cout << nodes[y]->sum_p << "\n"; make_root(cur_root); }
        else if (op == 11) { cin >> x; access(nodes[x]); cout << nodes[x]->val + nodes[x]->sum_v << "\n"; }
    }
    return 0;
}