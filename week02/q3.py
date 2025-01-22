def charCount(t):
   
    char_dict = {}

    try:
        with open(t, 'r') as file:
            for line in file:
                for char in line.strip():
                    
                    if char.isspace():
                        continue

                    if char in char_dict:
                        char_dict[char] += 1
                    else:
                        char_dict[char] = 1
    except FileNotFoundError:
        print(f"Error: The file '{t}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

    return char_dict

print(charCount('example.txt'))
