function solution(bridge_length, weight, truck_weights) {
	let sec = 0;
	const currBridge = [];
	let currBridgeWeight = 0;

	// 1초마다
	while (true) {
		sec++;
		let truck = truck_weights[0];

		// 기존에 다리에 올라와있는 트럭이 있다면 올라와있던 시간을 늘려준다
		if (currBridge.length > 0) {
			currBridge.map((val) => val.time++);
		}

		// 기존 트럭이 다리를 건넜다면
		if (currBridge.length > 0 && currBridge[0].time > bridge_length) {
			let tmp = currBridge.shift();
			currBridgeWeight -= tmp.weight;
		}

		if (currBridge.length > 0) {
			currBridgeWeight = currBridge.reduce((acc, val) => acc + val.weight, 0);
		} else {
			currBridgeWeight = 0;
		}

		// 트럭 다리에 추가 가능하면 추가
		if (currBridgeWeight + truck <= weight) {
			truck_weights.shift();
			currBridge.push({ weight: truck, time: 1 });
		}

		// 다리에 트럭이 아무것도 없고 대기중인 트럭이 아무것도 없다면
		if (!currBridge.length && !truck_weights.length) {
			break;
		}
	}
	return sec;
}

// solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1])
solution(2, 10, [7, 4, 5, 6]);
