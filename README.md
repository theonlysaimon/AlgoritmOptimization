# AlgoritmOptimization

1. Установите необходимы библиотеки с помщью pip:

+ json
+ string
+ os 
+ setuptools
+ Cython
+ nltk
+ string
+ re
+ ymystem3

2. После успешной установки файлов на свой ПК, 
необходимо переименовать файл test.pyx -> test_module.pyx
3. Теперь заходим в файл setup.py открываем терминал и теперь вводим команду
python setup.py build_ext --inplace. 
4. Теперь файл, который был переименован в test_module.pyx должем 
быть перименован в test.pyx.
5. Теперь смело можно запускать файл main_cython.py.
