# 2022-algorithm-study
2Digit 사내 알고리즘 스터디를 위한 레파지토리입니다.

<hr>

# Welcome! 🎉

안녕하세요!🙇‍♂️ 스터디장 🦒기린입니다. 이 페이지에서는 어떻게 공부해야 할 지, 어떤 방식으로 이루어지는지, 스터디 간 지켜야 할 규칙은 어떤 것이 있는지를 명시합니다.

<hr>

# 방식

* 해당 레파지토리에 직접적으로 `PUSH`하는 것을 금합니다. 🚫

* `Organization Repository`의 `branch` 목록을 보면 본인의 이름으로 된 branch가 생성되어 있습니다. 해당 브런치가 `PR Target Repository`가 됩니다.

* 모든 `PUSH`는 `Fork`를 통해 본인의 레파지토리에 복제한 후, 본인의 이름과 같은 `branch`에 `Pull Request(PR)`를 통해 반영하게 됩니다. 
 - [`Pull Request`에 대해 알고 싶다면?](https://inpa.tistory.com/entry/GIT-%E2%9A%A1%EF%B8%8F-%EA%B9%83%ED%97%99-PRPull-Request-%EB%B3%B4%EB%82%B4%EB%8A%94-%EB%B0%A9%EB%B2%95-folk-issue)

* `Github Pull Request`의 경우 문제를 풀고 `Push`한 후 `PR`을 하였는데, **다시 다른 문제를 풀어 `Push` 한다면** 해당 커밋 리스트가 그대로 반영이 되어 PR이 쌓이면 보기 좋지 않습니다. 
> 이런 일을 방지하기 위해 `Target Repository(Organization Repository)`의 `branch`는 만들어져 있는 자신의 이름으로 하되, `Origin Repository(본인의 Fork된 Repository)`의 `Branch`는 문제 번호, 문제를 푼 날짜 등으로 설정하여, `1~2개`까지의 문제만 `PR`할 수 있도록 합니다. 

* 반영을 위한 최소 `Approve` 수는 `1개` 입니다. ✅

* Code Review의 종류에 제한은 없습니다. 해당 코드에서 고쳐야 할 부분 뿐 아니라, 자신과 다른점, 배운 점, 어떤 것이 더 효율적인지 등 본인의 성장을 위해서 어떤 것이든 의견을 나누길 바랍니다.👍<br>
> _- 코드리뷰 예시 사진 -_
<img width="798" alt="image" src="https://user-images.githubusercontent.com/59782504/165787003-d5ed07f6-2a31-4483-ada0-767b1cd35e5c.png">

* `Merge` 전략은 `Git History`의 깔끔한 관리를 위해 (`Squash` || `Rebase`)로 한정합니다. 
  _(참고 Link: [Git Merge Strategy 비교](https://inmoonlight.github.io/2021/07/11/Git-merge-strategy/))_
  <br> _(`Merge`로 할 경우 해당 멤버의 `Branch`에 접속하여 `Reset` 하겠음. 충돌로 인해 `rabase` or `squash`가 되지 않는 경우, 질문하거나, 스스로 원인파악 후 직접 히스토리를 관리하여, `Git History`를 정리할 것.)_

* 문제를 풀다가 어려운 부분이 있다면 `Discussion`을 활용할 수 있습니다. 모르는 문제나 알고리즘적인 성능 등에 대해 질문하고, 의견을 교환합니다. 👩‍👩‍👧‍👦
<img width="131" alt="image" src="https://user-images.githubusercontent.com/59782504/165785529-80f8821e-9c78-493d-92c6-ddf3ae64c7cc.png">

* 정답 코드를 보는 것은 허용합니다. **단 주석이나, 위키를 통해 어떤 것을 배웠는지 남겨야 합니다.** 📖

## Panalty

* `3번` 연속 불참하신 분은 해당 스터디에서 강퇴합니다. 🚫

* `Code Review`는 최소 주당 `2회` 이상 하지 않을 시 강퇴합니다. 🚫

## 가상 시나리오

1. 내 레파지토리에 해당 `Repository`를 `Fork`한다.

<img width="112" alt="image" src="https://user-images.githubusercontent.com/59782504/165771133-2b0976c6-5739-479c-a67c-14ad91155b17.png">

2. 문제 제목, 번호 등을 이용하여 본인 레파지토리의 로컬 `branch`를 만든다.

3. 해당 브런치에서 문제를 풀고, 본인의 `Repository`에 `Commit` & `Push` 한다.

4. `Pull Request`를 통해 반영 요청을 보낸다.

5. `Approve`를 받을 시 본인이 확인 후 해당 부분을 반영, `Change Request`를 받을 시 피드백을 반영하여 코드를 수정한다.

6. 최종적으로 `Merge`한다. 

7. 문제 중 얻은 점이나 공유하고 싶은 것은 `Organization Repository`의 `Wiki`탭에 `markdown`을 통해 남긴다.  

<hr>

# 알고리즘, 자료구조 문제를 풀어본 적이 없다면? 📚

관련 도서 링크: [파이썬 알고리즘 공부 도서](https://1drv.ms/b/s!AumORQdGTpjTg8Bj7-yizwCBij5ukA?e=8fcSzU) <br>
> _저작권 문제로 public하게 공개가 불가능하기 떄문에 필요하신 분은 저에게 비밀번호를 물어주세요!_

## 동빈나 - 실전 알고리즘 강의 📺

C++언어 기반으로 되어 있는 강의이며 언어가 익숙하시다면, 설명과 이론 부분이 좋은 강의이기 때문에 추천합니다. <br>
유투브 링크: [동빈나 - 실전알고리즘 강의](https://www.youtube.com/watch?v=qQ5iLNjpxSk&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz)

