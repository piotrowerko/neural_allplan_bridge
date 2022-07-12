import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm

class ResponseGen():
    def __init__(self, label) -> None:
        self.name = label
    
    def __str__(self) -> str:
        return f'bridge class label: {self.name}'
    
    def numpy_eigen_res_single(self, path):
        """returns numpy array with 
        eigen results from one, selected bridge model"""
        df = pd.read_excel(path,
                           #index_col=1,
                           usecols="C:D",
                           skiprows=(0,1,2))
        return df.to_numpy()
    
    def agregate_n_th_freq(self, 
                           start_par=-25,
                           end_par=25, 
                           step=1,
                           freq_no=1,
                           source_path=''):
        """returns np array with 
        skew angles and according n-th freq. res."""
        __range = list(range(start_par, end_par+1, step))
        model_no = np.asarray(__range)
        freq_agregated = np.array([])
        
        for i in __range:
            file_name = f'EIGEN{i}.xlsx'
            path = os.path.join(source_path, file_name)
            freq_single = self.numpy_eigen_res_single(path)[freq_no-1][0]
            freq_agregated = np.append(freq_agregated, [freq_single])
        return model_no, freq_agregated
        

def main():
    source_path = 'C:/Python/git_projects/neural_allplan_bridge/eigen_res'
    model_1 = ResponseGen('double_gird_pt_bridges')
    
    model_no, freq_agregated = model_1.agregate_n_th_freq(freq_no=1,
                                                          source_path=source_path)
    model_no, freq_agregated2 = model_1.agregate_n_th_freq(freq_no=2,
                                                          source_path=source_path)
    print(len(freq_agregated)) 
    
    fig0, ax0 = plt.subplots()
    fig0.set_size_inches(9, 6)
    ax0.plot(model_no, freq_agregated, label='freq1_vs_skew_angle')
    ax0.plot(model_no, freq_agregated2, label='freq2_vs_skew_angle')
    ax0.xaxis.grid(True, which='major')
    ax0.yaxis.grid(True, which='major')
    ax0.set_xlabel('Skew [deg]', fontsize=15)
    ax0.set_ylabel('Freq. [Hz]', fontsize=15)
    ax0.tick_params(labelsize=15)
    plt.show()
    

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # surf = ax.plot_wireframe(model_no, freq_agregated, freq_agregated2, cmap=cm.jet, linewidth=0)
    #cset = ax.contour(model_no, freq_agregated, freq_agregated2, cmap=cm.coolwarm)
    ppp = ax.scatter(model_no, freq_agregated, freq_agregated2)
    #surf = ax.plot_trisurf(model_no, freq_agregated, freq_agregated2, cmap=cm.jet, linewidth=0)
    #fig.colorbar(surf)
    ax.view_init(30, 20)
    plt.show()

if __name__ == '__main__':
    main()
