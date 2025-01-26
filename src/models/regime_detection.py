from sklearn.cluster import KMeans
from sklearn.preprocessing import StandedScaler

def detect_regimes(data):
	scaler = StandardScaler()
	scaled = scaler.fit_transform(data)
	kmeans = KMeans(n_cluster = 4, random_state = 42).fit(scaled)
	data['regime'] = kmeans.labels_
	return data
