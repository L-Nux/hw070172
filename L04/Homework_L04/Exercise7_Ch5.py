#Exercise 7 CH5 (Zelle 2017, Python Programming: An Introduction to Computer Science)

def main():
    
    print("This program can encode and decode Caesar ciphers.")

    text1 = input("Enter a short text to encode: ")
    key = int(input("Enter the key: "))

    encoded_char =[]

    #encoding
    for t in text1: 
    	encoded_char.append(chr(ord(t)+key))

    encoded_text = "".join(encoded_char)

    print("The encoded message is: ", encoded_text)

    #decoding
    text2 = input("Enter a short text to decode: ")
    key2 = int(input("Enter the key: "))

    decoded_char =[]

    for t in text2: 
    	decoded_char.append(chr(ord(t)+(-key2)))

    decoded_text = "".join(decoded_char)

    print("The decoded message is: ", decoded_text)


main()