from dotenv import load_dotenv
import os

load_dotenv()

access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

print('Access Key:')
print(f'  Value: {access_key}')
print(f'  Length: {len(access_key) if access_key else 0}')
print(f'  First 10 chars: {access_key[:10] if access_key else "None"}')

print('\nSecret Key:')
print(f'  Value: {secret_key}')
print(f'  Length: {len(secret_key) if secret_key else 0}')
print(f'  Expected length: 40')
print(f'  First 10 chars: {secret_key[:10] if secret_key else "None"}')
print(f'  Last 5 chars: {secret_key[-5:] if secret_key else "None"}')

# Check for hidden characters
if secret_key:
    print(f'\n  Has whitespace? {secret_key != secret_key.strip()}')
    print(f'  Repr: {repr(secret_key)}')
