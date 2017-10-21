from hrange import plot_events 

friends_like= [('Seinfield (NBC)', 1989, 1998),
               ('Friends (NBC)', 1994, 2004),
               ('How I met your mother (CBS)', 2005, 2014),
               ('The Big Bang Theory (CBS)', 2007, 2018)]

fig = plot_events(friends_like)
# issue - this was cut out
fig.savefig('sitcom.pdf')

"""
> The closest thing to Frasier on TV today is probably Modern Family 
> (co-created by Christopher Lloyd and Steve Levitan, both of whom formerly 
> worked on Frasier), simply because both shows focus on how we do or don't 
> relate to the people we're related to. 
"""
