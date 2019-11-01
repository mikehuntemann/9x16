
# 9x16: Verticality and the Paradigm of Mobile Video

Run `phyton aggregator.py` to get one document out of the folder structure for each chapter.

Currently you have to manually include the YAML meta block into the header of the generated `collections.md` file.

```
title: "9x16: Verticality and the Paradigm of Mobile Video"
author: Mike Huntemann
date: "2019"
subject: "Research"
keywords: [Markdown, Example]
subtitle: "This can be the subtitle for the cover."
lang: "en"
```  

Use ```pandoc exports/collection.md -o exports/collection.pdf --from markdown --template eisvogel``` to generate the final PDF from the source.

You can also add the `-V book` flag for book printing PDFs.