#https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python
# simple encryption #1
# def decrypt(encrypted_text, n):
#     for j in range(n):
#         s1 = encrypted_text[0:(len(encrypted_text) )// 2]
#         s2 = encrypted_text[(len(encrypted_text) )// 2:len(encrypted_text)]
#         i = 0
#         text = ''
#         for i in range(min(len(s1),len(s2))):
#             text += s2[i] + s1[i]
#             i += 1
#         if len(s2)>len(s1):
#             text += s2[len(s2)-1]
#         encrypted_text=text
#     return encrypted_text


def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    else:
        s1 = encrypted_text[0:(len(encrypted_text)) // 2]
        s2 = encrypted_text[(len(encrypted_text)) // 2:len(encrypted_text)]
        i = 0
        text = ''
        for i in range(min(len(s1), len(s2))):
            text += s2[i] + s1[i]
            i += 1
        if len(s2) > len(s1):
            text += s2[len(s2) - 1]
        encrypted_text = text
        return decrypt(encrypted_text,n-1)

def encrypt(text, n):
    if n <= 0:
        print(text, n == 0)
        return text
    else:
        i = 0
        s1 = ''
        s2 = ''
        for el in text:
            if i % 2 == 1:
                s1 += el
            else:
                s2 += el
            i += 1
        text = s1 + s2
        return encrypt(text, n -1 )

strg = "This is a test!"
n = 12
a = encrypt("This kata is very interesting!", 1)
# b = decrypt(a, n)
print(a)



