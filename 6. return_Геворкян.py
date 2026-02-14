# def define_age(current_year , birth_year):
#     age = current_year - birth_year
#     return age
# my_age = define_age(2049 , 1993)
# dads_age = define_age(2049 , 1953)
# print('My age is '+str(my_age)+' , my dads age is '+str(dads_age)+'')


# def get_boundaries(target , margin):
#     low_limit = target - margin
#     high_limit = target + margin
#     return low_limit, high_limit
#
# low_limit , high_limit = get_boundaries(100,20)
# print('low limit is '+str(low_limit)+' and high limit is '+str(high_limit)+'')


def repeat_stuff(stuff, num_repeats = 10):
    statement = stuff * num_repeats
    return statement

lyrics = repeat_stuff('row', 3) + ' your boat.'
song = repeat_stuff(lyrics)
print(song)
