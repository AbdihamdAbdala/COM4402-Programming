# Login Name Normaliser
# Raw strings especially usernames can be used to force strict integrity, meaning case sensitivity. IT HAS TO BE THE EXACT SAME VALUE
# when performing comparisons
username = input("What is your username:")
raw_username = username
username = username.strip().lower()

print(f"Raw '{raw_username}'\nProcessed: '{username}' ")


