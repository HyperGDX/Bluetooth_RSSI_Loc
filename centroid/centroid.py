from shapely import geometry
import matplotlib.pyplot as plt
import top_n


def gen_circles_geo(circle_parse):
    # def gen_circle(circle_pos, r):
    #     return geometry.Point(circle_pos[:2]).buffer(r)
    circles_lst = []
    for circle in circle_parse:
        # circles_lst.append(gen_circle(circle[0], circle[1]))
        circles_lst.append(geometry.Point(circle[0]).buffer(circle[1]))
    return circles_lst


###############################################################
# 最重要的部分
def cal_inter(rssi_lst, beacon_lst):
    # 逐渐增加幅度计算交集
    inter = None
    up_rate = 0.95
    while not inter:
        up_rate += 0.05
        circles_parse = top_n.gen_circles_parse(rssi_lst, beacon_lst, up_rate)
        circles_geo = gen_circles_geo(circles_parse)
        inter = circles_geo[0]
        for i in range(1, len(circles_geo)):
            inter = inter.intersection(circles_geo[i])
        if inter:
            print(circles_parse)
            draw_circles(circles_geo)
            print(up_rate)
    return inter


def cal_centroid(inter):
    inter = inter
    centroid = inter.centroid
    xx, yy = centroid.x, centroid.y
    return xx, yy


def draw_circles(circles_geo):
    for cir in circles_geo:
        x, y = cir.exterior.xy
        plt.plot(x, y)


def draw_inter_centroid(inter):
    inter = inter
    x, y = inter.exterior.xy
    plt.plot(x, y)
    cx, cy = cal_centroid(inter)
    plt.plot(cx, cy, '^')
    print(cx, cy)
    plt.show()

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
