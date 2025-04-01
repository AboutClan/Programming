// 18258: 큐2
// slice => 메모리 초과, shift => 시간 초과 => 직접적으로 배열을 수정하여 재구성 방식이 아니라 index 조정으로 바꿈

function solution(n, arr) {
  let answer = [];
  let queue = [];
  let frontIndex = 0;

  for (let i = 0; i < n; i++) {
    if (arr[i][0] === "push") {
      queue.push(arr[i][1]);
    } else if (arr[i][0] === "pop") {
      if (frontIndex < queue.length) {
        answer.push(queue[frontIndex]);
        frontIndex++;
      } else {
        answer.push(-1);
      }
    } else if (arr[i][0] === "size") {
      answer.push(queue.length - frontIndex);
    } else if (arr[i][0] === "empty") {
      queue.length - frontIndex ? answer.push(0) : answer.push(1);
    } else if (arr[i][0] === "front") {
      queue.length - frontIndex
        ? answer.push(queue[frontIndex])
        : answer.push(-1);
    } else if (arr[i][0] === "back") {
      queue.length - frontIndex
        ? answer.push(queue[queue.length - 1])
        : answer.push(-1);
    }
  }
  return answer.join("\n");
}

console.log(
  solution(15, [
    ["push", 1],
    ["push", 2],
    ["front"],
    ["back"],
    ["size"],
    ["empty"],
    ["pop"],
    ["pop"],
    ["pop"],
    ["size"],
    ["empty"],
    ["pop"],
    ["push", 3],
    ["empty"],
    ["front"],
  ])
);
