import re
class revstr:
    def revword(self,s):
        self.s=s
        regex=r'\w+'
        result=re.findall(regex,s)
        result.reverse()
        return ' '.join(result)

q="y"
while q.lower()=="y":
    string = input("Enter a string: ")
    print("Reverse of string is:",revstr().revword(string))
    q=input("want to continue?(y/n): ")
