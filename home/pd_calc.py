# -*- coding: utf-8 -*-
import homcloud.interface as hc
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import gc

for i in range(0,228) :
    pointcloud = np.loadtxt("homcloud_p{:03d}_out.txt".format(i))
    hc.PDList.from_alpha_filtration(pointcloud, save_to="pd/p{:03d}.idiagram".format(i), save_boundary_map=True)

del pointcloud
gc.collect()

mesh = hc.PIVectorizerMesh((0, 20), 64, sigma=0.002, weight=("atan", 0.01, 3))

for i in range(0,228) :
    PDList = hc.PDList("pd/p{:03d}.idiagram".format(i))
    pd = PDList.dth_diagram(0)
    pd.histogram((0,20),64).plot(colorbar={"type": "log","max":100000})
    plt.savefig("pd_result3/p{:03d}_pd0.png".format(i))
    plt.close()
    pd = PDList.dth_diagram(1)
    pd.histogram((0,20),64).plot(colorbar={"type": "log","max":100000})
    plt.savefig("pd_result3/p{:03d}_pd1.png".format(i))
    plt.close()
    pd = PDList.dth_diagram(2)
    pd.histogram((0,20),64).plot(colorbar={"type": "log","max":100000})
    plt.savefig("pd_result3/p{:03d}_pd2.png".format(i))
    plt.close()
    pd_vects = mesh.vectorize(pd)
    np.savetxt('pd_vector3/p{:03d}.dat'.format(i), pd_vects, header='pd_vector')


    