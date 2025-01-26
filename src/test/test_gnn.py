import pytest
import torch
from src.gnn_correlation import CorrelationGNN

def test_genn_forward():
	model = CorrelationGNN(node_features = 1, periods = 20)
	x = torch.randn(10,1)
	edge_index = torch.tensor([[0,1],[0,1])
	edge_weight = torch.tensor([1.0,1.0])
	output = model(x, edge_index, edge_weight)
	assert output.shape == (10,1), "GNN forward pass failed"
