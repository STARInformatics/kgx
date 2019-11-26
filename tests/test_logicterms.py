from kgx import LogicTermTransformer


# TODO: make this a proper test with assertions
def save(g, outfile):

    w = LogicTermTransformer(g)
    w.save('target/' + outfile + '.sxpr')

    w1 = LogicTermTransformer(g, 'prolog')
    w1.save("target/" + outfile + ".pl")

