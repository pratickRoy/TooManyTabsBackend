import tensorflow as tf


def process(index_id_map, points, n_clusters):
    cluster_indices = cluster(points, n_clusters, 50)
    cluster_index_map = {k: [] for k in range(n_clusters)}
    for i, point in enumerate(points):
        cluster_index_map[cluster_indices[i]].append(index_id_map[i])
    return cluster_index_map


def cluster(points, n_clusters, n_iterations):
    input_fn = lambda: tf.train.limit_epochs(tf.convert_to_tensor(points, dtype=tf.float32), num_epochs=10)

    k_means = tf.contrib.factorization.KMeansClustering(num_clusters=n_clusters, use_mini_batch=False)
    for iteration in range(n_iterations):
        print('Iteration #{}'.format(iteration))
        k_means.train(input_fn)

    # map the input points to their clusters
    return list(k_means.predict_cluster_index(input_fn))
