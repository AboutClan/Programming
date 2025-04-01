//// 9012:괄호

function solution(N, arr) {
  let answer = [];
  for (let i = 0; i < N; i++) {
    let stack = [];
    let temp = [];
    for (let j = 0; j < arr[i].length; j++) {
      if (arr[i][j] === "(") {
        stack.push("(");
      } else if (arr[i][j] === ")") {
        if (stack[stack.length - 1] === "(") {
          stack.pop();
        } else {
          temp.push(")");
        }
      }
    }
    !stack.length && !temp.length ? answer.push("YES") : answer.push("NO");
  }

  return answer.join("\n");
}

console.log(
  solution(6, [
    "(())())",
    "(((()())()",
    "(()())((()))",
    "((()()(()))(((())))()",
    "()()()()(()()())()",
    "(()((())()(",
  ])
);
// NO
// NO
// YES
// NO
// YES
// NO
