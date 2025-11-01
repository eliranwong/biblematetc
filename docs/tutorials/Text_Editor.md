# ✒️ 內建文字編輯器

<img width="866" height="629" alt="Image" src="https://github.com/user-attachments/assets/d62658d0-10df-4e56-8de3-58787600327f" />

您可以透過在 BibleMate AI 提示欄位中輸入 `.editprompt` 或按下 `Ctrl+O` 來使用我們的內建文字編輯器編輯當前提示。

您也可以單獨執行 `etextedit` 來啟動內建編輯器。

您可以在我們的內建文字編輯器 `etextedit` 中使用以 BibleMate AI 和 AgentMake AI 建構的外掛程式。

BibleMate AI 隨附安裝了外掛程式 `Extract Bible References` 和 `Insert Bible Text`。

您也可以新增自己的 `etextedit` 外掛程式並將它們放置在 `~/etextedit/plugins` 中。

閱讀更多關於 `etextedit` 的資訊：https://github.com/eliranwong/etextedit

# 匯出為 DOCX 或 PDF [選用]

`etextedit` 提供將內容匯出為 DOCX 和 PDF 檔案的選項。

- 匯出內容為 DOCX 格式需要 `pandoc`。例如，在 Debian/Ubuntu 上安裝：

> sudo apt install pandoc

- 匯出內容為 PDF 格式需要 `pdflatex`。例如，在 Debian/Ubuntu 上安裝：

> sudo apt install texlive-full

# 第三方文字編輯器 [選用]

您可以使用自己選擇的第三方文字編輯器。在 BibleMate AI 提示中輸入 `.backend` 並將 `DEFAULT_TEXT_EDITOR` 的值指定為呼叫您喜歡的文字編輯器的命令，例如 `micro -softwrap true -wordwrap true`。若要使用內建文字編輯器 `etextedit` 進行更改，您只需一個步驟，即儲存 `Ctrl+S` 或退出 `Ctrl+Q`，即可返回 BibleMate AI 提示。然而，對於第三方文字編輯器，您需要在退出前先儲存更改。
