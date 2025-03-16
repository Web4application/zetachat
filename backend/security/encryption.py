from cryptography.fernet import Fernet

# Generate a key for encryption (do this once and save it securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt a message
message = b"Hello, secure world!"
encrypted_message = cipher_suite.encrypt(message)
print("Encrypted:", encrypted_message)

# Decrypt the message
decrypted_message = cipher_suite.decrypt(encrypted_message)
print("Decrypted:", decrypted_message)
