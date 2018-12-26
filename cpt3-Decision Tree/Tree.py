# 树

from .Uncertainty import Uncertainty

class ID3Node():

    def __init__(self,df,labelCol):
        self.df = df
        self.children = []
        self.labelCol = labelCol

    def NodeEntropy(self):
        return Uncertainty(self.df,self.labelCol).entropy(self.labelCol)

    def getChildren(self):
        pass

