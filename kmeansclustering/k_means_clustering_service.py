import json
import random
import string
import kmeansclustering.k_means_clustering_processor as processor
import kmeansclustering.k_means_clustering_transformer as transformer

input_python = []
for ind in range(100):
    random.seed(ind % 10 + random.randint(-2, 2))
    input_python.append(
        {
            "id": "ID_" + str(ind),
            "tabOpenedTimeInMillis": random.random(),
            "lastAccessedTimeInMillis": random.random(),
            "noOfAccesses": random.random(),
            "title": ''.join([random.choice(string.ascii_letters + string.digits) for n in range(50)]),
            "pageContentHTML": ''.join([random.choice(string.ascii_letters + string.digits) for n in range(50)]),
            "latitudeWhenOpened": random.random(),
            "longitudeWhenOpened": random.random(),
        }
    )

input_json_seeded = json.dumps(input_python)

with open('new_json.json', 'r') as f: input_json_from_file = json.dumps(json.load(f))
index_id_map, points = transformer.transform(input_json_from_file)
print(points)
print(processor.process(index_id_map, points, 10))
