import requests

webhook_url = "https://discord.com/api/webhooks/1067742794413785088/j4s9iURUbfYol0pdpGPyoNSWHiUpFFHS9TNobTvEW8GMXN9CS8b9aDWQ2pv_xnWAQ3Us"

def send_webhook_message(content):
    data = {
        "content": content
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Error code: {response.status_code}")

# Example usage
send_webhook_message("This is a test message!")
