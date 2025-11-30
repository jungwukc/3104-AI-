def check_security_headers(headers):
    results = {}

    required_headers = [
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Content-Security-Policy",
        "Strict-Transport-Security"
    ]

    for h in required_headers:
        results[h] = (h in headers)

    return results