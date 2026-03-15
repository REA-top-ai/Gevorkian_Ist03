#1
contains_a = lambda row: 'true' if  'a' in row or 'A' in row else 'false'

#2
long_string = lambda row: 'true' if len(row) > 12 else 'false'

#3
ends_in_a = lambda row: 'true' if row[-1] == 'a' or row[-1] == 'A' else 'false'

#4
even_or_odd = lambda num: 'even' if num % 2 == 0 else 'odd'

#5
multiple_of_three = lambda num: 'multiple of three' if num % 3 == 0 else 'not a multiple'

#6
rate_movie = lambda rating: 'liked this movie' if rating > 8.5 else 'this movie wasnt very good'

