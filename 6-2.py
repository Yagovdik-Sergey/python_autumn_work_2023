first_student = input().split(', ')
second_student = input().split(', ')
common_books = set(first_student) & set(second_student)
print(f'Количество книг, прочитанное обоими учениками: {len(common_books)}')