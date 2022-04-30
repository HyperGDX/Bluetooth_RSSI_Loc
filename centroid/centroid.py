from shapely import geometry
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint


# # (4,0) r=2
# circ1 = geometry.Point(0, 0).buffer(1)
# # 取圆边界上的点
# circ2 = geometry.Point(2, 0).buffer(1.5)
# jiao = circ1.intersection(circ2)
# print(jiao.centroid)

def cal_intersection_2_cir(cir1, cir2):
    """
    :param cir1: tuple(pos_x1,pos_y1,r1)
    :param cir2: tuple(pos_x2,pos_y2,r2)
    :return: 若有交点，返回交点lists，没有就返回none
    """
    x1, y1, r1 = cir1
    x2, y2, r2 = cir2
    x3 = 1
