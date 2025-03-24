// 2751: 수 정렬하기2

function solution(n, arr) {
  let sorted = arr.sort((a, b) => a - b);
  let answer = [...sorted].join("\n");

  return answer;
}

console.log(solution(5, [5, 4, 3, 2, 1]));
