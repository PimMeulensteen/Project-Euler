#21124
import inflect
p = inflect.engine()
counter = 0
text = 'Hello world'
print(text)
for x in range(1, 1001):
    text = p.number_to_words(x)
    text = text.replace(" ", "")
    text = text.replace("-", "")
    print(text, len(text))
    counter = counter + len(text)
print(counter)
