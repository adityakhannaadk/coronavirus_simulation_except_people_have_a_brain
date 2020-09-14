from sklearn.neural_network import MLPClassifier

""""
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)

input_train = [1,2,3], [3,2,1]]
output_train = [0, 1]
clf.fit(input_train,output_train)
"""



class hive():
    def train(self, classifier, X_data, y):
        classifier.fit(X=X_data, y=y)

    def predict(self, data, clf):
        va = clf.predict([data]).reshape(1, -1))
        va = list(value[0])
        return va

    def get_move_dist(self, data, clf):
        pred = self.predict(data,clf)
        return (pred)

    def net_do(self, pre_train_data_x,pre_train_data_y):
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
        self.train(pre_train_data_x,pre_train_data_y)
        return classifier
        # I used a 5,2 configuration to make sure its not too computationally intensive
        # Also to make it more realistic :/
