function test(num) {
	const check = new Array(num + 1).fill(true).splice(0, 2, false, false);
	const maxN = Math.sqrt(num);

	// 주어진 수의 제곱근까지만 계산해서 불필요한 반복을 최소화한다.
	// arr[i] 가 소수일 경우, 반복문을 진행한다.
	// 맨 처음 시작하는 2는 소수이므로,
	// 2를 제외한 2의 제곱부터, 제곱 값만 체크하여 지워나간다.
	// 제곱근까지 반복한다.
	for (let i = 2; i <= maxN; i++) {
		if (check[i] === false) continue;
		for (let j = i * i; j <= num; j += i) {
			check[j] = false;
		}
	}
	return check.filter((val) => val === true).length;
}
