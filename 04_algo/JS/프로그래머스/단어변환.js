function solution(begin, target, words) {
	// 최종 단어로 바꿀 수 없을 경우
	if (words.indexOf(target) === -1) {
		return 0;
	}

	let result = Infinity;

	const visited = [begin];
	const queue = [[begin, 0]];

	while (queue.length > 0) {
		const [word, step] = queue.shift();

		words.forEach((val) => {
			if (word === target) {
				if (result > step) {
					result = step;
					return;
				}
			}

			if (visited.includes(val)) {
				return;
			}

			let check = 0;
			for (let i = 0; i < word.length; i++) {
				if (word[i] !== val[i]) {
					check++;
				}
			}
			// 변환 가능한 경우
			if (check === 1) {
				visited.push(val);
				queue.push([val, step + 1]);
			}
		});
	}
	return result;
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));
