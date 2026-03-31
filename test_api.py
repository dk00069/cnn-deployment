import requests

# 1. Your Live Render URL
url = "https://waste-classifier-api-dzfk.onrender.com/predict"

# 2. Path to a sample image on your PC
image_path = "C:/Users/K Dhurba/Downloads/plastic_bottle.jpg" 

with open(image_path, "rb") as img:
    files = {"image": img}
    print("Sending request to Render... (Wait for cold start if needed)")
    
    response = requests.post(url, files=files)

# 3. Print the result
if response.status_code == 200:
    print("Success!")
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")