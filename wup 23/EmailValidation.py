def validateEmail(address):
    validated = False
    
    correctEnding = False
    hasAt = False
    realEmail = False
    
    mid = len(address)
    endingList = ['.com', '.tw', '.org']
    emailList = ['gmail', 'Outlook', 'yahoo', 'Inbox', 'iCloud', 'Mail']
    invalid = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=','+',
               '`', '~', '"', "'", ';', '/', '\\', "|", "[", "]", "{", "}",
               ':', ',', '?']
                
    for end in endingList:
        if end in address[-len(end) : ]:
            correctEnding = True
            mid -= len(end)
            break

    for email in emailList:
        if email in address[mid - len(email) : mid]:
            realEmail = True
            break
        
    if '@' in address and address.index('@') < mid - 3:
        hasAt = True

    if hasAt and correctEnding and realEmail:
        validated = True

    for i in invalid:
        if i in address:
            validated = False
            break
        
    return validated

print(validateEmail('xxx@gmil.com'))
