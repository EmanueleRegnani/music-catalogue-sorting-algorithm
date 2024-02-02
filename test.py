import importlib

# In this file change only the group_id
group_id = 16


def test(gid, filename):
    g = importlib.import_module('group{}.project'.format(gid))
    g.prepare(filename)

    r = g.top_authors(5, ['rock', 'pop'])
    print(r)
    # Must return ['The Police', 'U2', 'The Cure', 'Elvis Presley', 'Michael Jackson']

    r = g.top_authors(20, ['indie', 'rock', 'metal'])
    print(r)

    r = g.top_authors(10, ['pop'])
    print(r)


test(group_id, 'small.csv')
