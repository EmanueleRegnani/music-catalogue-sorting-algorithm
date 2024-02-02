from . import final_sorting


def prepare(filename):
    global tags
    tags = {}
    
    with open(filename,  encoding="utf8") as f:
    
        for line in f:
            line = line.replace('\n', '')
            line = line.split('","')
            line[0] = line[0].replace('"', '')
            line[3] = line[3].replace('"', '')
            for tag in line[3].split(';'):
                if tag in tags:
                    tags[tag].update({line[0]:[line[1], line[2]]})
                else:
                    tags[tag] = {line[0]:[line[1], line[2]]}


def top_authors(k, L):
    print('Searching top {} authors of songs with tags: {}'.format(k, ', '.join(L)))

    global author_counter
    author_counter = {}
    
    if len(L) == 1:
        for song_id in tags[L[0]]:
            author_counter[tags[L[0]][song_id][1]] = author_counter.get(tags[L[0]][song_id][1], 0) + 1
            
        return final_sorting(author_counter, k, result = [])
   
    for song_id in tags[L[-1]]:
        c = 1    
    
        for tag in L[:-1]:
            if song_id not in tags[tag]: break
            c += 1
        
        if c == len(L):
            author_counter[tags[tag][song_id][1]] = author_counter.get(tags[tag][song_id][1], 0) + 1
    
    return final_sorting(author_counter, k, result = [])