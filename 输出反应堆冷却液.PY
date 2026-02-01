for reactor in Env.links():
    reactor.enabled(reactor.heat < 0.6)