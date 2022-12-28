import {
	S as H,
	i as I,
	s as N,
	k as m,
	q as S,
	a as y,
	l as b,
	m as f,
	r as $,
	c as q,
	h as u,
	n as T,
	b as k,
	C as n,
	u as x,
	B as A,
	H as B
} from '../../chunks/index-3e2ded46.js';
import { s as L } from '../../chunks/singletons-f5352351.js';
const O = () => {
		const e = L;
		return {
			page: { subscribe: e.page.subscribe },
			navigating: { subscribe: e.navigating.subscribe },
			updated: e.updated
		};
	},
	P = {
		subscribe(e) {
			return O().page.subscribe(e);
		}
	};
function R(e) {
	let s,
		a,
		t,
		o = e[0].status + '',
		p,
		g,
		i = e[0].error.message + '',
		_,
		v,
		l,
		E;
	return {
		c() {
			(s = m('section')),
				(a = m('article')),
				(t = m('h3')),
				(p = S(o)),
				(g = y()),
				(_ = S(i)),
				(v = y()),
				(l = m('span')),
				(E = S('🕳')),
				this.h();
		},
		l(r) {
			s = b(r, 'SECTION', { class: !0 });
			var c = f(s);
			a = b(c, 'ARTICLE', {});
			var h = f(a);
			t = b(h, 'H3', {});
			var d = f(t);
			(p = $(d, o)), (g = q(d)), (_ = $(d, i)), d.forEach(u), (v = q(h)), (l = b(h, 'SPAN', {}));
			var C = f(l);
			(E = $(C, '🕳')), C.forEach(u), h.forEach(u), c.forEach(u), this.h();
		},
		h() {
			T(s, 'class', 'svelte-1f4ua4d');
		},
		m(r, c) {
			k(r, s, c), n(s, a), n(a, t), n(t, p), n(t, g), n(t, _), n(a, v), n(a, l), n(l, E);
		},
		p(r, [c]) {
			c & 1 && o !== (o = r[0].status + '') && x(p, o), c & 1 && i !== (i = r[0].error.message + '') && x(_, i);
		},
		i: A,
		o: A,
		d(r) {
			r && u(s);
		}
	};
}
function j(e, s, a) {
	let t;
	return B(e, P, (o) => a(0, (t = o))), [t];
}
let D = class extends H {
	constructor(s) {
		super(), I(this, s, j, R, N, {});
	}
};
export { D as default };
