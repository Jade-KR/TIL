class Node {
	constructor(data) {
		this.data = data; // 다른 노드와 차별점을 두는 데이터
		this.children = []; // 자식들과의 정보(주소)를 담을 배열
	}

	add(data) {
		// 자식 추가하는 메소드
		this.children.push(new Node(data)); // 자식 노드를 생성하고 바로 배열에 저장한다. (주소를 저장하는 행위)
	}

	remove(data) {
		// 자식의 정보를 지우는 메소드
		this.children = this.children.filter((child) =>
			child.data === data ? false : true
		); // filter 를 거쳐서 해당하는 자식의 정보를 배열에서 빼주면 된다.
	}
}

class Tree {
	constructor() {
		this.root = null;
	}
}

const t = new Tree(); // 빈 트리를 생성 해 주고
t.root = new Node("a"); // 루트가 node 'a'의 주소를 가리키면 'a' 의 자식들까지 접근 가능하다.
t.root.add("b"); // a의 자식 'b', 'c'
t.root.add("c");
t.root.children[0].add("d"); // 'b' 의 자식으로 'd'가 추가된다.
