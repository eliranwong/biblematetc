# 🧠 支援的 AI 後端

由 AgentMake AI 驅動，BibleMate AI 讓使用者可以靈活使用各種 AI 後端。更多資訊請參閱 https://github.com/eliranwong/agentmake#supported-backends

為了比較，我們在下面的測試中使用相同的主題「深入研究耶利米哀歌 3:22-24」測試了一些支援的後端：

BibleMate AI + `Azure + ChatGPT 5` https://youtu.be/QvPIyHOhrP0

BibleMate AI + `Gemini API + Gemini 2.5 Flash` https://youtu.be/AZ-zEl_StC0

BibleMate AI + `Mistral Large` https://youtu.be/7sBfj2TMoOE

BibleMate AI + `DeepSeek 3.1` https://youtu.be/FUr--ULDCZM

BibleMate AI + `Groq + GPT-OSS 120B` https://youtu.be/7sBfj2TMoOE

BibleMate AI + `Groq + Llama 3.3 70B` https://youtu.be/oKQyIEnMM8M

BibleMate AI + `XAI + Grok 4` https://youtu.be/JgcxciOc_Ys

## 後端設定範例

更多詳細資訊請參閱 https://github.com/eliranwong/biblematetc/tree/main/docs/backends_setup。

## 提示

為了快速上手，我們建議從 `googleai` 後端開始，該後端已與 BibleMate AI 進行了廣泛的測試。您可以免費獲取 Gemini API 金鑰。更多資訊，請瀏覽：[https://github.com/eliranwong/biblematetc/blob/main/docs/backends_setup/googleai.md](https://github.com/eliranwong/biblematetc/blob/main/docs/backends_setup/googleai.md)。

# ⚙️ 設定 AI 後端

啟動 BibleMate AI 後，輸入：

> .backend

將會開啟一個文字編輯器，讓您編輯 AgentMake AI 設定。將 `DEFAULT_AI_BACKEND` 變更為您選擇的 AI 後端，並在適當的位置輸入 API 金鑰。

您可以使用 CLI 選項 `-b` 或 `--backend` 暫時覆寫預設的 AI 後端。例如：

> biblematetc -b googleai

## 設定 UBA API [可選]

您可以選擇性地透過編輯以下項目來設定 UBA API 後端：

```
# Tool: UBA API
UBA_API_LOCAL_PORT=8080
UBA_API_ENDPOINT="https://bible.gospelchurch.uk/plain"
UBA_API_TIMEOUT=10
UBA_API_PRIVATE_KEY=
```

## 設定遠端 MCP 伺服器驗證 [可選]

您可以選擇性地透過編輯以下項目來設定遠端 MCP 伺服器的驗證資訊：

```
# BibleMate AI
BIBLEMATE_STATIC_TOKEN=
BIBLEMATE_MCP_PUBLIC_KEY=
BIBLEMATE_MCP_PRIVATE_KEY=
BIBLEMATE_MCP_ISSUER=
BIBLEMATE_MCP_AUDIENCE=
```

## 更多範例

請在 https://github.com/eliranwong/biblematetc/tree/main/docs/backends_setup 查看個別範例
