# Othello

## 프로토콜 설계
이 프로토콜 설계 문서는 네트워크 상에서 플레이하는 Othello 게임에 대한 프로토콜로 텍스트 기반으로 작성하였다. 

텍스트 기반으로 작성한 이유는 바이너리 기반으로 작성할 경우 패킷의 크기가 작아져서 통신 속도가 빨라지는 장점이 있지만 이 프로토콜을 사용하는 Othello는 소규모(1:1)로 네트워크 통신을 하기 때문에 속도 차이가 크지 않을 것이라 생각하였으며 여러 사람이 각자 Othello 프로그램을 제작하기 때문에 프로토콜 구조를 쉽게 알아볼 수 있는 텍스트 기반으로 작성하기로 결정하였다.

이 프로토콜 설계 문서에서 프토토콜 구조는 [COMMEND] DATA 형식이며 Request, Reply, Notify 세가지 종류의 통신 방식이 있다. Request는 상대의 응답이 필요할 때 사용하고 Reply는 Request에 대해 응답하기 위해 사용한다. 그리고 Notify는 항상 응답을 필요로 하지는 않고 상대에게 무언가를 알리기 위해 사용한다.

### 목차

- [1. Server](#1-server)
- [2. Client](#2-client)
- [3. Request-Reply 상관관계](#3-Request-Reply-상관관계)
- [4. 통신흐름](#4-통신흐름)

#### 1. Server

| 종류    | 명령         | 의미 |
  ------- | -------     | -------
| Request | [TURN]1 1   | 상대 플레이어가 1행 1열에 돌을 둔 것을 알리고 플레이어에게 돌을 놓으라고 요청한다. 게임을 시작할 때 가장 먼저 돌을 놓는 플레이어에게는 DATA를 포함하지 않고 [TURN]만 보낸다. |
| Request | [AGAIN]     | 상대 플레이어가 돌을 놓을 수 없어 플레이어에게 한번 더 돌을 놓으라고 요청한다. |
| Request | [MISS]      | 플레이어가 돌을 놓을 수 없는 곳에 놓아 다시 돌을 놓으라고 요청한다. |
| Reply   | [COME]black | 플레이어가 사용할 돌의 색(black, white)과 함께 접속된 것을 알린다. |
| Reply   | [FULL]      | 플레이어에게 자리가 없는 것을 알리고 연결을 끊는다. |
| Notify  | [ENTER]name | ID가 name인 상대 플레이어가 접속한 것을 알린다. |
| Notify  | [START]60   | 플레이어 모두가 준비가 되면 턴당 제한시간(60초)과 함께 게임이 시작된 것을 알린다. |
| Notify  | [ACCEPT]    | 플레이어가 올바른 위치에 돌을 놓았다고 알린다. |
| Notify  | [PASS]1 1   | 상대 플레이어가 1행 1열에 돌을 두어 자신이 놓을 곳이 없음을 알린다. 또한 상대 플레이어가 마지막 돌을 둘 때 플레이어에게 알리기 위해 사용한다. |
| Notify  | [TIMEOUT]   | 시간이 초과하여 플레이어가 패배함을 알린다. |
| Notify  | [EXIT]      | 상대 플레이어가 게임을 종료한 것을 알린다.(알수없는 오류로 인해 종료할 때도 포함) |
| Notify  | [WIN]       | 플레이어가 게임에서 승리함을 알린다. |
| Notify  | [LOSS]      | 플레이어가 게임에서 패배함을 알린다. |

#### 2. Client

| 종류    | 명령        | 의미 |
-------   |-------     |-------
| Request | [JOIN]name | 플레이어가 사용할 ID name과 함께 서버에 접속을 요청한다. |
| Reply   | [PUT]1 1   | 플레이어가 1행 1열에 돌을 놓는다고 서버에 알린다. |
| Notify  | [READY]    | 플레이어가 게임 준비가 되었다고 서버에 알린다. |
| Notify  | [UNREADY]  | 플레이어가 게임 준비가 되지않았다고 서버에 알린다. |

#### 3. Request-Reply 상관관계

Request-Reply 상관관계에서는 어떤 Request가 요청되면 Reply 응답을 하는지에 대해 설명한다. 

<img src="https://user-images.githubusercontent.com/39123255/51222709-4e343d00-1982-11e9-9ad6-ede33741e8de.png" width=500></p>

#### 4. 통신흐름

게임을 진행하면서 발생할 수 있는 통신흐름을 다음과 같이 그림으로 표현하였다.

##### 4-1. 게임 접속 성공
Client에서 [JOIN]name 명령으로 접속을 요청한 뒤 접속이 가능하면 Server에서 [COME]black 또는 [COME]white 명령으로 접속이 되었음과 플레이어가 사용할 돌의 색을 알린다. 그리고 [ENTER]name 명령으로 ID가 name인 상대 플레이어가 접속하였음을 알린다.

<img src="https://user-images.githubusercontent.com/39123255/51224044-9b66dd80-1987-11e9-8314-302e75bf9261.png" width=500></p>

##### 4-2. 자리가 없어 게임 접속 실패
Client에서 [JOIN]name 명령으로 접속을 요청하였으나 자리가 없을 경우 서버에서 [FULL] 명령으로 접속할 수 없음을 알린다.

<img src="https://user-images.githubusercontent.com/39123255/51219421-41105180-1974-11e9-8f25-1fce480d463a.png" width=500></p>

##### 4-3. 게임 준비
Client에소 [READY] 명령으로 게임할 준비가 되었음을 서버에 알리고 Server에서는 Client 모두가 준비되면 각 Client에게 [START]60 명령으로 턴당 제한시간(60초)과 게임이 시작되었음을 알린다. 그리고 만약 한 Client가 [UNREADY] 명령으로 게임을 할 준비가 되지 않았음을 서버에 알리면 해당 Client가 [READY] 명령을 서버에 알릴 때까지 게임을 시작하지 않는다.

<img src="https://user-images.githubusercontent.com/39123255/51224178-1a5c1600-1988-11e9-9d9c-5d3bd7d30fd7.png" width=500></p>

##### 4-4. 게임 시작
Server에서 각 Client에게 [START] 명령으로 게임이 시작됨을 알린 후 서버에서 [TURN] 명령을 받은 Clinet가 먼저 돌을 놓는다. Clinet는 [PUT]5 6 명령과 같이 몇 행, 몇 열에 돌을 놓을건지 Server에게 알리고 정상적으로 처리될 경우 Server에서는 [ACCEPT] 명령을 해당 Clinet에게 보낸다. 그리고 서버에서 상대 Client에게 [TURN]5 6 명령으로 상대 플레이어가 돌을 놓은 위치와 함께 플레이어가 돌을 놓을 차례임을 알린다.  

<img src="https://user-images.githubusercontent.com/39123255/51224350-c140b200-1988-11e9-8f22-d6eb79c3261a.png" width=500></p>

##### 4-5. 플레이어가 돌을 놓을 수 없는 곳에 돌을 놓았을 때
Client 프로그램의 문제로 플레이어가 놓을 수 없는 곳에 돌을 놓을 경우(Server에서는 문제가 없다고 가정) Server에서 [MISS] 명령으로 해당 플레이어에게 다른 곳에 놓으라고 요청한다.

<img src="https://user-images.githubusercontent.com/39123255/51224677-64de9200-198a-11e9-84f3-e3ca75d87401.png" width=500></p>

##### 4-6. PASS 발생
Client1이 [PUT]8 1 명령으로 8행 1열에 돌을 놓겠다는 것을 서버에 알린 후 서버에서 Client2가 돌을 놓을 수 있는 곳이 없다고 확인되면 Client1에게 [AGAIN] 명령으로 한 번더 돌을 놓으라고 요청하며 Client2에게는 [PASS]8 1 명령으로 Client1이 돌을 놓은 위치와 Client2가 돌을 놓을 곳이 없다는 것을 알린다. 

<img src="https://user-images.githubusercontent.com/39123255/51224745-b0913b80-198a-11e9-81e4-98512ba9d084.png" width=500></p>

##### 4-7. TIMEOUT 발생
서버에서 각 Client에게 [START]60 명령으로 알려준 턴당 제한시간을 어떤 Client가 초과할 경우 해당 Client는 Server로 부터 [TIMEOUT] 명령과 [LOSS] 명령을 받아 시간제한으로 게임에 패배함을 확인하고 상대 Client에게는 [WIN] 명령을 전달해 게임에 승리함을 알린다.

<img src="https://user-images.githubusercontent.com/39123255/51224945-afacd980-198b-11e9-823f-33f7c61bdfb6.png" width=500></p>

##### 4-8. 게임 종료
Client2가 마지막 돌을 놓으면 Server에서는 Client1에게 [PASS]4 6 명령으로 Client2가 놓은 돌의 위치를 알려준다. 그리고 Server에서 결과를 계산한 다음 Client2에게는 [LOSS] 명령으로 패배를 알리고 Client1에게는 [WIN] 명령으로 승리를 알린다.

<img src="https://user-images.githubusercontent.com/39123255/51220163-7bc7b900-1977-11e9-8155-e1551931c92f.png" width=500></p>
