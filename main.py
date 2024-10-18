import random

# داده های اولیه
lowercase_letters = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 'pass_count' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
numbers = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
symbols = [ '!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '(' , ')' , '-' , '_' , '=' , '+' , '[' , ']' , '{' , '}' , ';' , ':' , '<' , '>' , ',' , '.' , '/' , '?' , '|' , '~' , '`' ]

# کپشن های نمایش
welcome_title = "hi , You can create strong password !"
pass_count_title = "How many passwords? :  "
include_numbers_title = "Does it include numbers?"
include_symbole_title = "Does it include symbols?"

# پردازش
print ( welcome_title.title ( ) )
pass_count = input ( pass_count_title )
is_need_number = input ( include_numbers_title.title ( ) )
is_need_symbole = input ( include_symbole_title.title ( ) )

# خروجی
if is_need_number == 'yes' :
    print ( "yes" )
else :
    print ( "no" )
