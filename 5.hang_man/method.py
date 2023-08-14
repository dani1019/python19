def match_letter(display_string, answer,letter):
    print(answer)
    print(letter)
    for answer_letter in list(answer):
        print(f"answer_letter:{answer_letter}")
        print(f"letter: {letter}")
        if answer_letter == letter:
            display_string.append(letter)
        else:
            display_string.append("_")
    
    return display_string