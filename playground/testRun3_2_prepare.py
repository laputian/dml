import network3_2
from network3_2 import Network
from network3_2 import FullyConnectedLayer, SoftmaxLayer
training_data, validation_data, test_data = network3_2.load_data_shared()
mini_batch_size = 10
net = Network([
	FullyConnectedLayer(n_in=784, n_out=100),
        SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)
net.SGD(training_data, 10, mini_batch_size, 0.1,validation_data, test_data)