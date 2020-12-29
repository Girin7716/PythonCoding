# 파이썬 책 문제에 대한 풀이법

## Q1
<details>
<summary></summary>
</details>

---

## Q17
<details>
<summary>경쟁적 전염</summary>

- 링크 : https://www.acmicpc.net/problem/18405
- 풀이 방법
  - 우선순위 큐(min heap)를 사용하여 (시간,바이러스 번호, x좌표, y좌표)를 원소로 하여 큐에 삽입한다. 
  - 이때, 시간, 바이러스 순으로 우선순위를 가지며 바이러스가 퍼진다.
  - 4방향을 검사하면서 board가 0인 지점의 (시간+1, 바이러스 번호, 좌표1,좌표2)를 우선순위 큐에 넣는다. 
  - 반복하다가 우선순위큐에서 꺼낸 원소의 시간이 S+1이면 그만하고 board[X-1][Y-1] 값을 출력한다.
</details>

---

## Q18
<details>
<summary>괄호 변환</summary>

- 링크 : https://programmers.co.kr/learn/courses/30/lessons/60058
- 풀이 방법(주어진 알고리즘대로 구현함)
  1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
  2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
  3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
  4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
    4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
    4-3. ')'를 다시 붙입니다. 
    4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
    4-5. 생성된 문자열을 반환합니다.
- 주의 할 점은 def solution(p)에서 p는 문자열이므로 p의 값으로 줄때 이 값이 리스트인지 생각해봐야한다. 만약 리스트라면 ''.join(p)를 해서 문자열로 변화시킨 후 값을 넘긴다.

</details>

---

## Q19

<details>
<summary>연산자 끼워 넣기</summary>

- 링크 : https://www.acmicpc.net/problem/14888
- 풀이 방법
  - 연산자(+,-,*,/)에 대한 정보를 가지는 op 리스트를 만든다
  - op 리스트에 대한 순열(permutations)을 구한 뒤 중복 값을 막기 위해 set() 처리를 한다.
  - set에 대하여 순서대로 연산한다.

</details>

---

## Q20

<details>
<summary>감시 피하기</summary>

- 링크 : https://www.acmicpc.net/problem/18428
- 풀이 방법
  - 시간 제한이 2초이며, 복도의 크기는 N * N이며, N은 최대 6이다.
  - 따라서, 장애물 3개 설치하는데 모든 경우의 수(조합)는 36C3 = 7140이다.
  - 즉, 완전탐색(DFS,BFS)를 해도 시간초과 걱정이 없다.
  - 벽을 설치할 수 있는 좌표를 가지는 리스트 wall을 만든 후 per = list(permutations(wall,3))를 통해 3개씩 뽑은 후, board에 설치 -> 검사(teacher 위치를 기반으로 검사) -> 벽 지우기를 반복하며, 만약 학생들을 못 발견한다면 YES 출력 후 종료
  - 만약 for 문 밖으로 나올 경우 계속 학생을 발견했다는 말로 NO 출력 후 종료

</details>

---

## Q23

<details>
<summary>국영수</summary>

- 링크 : https://www.acmicpc.net/problem/10825
- 풀이 방법
  - 조건에 맞춰 정렬함.
  - 단, 계수 정렬(radix sort)등과 같은 특별한 상황에서의 정렬 알고리즘이 아닐경우 python에서 제공하는 정렬 라이브러리는 최악의 경우 O(NlogN)을 보장하므로 이를 사용하여 정렬했다.

</details>

---

## Q24

<details>
<summary>안테나</summary>

- 링크 : https://www.acmicpc.net/problem/18310
- 풀이 방법
  - 안테나 설치는 입력 받은 리스트의 가운데 값(Median,중간값)에 설치하면 최소로 할 수 있다.
  - 또한 시간 제한은 1초이며 input은 최대 200,000이므로 N<sup>2</sup>의 경우 40,000,000,000이므로 파이썬의 1초인 20,000,000번을 넘어서 사용하면 안된다.
  - NlogN의 경우 대략 1,000,000이므로 1초내이다.
  - 그리하여 sort()를 사용시 괜찮으며, 그 후 중간 값을 구했다.

</details>

---

## Q25

<details>
<summary>실패율</summary>

- 링크 : https://programmers.co.kr/learn/courses/30/lessons/42889
- 풀이 방법
  - stages의 수만큼 반복하며 각각의 스테이지에 해당하는 stages[] 리스트에서의 개수를 구한다(이때, bisect를 사용해서 구함.)
  - 그리하여 실패율과 해당 stage를 저장하는 rem에 저장하고 분모(denominator)에서 해당 개수를 뺀 후 반복하면서 실패율을 구한다.
  - 그후 실패율, stage 순으로 정렬한 뒤 answer에는 stage만 담아 return한다.