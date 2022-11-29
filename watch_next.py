import spacy

nlp = spacy.load('en_core_web_md')

def watch_next(desc):
    hulk = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'
    hulk = nlp(hulk)
    desc = nlp(desc)
    sim = hulk.similarity(desc)
    return sim
with open('movies.txt', 'r+') as f:
    text = f.readlines()
    similarities = {}
    for x in text:
        similarities[x[:7]] = watch_next(x)
        
f.close()

print(f"{max(similarities, key = similarities.get)} is the movie you should watch next")

    