import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

username = "admin"
password = "password"

response = requests.get(
    f"https://httpbin.org/basic-auth/{username}/{password}",
    auth=HTTPBasicAuth(username, password)
)

print("Basic:", {
    "authenticated": response.json()["authenticated"],
    "user": username,
    "password": password
})



response = requests.get(
    f"https://httpbin.org/digest-auth/auth/{username}/{password}",
    auth=HTTPDigestAuth(username, password)
)

print("Digest:", {
    "authenticated": response.json()["authenticated"],
    "user": username,
    "password": password
})

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30'
response = requests.get(
    "https://httpbin.org/bearer",
    headers={"Authorization": f"Bearer {token}"}
)

print("Bearer:", {
    "authenticated": response.json()["authenticated"],
    "user": username,
    "token": response.json()["token"]
})