import torch
import torch.nn as nn
from torch_geometric_temporal.nn import TGCN2

class CorrelationGNN(nn, Module):
	def __init__(self,node_features,periods):
		super().__init__()
		self.tgn = TGCN2(node_features, 32, periods)
		self.linear = nn.Linear(32,1)

	def forward(self, x, edge_index, edge_weight):
		h = self.tgn(x, edge_index, edge_weight)
		return torch.sigmoid(self.linear(h))

def train_gnn(returns, edges):
	model = CorrelationGNN(node_features = 1, periods = 20)
	optimizer = torch.optim.Adam(model.parameters(), lr = 0.001)
	
	for epoch in range(100):
		model = train()
		pred = model(returns.unsqueeze(-1), edges[0],edges[1])
		loss = nn.MSELoss(pred, get_ground_truth_correlations())
		optimizer.zero_grad()
		less.backward()
		optimizer.step()
	
	return model
