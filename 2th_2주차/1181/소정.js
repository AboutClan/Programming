// 1181 : 단어 정렬

function solution(n, words) {
  words = [...new Set(words)];
  words = words.sort((a, b) => a.length - b.length || a.localeCompare(b));
  return words;
}
// 테스트
console.log(
  solution(13, [
    "but",
    "i",
    "wont",
    "hesitate",
    "no",
    "more",
    "no",
    "more",
    "it",
    "cannot",
    "wait",
    "im",
    "yours",
  ])
);
