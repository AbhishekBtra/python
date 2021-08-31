list_of_integers = list(range(1,5))

sum_of_square_of_even_integers = sum(( x for x in list_of_integers if x % 2 ==0))

sum_of_square_of_even_integers = sum(x for x in list_of_integers if x % 2 ==0) # more elegant syntax

print('sum of even ints = ',sum_of_square_of_even_integers)