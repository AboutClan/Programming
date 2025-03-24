// 7785: 회사에 있는 사람

function solution(n, arr) {
  let inCompany = new Set();
  for (let i = 0; i < n; i++) {
    if (arr[i][1] === "enter") {
      inCompany.add(arr[i][0]);
    } else {
      inCompany.delete(arr[i][0]);
    }
  }
  //   let reverseName = [...inCompany].sort((a, b) => b.localeCompare(a));
  // // 현재 시스템의 로케일을 고려해서 비교하기 때문에 정렬 결과가 환경마다 다를 수 있다.
  let reverseName = [...inCompany].sort((a, b) => (a > b ? -1 : 1));
  // 아스키코드를 기반으로 하기 때문에 일관된 결과를 나타낸다.

  return reverseName.join("\n");
}
