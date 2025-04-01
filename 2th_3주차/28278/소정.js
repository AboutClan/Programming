// 28278: 스택 2

function solution(N, arr) {
  let answer = [];
  let stack = [];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i].length === 2 && arr[i][0] === 1) {
      stack.push(arr[i][1]);
    } else if (arr[i] === 2) {
      if (stack.length) {
        let out = stack.pop();
        answer.push(out);
      } else {
        answer.push(-1);
      }
    } else if (arr[i] === 3) {
      answer.push(stack.length);
    } else if (arr[i] === 4) {
      stack.length ? answer.push(0) : answer.push(1);
    } else if (arr[i] === 5) {
      if (stack.length) {
        answer.push(stack[stack.length - 1]);
      } else {
        answer.push(-1);
      }
    }
  }
  return answer.join("\n");
}

console.log(solution(9, [4, [1, 3], [1, 5], 3, 2, 5, 2, 2, 5]));
// 1
// 2
// 5
// 3
// 3
// -1
// -1
