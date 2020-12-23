import numpy as np
class Methods:
    """"""
    def __init__(self):

    def pca(self, data, k_largest):
        """"""
        u, s, vh = np.linalg.svd(data)
        s = s[0:k_largest]
        for i in range(0,k_largest):
            for row in data[:]
        
        return 

    def k_means(self, data):
        """"""
        pass

    def lms_regression(self, data, labels):
        """"""
        pass

    def lasso_regression(self, data, labels):
        """"""
        pass

    def locally_weighted_linear_regression(self, data, labels):
        """"""
        pass

    def regularized_linear_regression(self, data, labels):
        """"""
        pass

    def logistic_regression(self, data, labels):
        """"""
        pass

    def regularized_logistic_regression(self, data, labels):
        """"""
        pass

    def exact_lms_regression(self, data, labels):
        """"""
        pass

    def svm(self, data, labels):
        """"""
        pass

    def kernel_svm(self, data, labels):
        """"""
        pass

    def perceptron(self, data, labels):
        """"""
        pass

    def gda(self, data, labels):
        """"""
        pass

    def naive_bayes(self, data, labels, smoothing = True):
        """"""
        pass

    def min_ann(self):
        """"""
        pass
    def min_cnn(self):
        """"""
        pass
    def min_rnn(self, data):
        """"""
        pass
    def min_transformer(self, data):
        """"""
        pass
    def gan(self, data):
        """"""
        pass
    def autoencoder(self, data):
        """"""
        pass
    def lstm(self, data):
        """"""
        pass
    def gru(self, data):
        """"""
        pass
    def variational_autoencoder(self, data):
        """"""
        pass
    def min_rl(self, data):
        pass
    def guassian_mixture_model(self, data, labels):
        """"""
        pass
    def guassian_mixture_model(self, data):
        """"""
        pass
    def guassian_processes(self, data):
        """"""
        pass
    def decision_trees(self, data):
        """"""
        pass
    def factor_analysis(self, data):
        """"""
        pass
    def ensemble(self, data):
        """"""
        pass
    def feature_extractor(self, data):
        """"""
        pass
        
    