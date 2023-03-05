class PS22():
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter your string: ")

    def put_string(self):
        print("Uppercase is: ",self.str1.upper())

        
q="y"
while q.lower()=="y":
    str1 = PS22()
    str1.get_string()
    str1.put_string()
    q=input("want to continue?(y/n): ")
