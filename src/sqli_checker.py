from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import requests

SQL_ERROR_PATTERNS = [
    "You have an error in your SQL syntax",
    "mysql_fetch",
    "Unclosed quotation mark",
    "quoted string not properly terminated",
    "SQLSTATE",
    "syntax error",
]


def check_sqli(url):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    if not params:
        return {"status": "no_params"}

    # 테스트용 특수문자
    test_value = "'"

    # 새로운 파라미터 구성
    new_params = {k: (v[0] + test_value) for k, v in params.items()}
    new_query = urlencode(new_params)
    new_url = urlunparse(parsed._replace(query=new_query))

    try:
        response = requests.get(new_url, timeout=5)
        html = response.text.lower()

        # 에러 패턴 탐지
        for err in SQL_ERROR_PATTERNS:
            if err.lower() in html:
                return {
                    "status": "possible",
                    "test_url": new_url,
                    "error_pattern": err
                }

        return {"status": "not_found"}

    except Exception as e:
        return {"status": "error", "message": str(e)}