from backend.auth import login_user

success, message = login_user(
    "javeria@test.com",
    "12345678"
)

print(message)