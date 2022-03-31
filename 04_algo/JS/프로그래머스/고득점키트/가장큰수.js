function solution(numbers) {
	const result = numbers
		.map((num) => String(num))
		.sort((a, b) => b + a - (a + b))
		.join("");

	return result[0] === "0" ? "0" : result;
}

solution([3, 30, 34, 5, 9], "9534330");
