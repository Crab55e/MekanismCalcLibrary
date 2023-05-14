# Contribution Guide

このツールへのコントリビュート方法についてガイドです。

## Issues

次のIssueを受け付けています。

- ツールに対する質問 => [こちらから質問できます](https://github.com/hihimamuLab/MekanismCalcLibrary/issues/new?template=question.md)
- ツールのエラーやバグの報告 => [こちらからバグ報告できます](https://github.com/hihimamuLab/MekanismCalcLibrary/issues/new?template=bug.md)
- ツールの改善を提案 => [こちらから提案できます](https://github.com/hihimamuLab/MekanismCalcLibrary/issues/new?template=improvement.md)
- 新しいトピックなどの提案 => [こちらから提案できます](https://github.com/hihimamuLab/MekanismCalcLibrary/issues/new?template=feature.md)

[その他のIssue](https://github.com/hihimamuLab/MekanismCalcLibrary/issues/new?template=other.md)も歓迎しています。

## Pull Request

Pull Requestはいつでも歓迎しています。

**受け入れるPull Request**

次の種類のPull Requestを受け付けています。
基本的なPull Request（特に細かいもの）は、Issueを立てずにPull Requestを送ってもらって問題ありません。

「このような修正/改善はどうでしょう？」という疑問がある場合は、Issueを立てて相談してください。

- 誤字の修正
- サンプルコードやスペルの修正
- 別の説明方法の提案や修正
- 文章をわかりやすくするように改善

**受け入れていないPull Request**

- [CODE OF CONDUCT](./CODE_OF_CONDUCT.md)に反する内容を含むもの

## 修正の送り方

文章の誤字の修正程度なら、直接GitHub上で編集してPull Requestを送ってください。



## ディレクトリ構造
root(MekanismCalcLibrary)以下にファイルおよびフォルダを配置しています

```
MekanismCalcLibrary
  ┣.github/
  ┃    ┃
  ┃    ┣ISSUE_TEMPLATE/
  ┃    ┃    ┣issues_bug.md 
  ┃    ┃    ┣issues_feature.md
  ┃    ┃    ┣issues_improvement.md
  ┃    ┃    ┣issues_other.md
  ┃    ┃    ┗issues_questiong.md
  ┃    ┃
  ┃    ┗workflows/
  ┃　　　    ┗pypi_release.yml
  ┃
  ┣mekanismPy/
  ┃    ┣__init__.py
  ┃    ┣calc.py
  ┃    ┣item_lib.py
  ┃    ┗mb_materials.py
  ┃
  ┣.gitignore
  ┣CODE_OF_CONDUCT.md
  ┣CONTRIBUTING.md
  ┣LICENSE
  ┣README.md
  ┣README.rst
  ┗setup.py
```

