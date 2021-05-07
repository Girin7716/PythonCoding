# 문제풀이

## 무지의 먹방 라이브

<details>
    <summary>링크</summary>
    https://programmers.co.kr/learn/courses/30/lessons/42891
</details>

<details>
<summary>문제풀이</summary>

완전탐색을 할 경우 food_times 가 최대 `100,000,000`이므로 시간초과가 발생할 거라 생각했다.

그러므로, 이에 대한 방법을 생각해야했고 `우선순위 큐`를 사용하고자 했다.

주어진 input인 `food_times`를 우선순위 큐(minHeap)인 `pq`에 (food_time,index)로 넣어준다. 

그 다음, 가장 시간 소비가 적은 값인 `pq[0][0]`를 확인하면서 해당 음식이 `k` 시간안에 먹을 수 있는지 파악한다. 만약 `k` 시간안에 먹을 수 없다면 이제는 남은 음식들과 남은 시간으로 무슨 음식을 먹어야하는지 확인해야하므로 break 한다
```python
now_food = pq[0][0]
if k < (now_food-prev_food) * len(pq):
    break
```

`k`시간안에 먹을 수 있다면, 해당 시간을 `k`에서 빼주고, 현재의 음식을 `prev_food`에 저장해준다.(왜냐하면, 다음 먹은 시간을 구할 때 (현재 음식 횟수-이전 음식 횟수)를 통해 현재 음식을 먹는데 걸리는 시간을 구할 수 있기 때문.) 그리고, minHeap에서 원소를 빼주면 된다.
```python
k -= (now_food - prev_food) * len(pq)

prev_food = pq[0][0]
value,idx = heapq.heappop(pq)
```

위 과정을 마무리하면 이제는 남은 음식들과 남은 시간으로 어떤 음식을 먹어야하는지 결정해야한다. 이때, 만약 남은 음식이 없다면(`pq==[]`), 먹을 음식이 없기때문에 -1을 반환하고, 있다면 pq를 index순으로 정렬한 뒤 `k = k % len(pq)`를 통해(어차피 남은 음식들은 0가 될 수 없기때문에)  `pq[k][1]`를 반환하면 된다.

```python
# 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    pq = []
    for idx, food_time in enumerate(food_times):
        heapq.heappush(pq,(food_time,idx+1))

    prev_food = 0
    now_food = 0

    while pq:
        now_food = pq[0][0]
        if k < (now_food-prev_food) * len(pq):
            break
        k -= (now_food - prev_food) * len(pq)

        prev_food = pq[0][0]
        value,idx = heapq.heappop(pq)
    if pq == []:
        return -1
    pq.sort(key = lambda x:x[1])
    k = k % len(pq)

    return pq[k][1]

print(solution([1,1,1,1],4))
print(solution([3,1,2],5))
print(solution([8,6,4],15))
```




</details>





