
#3.
import re
s="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better"
m=re.findall('[bB.*]', s)
print(m)

#2.
import re
s="A, very very; irregular_sentence"
n=re.sub(r'[,;_ ]'," ",s)
print("word sentence:",n)

#1.
emails=["zuck26@facebook.com","page33@google.com","jeff42@amazon.com"]
def email_splitter(email):
    username=email.split('@')[0]
    domain=email.split('@')[1]
    domain_name=domain.split('.')[0]
    domain_type = domain.split('.')[1]
    print('Username:',username)
    print('Domain:',domain_name)
    print('Type:', domain_type)
    print("\n")
for email in emails:
    email_splitter(email)

