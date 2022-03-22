function lcm(a, b) {
	return (a * b) / gcd(a, b);
}

function gcd(a, b) {
	let r;
	while (b != 0) {
		r = a % b;
		a = b;
		b = r;
	}
	return a;
}
