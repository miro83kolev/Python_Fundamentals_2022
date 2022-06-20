words = input().split()
print('\n'.join(text for text in words if len(text)%2 == 0))