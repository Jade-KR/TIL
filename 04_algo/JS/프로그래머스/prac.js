// const fs = require("fs");
// let input = fs.readFileSync("./prac.txt").toString().trim().split("\n");
let input = [
	"4",
	"10 15 20 25",
	"2",
	"3 10",
	"2 20",
	"0",
	"1",
	"4 10",
	"1",
	"1 10",
];
input.toString().trim().split("\n");
const typeCnt = parseInt(input.shift());
let costs = input
	.shift()
	.split(" ")
	.map((val) => parseInt(val));

const discountInfo = {};
let a = 1;
input.forEach((val, idx) => {
	if (val.split(" ").length === 1) {
		val = parseInt(val);
		for (let i = idx + 1; i <= idx + val; i++) {
			if (discountInfo[a]) {
				discountInfo[a] = [
					discountInfo[a],
					input[i].split(" ").map((val) => parseInt(val)),
				];
			} else {
				discountInfo[a] = input[i].split(" ").map((val) => parseInt(val));
			}
		}
		a++;
	}
});

const drinks = [];
for (let i = 1; i <= typeCnt; i++) {
	drinks.push(i);
}
let copyCosts = [...costs];
let min = Infinity;
let totalCost = 0;
``;

const orderLists = getPermutations(drinks, typeCnt);

orderLists.forEach((order) => {
	order.forEach((drink) => {
		buyItem(drink);
		applyDiscount(drink);
	});
	if (totalCost < min) {
		min = totalCost;
	}
	totalCost = 0;
	copyCosts = [...costs];
});

console.log(min);

function getPermutations(arr, selectNumber) {
	const results = [];
	if (selectNumber === 1) return arr.map((el) => [el]);
	arr.forEach((fixed, index, origin) => {
		const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
		const permutations = getPermutations(rest, selectNumber - 1);
		const attached = permutations.map((el) => [fixed, ...el]);
		results.push(...attached);
	});
	return results;
}

function buyItem(num) {
	totalCost += copyCosts[num - 1];
}

function applyDiscount(num) {
	if (discountInfo[num]) {
		if (Array.isArray(discountInfo[num][0])) {
			discountInfo[num].forEach((info) => {
				copyCosts[info[0] - 1] -= info[1];
				if (copyCosts[info[0] - 1] <= 0) {
					copyCosts[info[0] - 1] = 1;
				}
			});
		} else {
			copyCosts[discountInfo[num][0]] -= discountInfo[num][1];
			if (copyCosts[discountInfo[num][0] - 1] <= 0) {
				copyCosts[discountInfo[num][0] - 1] = 1;
			}
		}
	}
}
