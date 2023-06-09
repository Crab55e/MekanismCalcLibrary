MekanismCalcLibrary
===================

.. figure:: https://user-images.githubusercontent.com/122292089/236683530-15675752-b36e-428e-9e9f-1a1f292853f0.png
   :alt: mknsmPy rogo


mekanismの材料計算をもっと簡単に
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|MIT License| |PyPI version|

   pip install mknsmPy

作りたいものの名前と個数を引数に代入すると材料を辞書型で返します。

・使用例

   mknsmPy.Calc(“アイテム名”, 42)

::

   {"材料1": "個数",
    "材料2": "個数",
    "材料3": "個数",
    ...}

その他質問やバグ報告など
~~~~~~~~~~~~~~~~~~~~~~~~

`コントリビュート <https://github.com/hihimamuLab/MekanismCalcLibrary/blob/main/CONTRIBUTING.md>`__

.. |MIT License| image:: http://img.shields.io/badge/license-MIT-blue.svg?style=flat
   :target: https://github.com/hihimamuLab/MekanismCalcLibrary/blob/main/LICENSE
.. |PyPI version| image:: https://badge.fury.io/py/mknsmPy.svg
   :target: https://pypi.org/project/mknsmPy/
