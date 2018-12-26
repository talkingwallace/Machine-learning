# 用于计算不确定性的函数

# input: 一个pandas dataframe

from numpy import log
from numpy import power

class Uncertainty():

    """
    df: the input dataframe
    """
    def __init__(self,df,labelCol):
        self.df = df
        self.labelCol = labelCol


    # get occurrence probabilities of every unique value in a Series
    def getProbabilities(self,sr):
        counter = sr.value_counts()
        total = sr.count()
        p = counter / total
        return p

    # divide by attr
    def divide(self,col):
        uni = self.df[col].unique()
        l = []
        for i in uni:
            l.append(self.df[self.df[col] == i])
        return l

    # the input is a pandas Series which is a column from the input pandas DataFrame
    # we compute the entropy of this input Series
    def entropy(self,sr,eps = 1e-12):
        p = self.getProbabilities(sr)
        ent = -((p*log(p)).sum())
        ent = max(eps,ent)
        return ent

    # compute gini
    def gini(self,sr):
        p = self.getProbabilities(sr)
        p = power(p,2)
        g = 1 - p.sum()
        return g

    def con_chaos(self,col,method='ent'):
        blocks = self.divide(col)
        totalNum = self.df[self.labelCol].count()
        res = 0
        for b in blocks:
            if method == 'ent':
                val = self.entropy(b[self.labelCol])
            else:
                val = self.gini(b[self.labelCol])
            res += (b[col].count()/totalNum)*val

        return res

    def info_gain(self,col,method='ent'):
        ent = self.entropy(self.df[self.labelCol])
        conChaos= self.con_chaos(col,method)
        return ent - conChaos


    def bin_con_chaos(self):
        pass

