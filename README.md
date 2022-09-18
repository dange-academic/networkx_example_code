# NetworkX编程实践基础25课：NetworkX官方手册使用解读

```python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Author ： 单哥的科研日常（公众号、B站）
# 示例程序所用库的版本：networkx==2.6.3, matplotlib==3.5.2, pandas==1.4.3
# 点击蓝色标题可跳转视频讲解界面
```

NetworkX编程实践基础课程是入门复杂网络很关键的一门课程，是专门针对编程基础薄弱的同学而推出的一门编程实践课程。在具备NetworkX编程基础之后，可以继续学习[复杂网络建模](https://www.bilibili.com/video/BV1WR4y1G7kH/?vd_source=519dd7a4b1f4260ebe31140657f52698)（点击可跳转课程界面）课程以加深对复杂网络的理解。

NetworkX编程实践基础课程源代码见：

[https://github.com/dange-academic/networkx_example_code](https://)

## 目录

01 [熟悉networkx官方教程](https://www.bilibili.com/video/BV1Wa411N7NH/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

02 [生成一个简单图](https://www.bilibili.com/video/BV1wB4y1r7zr/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

03 [获取网络的邻接矩阵](https://www.bilibili.com/video/BV1gW4y1a7e1/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

04 [根据邻接矩阵生成网络](https://www.bilibili.com/video/BV1bT411L7ZA/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

05 [网络节点的度、平均度以及度分布](https://www.bilibili.com/video/BV1LW4y1Y7E5/?vd_source=519dd7a4b1f4260ebe31140657f52698)

06 [网络的最短距离和平均距离](https://www.bilibili.com/video/BV1na411P7yi/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

07 [网络的局部集聚系数、平均集聚系数以及全局集聚系数](https://www.bilibili.com/video/BV1qD4y1z772/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

08 [网络节点之间的独立路径数量](https://www.bilibili.com/video/BV1aB4y1x7fs/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

09 [计算网络的相关性系数和平均近邻度](https://www.bilibili.com/video/BV1Kt4y1E7Q1/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

10 [计算网络节点的中心性](https://www.bilibili.com/video/BV1NB4y1G7UN/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

11 [获取网络的最大连通子图](https://www.bilibili.com/video/BV1ng411S7pP/?vd_source=519dd7a4b1f4260ebe31140657f52698)

12 [网络的k核](https://www.bilibili.com/video/BV1XD4y1B7ib/?vd_source=519dd7a4b1f4260ebe31140657f52698)

13 [连通网络的效率](https://www.bilibili.com/video/BV1b14y1s7mn/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

14 [针对图、节点以及连边的一些基本功能](https://www.bilibili.com/video/BV1NG4y1r7Au/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

15 [常见的图（网络）生成器-规则、ER随机、WS小世界以及BA无标度网络的生成](https://www.bilibili.com/video/BV1og411U7Ps/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

16 [图的各种矩阵](https://www.bilibili.com/video/BV1dg411m71J/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

17 [计算图的邻接矩阵的谱和拉普拉斯矩阵的谱（特征值）](https://www.bilibili.com/video/BV1dV4y1T7AK/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

18 [网络与其他数据之间的转换](https://www.bilibili.com/video/BV1cg411U7af/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

19 [通过pandas读取外部网络数据生成网络](https://www.bilibili.com/video/BV1yD4y1q7Ba/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

20 [对网络节点重新编号](https://www.bilibili.com/video/BV1md4y1X756/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

21 [网络的读与写功能介绍](https://www.bilibili.com/video/BV1pT411u7Vq/?vd_source=519dd7a4b1f4260ebe31140657f52698)

22 [网络可视化（初级）](https://www.bilibili.com/video/BV1se411M7hB/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

23 [网络可视化（进阶）](https://www.bilibili.com/video/BV1NP4y1o77H/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

24 [网络可视化（高阶）](https://www.bilibili.com/video/BV1mP411H7Vi/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)

25 [facebook社交网络分析案例](https://www.bilibili.com/video/BV1qd4y1B7j2/?spm_id_from=333.788&vd_source=519dd7a4b1f4260ebe31140657f52698)