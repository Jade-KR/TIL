function solution(operations) {
	const q = [];
	const result = [0, 0];
	operations.forEach((val) => {
		let tmp = val.split(" ");
		operate(tmp);
	});

	if (q.length > 0) {
		result[0] = Math.max(...q);
		result[1] = Math.min(...q);
	}

	return result;

	function operate(v) {
		if (v[0] == "I") {
			q.push(parseInt(v[1]));
		} else if (v[0] == "D") {
			if (v[1] == 1) {
				let max = Math.max(...q);
				let idx = q.indexOf(max);
				q.splice(idx, 1);
			} else {
				let min = Math.min(...q);
				let idx = q.indexOf(min);
				q.splice(idx, 1);
			}
		}
	}
}

solution(["I 16", "D 1"]);
// solution(["I 7", "I 5", "I -5", "D -1"]);
