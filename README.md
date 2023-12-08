<a href='https://github.com/Junwu0615/LCII-Rec-Model'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/LCII-Rec-Model.svg'> 
<a href='https://github.com/Junwu0615/LCII-Rec-Model'><img alt='GitHub Clones' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/7f654406c51d568d31d565347f22d609/raw/LCII-Rec-Model_clone.json&logo=github'> </br>
[![](https://img.shields.io/badge/Project-RecommendationSystem-blue.svg?style=plastic)](https://pse.is/5jtztg) 
[![](https://img.shields.io/badge/Project-Tensorflow_1.14.0-blue.svg?style=plastic)](https://pypi.org/project/tensorflow/) 
[![](https://img.shields.io/badge/Language-Python_3.7.16-blue.svg?style=plastic)](https://www.python.org/) </br>
[![](https://img.shields.io/badge/Package-Numpy_1.21.6-green.svg?style=plastic)](https://pypi.org/project/numpy/) 
[![](https://img.shields.io/badge/Package-Pandas_1.3.5-green.svg?style=plastic)](https://pypi.org/project/pandas/) 
[![](https://img.shields.io/badge/Package-Matplotlib_3.5.3-green.svg?style=plastic)](https://pypi.org/project/matplotlib/) 
[![](https://img.shields.io/badge/Model-LCII_v1.1-red.svg?style=plastic)](https://github.com/Junwu0615/LCII-Rec-Model) 
[![](https://img.shields.io/badge/Model-II_RNN-red.svg?style=plastic)](https://github.com/olesls/master_thesis) 

## 歷史紀錄
| 事件 | 敘述 | 時間 |
| :--: | :-- | :--: |
| 碩論完成 | 推薦系統模型 : [LCII-Rec-Model](https://pse.is/5jtztg) | 2023/01/19 |
| LCII v1.0 | 第一次將程式碼發布於 GitHub | 2023/12/09 |
| LCII v1.1 | 如何建立 TF1.14.0 版本環境安裝說明，以及精簡程式碼 | 2024/01/21 |

</br>

## HOW TO USE
### STEP.1　CREATE ENVIRONMENT
本論文程式碼是建立於 Tensorflow 1.14.0 版本，但該版本已被淘汰...最終我找到安裝舊有版本的方式，讓架構不至於需要重構...
- 當初程式是在 Anaconda 環境下完成，因此我也將可運行之環境匯出成 yaml 檔。
  - 由於我更換電腦，顯卡從 N 卡變 A 卡，對於要運行 ML 的我來說非常不便...懊悔中，差異在於其中 Tensorflow 套件是用 CPU 運行，而不是 GPU 版本。
  - `conda env create -f C:\Users\xxx\LCII-Rec-Model\environment.yaml` (自己設路徑安裝環境檔)
- Tensorflow 1.14.0 版本安裝指令如下所示，根據需求自行安裝。
  - N 卡安裝 TF-GPU 環境網路教學很多，這邊不多贅述。
  - `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow==1.14.0`
  - `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorflow-gpu==1.14.0`

</br>

### STEP.2　CLONE 

```code
git clone https://github.com/Junwu0615/LCII-Rec-Model.git
```
跳至 **LCII-Rec-Model** 專案目錄 : `cd LCII-Rec-Model`

</br>

### STEP.3　DOWNLOADS DATASETS

跳至 **preprocess** 目錄 : `cd preprocess`</br>
#注意: Amazon's Clothing Shoes and Jewelry 資料集 2012-2014 已被取消發布，現階段版本為 2018，而本論文使用的是 2012-2014 版本。

#### 資料集來源如下所示　|　可於頁面中搜尋關鍵字 :
[Amazon](https://nijianmo.github.io/amazon/index.html) :　`Clothing Shoes and Jewelry | 32,292,099 reviews`</br>
[MovieLens-1M](https://grouplens.org/datasets/movielens/) :　`ml-1m.zip | 6 MB`</br>
[Steam](https://cseweb.ucsd.edu/~jmcauley/datasets.html#steam_data) :　`Version 2: Review Data | 1.3 GB`

#### 下載資料集並解壓縮到指定位置，如表所示 :
| Dataset | Path |
| :-- | :-- |
| Amazon | 需將 `Clothing_Shoes_and_Jewelry.json.gz` 放置於 `LCII-Rec-Model/datasets`</br>解壓縮完路徑為: `LCII-Rec-Model/datasets/Clothing_Shoes_and_Jewelry.json` |
| MovieLens-1M | 需將 `ml-1m.zip` 放置於 `LCII-Rec-Model/datasets`</br>解壓縮完路徑為: `LCII-Rec-Model/datasets/ml-1m` |
| Steam | 需將 `steam_reviews.json.gz` 放置於 `LCII-Rec-Model/datasets`</br>解壓縮完路徑為: `LCII-Rec-Model/datasets/steam_new.json` |

Amazon 資料集需先進行處理
- 由於 Json 檔案過於龐大，我將它額外地拉出來做格式轉換，最終會輸出成 cvs 檔，指令如下:
  ```
  python amazon_clothing_shoes_and_jewelry_json_to_csv.py
  ```
  ![amazon.gif](/sample_gif/amazon.gif)

</br>

### STEP.4　PREPROCESS

#### 資料預處理指令
| Dataset | Program Instructions |
| :-- | :-- |
| Amazon | `python amazon_preprocess.py -d Amazon` |
| Amazon ver. BERT4Rec | `python amazon_preprocess_ver_bert4rec.py` |
| MovieLens-1M | `python ml_steam_preprocess.py -d MovieLens-1M` |
| Steam | `python ml_steam_preprocess.py -d Steam` |

![preprocess_ml-1m.gif](/sample_gif/preprocess_ml-1m.gif)

#### 查閱預處理後之資料
| Dataset | Program Instructions |
| :-- | :-- |
| Amazon | `python see_pickle_amazon.py` |
| MovieLens-1M | `python see_pickle_ml_steam.py -d MovieLens-1M` |
| Steam | `python see_pickle_ml_steam.py -d Steam` |

![see_ml-1m.gif](/sample_gif/see_ml-1m.gif)

</br>

### STEP.5　HELP
回到 **LCII-Rec-Model** 專案目錄 `cd ..`
```
python LCII-Rec-Model.py -h
```
 - `-d`　Dataset :　`Amazon` / `MovieLens-1M` / `Steam`
 - `-sp`　Switch Plot :　`sum` / `dot` / `attention_gate_sum` / `attention_gate_dot`
 - `-sis`　Switch Initial State :　`True` / `False`
 - `-fw`　Fusion Way :　`att` / `lp` / `fix` / `none`
 - `-s`　Strategy :　`pre-combine` / `post-combine` / `original`
 - `-w`　Window :　`0-100` / `'no_use'`
 - `-ls`　Long Score :　`0.0-1.0` / `'no_use'`
 - `-ss`　Short Score :　`0.0-1.0` / `'no_use'`
 - `-es`　Embedding Size :　`30` / `50` / `80` / `100` / `200` / `300` / `500` / `800` / `1000`
 - `-bs`　Batch Size :　`16` / `32` / `64` / `100` / `128` / `256` / `512`
 - `-lr`　Learning Rate :　`0.001` / `0.01` / ...
 - `-dr`　Dropout :　`0.8`
 - `-me`　Max Epoch :　`100` / `200` / ...
 - `-t`　Threshold :　`98`
 - `-add`　Whether to finally add FC to input_sum :　`True` / `False`<br/>

</br>

### STEP.6　RUN MAIN PROGRAM
下列為 LCII 模型在各資料集中的程式運行之指令範例，執行完畢後會在 `/testlog/` 產出實驗結果 ( .txt / .png )。

Amazon
```Python
python LCII-Rec-Model.py -d Amazon -sp attention_gate_dot -sis True -fw none -s original -w 'no_use' -ls 'no_use' -ss 'no_use' -es 80 -bs 100 -lr 0.001 -dr 0.8 -me 100 -t 98 -add False
```

MovieLens-1M
```Python
python LCII-Rec-Model.py -d MovieLens-1M -sp attention_gate_dot -sis True -fw fix -s pre-combine -w 30 -ls 0.8 -ss 0.2 -es 80 -bs 100 -lr 0.01 -dr 0.8 -me 200 -t 98 -add False
```

Steam
```Python
python LCII-Rec-Model.py -d Steam -sp attention_gate_dot -sis True -fw fix -s post-combine -w 4 -ls 0.2 -ss 0.8 -es 80 -bs 100 -lr 0.001 -dr 0.8 -me 200 -t 98 -add False
```
</br>

下列為相關 Baseline
- [II-RNN](https://github.com/olesls/master_thesis)
- [BERT4Rec](https://github.com/theeluwin/session-aware-bert4rec)
- most-recent / most-pop / kNN
  - 跳至 **baseline** 目錄 : `cd baseline`</br>
  - 需要自行做資料集的設定切換
  ```Python
  from baseline_utils_v1 import PlainRNNDataHandler # amazon
  #from baseline_utils_v2 import PlainRNNDataHandler # ml-1m steam
  from baseline_test_util import Tester

  amazon = "amazon"
  MovieLens_1M = 'ml-1m'
  steam = 'steam'

  ### Choose dataset here
  dataset = MovieLens_1M
  ```
  - 執行指令如下 :
  ```Python
  python Baseline.py
  ```
