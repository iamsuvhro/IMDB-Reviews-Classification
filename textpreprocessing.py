#Function to clean html tags from a sentence
import re
def clean_html(sentence): 
    pattern = re.compile('<.*?>')
    cleaned_text = re.sub(pattern,' ',sentence)
    return cleaned_text

print("Removing Html")
print('After Removing HTML tags:',clean_html('<a href="foo.com" class="bar">This is a demo test<b>text!</b></a><>'))
print("---------------------------------------------------")
print("---------------------------------------------------")
print('\n')

#Function to keep only words containing letters A-Z and a-z.
#this will remove all punctuations, special characters.
def rem_pun(sentence):
    cleaned_text  = re.sub('[^a-zA-Z]',' ',sentence)
    return (cleaned_text)

print("Removing Punctuations")
print("After Removing Punctuations:",rem_pun("fsd*?~,,,( sdfsdfdsvv)#"))
print("---------------------------------------------------")
print("---------------------------------------------------")
print("\n")

#Remove URL from sentences.
def rem_url(sen):
    txt = re.sub(r"http\S+", " ", sen)
    sen = re.sub(r"www.\S+", " ", txt)
    return (sen)

print("Removing URL")
print("After Removing URL:",rem_url("https://colab.research.google.com/drive/1dG8sy949kwnxsOX6BN4Dkime6JdVjGqL#scrollTo=_0_gNhnK6TRY notice the URL is removed"))
print("---------------------------------------------------")
print("---------------------------------------------------")
print("\n")

#Remove words like 'ddddddddd', 'funnnnnn', 'coolllllll' etc. Preserves words like 'goods', 'cool', 'best' etc. We will remove all such words which has three consecutive repeating characters.
def remove_extra(sen): 
    cleaned_text  = re.sub("\\s*\\b(?=\\w*(\\w)\\1{2,})\\w*\\b",' ',sen)
    return (cleaned_text)


print("Removing Extra")
print("After Removing Extra:",remove_extra("This looks soooooooo good!,I am so happpyyy"))
print("---------------------------------------------------")
print("---------------------------------------------------")
print("\n")
