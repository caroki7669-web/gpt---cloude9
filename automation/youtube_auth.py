from google_auth_oauthlib.flow import Flow
import os

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    flow = Flow.from_client_secrets_file(
        os.path.join(BASE_DIR, "client_secret.json"),
        scopes=SCOPES,
        redirect_uri="urn:ietf:wg:oauth:2.0:oob",
    )
    auth_url, _ = flow.authorization_url(prompt="consent")
    print("افتح الرابط ده في أي متصفح وسجّل دخول:")
    print(auth_url)
    code = input("الصق الكود اللي هيديهولك جوجل هنا: ").strip()
    flow.fetch_token(code=code)
    creds = flow.credentials
    with open(os.path.join(BASE_DIR, "token.json"), "w") as f:
        f.write(creds.to_json())
    print("تم الحفظ في token.json — مش هتحتاج تكرر الخطوة دي تاني")

if __name__ == "__main__":
    main()
