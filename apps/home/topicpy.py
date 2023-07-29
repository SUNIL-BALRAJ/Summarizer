def topic(text):
    text = text.lower()
    if 'heart pain' in text:
        a= 'Heart Problem'
    elif 'stomach pain' in text:
        a= 'Kidney Problem'
    elif 'skin rashes' in text:
        a= 'Skin Problem'
    elif 'have diabetes' in text:
        a= 'Diabetes'
    elif 'bladder' in text:
        a= 'Urinary Problem'
    elif 'asthma' in text:
        a= 'Asthma'
    return a
    
