class Color:
    def display_color(self,char):
        rainbow_color = {'V':'Violet','I':'Indigo','B':'Blue','G':'Grey','Y':'Yellow','O':'Orange','R':'Red'}
        char = char.upper()
        print(rainbow_color[char])
        
class invalidAlphabet(Exception):
    def msg(self):
        print("Please enter valid alphabet")
        
class invalidCharacter(Exception):
    def msg(self):
        print("Please Enter valid character for rainbow colors")
        
obj1 = Color()
q = 'y'
while q.lower() == 'y':
    char = input("\nEnter the character: ")
    try:
        if char.isalpha():
            rainbow_list = ['v','i','b','g','y','o','r']
            if char.lower() in rainbow_list:
                obj1.display_color(char)
            else:
                raise invalidCharacter
        else:
            raise invalidAlphabet
    except invalidAlphabet as err:
        err.msg()
    except invalidCharacter as err1:
        err1.msg()
    while True:
        q1 = input("want to continue?(y/n): ")
        if q1.lower() == 'y' or q1.lower() == 'n':
            break
    q=q1
