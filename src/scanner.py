from fetcher import fetch
from header_checker import check_security_headers
from xss_checker import check_xss
from sqli_checker import check_sqli

def scan(url):
    print(f"[+] 대상 URL 스캔 시작: {url}")

    # 1) 웹페이지 가져오기
    data = fetch(url)

    if "error" in data:
        print(f"[!] URL 요청 중 오류 발생: {data['error']}")
        return

    
    # 2) 보안 헤더 검사

    headers = data["headers"]
    header_results = check_security_headers(headers)

    print("\n[ 보안 헤더 검사 결과 ]")
    for header, exists in header_results.items():
        if exists:
            print(f"  ✓ {header} : 적용됨")
        else:
            print(f"  ✗ {header} : 미적용")

    
    # 3) XSS 검사
    
    print("\n[ XSS 취약점 검사 ]")
    xss_result = check_xss(url)

    if xss_result["status"] == "possible":
        print("  ✗ XSS 취약점 가능성이 있습니다!")
        print(f"    테스트 URL: {xss_result['test_url']}")
    elif xss_result["status"] == "not_found":
        print("  ✓ 반사형 XSS 징후가 발견되지 않았습니다.")
    elif xss_result["status"] == "no_params":
        print("  - URL에 파라미터가 없어 XSS 검사를 수행할 수 없습니다.")
    else:
        print(f"  ! XSS 검사 중 오류 발생: {xss_result['message']}")

    
    # 4) SQL Injection 검사
    
    print("\n[ SQL Injection 검사 ]")
    sqli_result = check_sqli(url)

    if sqli_result["status"] == "possible":
        print("  ✗ SQL Injection 취약점 가능성이 있습니다!")
        print(f"    테스트 URL: {sqli_result['test_url']}")
        print(f"    감지된 에러 패턴: {sqli_result['error_pattern']}")
    elif sqli_result["status"] == "not_found":
        print("  ✓ SQL Injection 징후가 발견되지 않았습니다.")
    elif sqli_result["status"] == "no_params":
        print("  - URL에 파라미터가 없어 SQL Injection 검사를 수행할 수 없습니다.")
    else:
        print(f"  ! SQL Injection 검사 중 오류 발생: {sqli_result['message']}")

    print("\n[✓] 스캔 완료되었습니다.")


if __name__ == "__main__":
    url = input("스캔할 URL을 입력하세요: ")
    scan(url)