function lcm(a, b) {
	return (a * b) / getGcd(a, b);
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

function getGcd(a, b) {
	if (b === 0) return a;
	return getGcd(b, a % b);
}

console.log(getGcd(4, 6));
console.log(lcm(4, 5));
