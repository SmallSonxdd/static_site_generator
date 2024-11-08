def block_to_block_type(markdown_block):
    block_copy = markdown_block
    if block_copy[0] == '#':
        count = 1
        character = block_copy[1]
        while character == '#':
            count +=1
            character = block_copy[count]
            if count > 6:
                return 'PARAGRAPH'
        if block_copy[count] == ' ':
            return f'h{count}'
    
    if block_copy[0:3] == '```' and block_copy[-1:-4:-1] == '```':
        return 'CODE'
    
    if block_copy[0:2] == '> ':
        copy_list = block_copy.split('\n')
        block_is_quote = 'QUOTE'
        for line in copy_list:
            if line[0:2] != '> ':
                block_is_quote = 'PARAGRAPH'
                break
        return block_is_quote
    
    if block_copy[0:2] in [('* '), ('- ')]:
        copy_list = block_copy.split('\n')
        block_is_unordered = 'UNORDERED LIST'
        for line in copy_list:
            if line[0:2] not in [('* '), ('- ')]:
                block_is_unordered = 'PARAGRAPH'
                break
        return block_is_unordered
    
    if block_copy[0:3] == '1. ':
        copy_list = block_copy.split('\n')
        block_is_ordered = 'ORDERED LIST'
        index = 0
        for line in copy_list:
            index +=1
            if line[0:3] != f'{index}. ':
                block_is_ordered = 'PARAGRAPH'
                break
        return block_is_ordered

    return 'PARAGRAPH'