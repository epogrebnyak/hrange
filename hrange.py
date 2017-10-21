"""Create horizontal range barplots.

See also:
    <https://stackoverflow.com/questions/44518170/how-to-draw-a-bar-timeline-with-matplotlib>    
    <https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.barh.html>    
"""

from operator import itemgetter
import matplotlib.pyplot as plt


def get_elements(k, list_of_tuples):
    """Return k-th elenet of each tuple in *list_of_tuples*.""" 
    return list(map(itemgetter(k), list_of_tuples))                


def to_vectors(events):
    """Vectorise *events* list of tuples."""
    return dict(event=get_elements(0, events),
                begin=get_elements(1, events),
                end=get_elements(2, events))


def plot_hrange(event, begin, end):    
    vrange = range(len(begin))
    w = [abs(e-b) for b, e in zip(begin, end)]
    fig, ax = plt.subplots()
    ax.barh(vrange, width=w, left=begin, height=0.5)
    plt.yticks(vrange, event)
    return fig

def plot_events(events):
    events = list(reversed(events))
    return plot_hrange(**to_vectors(events))
   
if __name__ == "__main__":
    # original data as vectors
    begin = [2003,1991,2008,1986,2013,1994,2002]
    end = [2007,2016,2016,2015,2013,1999,2003]
    event = ["Event {}".format(i) for i in range(len(begin))]
    plot_hrange(event, begin, end)
        
    # data as rows
    # serialised as list of tuples like (event name, start year, end year)        
    events = [('Event 0', 2003, 2007),
         ('Event 1', 1991, 2016),
         ('Event 2', 2008, 2016),
         ('Event 3', 1986, 2015),
         ('Event 4', 2013, 2013),
         ('Event 5', 1994, 1999),
         ('Event 6', 2002, 2003)]    
    plot_hrange(**to_vectors(events))
    
    events = [('Event 0............', 2003, 2007)]
    fig = plot_hrange(**to_vectors(events))
    fig.savefig('fig.png')