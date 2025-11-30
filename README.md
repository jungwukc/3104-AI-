# 20253104-천정욱-AI와 데이터기초
이 프로젝트는 웹사이트의 취약점을 간단히 점검할 수 있는 학습용 보안 스캐너 입니다
주요기능
• URL로부터 HTML/헤더 수집
• 보안 헤더 적용 여부 검사
• XSS(반사형) 취약 가능성 탐지
• SQL Injection 의심 패턴 탐지
• 모듈 단위로 확장 가능한 구조
  1. 웹페이지 요청 및 정보 수집(Fetcher) (fetcher.py)
   입력한 URL로 HTTP GET요청을 보내고 다음 정보를 수집
   HTML 문서 내용(웹페이지의 구조와 내용)
   응답 헤더(웹서버 정보)
   HTTP상태 코드
   요청 실패 시 오류 메세지 반환
   
  2. 보안헤더 적용 여부 검사 (header_checker.py)
   X-Frame-Options
  웹페이지가 iframe에 포함되는 것을 막아 클릭재킹 공격을 방지합니다.

  X-Content-Type-Options
  브라우저의 MIME 타입 추측을 방지해 악성 파일 실행 위험을 줄입니다.

  Content-Security-Policy (CSP)
  스크립트, 리소스 로딩을 엄격히 제한해 XSS 등의 공격을 효과적으로 차단합니다.

  Strict-Transport-Security (HSTS)
  HTTPS 연결을 강제하여 중간자 공격을 방지합니다.
  
  3. 반사형 XSS 취약 가능성 검사 (Reflected XSS Detection) (xss_checker.py)
   xss란 악의적인 사용자가 공격하려는 사이트에 스크립트를 넣는 공격입니다.
   URL 파라미터 확인
   모든 파라미터 값에 테스트 문자열(xss_test_123) 삽입
   해당 URL로 다시 요청
   반환된 HTML에 테스트 문자열이 그대로 포함되었는지 검사
  
  포함됨 → 반사형 XSS 가능성 있음
  포함되지 않음 → 가능성 없음
  파라미터가 없으면 검사 불가

  4. SQL Injection 의심 패턴 검사 (sqli_checker.py)
   SQL는 데이터베이스에 명령하는 언어입니다.
   SQL Injection은 공격자가 데이터 베이스에 접근하는 로직을 주입하는 공격입니다
    URL 파라미터 값 뒤에 '(싱글쿼트)를 삽입해 서버가 오류를 반환하는지 확인합니다.

    URL 파라미터 수집
    값에 ' 추가
    새 URL로 요청
    응답 HTML에 SQL 에러 패턴 탐지
    탐지하는 대표적인 SQL 에러 문자열:

     "You have an error in your SQL syntax"
     "SQLSTATE"
     "Unclosed quotation mark"
     "mysql_fetch"
     "syntax error"

     발견됨 → SQL Injection 가능성 의심됨
     없으면 문제 없음
     파라미터 없음 → 검사 불가
     
실행방법 
  1. 이 프로그램은 3개의 Python 라이브러리를 사용합니다
     requests
     beautifulsoup4
     lxml
  2. 터미널을 열고 프로젝트가 있는 폴더로 이동합니다
     pip 명령을 사용해서 3개의 라이브러리를 설치합니다
  3. 프로그램 실행하기
     python src\scanner.py를 입력하면
     스캔할 URL을 입력하세요: 라고 뜹니다
  4. 검사할 URL을 입력하기
     검사할 URL을 입력하면
       보안헤더 적용여부
       XSS 반사형 취약 가능성
       SQL Injection 의심여부
     를 검사합니다

기술 스택
  1. Python 3.x
     전체 프로그램은 Python으로 작성되었으며 이 프로그램은 3.13.9버전으로 작성되었습니다
  2. requests
     HTTP 요청 및 응답 처리
      웹서버에 GET요청을 보내고 HTML, 헤더 정보, 응답 상태 코드를 수집하는 데 사용됩니다.
  3. BeautifulSoup4 + lxml
       응답 받은 HTML 문서에서 특정 문자열이나 구조를 빠르고 안정적으로 검사할 수 있게 해줍니다.
  4. URL 분석 – urllib.parse
       URL을 다음으로 분리하고 조작할 때 사용됩니다:
      스킴(https://)
      도메인(example.com)
      쿼 리 파라미터
      파라미터 수정 및 재조합

