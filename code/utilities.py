def if_have_head(conf):
    top_stack = conf.stack[-1]
    for arc in conf.arcs:
        if top_stack == arc[2]:
            return True
    return False
