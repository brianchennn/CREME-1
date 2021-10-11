# CREME: A toolchain of automatic dataset collection for machine learning in intrusion detection

<!-- ABOUT THE PROJECT -->
## About The Project

This project is a part of "CREME: A toolchain of automatic dataset collection for machine learning in intrusion detection" paper.

### Built With

* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com)
* [Drain](https://github.com/logpai/logparser/tree/master/logparser/Drain)
* [Expect](https://linux.die.net/man/1/expect)

<!-- GETTING STARTED -->
## Getting Started

For the first trial version, please refer to the document [here](https://drive.google.com/drive/folders/1YgQs4MJjuBBz8sdJkAw_0OIyy3_d5gsL?usp=sharing)


<!-- Dataset -->
## Dataset

The dataset can be found at [here](https://drive.google.com/drive/folders/1bEsx64H2vogJKgI_OTVQ8n71VahtLxz5?usp=sharing)

## 9/30 meeting進度
- FirstStage 新增了 unix/ftp/proftpd_modcopy_exec 這個 exploit 。
- 前端的FristStage新增選項讓使用者選擇。

### 困境
- FirstStage目前還是分成7個，只是code長一樣，因為不知道改CREME的路徑會發生什麼錯誤。
- 目前用if else去判斷是用哪個App exploit，再決定用哪個privilege escalation的exploit，我認為這應該被優化。

