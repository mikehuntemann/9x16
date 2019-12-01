
# 9x16: Verticality and the Paradigm of Mobile Video

Run `phyton aggregator.py` to get one document out of the folder structure for each chapter.

Currently you have to manually include the YAML meta block into the header of the generated `collections.md` file.

```
---
author: Mike Huntemann
title: "9x16: Verticality and the Paradigm of Mobile Video"
subtitle: "An Exploratory Research about the Internet, Platforms and Approaches"
date: "2019"
lang: "en"
titlepage: true
titlepage-rule-color: "FFFFFF"
titlepage-text-color: "000000"
link-citations: yes
linkcolor: blue
...
```  

Then replace ```(/assets``` with full file path.

Use ```pandoc exports/collection.md -o exports/collection.pdf --from markdown --template eisvogel``` to generate the final PDF from the source.

You can also add the `-V book` flag for book printing PDFs.