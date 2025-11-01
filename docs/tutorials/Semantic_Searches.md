# 🔎 語意搜尋 [選用]

若要啟用語意搜尋，您需要兩件事：

1. 安裝 Ollama - BibleMate AI 使用 `Ollama` 來生成語意搜尋的嵌入。您可以在 https://ollama.com/ 找到說明。
2. 下載一些資料檔案。在 BibleMate AI 提示中輸入 `.download` 並按照彈出對話框下載它們。

<img width="510" height="326" alt="Image" src="https://github.com/user-attachments/assets/ee05517f-1d48-47d1-85e8-5c134a646e03" />

您也可以手動下載檔案，解壓縮，並將它們放置在 `~/agentmake/biblematetc/data` 目錄中，其中 `~` 代表使用者的主目錄：

[bible.db](https://drive.google.com/file/d/1E6pDKfjUMhmMWjjazrg5ZcpH1RBD8qgW/view?usp=sharing)

範例：

> @search_the_whole_bible 神創造

> //john/KJV/耶穌 愛

[collection.db](https://drive.google.com/file/d/1y4txzRzXTBty0aYfFgkWfz5qlHERrA17/view?usp=sharing)

範例：

> //promise/希望

> //parallel/洗禮

[dictionary.db](https://drive.google.com/file/d/1UxDKGEQa7UEIJ6Ggknx13Yt8XNvo3Ld3/view?usp=sharing)

範例：

> //dictionary/以色列

[encyclopedia.db](https://drive.google.com/file/d/1NLUBepvFd9UDxoGQyQ-IohmySjjeis2-/view?usp=sharing)

範例：

> //encyclopedia/耶穌

> //encyclopedia/ISB/耶穌

[exlb.db](https://drive.google.com/file/d/1Hpo6iLSh5KzgR6IZ-c7KuML--A3nmP1-/view?usp=sharing)

範例：

> //topic/希望

> //name/伯利恆

> //character/撒母耳

> //location/耶路撒冷
