# ✝️ UniqueBible 資源

我們在 BibleMate AI 中匯集了兩者的優點，以增強您的聖經學習。除了動態 AI 工具，我們還透過 BibleMate AI 提示整合了對大多數 [UniqueBible 資源](https://github.com/eliranwong/UniqueBible) 的直接存取。在與 AI 代理的對話中，您可以隨時將 UniqueBible App 資料直接納入討論，以豐富學習流程和內容。

在 BibleMate AI 提示中輸入 `.resources` 以查看可用資源。可用 UniqueBible 資源的數量取決於您在後端設定中配置的 [UniqueBible 網路伺服器](https://github.com/eliranwong/UniqueBible)。預設情況下，BibleMate AI 使用運行在 https://bible.gospelchurch.uk 的 UniqueBible 網路伺服器。UniqueBible 伺服器高度可自訂；您可以設定一個帶有自訂資源的本地伺服器以與 BibleMate AI 一起使用。

要將 BibleMate AI 與您的本地伺服器連接，請在 BibleMate AI 提示中輸入 `.backend`，找到下面的會話，並填寫您的本地伺服器詳細資訊：

```
# 工具：UBA API
UBA_API_LOCAL_PORT=8080
UBA_API_ENDPOINT="http://127.0.0.1:8080/plain"
UBA_API_TIMEOUT=10
UBA_API_PRIVATE_KEY=
```

提示：以 `//` 開頭您的提示，以從輸入建議中查看可用資源。

# 鍵盤快捷鍵

UniqueBible App 的大多數資源都可以透過熱鍵存取：

`Ctrl+B` 開啟聖經選項 [助記符：B -> Bible]
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/2016b4cc-f370-4aa1-bcd9-8b8b30f8a727" />

`Ctrl+C` 開啟聖經註釋功能 [助記符：C -> Commentary]
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/9a175b0e-7385-4aaa-9f6e-00f57ae675fa" />

`Ctrl+V` 開啟單節經文學習功能 [助記符：V -> Verse]
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/2089542c-573d-47f7-ae57-4704295b9417" />

`Ctrl+X` 開啟串珠功能 [助記符：X -> Cross-references]
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/aa2e31fb-e89c-4af8-bd5e-53e631fc12ce" />

`Ctrl+F` 搜尋聖經資料庫 [助記符：F -> Find]。此功能需要額外設定，請參閱 https://github.com/eliranwong/biblematetc/blob/main/docs/installation/macOS.md#%E6%94%AF%E6%8F%B4%E8%AA%9E%E7%BE%A9%E6%90%9C%E7%B4%A2-semantic-searches-optional
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/a5005066-029f-432f-88a2-771dddd52f8f" />
