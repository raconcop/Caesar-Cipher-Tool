def encrypt(text, shift):
    text = text.lower()
    encrypted_text = ""
    
    for char in text:
        if char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 27 + 97)
            
        else:
                encrypted_text += char
                
                
    return encrypted_text


original= "lmfao"
encrypted_message = encrypt(original, 2)
print(encrypted_message)