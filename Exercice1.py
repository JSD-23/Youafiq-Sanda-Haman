def lengthOfLastWord(s):
    # Votre code ici
    list_word = s.split(' ')
    n=len(list_word)-1
    while(list_word[n]=="" or list_word[n]==" "):
      n = n - 1
    return len(list_word[n])