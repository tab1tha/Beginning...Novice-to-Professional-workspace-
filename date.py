month_name=['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august','september', 'october', 'november', 'december']
ordinal=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
month=input('month(1-12):')
mnumber=int(month)
m=month_name[mnumber-1]
day=input('day(1-31):')
dnumber=int(day)
d=day+ordinal[dnumber-1]
year=input('year:')
print('d+m+year')