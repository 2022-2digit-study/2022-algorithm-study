# 2022-algorithm-study
2Digit 사내 알고리즘 스터디를 위한 레파지토리입니다.

### [Wiki](https://github.com/2022-2digit-study/2022-algorithm-study/wiki)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Discussion](https://github.com/2022-2digit-study/2022-algorithm-study/discussions)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Issue](https://github.com/2022-2digit-study/2022-algorithm-study/issues)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Code PR](https://github.com/2022-2digit-study/2022-algorithm-study/pulls)
<hr>

# Welcome! 🎉

안녕하세요!🙇‍♂️ 스터디장 🦒기린입니다. 이 페이지에서는 어떻게 공부해야 할 지, 어떤 방식으로 이루어지는지, 스터디 간 지켜야 할 규칙은 어떤 것이 있는지를 명시합니다.

> 소개 부분은 주저리 주저리를 적어두셨으니 방식 부분으로 바로 패스하셔도 됩니다.

<hr>

# 소개

컴퓨터 공학 수업을 들으며 교수니께서 알고리즘이란 **"입력을 적절한 출력으로 바꾸는 것"** 이라고 간단하게 설명하셨습니다. **현실 세계에서 일어나는 일들을 해결하는 문제해결 단위**, 그것을 우리는 `알고리즘`이라고 정의합니다.

## 그럼 왜 알고리즘이 필요해?

한 문제를 해결하는 방법은 1가지가 있을 수도 있고 수십가지가 될 수도 있습니다. 정렬 알고리즘만 봐도 매우 빠르다고 알려진 퀵 정렬 부터, 기수정렬, 버블정렬, 힙정렬 등이 존재하고, 매우 느리고 비효율적이라고 알려진 Bogo 정렬 과 같은 무식한 방법도 존재합니다. _(참고: [정렬 시각화 비교 영상](https://www.youtube.com/watch?v=kPRA0W1kECg))_ <br>
<br>
다만 문제는 특정 문제를 맞닥뜨렸을 때 정렬하는 방법론과 마찬가지로 어떤 것은 매우 빠르나, 어떤 것들은 매우 느리게 동작할 수 있다는 것입니다.<br>
조금 어려운 문제에 대해 어떤 것들은, 매우 빠르게 동작하나, 일부 케이스에서는 답이 의도한 것과 다른 휴리스틱과 같은 알고리즘이 존재하기도 합니다.<br>
<br>
우리는 이러한 문제에 있어 조금 더 효율적으로 푸는 방법을 익히고, 본인의 알고리즘 설계능력을 향상시키며, 이를 자신의 개발에 적용하는 것을 목적으로 합니다.<br>
<br>
> 그리고 평소에 쓰던 Git을 조금 다르게 써보시면서, 이런식으로도 Git과 Github을 사용할 수 있다는 것을 알아가셨으면 합니다. 

<hr>

# Code Style

> 필수 사항은 아니나 따르시는 것이 좋습니다. _(Code Style은 강력하게 Review 하겠습니다)_
>
> \+ Jetbrains 계열 IDE의 경우 `Ctrl` + `Alt` + `L` (Windows, Linux), `Command` + `Option` + `L` (Mac OS)로 코드 정리를 쉽게 할 수 있습니다.

* Python 언어의 경우 PEP8 스타일가이드를 따라 코드를 작성하도록 합니다.
> [Python PEP8 Style Guide](https://peps.python.org/pep-0008/)

* Java의 경우 Google Java Style Guide를 따라 코드를 작성하도록 합니다.
> [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)

* C++의 경우 Google C++ Style Guide를 따라 코드를 작성하도록 합니다.
> [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)


# 방식

### Branch 

* 먼저 해당 레파지토리(Organization Repository)에 직접적으로 `Push`하는 것을 엄금합니다. 🚫

* `Organization Repository`의 `branch` 목록을 보면 본인의 이름으로 된 branch가 생성되어 있습니다. 해당 브런치가 `PR Target Repository`가 됩니다.

### Pull Request

* 모든 `PUSH`는 `Fork`를 통해 본인의 레파지토리에 복제한 후, 본인의 이름과 같은 `branch`에 `Pull Request(PR)`를 통해 반영하게 됩니다. 
 - [`Pull Request`에 대해 알고 싶다면?](https://inpa.tistory.com/entry/GIT-%E2%9A%A1%EF%B8%8F-%EA%B9%83%ED%97%99-PRPull-Request-%EB%B3%B4%EB%82%B4%EB%8A%94-%EB%B0%A9%EB%B2%95-folk-issue)

* `Github Pull Request`의 경우 문제를 풀고 `Push`한 후 `PR`을 하였는데, **다시 다른 문제를 풀어 `Push` 한다면** 해당 커밋 리스트가 그대로 반영이 되어 한 `PR`당 문제가 쌓이면 보기 좋지 않습니다. 
> 이런 일을 방지하기 위해 `Target Repository(Organization Repository)`의 `branch`는 만들어져 있는 자신의 이름으로 하되, `Origin Repository(본인의 Fork된 Repository)`의 `Branch`는 문제 번호, 문제를 푼 날짜 등으로 설정하여,  **`PR`당 최대 `1~2개`까지의 문제만 포함할 수 있도록 합니다.**

* 반영을 위한 최소 `Approve` 수는 `1개` 입니다. ✅

* Pull Request의 제목 양식은 아래와 같습니다.
> (이름) 문제 사이트 제목[예:백준, 프로그래머스 등] - 문제 제목1
> 예: (Giraffe) 프로그래머스 - 프렌즈 사천성

### Merge Strategy

* `Merge` 전략은 `Git History`의 깔끔한 관리를 위해 (`Squash` || `Rebase`)로 한정합니다. 
  _(참고 Link: [Git Merge Strategy 비교](https://inmoonlight.github.io/2021/07/11/Git-merge-strategy/))_
  <br> _(`Merge`로 할 경우 해당 멤버의 `Branch`에 접속하여 `Reset` 하겠음. 충돌로 인해 `rabase` or `squash`가 되지 않는 경우, 질문하거나, 스스로 원인파악 후 직접 히스토리를 관리하여, `Git History`를 정리할 것.)_

### Code Review & Discussion

* `Code Review`의 종류에 제한은 없습니다. 해당 코드에서 고쳐야 할 부분 뿐 아니라, 자신과 다른점, 배운 점, 어떤 것이 더 효율적인지 등 본인의 성장을 위해서 어떤 것이든 의견을 나누길 바랍니다.👍<br>
> _- 코드리뷰 예시 사진 -_
<img width="798" alt="image" src="https://user-images.githubusercontent.com/59782504/165787003-d5ed07f6-2a31-4483-ada0-767b1cd35e5c.png">


* 문제를 풀다가 어려운 부분이 있다면 `Discussion`을 활용할 수 있습니다. 모르는 문제나 알고리즘적인 성능 등에 대해 질문하고, 의견을 교환합니다. 👩‍👩‍👧‍👦
<img width="131" alt="image" src="https://user-images.githubusercontent.com/59782504/165785529-80f8821e-9c78-493d-92c6-ddf3ae64c7cc.png">

### Comment

* 문제 풀이 주석의 첫 부분에는 문제의 제목, 문제의 주석이 담겨야 합니다.
> in solution.py
```python
# 프로그래머스 - http://문제링크.com

def solution():
    return "Hello World"
```

* 정답 코드를 보는 것은 허용합니다. **단 `주석`이나, `Wiki`를 통해 어떤 것을 배웠는지 남겨야 합니다.** 📖
<img width="97" alt="image" src="https://user-images.githubusercontent.com/59782504/165789472-6098a25d-8451-4c16-99a1-4cf5e8a23357.png">

## Benefit

* 열심히 코드를 본 당신, 쉬세요! 
> 코드 리뷰한 PR 5개당 1번 쉴 수 있습니다 (패널티에 들어가지 않습니다.)


## Panalty

* `3번` 연속 불참하신 분은 해당 스터디에서 강퇴합니다. 🚫
> 아파도 3번 연속 아플 수는 없겠죠..?

* `Code Review`는 최소 주당 `2회` 이상 하지 않을 시 강퇴합니다. 🚫
> 다른 사람의 코드도 봐주세요 😭

* Merge가 주당 1회 이상 하지 않을 시 강퇴합니다. (첫주는 제외합니다.) 🚫

## 가상 시나리오

1. 내 레파지토리에 해당 `Repository`를 `Fork`한다.

<img width="112" alt="image" src="https://user-images.githubusercontent.com/59782504/165771133-2b0976c6-5739-479c-a67c-14ad91155b17.png">

2. 문제 제목, 번호 등을 이용하여 본인 레파지토리의 로컬 `branch`를 만든다.

3. 해당 브런치에서 문제를 풀고, 본인의 `Repository`에 `Commit` & `Push` 한다. 

4. `Pull Request`를 통해 반영 요청을 보낸다. ✉️

5. `Approve`를 받을 시 본인이 확인 후 해당 부분을 반영, `Change Request`를 받을 시 피드백을 반영하여 코드를 수정한다. ✏️

6. 최종적으로 `Merge`한다. 🙏

7. 문제 중 얻은 점이나 공유하고 싶은 것은 `Organization Repository`의 `Wiki`탭에 `markdown`을 통해 남긴다.  

<hr>

# 알고리즘, 자료구조 문제를 풀어본 적이 없다면? 📚

관련 도서 링크: [파이썬 알고리즘 공부 도서](https://1drv.ms/b/s!AumORQdGTpjTg8Bj7-yizwCBij5ukA?e=OflR47) <br>
> _저작권 문제로 public하게 공개가 불가능하기 떄문에 필요하신 분은 저에게 비밀번호를 물어주세요!_

## 동빈나 - 실전 알고리즘 강의 📺

C++언어 기반으로 되어 있는 강의이며 언어가 익숙하시다면, 설명과 이론 부분이 좋은 강의이기 때문에 추천합니다. <br>
유투브 링크: [동빈나 - 실전알고리즘 강의](https://www.youtube.com/watch?v=qQ5iLNjpxSk&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz)

<hr>

# 종료
> 해당 스터디는 6.30 부로 종료되었습니다.
