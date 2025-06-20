import requests

access_token = "AQUÍ_TU_ACCESS_TOKEN"  # <- reemplaza esto

headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get("https://api.linkedin.com/v2/userinfo", headers=headers)

if response.status_code == 200:
    print("✅ Datos del usuario:")
    print(response.json())
else:
    print("❌ Error:", response.status_code)
    print(response.text)
