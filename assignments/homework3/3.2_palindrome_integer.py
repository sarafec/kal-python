def reverse(num):
	return int(str(num)[::-1])

def isPalindrome():
	inputNum = int(input("Please input an integer: "))

	reversedNum = reverse(inputNum)

	if reversedNum == inputNum:
		print("Your number is a palindrome")
	else:
		print("Your number is not a palindrome")

isPalindrome()