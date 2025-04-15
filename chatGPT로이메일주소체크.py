import re

# 이메일 유효성 검사 함수
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# 테스트용 이메일 주소 10개
sample_emails = [
    "test@example.com",         # 유효
    "user.name@domain.co",      # 유효
    "user_name@domain.com",     # 유효
    "username@sub.domain.org",  # 유효
    "user-name@domain.io",      # 유효
    "user@.com",                # ❌ 도메인이 없음
    "user@domain",              # ❌ 도메인 끝이 없음
    "@domain.com",              # ❌ 사용자명이 없음
    "user@domain..com",         # ❌ 잘못된 도메인
    "user@@domain.com"          # ❌ @가 2개
]

# 검사 실행
def test_emails(emails):
    for email in emails:
        result = "✅ Valid" if is_valid_email(email) else "❌ Invalid"
        print(f"{email:30} => {result}")

# 실행
if __name__ == "__main__":
    test_emails(sample_emails)
