function solution(n, times) {
	// 최대 심사 시간을 구한다
	const max = Math.max(...times);

	times.sort((a, b) => a - b);
	let left = 0;
	let right = max * n;
	let mid = parseInt((left + right) / 2);
	let result = Infinity;

	while (left <= right) {
		let count = times.reduce((acc, el) => acc + parseInt(mid / el), 0);

		if (count === n) {
			result = Math.min(result, mid);
		}

		if (count > n) {
			right = mid - 1;
		} else {
			left = mid + 1;
		}

		mid = parseInt((left + right) / 2);
	}
	return result;
}

solution(6, [7, 10]);
