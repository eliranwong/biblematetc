# 🏃 操作選單

| 命令 | 描述 |
|---|---|
| `.new` | 新對話 |
| `.exit` | 退出 BibleMate AI |
| `.backend` | 更改後端 |
| `.mode` | 更改 AI 模式 |
| `.tools` | 列出可用工具 |
| `.plans` | 列出可用計畫 |
| `.resources` | 列出可用資源 |
| `.editprompt` | 編輯當前提示 |
| `.backup` | 備份對話 |
| `.reload` | 重新載入當前對話 |
| `.edit` | 編輯當前對話 |
| `.trim` | 修剪當前對話 |
| `.import` | 匯入對話 |
| `.export` | 匯出對話 |
| `.find` | 搜尋對話 |
| `.content` | 顯示當前目錄內容 |
| `.open` | 開啟檔案或目錄 |
| `.ideas` | 產生想法 |
| `.autotool` | 切換自動工具選擇 |
| `.autosuggest` | 切換自動輸入建議 |
| `.autoprompt` | 切換自動提示工程 |
| `.light` | 切換輕量級上下文 |
| `.steps` | 設定最大步驟數 |
| `.matches` | 設定最大語意符合數 |
| `.download` | 下載資料檔案 |
| `.help` | 顯示說明頁面 |

有些指令設計用於從 UniqueBible App 檢索內容：

| 命令 | 描述 |
|---|---|
| `.bible` | 開啟聖經經文 |
| `.chapter` | 開啟聖經章節 |
| `.compare` | 比較聖經經文 |
| `.comparechapter` | 比較聖經章節 |
| `.chronology` | 開啟聖經年代表 |
| `.commentary` | 開啟註釋 |
| `.aicommentary` | 開啟 AI 註釋 |
| `.index` | 開啟經文研究索引 |
| `.translation` | 開啟經文分析和翻譯 |
| `.discourse` | 開啟語篇分析 |
| `.morphology` | 開啟形態學資料 |
| `.xref` | 開啟串珠 |
| `.treasury` | 開啟 TSKE |
| `.search` | 搜尋聖經 |
| `.parallel` | 搜尋聖經平行經文 |
| `.promise` | 搜尋聖經應許 |
| `.dictionary` | 搜尋辭典 |
| `.encyclopedia` | 搜尋百科全書 |
| `.lexicon` | 搜尋原文辭典 |
| `.topic` | 搜尋聖經主題 |
| `.name` | 搜尋聖經名稱 |
| `.character` | 搜尋聖經人物 |
| `.locations` | 搜尋聖經地點 |

快捷鍵 `Ctrl+B`、`Ctrl+C`、`Ctrl+V` 和 `Ctrl+X` 設計用於在 BibleMate AI 中開啟 UBA 內容 [[閱讀](https://github.com/eliranwong/biblemate#%EF%B8%8F-keyboard-shortcuts)]。

## 備註：

* 輸入 `.` 開啟操作選單以選擇操作。
* 使用 `.light` 啟用或停用*輕量級上下文*。當*輕量級上下文*啟用時（預設），BibleMate 執行速度稍快，工具回應品質略有犧牲。當*輕量級上下文*停用時，將使用完整上下文，這會消耗更多權杖進行處理，但提供更高的回應品質。
* 若要使用 `.import`，您需要指定一個包含已儲存對話的 python 檔案。每次執行備份時，對話都會儲存到一個檔案中。請檢查訊息 `Conversation backup saved to ...` 或在 `~/agentmake/computemate` 中找到備份。除了僅載入對話，您還可以同時載入對話及其主要計畫。為此，請指定一個包含 `conversation.py` 和 `master_plan.md` 的備份目錄路徑。
* 若要使用 `.open`，您需要指定要開啟的檔案或目錄。
* `.edit` 指令可讓您使用我們內建的文字編輯器編輯當前對話。您可以自訂以使用您喜歡的文字編輯器。輸入 `.backend` 並使用呼叫您喜歡的文字編輯器的指令變更 `DEFAULT_TEXT_EDITOR` 的值。
* 使用 `.autosuggest` 切換自動輸入建議。如果停用，您可以使用 `TAB` 鍵開啟輸入建議選單。
* 使用 `.reload` 重新載入上次儲存的對話（如果有的話）。這對於在對話因任何原因中斷後繼續未完成的代理流程很有用。
* 指令 `.matches` 僅適用於本機 MCP 連線。它不適用於遠端 MCP 連線，因為本機設定的變更不會影響遠端伺服器中的設定。
* 當 `.` 後面的內容與上面列出的操作指令不符時，請以 `.` 開頭您的請求以直接檢索聖經經文或章節，或執行聖經搜尋。例如：
    - 輸入 `.John 3:16` 閱讀約翰福音 3:16
    - 輸入 `.John 3:16; Rm 5:8` 閱讀約翰福音 3:16 和羅馬書 5:8
    - 輸入 `.John 3` 閱讀約翰福音第 3 章
    - 輸入 `.John 3, 4` 閱讀約翰福音第 3 章和第 4 章
    - 輸入 `.Jesus love` 執行 `耶穌 愛` 的聖經搜尋
