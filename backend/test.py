response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="こんにちは"
)
print(response.text)
