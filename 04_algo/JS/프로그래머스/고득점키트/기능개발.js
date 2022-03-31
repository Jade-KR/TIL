function solution(progresses, speeds) {
	// 완료까지 남은 일 수 구하기
	const remain = progresses.map((val, idx) =>
		Math.ceil((100 - val) / speeds[idx])
	);
	let completed = remain[0];
	const result = [];
	let deployCnt = 0;
	for (let i = 0; i < remain.length; i++) {
		// 배포 날짜 안에 기능 개발이 완료된 경우
		if (remain[i] <= completed) {
			deployCnt++;
		} else {
			// 배포 날짜 보다 기능 개발 기간이 더 남은 경우
			result.push(deployCnt);
			deployCnt = 1;
			completed = remain[i];
		}
	}
	result.push(deployCnt);
	return result;
}
solution([93, 30, 55], [1, 30, 5]);
