def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

print("Palindrome Checker")
user_input = input("Enter a word or phrase: ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is NOT a palindrome.")
