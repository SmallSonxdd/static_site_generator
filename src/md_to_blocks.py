def markdown_to_blocks(markdown):
    md_copy = markdown.split('\n\n')
    cleaned_blocks = []
    for string in md_copy:

        cleaned_string = string.strip()
        if cleaned_string != '':
            cleaned_blocks.append(cleaned_string)
    
    return cleaned_blocks