import random

# داده های اولیه
lletters = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 'pass_count' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
numbers = [ '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' ]
symbols = [ '!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '(' , ')' , '-' , '_' , '=' , '+' , '[' , ']' , '{' , '}' , ';' , ':' , '<' , '>' , ',' , '.' , '/' , '?' , '|' , '~' , '`' ]

# تایتل های نمایش
welcome_title = "hi , You can create strong password !"

pass_count_title = "How many passwords? :  "
numbers_count_title = "How Many  numbers?"
symbole_count_title = "How Many symbols?"

# مرحله نمایش
print ( welcome_title.title ( ) )
pass_count = int ( input ( pass_count_title ) )
numbers_Count = int ( input ( numbers_count_title.title ( ) ) )
symbole_count = int ( input ( symbole_count_title.title ( ) ) )

#  مرحله پردازش
password_list = [ ]
for char in range ( 0 , pass_count ) :
    password_list.append ( random.choice ( lletters ) )

for char in range ( 0 , numbers_Count ) :
    password_list.append ( random.choice ( numbers ) )

for char in range ( 0 , symbole_count ) :
    password_list.append ( random.choice ( symbols ) )

# خروجی
random.shuffle ( password_list )
print ( password_list )

