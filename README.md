# OI_stats
Przełącz widoczność menu
Wiekuisty ONTAK 2022
polski 
 
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
#pragma GCC optimize("Ofast,inline")
// Olaf Surgut 04.07.2022 17:47:05
#include <bits/stdc++.h>

using namespace std;

const int N = 500000;

typedef long long LL;

const LL inf = 1e18L;

struct Point {
	int x, y;
};

struct Node {
	int x1, y1;
	int x2, y2;

	Node *l, *r;

	int diff(int L, int v, int R) const {
		if (v < L)	return v - L;
		if (v > R)	return R - v;
		return 0;
	}

	LL dist(const Point &p) const {
		LL dx = diff(x1, p.x, x2);
		LL dy = diff(y1, p.y, y2);

		return dx * dx + dy * dy;
	}
};

Node nodes[2 * N];
int nodes_cnt;

typedef vector<Point>::iterator Iter;

bool compare_x(const Point &a, const Point &b) {
	return a.x < b.x;
}

bool compare_y(const Point &a, const Point &b) {
	return a.y < b.y;
}

Node* build(Iter L, Iter R) {
	if (distance(L, R) == 1)
		return &(nodes[nodes_cnt++] = Node{L->x, L->y, L->x, L->y, 0, 0});
	
	Node *u = &nodes[nodes_cnt++];

	u->x1 = min_element(L, R, compare_x)->x;
	u->x2 = max_element(L, R, compare_x)->x;
	u->y1 = min_element(L, R, compare_y)->y;
	u->y2 = max_element(L, R, compare_y)->y;

	Iter M = L + (R - L) / 2;

	nth_element(L, M, R, u->x2 - u->x1 > u->y2 - u->y1 ? compare_x : compare_y);

	u->l = build(L, M);
	u->r = build(M, R);

	return u;
}

pair<LL, Point> nearest(Node *node, const Point &p) {
	if (node->l == 0) {
		LL d = node->dist(p);

		if (d == 0)
			return {inf, p};
		return {d, Point{node->x1, node->y1}};
	}

	pair<LL, Node*> A = {node->l->dist(p), node->l};
	pair<LL, Node*> B = {node->r->dist(p), node->r};

	if (A.first > B.first)
		swap(A, B);

	pair<LL, Point> best = nearest(A.second, p);

	if (best.first > B.first) {
		pair<LL, Point> cur = nearest(B.second, p);
		
		if (best.first > cur.first)
			best = cur;
	}

	return best;
}

char get_char() {
	static char buf[1 << 21];
	static size_t pos, len;
	if (pos >= len) {
		pos = 0;
		len = fread(buf, 1, sizeof(buf), stdin);
	}
	return buf[pos++];
}

int read_int() {
	int a, c;
	while ((a = get_char()) < '-');
	if (a == '-')
		return -read_int();
	while ((c = get_char()) >= '0')
		a = a * 10 + c - '0' * 10;
	return a - '0';
}

int main() {
	int n = read_int(), m = read_int();

	vector<Point> stars(n), holes(m);

	for (auto &[x, y] : stars)	x = read_int(), y = read_int();
	for (auto &[x, y] : holes)	x = read_int(), y = read_int();

	Node *stars_root = build(stars.begin(), stars.end());

	LL cur = inf;
	
	for (auto p : stars) {
		cur = min(cur, nearest(stars_root, p).first);	
	}

	double ans = sqrt(cur);

	if (m > 0) {
		nodes_cnt = 0;

		Node *holes_root = build(holes.begin(), holes.end());

		vector<LL> distances;
		for (auto p : stars) {
			distances.push_back(nearest(holes_root, p).first);
		}

		nth_element(distances.begin(), distances.begin() + 2, distances.end());

		ans = min(ans, sqrt(distances[0]) + sqrt(distances[1]));
	}

	printf("%.7lf\n", ans * 0.5);
}
Działa na bazie OIOIOI, części SIO2 Project.
