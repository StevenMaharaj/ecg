# A Machine Learning approach to Predict Respiratory Rates from ECGs

Author : Steven Maharaj 695281

In this this README file will outline the the structure of the ecg repository.

## Software requirements
Most of the code requires the following software
- python 3.7
- numpy
- pandas
- Scipy
- The ECG package developed in this project
- seaborn
- matplotlib

In order to run the neural Net ([NN_2.ipynb](https://github.com/StevenMaharaj/ecg/blob/master/predictions/NN_2.ipynb))
- Tensorflow 2.0 (CPU version)

In order to run the web applications ([ECG](https://github.com/StevenMaharaj/ecg/blob/master/simulate_real_ecg/fri.py) and [Resp](https://github.com/StevenMaharaj/ecg/blob/master/simulate_real_ecg/resp.py))
- plotly 
- dash

## File Structure
<pre>
.
├── A1
│   ├── Correlations.ipynb
│   ├── ECG
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── ecg.cpython-37.pyc
│   │   │   ├── ecg_sig.cpython-37.pyc
│   │   │   ├── features.cpython-37.pyc
│   │   │   ├── reading.cpython-36.pyc
│   │   │   └── reading.cpython-37.pyc
│   │   ├── a01.dat
│   │   ├── ecg.py
│   │   └── ecg_sig.py
│   ├── a01.dat
│   ├── a01r.dat
│   └── fig
│       └── heat.png
├── ECG
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── __init__.cpython-37.pyc
│   │   ├── ecg.cpython-37.pyc
│   │   ├── ecg_sig.cpython-37.pyc
│   │   ├── features.cpython-37.pyc
│   │   ├── reading.cpython-36.pyc
│   │   └── reading.cpython-37.pyc
│   ├── a01.dat
│   ├── ecg.py
│   └── ecg_sig.py
├── README.md
├── Steven_Maharaj_695281_code_task_1
│   ├── LCG.py
│   ├── __init__.py
│   ├── __pycache__
│   │   └── LCG.cpython-37.pyc
│   ├── a_test.py
│   ├── b_test.py
│   ├── d_test.py
│   ├── e_test.py
│   ├── f_test.py
│   ├── fig
│   │   ├── dice_freqency.png
│   │   └── dice_freqency_bad.png
│   ├── g_test.py
│   └── report
│       ├── Steven_maharaj_695281_code_task_1.aux
│       ├── Steven_maharaj_695281_code_task_1.log
│       ├── Steven_maharaj_695281_code_task_1.pdf
│       ├── Steven_maharaj_695281_code_task_1.synctex.gz
│       └── Steven_maharaj_695281_code_task_1.tex
├── chapter2
│   ├── ECG
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── ecg.cpython-37.pyc
│   │   │   ├── ecg_sig.cpython-37.pyc
│   │   │   ├── features.cpython-37.pyc
│   │   │   ├── reading.cpython-36.pyc
│   │   │   └── reading.cpython-37.pyc
│   │   ├── a01.dat
│   │   ├── ecg.py
│   │   └── ecg_sig.py
│   ├── a01.dat
│   ├── a01r.dat
│   ├── binaryex.py
│   ├── fftresp.py
│   ├── fig
│   │   └── sample_resp.png
│   ├── get_features.py
│   ├── sample_resp.py
│   └── table
│       └── features.csv
├── chapter4
│   ├── ECG
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── ecg.cpython-37.pyc
│   │   │   ├── ecg_sig.cpython-37.pyc
│   │   │   ├── features.cpython-37.pyc
│   │   │   ├── reading.cpython-36.pyc
│   │   │   └── reading.cpython-37.pyc
│   │   ├── a01.dat
│   │   ├── ecg.py
│   │   └── ecg_sig.py
│   ├── a01.dat
│   ├── a01r.dat
│   ├── band_pass.py
│   ├── calib.py
│   ├── fig
│   │   ├── fft.png
│   │   ├── many_sample_resp.png
│   │   └── many_sample_resp_fil.png
│   ├── fourier.py
│   ├── res_many_samples.py
│   └── res_many_samples_fil.py
├── initial_project
│   ├── ECG
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── ecg.cpython-37.pyc
│   │   │   ├── ecg_sig.cpython-37.pyc
│   │   │   ├── features.cpython-37.pyc
│   │   │   ├── reading.cpython-36.pyc
│   │   │   └── reading.cpython-37.pyc
│   │   ├── a01.dat
│   │   ├── ecg.py
│   │   └── ecg_sig.py
│   ├── Report\ 4th\ sep.ipynb
│   ├── Report\ 5th\ sep.ipynb
│   ├── Report\ sept18.ipynb
│   ├── Respirator\ Team\ _pdf_.pdf
│   ├── a01.csv
│   ├── a01.dat
│   ├── a01r.dat
│   ├── corr_custer_search
│   │   ├── ECG
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-36.pyc
│   │   │   │   ├── __init__.cpython-37.pyc
│   │   │   │   ├── ecg.cpython-37.pyc
│   │   │   │   ├── ecg_sig.cpython-37.pyc
│   │   │   │   ├── features.cpython-37.pyc
│   │   │   │   ├── reading.cpython-36.pyc
│   │   │   │   └── reading.cpython-37.pyc
│   │   │   ├── a01.dat
│   │   │   ├── ecg.py
│   │   │   └── ecg_sig.py
│   │   ├── ecg_and_res_table.py
│   │   ├── plot_cluster.py
│   │   └── plot_corr.py
│   ├── dataframe_of_features.py
│   ├── figs
│   │   └── sample_ecg.png
│   ├── filter_resp_a.py
│   ├── find_peak_scipy.py
│   ├── freq_fft.py
│   ├── learnign_hreading
│   │   ├── ay.py
│   │   └── lt.ipynb
│   ├── median_filtering.py
│   ├── my_find_peaks.py
│   ├── overlay_ecg_r.py
│   ├── plot_300_samples.py
│   ├── reada001r.py
│   ├── real_time_demo.ipynb
│   ├── report\ sept23.ipynb
│   ├── report\ sept23v2.ipynb
│   ├── report13.ipynb
│   ├── sample_ecg.png
│   └── understandbutter
│       ├── ECG
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   │   ├── __init__.cpython-36.pyc
│       │   │   ├── __init__.cpython-37.pyc
│       │   │   ├── ecg.cpython-37.pyc
│       │   │   ├── ecg_sig.cpython-37.pyc
│       │   │   ├── features.cpython-37.pyc
│       │   │   ├── reading.cpython-36.pyc
│       │   │   └── reading.cpython-37.pyc
│       │   ├── a01.dat
│       │   ├── ecg.py
│       │   └── ecg_sig.py
│       ├── a01.dat
│       ├── a01r.dat
│       ├── b2.ipynb
│       ├── butter\ with\ resp.ipynb
│       └── understandbutter.ipynb
├── out.txt
├── predictions
│   ├── 18oct.ipynb
│   ├── ECG
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── ecg.cpython-37.pyc
│   │   │   ├── ecg_sig.cpython-37.pyc
│   │   │   ├── features.cpython-37.pyc
│   │   │   ├── reading.cpython-36.pyc
│   │   │   └── reading.cpython-37.pyc
│   │   ├── a01.dat
│   │   ├── ecg.py
│   │   └── ecg_sig.py
│   ├── NN.ipynb
│   ├── NN_2.ipynb
│   ├── a01.dat
│   ├── a01r.dat
│   ├── a02.dat
│   ├── a02r.dat
│   ├── a03.dat
│   ├── a03r.dat
│   ├── a04.dat
│   ├── a04r.dat
│   ├── c01.dat
│   ├── c01r.dat
│   ├── c02.dat
│   ├── c02r.dat
│   ├── c03.dat
│   ├── c03r.dat
│   ├── fit_model.ipynb
│   ├── freq_DT_Ampli_freq.csv
│   ├── freq_DT_Ampli_freq1.csv
│   ├── freq_DT_Ampli_freq2.csv
│   ├── freq_DT_Ampli_freq3.csv
│   ├── freq_DT_Ampli_freq4.csv
│   ├── freq_DT_Ampli_freqa1.csv
│   ├── freq_DT_Ampli_freqa2.csv
│   ├── freq_DT_Ampli_freqa3.csv
│   ├── freq_DT_Ampli_freqa4.csv
│   ├── freq_DT_Ampli_label.csv
│   ├── grid_search.ipynb
│   └── perdat.ipynb
└── simulate_real_ecg
    ├── ECG
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-36.pyc
    │   │   ├── __init__.cpython-37.pyc
    │   │   ├── ecg.cpython-37.pyc
    │   │   ├── ecg_sig.cpython-37.pyc
    │   │   ├── features.cpython-37.pyc
    │   │   ├── reading.cpython-36.pyc
    │   │   └── reading.cpython-37.pyc
    │   ├── a01.dat
    │   ├── ecg.py
    │   └── ecg_sig.py
    ├── __pycache__
    │   ├── fri.cpython-37.pyc
    │   └── resp.cpython-37.pyc
    ├── a01.dat
    ├── a01r.dat
    ├── an.py
    ├── ecg_sim.py
    ├── ecg_sim2.py
    ├── fig
    │   ├── ECGapp.png
    │   └── respapp.png
    ├── fri.py
    ├── fri5.ipynb
    ├── live_updates.py
    ├── live_updates_graph.py
    ├── live_updates_graph2.py
    ├── resp.py
    └── sendextut.py

38 directories, 217 files
</pre>
 
## Import Directories

- 


 