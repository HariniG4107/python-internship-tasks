import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    users = response.json()

    print("\nUSER DATA\n")

    # Display only first 5 users
    for user in users[:5]:
        print("ID :", user['id'])
        print("Name :", user['name'])
        print("Email :", user['email'])
        print("-" * 30)

    search_id = int(input("\nEnter User ID to search: "))

    found = False

    for user in users[:5]:
        if user['id'] == search_id:
            print("\nUSER FOUND")
            print("Name :", user['name'])
            print("Email :", user['email'])
            print("City :", user['address']['city'])
            found = True
            break

    if not found:
        print("User not found")

except requests.exceptions.RequestException:
    print("API connection error")

except ValueError:
    print("Please enter a valid number")