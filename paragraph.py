paragraph='''Mastering Python is like learning a modern lingua franca for technology, opening doors to a world of endless creation. This course distills the languages celebrated simplicity into an elegant learning journey, transforming abstract syntax into a tool for genuine problem-solving.
From the very first line of code, you will discover how its clean, readable design makes complex concepts intuitive and accessible.'''
print("Paragraph length:", len(paragraph))

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

preview = paragraph[:50]
print("First 50 characters preview:", preview)

replaced_text = paragraph.replace("Python", "PYTHON")
print("Replaced text:\n", replaced_text)

lowercase_text = paragraph.lower()
print("Lowercase text:\n", lowercase_text)

trimmed_text = paragraph.strip()
print("Trimmed text:\n", trimmed_text)

words_list = paragraph.split()
print("List of words:", words_list)
if "course" in paragraph:
    print("Success: The word 'course' was found in the description!")
    
    final_message = "The course description is {} characters long and has {} words.".format(
    len(paragraph), len(words_list)
)
print(final_message)
