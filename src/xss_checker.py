from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import requests

def check_xss(url):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    # 파라미터가 없으면 검사 불가
    if not params:
        return {"status": "no_params"}

    # 테스트 페이로드
    test_value = "xss_test_123"
    new_params = {k: test_value for k in params}

    # 새로운 URL 구성
    new_query = urlencode(new_params, doseq=True)
    new_url = urlunparse(parsed._replace(query=new_query))

    try:
        response = requests.get(new_url, timeout=5)
        html = response.text

        # 테스트 문자열이 HTML에 그대로 있다면 XSS 의심
        if test_value in html:
            return {"status": "possible", "test_url": new_url}
        else:
            return {"status": "not_found"}

    except Exception as e:
        return {"status": "error", "message": str(e)}