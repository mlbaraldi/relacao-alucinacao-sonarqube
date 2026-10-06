

def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    from collections import namedtuple
    Graph = namedtuple('Graph', field_names)
    graph = []
    
    if make_value is None:
        make_value = lambda bin_: bin_
    
    for bin_ in hist:
        if get_coordinate == "left":
            x = bin_.left
        elif get_coordinate == "right":
            x = bin_.right
        elif get_coordinate == "middle":
            x = (bin_.left + bin_.right) / 2
        else:
            raise ValueError("Invalid get_coordinate value")
        
        y = make_value(bin_)
        graph.append(Graph(x, *y))
    
    if scale is True:
        scale = hist.scale
    
    return graph, scale
