// 11866:요세푸스 문제0
// 사람들이 제거되어야 끝나기 때문에 While

function solution(n, k) {
  let answer = [];
  let arr = Array.from({ length: n }, (_, i) => i + 1);
  let index = 0;

  while (arr.length > 0) {
    index = (index + k - 1) % arr.length;
    answer.push(arr[index]);
    arr.splice(index, 1);
  }
  return "<" + answer.join(", ") + ">";
}

console.log(solution(7, 3));
// <3, 6, 2, 7, 5, 1, 4>
