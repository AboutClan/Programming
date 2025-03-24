// 10815 : 숫자 카드

function solution(n, arr1, m, arr2) {
  // 시간초과 발생 코드 O(n*m)
  //   let answer = Array(m).fill(0);
  //   for (let i = 0; i < n; i++) {
  //     for (let j = 0; j < m; j++) {
  //       if (arr1[i] === arr2[j]) {
  //         answer[j] = 1;
  //         break;
  //       }
  //     }
  //   }

  // Set을 사용하여 O(n+m)
  let answer = Array(m).fill(0);
  let arr1set = new Set(arr1);
  console.log(answer);
  for (let i = 0; i < m; i++) {
    if (arr1set.has(arr2[i])) {
      answer[i] = 1;
    }
  }

  return answer;
}
