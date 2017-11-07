def agreement (i1, i2):
    agreements = []

    for each in i1:
        if each in i2:
            agreements.append(each)

    return agreements

def disagreement (i1, i2):
    disagreements = []

    for each in i1:
        if each not in i2:
            disagreements.append(each)

    for each in i2:
        if each not in i1:
            disagreements.append(each)

    return disagreements

def compatibility (i1, i2):
    agreements = agreement (i1, i2)
    disagreements = disagreement (i1, i2)

    compatibility = len(agreements) / (len(agreements) + len(disagreements))

    return compatibility

def bestmatch (me, others):
    """Returns a most-compatible person.

    Parameters:
        me:     a list of things I like

        others: a list of pairs, where each pair is a name
                and a list of things that person likes; for example,
                [ ["Scrooge", ["money", "food"]],
                  ["Cratchit", ["family", "heat", "food"]]
                ]
    """
    whom = 'no one'
    comp = -1
    for person in others:
        name, likes = person
        match = compatibility (me, likes)
        if match > comp:
            comp = match
            whom = name
    return whom
