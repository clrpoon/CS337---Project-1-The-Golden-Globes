import csv
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

movies = []
with open("title.basics.tsv") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for line in tsvreader:
        try : 
            if line[1] == 'movie' and int(line[5]) >= 2000 :
                movies.append(line)
        except: 
            do = []


with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(movies)

# for movie in movies :
#     s = StringIO(','.join(movie))

#     with open('fileName.csv', 'w') as f:
#         f.append(s)

