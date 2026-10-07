#Given a sentence, find out the no. of words in the sentence. You can assume that there are no whitespaces before the first word and after the last word in the sentence.
input_str = input("Enter the sentences: ")
count = 1
for i in range(len(input_str)):
    if input_str[i] == " ":
        count += 1
print(count)
                
            
            