# Othello

## 프로토콜 설계
이 프로토콜 설계 문서는 네트워크 상에서 플레이하는 Othello 게임에 대한 프로토콜로 텍스트 기반으로 작성하였다. 

텍스트 기반으로 작성한 이유는 바이너리 기반으로 작성할 경우 패킷의 크기가 작아져서 통신 속도가 빨라지는 장점이 있지만 이 프로토콜을 사용하는 Othello는 소규모(1:1)로 네트워크 통신을 하기 때문에 속도 차이가 크지 않을 것이라 생각하였으며 여러 사람이 각자 Othello 프로그램을 제작하기 때문에 프로토콜 구조를 쉽게 알아볼 수 있는 텍스트 기반으로 작성하기로 결정하였다.

프토토콜 구조는 [COMMEND] DATA 형식이며 Request, Reply, Notify 세가지 종류의 통신 방식이 있다. Request는 상대에게 응답을 원할 때 사용하고 Reply는 Request에 대해 응답한 것이다. 그리고 Notify는 클라이언트에게 응답을 받지않고 단지 알리기만 한다.

### 목차

- [1. Server](#1-server)
- [2. Client](#2-client)
- [3. 상관관계](#3-상관관계)
- [4. 통신흐름](#4-통신흐름)

#### 1. Server

| 종류    | 명령         | 의미 |
  ------- | -------     | -------
| Request | [TURN]1 1   | 상대가 1행 1열에 돌을 두었으며 플레이어 자신의 차례인 것을 알린다. |
| Request | [AGAIN]     | 상대가 돌을 놓을 수 없어 플레이어가 한번 더 돌을 놓으라고 요청한다. |
| Request | [MISS]      | 플레이어가 돌을 놓을 수 없는 곳에 놓아 다시 놓으라고 요청한다. |
| Reply   | [COME]black | 사용해야 할 돌의 색(black, white)과 함께 접속된 것을 알린다. |
| Reply   | [FULL]      | 자리가 없는 것을 알리고 연결을 끊는다. |
| Reply   | [START]60   | 참가자 모두가 준비가 되면 턴당 제한시간(60초)과 함께 게임이 시작된 것을 알리며 검은색 돌을 가진 플레이어가 먼저 시작한다. |
| Reply   | [ACCEPT]    | 플레이어가 올바른 위치에 돌을 놓았다고 알린다. |
| Notify  | [ENTER]name | ID가 name인 상대가 접속되는 것을 알린다. |
| Notify  | [TIMEOUT]   | 시간이 초과하여 패배함을 알림 |
| Notify  | [PASS]1 1   | 상대가 1행 1열에 돌을 두어 자신이 놓을 곳이 없음을 알린다. 또한 상대가 마지막에 돌을 둘 때 플레이어에게 알리기  사용한다. |
| Notify  | [EXIT]      | 상대가 나감을 알린다.(알수없는 오류로 인해 나갈 때도 포함) |
| Notify  | [WIN]       | 게임에서 승리함을 알린다. |
| Notify  | [LOSS]      | 게임에서 패배함을 알린다. |

#### 2. Client

| 종류    | 명령        | 의미 |
-------   |-------     |-------
| Request | [JOIN]name | 사용할 ID name과 함께 서버에 접속을 요청한다. |
| Request | [READY]    | 게임 준비가 되었다고 서버에 알린다. |
| Request | [UNREADY]  | 게임 준비가 되지않았다고 서버에 알린다. |
| Request | [PUT]1 1   | 1행 1열에 돌을 둔다고 서버에 알린다. |

#### 3. 상관관계

상관관계에서는 어떤 Request가 요청되면 Reply 응답을 하는지에 대해 설명한다. 

#### 4. 통신흐름

게임을 진행하면서 발생할 수 있는 통신흐름을 다음과 같이 그림으로 표현하였다.

##### 4-1. 게임 접속 성공

<img src="https://user-images.githubusercontent.com/39123255/51219356-e545c880-1973-11e9-9a0c-f7533153763b.png" width=500></p>

#### 4-2. 자리가 없어 게임 접속 실패

<img src="https://user-images.githubusercontent.com/39123255/51219421-41105180-1974-11e9-8f25-1fce480d463a.png" width=500></p>

#### 4-3. 게임 준비

<img src="https://user-images.githubusercontent.com/39123255/51219522-a95f3300-1974-11e9-9541-444bf6f514b2.png" width=500></p>

#### 4-4. 게임 시작
서버에서 각 플레이어에게 [START] 명령을 내리면 [COME]black 명령을 받을 플레이어가 먼저 돌을 놓는다.

<img src="https://user-images.githubusercontent.com/39123255/51219582-db709500-1974-11e9-9355-2421ce555df7.png" width=500></p>

#### 4-5. 플레이어가 돌을 놓을 수 없는 곳에 돌을 놓았을 때

<img src="https://user-images.githubusercontent.com/39123255/51219695-55a11980-1975-11e9-933f-9c653b027f29.png" width=500></p>

#### 4-6. PASS 발생

<img src="https://user-images.githubusercontent.com/39123255/51219729-87b27b80-1975-11e9-99f0-f64c1688fe93.png" width=500></p>

#### 4-7. TIMEOUT 발생

<img src="https://user-images.githubusercontent.com/39123255/51219803-e2e46e00-1975-11e9-89ec-53ed7b99f03b.png" width=500></p>

#### 4-8. 게임 종료

<img src="https://user-images.githubusercontent.com/39123255/51220163-7bc7b900-1977-11e9-8155-e1551931c92f.png" width=500></p>
