import sys

def ap_title_case(input_string):
    # List of articles, conjunctions, and prepositions to be excluded from capitalization
    excluded_words = ['a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'in', 'nor', 'of', 'on', 'or', 'so', 'the', 'to', 'up', 'yet']
    
    # Split the input string into words
    words = input_string.split()
    
    # Initialize an empty list to store the title-cased words
    title_cased_words = []
    
    for i, word in enumerate(words):
        # Capitalize the first word regardless of its content
        if i == 0:
            title_cased_words.append(word.capitalize())
        else:
            # Convert the word to lowercase if it's in the list of excluded words, otherwise capitalize it
            if word.lower() in excluded_words:
                title_cased_words.append(word.lower())
            else:
                title_cased_words.append(word.capitalize())
    
    # Join the title-cased words to form the final title-cased string
    title_cased_string = ' '.join(title_cased_words)
    
    return title_cased_string

if __name__ == "__main__":
    # Check if the user provided a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python title_case.py <input_string>")
    else:
        # Get the input string from the command-line argument
        input_string = sys.argv[1]
        
        # Convert the input string to AP title case
        output_string = ap_title_case(input_string)
        
        # Print the result
        print(output_string)

