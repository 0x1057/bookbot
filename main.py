def main():
    # Opening Frankenstein (as example) and reading into a variable/printing
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        # print(file_contents)
        # print(book_length(file_contents))
        # print(char_count(file_contents))
        print(generate_report(file_contents))

# This function reads the number of words in the text
def book_length(file_contents):
    return len(file_contents.split())


# This is how sort method knows how to sort on list of dict
def sort_on(dict):
    return dict["num"]

# Counting the number of characters in the text
def char_count(file_contents):
    # Create a dict and iterate over text checking for 
    # presence of char/adding if needed
    char_dict = {}
    converted_list = []
    i = 0

    while i < len(file_contents):
        if file_contents[i].lower() not in char_dict:
            char_dict[file_contents[i].lower()] = 1
        else:
            char_dict[file_contents[i].lower()] += 1
        i += 1

    # Convert into list of dictionaries for better formatting
    # options, leaving aove option in for easy switching of methods
    for key in char_dict:
        temp_dict = {}
        if key.isalpha():
            temp_dict["name"] = key
            temp_dict["num"] = char_dict[key]
            converted_list.append(temp_dict)

    converted_list.sort(reverse=True, key=sort_on)

    return converted_list


def generate_report(file_contents):
    formatted_list = char_count(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(book_length(file_contents))
    print("")
    
    
    i = 0
    while i < len(formatted_list):
        current_key = formatted_list[i]["name"]
        current_value = formatted_list[i]["num"]
        print(f"The '{current_key}' character was found {current_value} times")
        i += 1

    


main()