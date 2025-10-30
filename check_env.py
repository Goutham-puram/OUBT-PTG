from dotenv import load_dotenv
import os

load_dotenv()

access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

print('Checking .env file contents:\n')
print(f'Access Key: {access_key}')
print(f'Access Key Length: {len(access_key) if access_key else 0}')
print(f'\nSecret Key: {secret_key}')
print(f'Secret Key Length: {len(secret_key) if secret_key else 0}')
print(f'Expected Length: 40')

# Check the actual .env file
print('\n.env file raw contents:')
with open('.env', 'r') as f:
    for i, line in enumerate(f, 1):
        print(f'Line {i}: {repr(line)}')
