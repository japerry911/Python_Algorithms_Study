def generateDocument(characters: str, document: str) -> bool:
    if len(document) == 0:
        return True
    elif len(document) > len(characters):
        return False
    
    doc_chrs = {}

    for idx in range(len(characters)):
        if idx < len(document):
            if document[idx] not in doc_chrs:
                doc_chrs[document[idx]] = 1
            else:
                doc_chrs[document[idx]] += 1

        if characters[idx] not in doc_chrs:
            doc_chrs[characters[idx]] = -1
        else:
            doc_chrs[characters[idx]] -= 1
    
    return len(list(
        filter(lambda x: x > 0, [v for _k, v in doc_chrs.items()])
    )) == 0
    