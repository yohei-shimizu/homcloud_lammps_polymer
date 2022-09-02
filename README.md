# homcloud_lammps_polymer
Machine learning converts the polymer calculation of Lammps results using lammps into descriptors using persistent homology.  
The files used in the paper are in the home folder.

## Operating Environment
We have used homcloud 2.9.0 to calculate persistent homology with python.
See the following web site to build the operationg environment.  
https://homcloud.dev/index.en.html

We used an Intel Xeon processor, Windows 10, WSL2 workstation with 64GB of memory. In particular, it consumes a lot of memory. Be careful if you recompute this result.  

Other library version is following.  
matplotlib==3.3.3  
numpy==1.19.4  
pandas==1.0.3  
plotly==5.4.0  
scikit-learn==0.23.0  
forwardable==0.4.1  
imageio==2.6.1  
Cython==0.29.14  
cached-property  
wheel  
ripser==0.4.1  
homcloud==2.9.0  
tqdm==4.46.0  
jupyter  
pymc-learn==0.0.1rc3  
pymc3==3.8  
GPy==1.9.9  
scipy==1.5.4  
Pillow==8.0.1  
arviz==0.11.0  
somoclu==1.7.5.1  

## Detailed description of files
See home folder.  
It is a jupyter format file, and persistent_vector_analysis.ipynb performs machine learning using persistent homology as a descriptor.  
Fingerprints_analysis.ipynb performs machine learning using fingerprints as descriptors for comparison.  
Persistent diagram graph is in pd_result folder.  
Persistent vector data as machine learning descriptor converted from persistent homology is in pd_vector folder.  
The graphs used in our paper are in the results folder.

## Docker container
If you are using Docker, you can build the environment by cloning this project and building a container.  
To build docker image,  
```
docker compose build  
```
and start container,  
```
docker compose up -d
```
you can use jupyter notebook at `localhost:8888` on your browser.

## Responsibility
Yohei SHIMIZU  
Graduate School of Simulation Studies, University of Hyogo, 7-1-28 Minatojima-minamimachi, Chuo-ku, Kobe, Hyogo 650-0047, Japan.

sb19x003@sim.u-hyogo.ac.jp
