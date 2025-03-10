#Função usando laço for
# def convert(text):
#     snake_cased_char_list = []
#     for char in text:
#         if char.isupper():
#             converted_character = '_' + char.lower()
#             snake_cased_char_list.append(converted_character)
#         else:
#             snake_cased_char_list.append(char)
#     snake_cased_string = ''.join(snake_cased_char_list)
#     clean_snake_cased_string = snake_cased_string.strip('_')

#     return clean_snake_cased_string


#Função usando list comprehension
def convert(text):
    snake_cased_char_list = ["_" + char.lower() if char.isupper() else char for char in text]

    return "".join(snake_cased_char_list).strip('_')

def main():
    print(convert('camelCasedString'))

main()
