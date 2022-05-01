from shapely import geometry
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
import sympy
from sympy import symbols
import top_n

# cirs_parse = [[(0, 0), 1], [(1, 1), 0.5], [(0.5, 0.5), 1]]
cirs_parse = top_n.gen_circles_parse()
print(cirs_parse)


def gen_circles(circles):
    """
    :param circles: [[(cir_x,cir_y),r]...]
    :return: list <class 'shapely.geometry.polygon.Polygon'>
    """

    def gen_circle(circle_pos, r):
        """
        :param circle_pos: (pos_x1,pos_y1)
        :param r: radius
        :return: <class 'shapely.geometry.polygon.Polygon'>
        """
        return geometry.Point(circle_pos[:2]).buffer(r)

    circles_lst = []
    for circle in circles:
        circles_lst.append(gen_circle(circle[0], circle[1]))
    return circles_lst


cirs = gen_circles(cirs_parse)
for cir in cirs:
    x, y = cir.exterior.xy
    plt.plot(x, y)


def cal_inter(circles):
    inter = circles[0]
    for i in range(1, len(circles)):
        inter = inter.intersection(circles[i])
        # x, y = inter.exterior.xy
        # plt.plot(x, y)
    return inter


def draw_inter(cirs):
    inter = cal_inter(cirs)
    x, y = inter.exterior.xy
    plt.plot(x, y)
    centroid = inter.centroid
    xx, yy = centroid.x, centroid.y
    plt.plot(xx, yy, '^')

    plt.show()


draw_inter(cirs)

# def cal_intersection_2_cir(cir1, cir2):
#     """
#     :param cir1: tuple(pos_x1,pos_y1,r1)
#     :param cir2: tuple(pos_x2,pos_y2,r2)
#     :return: 若有交点，返回交点lists，没有就返回none
#     """
#     x1, y1, r1 = cir1
#     x2, y2, r2 = cir2
#     # 不加real会出复数解
#     x, y = symbols('x y', real=True)
#     cir1_ueq = (x - x1) ** 2 + (y - y1) ** 2 - r1 ** 2 <= 0
#     cir2_ueq = (x - x2) ** 2 + (y - y2) ** 2 - r2 ** 2 <= 0
#     ans = sympy.solveset([cir1_ueq, cir2_ueq], [x, y])
#     if not ans:
#         return 0
#     else:
#         return ans


# a = cal_intersection_2_cir((0, 0, 1), (0.5, 0.5, 1))
# print(a)
# # [(-0.411437827766148, 0.911437827766148), (0.911437827766148, -0.411437827766148)]
