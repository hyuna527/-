# <<<<1-8주차 수업내용 총정리>>>>

# WEEK-8

# 개발작업의 3단계인 스토리 보드 작성부터 시작, 모의고객과 활발히 소통할 것

# 인정받는 개발자의 3원칙
# 1. 문제를 해결하려고만 하지 말고 원인을 찾을 것
# 2. 
# 3. 고객의 입장에서 편의를 생각하자

# 8주차 할 일
# 1. 가상미팅
# 2. 문서작업
# 3. 프론트엔드 부분 개발
#     - 스토리보드 작성(발생할 수 있는 모든 화면 작성, dialog까지)
#     - 기본적인 ui 이미지 구현(페이지 넘기는 로직까지만 구현)
#     - 클래스 다이어그램 구성(금요일쯤에 중간 컨펌받을 것)

# 9주차 할 일

#  ~~~ 이하 생략 ~~~

# 10주차 할 일
#   ~~~ 이하 생략 ~~~




# 미팅 전략과 개발자의 스피치
# 첫 미팅의 목표
# 1. 고객이 원하는 프로그램을 꾸준한 질문을 통해 정확히 확인할 것
# 2. 꾸준히 기록할 것


# ~~~ 8주차 수업 내용 이하 생략 ~~~



# WEEK-7
# 람다함수 : 함수를 ㅁ나드는 명령어의 한 종류로 익명함수를 만드는 명령어
# 익명함수는 일회성, 혹은 단발성 함수임, 함수의 이름이 존재하지 않음
# lambda 변수 : 함수내용(보통 일반함수를 파라미터전달하며 호출함)





# WEEK-6
# 개발외주 프로세스
# 1. 고객과 만나 미팅
# 2. 브레인 스토밍
# 3. 요구사항 명세서 작성
# 4. 스토리보드 작성<< 디자이너 투입
# 5. 역할분담과 파일설계, 개발 시작


# 개발외주 작업은 디자이너보다 개발자에게 주도권이 있다.
# 디자이너를 위해
# 1. 미팅에서 디자이너에게 필요한 내용 질문
#  - 디자인 컨셉
#  - 사용했으면 하는 색감, 폰트 종류
#  - 페이지 명세와 레이아웃상의 요구사항
#  - 프로그램의 플랫폼 정보, 창 크기

# 2. 사소한 것도 디자인에 필요한 모든 것을 전달해야 함(경험이 중요)
#  - 내 마음대로 정보 삭제 ㄴㄴ
#  - 플랫폼 정보, 창 크기도 임의로 ㄴㄴ

# 3. 디자인 요소를 정리해서 디자이너에게 요구사항 명세서를 전달함(하이라이트로)

# 디자이너가 우리에 주는 자료는 보통 Adove Xd나 Pigma



# PyQt 시작
# 파이큐티란 : 파이썬 기반의 GUI 프레임 워크
# 사용법이 쉽고, 웬만한건 다 되고, 따로 설치할 필요가 없다는 장점과, 느리다는 단점

# 1. 라이브러리
#  - 완성된 소프트웨어를 개발하기 위해 사용할 수 있는 모듈
#  - 다른 개발자가 만들어둔 모듈
#  - 사용 난이도고 높고 다 다를 수 있음
#  - 라이브러리는 우리가 직접 수정이 가능

# 2. 프레임워크
#  - 라이브러리봐 조금 더 넓은 개념의 소프트웨어로
#  - 예를 들어, Express, Spring, PyQt
#  - 라이브러리보다 사용 난이도가 쉽고, 일정한 규칙과 경로가 있으며 자유도가 떨어진다.

# 3. 서드 파티
#  - 그냥 완성된 소프트웨어를 말합니다. eX)카카오톡
#  - 코드 수정은 당연히 안되고 자유도라는 개념이 없고 사용만 가능하다.


# Widget
# - 파이큐티에서 눈에 보이는 것들의 단위로 계층구조(부모자식 구조)를 가진다.파이큐티란



# WEEK-5
# 데이터 베이스 : 데이터를 저장하는 공간
# 변수는 램에 만들어 지기 때문에 프로그램을 끄더라도 데이터를 보존하고 싶으면 DB에 저장하면 됨

# 1. RDB(관계형 데이터 베이스) - 프론트 엔드
#  - 일정한 규격이 있음
#  - 데이터가 저장될 때, 그 규격을 맞춰야 함
#  - 데이터가 체꼐적이거나 무결성이 보장되어야 할 때 사용??

# 2. NoSQL(비관계형 데이터 베이스) - 백엔드
#  - 일정한 규격이 없고, 대충 데이터를 때려 밖을 때 사용하는데, 대신 속도가 빠르다.


# RDB의 종류
# 1. MySQL(전 세계에서 가장 많이 사용함. 가장 보편적인 성능)
# 2. Oracle(2등, MySQL보다 성능은 좋지만 유료이다.)
# 3. PostgreSQL(몇몇 상황에서는 MySQL보다 빠르고 편리한 기능이 많다)
# 4. SQLite(기능이 거의 없다시피 하지만, 빠르고 서버가 아니라 로컬전용 DB이다.)

# class의 종류 3가지
# 1. 역할 구분을 위해 의미적으로 나누는 역할
# 2. 기능을 중복해서 사용하기 위한 역할
# 3. 모듈의 기능을 사용하기 위한 역할



# WEEK-4
# cpu, 코어, thread 내용

#  ~~~ 이하 생략 ~~~

# WEEK-3
# 좋은 코드는 수정할 곳을 찾기가 쉽고, 한번에 수정이 되어야 하며, 여러번 재사용이 가능해야 한다.

# 함수를 사용할 때
# 1. 띄어쓰기가 있는 부분에서 알파벳 대문자를 사용하고, 기능 유추가 가능한 함수명을 사용하자
# 2. 변수는 최대한 지역변수(클래스 안, 함수 안)를 사용하자. 전역변수는 메모리만 차지함
#  - 메인함수에서 선언한 변수는 전역변수이니까 최대한 생성 ㄴ 주로 member변수 사용(class내에서의 전역변수)


# 설계의 5원칙
# 1. 카멜 기법을 사용해 함수사용시 주의점도 지켜서 짓는다.
# 2. 하나의 함수 안에 두개 이상의 기능을 넣지 않는다.(논리만 있으면 어겨도 ㄱㅊ)
# 3. 멤버변수 선언은 꼭 class의 생성자에서 해준다.
# 4. class 밖에 main을 제외한 함수가 있으면 안된다.
# 5. main함수는 최대한 짧게 프로그래밍 해야 한다.





# WEEK-2

# 개발 작업의 특징
# 1. 협업이 기본 베이스
# 2. 매우 긴 프로젝트 기간에도 목표 유지
# 3. 잦은 팀원의 변경 - 이직이 흔함

# 문서작업의 목표
# 1. 어떤 개발자건 문서를 읽고 동일한 기능을 가진 프로그램을 개발해야 함(성능)
# 2. 프로그램의 목적, 사용자, UX적 고려사항을 생각해 작성할 것
# 3. 어떤 언어, 어떤 소프트웨어 사용할지 고려할 것, 고객의 입장에서 예외처리도 꼼꼼히 해줄 것




