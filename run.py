import base64

print("hello repo")

# Read and print config file in base64
with open("config/.conf", "r") as f:
    content = f.read()
    encoded = base64.b64encode(content.encode()).decode()
    print(f"Config file (base64): {encoded}")