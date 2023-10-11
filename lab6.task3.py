def count_vowels_and_consonants(text):
    vowels = set("aeioiyAEIOIY")
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

text = input("Введіть текст: ")

vowel_count, consonant_count = count_vowels_and_consonants(text)

if vowel_count > consonant_count:
    print("Голосних літер більше в тексті.")
elif vowel_count < consonant_count:
    print("Приголосних літер більше в тексті.")
else:
    print("Кількість голосних та приголосних літер однакова.")





