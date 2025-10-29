# 在 macOS 上安裝 MateMate AI 中文版

BibleMate AI 支援 十多個 AI 供應端，如 OpenAI, Google Gemini, xAI, Groq ... 等。這頁介紹其中一個方法，既免費又可以在一般的電腦配備上安裝。

BibleMate AI 支援在 Windows 11, macOS, linux, ChromeOS, Android 上運作，基本的步驟離不開下面三個：

1. [登記 AI 供應雲端服務](https://github.com/eliranwong/biblematetc/blob/main/docs/installation/macOS.md#%E7%AC%AC%E4%B8%80%E6%AD%A5---%E7%94%B3%E8%AB%8B-google-gemini-api-keys%E5%85%8D%E8%B2%BB)（如果有好的電腦配備，可以免去這步）
2. [安裝 Python 3.8-3.12](https://github.com/eliranwong/biblematetc/blob/main/docs/installation/macOS.md#%E7%AC%AC%E4%BA%8C%E6%AD%A5---%E5%AE%89%E8%A3%9D-python)（Linux 系統一般都預設安裝了 python，或可免這步）
3. [安裝 BibleMate AI](https://github.com/eliranwong/biblematetc/blob/main/docs/installation/macOS.md#%E7%AC%AC%E4%B8%89%E6%AD%A5---%E5%AE%89%E8%A3%9D-biblemate-ai-%E4%B8%AD%E6%96%87%E7%89%88)

## 第一步 - 申請 Google Gemini API Keys（免費）

1. 開啟網站 https://aistudio.google.com ，然後選擇 `Get Started` ，並使用你個人的 Google Account 登入<img width="1281" height="461" alt="Image" src="https://github.com/user-attachments/assets/e9a54d02-c245-4331-9de2-0764e94bc561" />

2.  於左邊目錄選擇 `Get API Key`，然後在右上角選擇 `Create API Key`

<img width="1617" height="1056" alt="Image" src="https://github.com/user-attachments/assets/63d5f1ab-9ba1-4eee-a213-af58ccf73541" />

3. 先選擇 `Create Project`，例如輸入：BibleMate

<img width="512" height="329" alt="Image" src="https://github.com/user-attachments/assets/97d677d5-22c5-42b2-b9e7-f7106efcb09c" />

4. 輸入 API 名稱方便日後識別，例如輸入：BibleMate

<img width="511" height="283" alt="Image" src="https://github.com/user-attachments/assets/9ceb7476-c56c-4459-90bd-69c4b168fceb" />

5. 複製 Copy 新建立的 API Key，並按你個人方式儲存好，在第三步有用，在不要與其他人分享這個 API Key。

<img width="1043" height="263" alt="Image" src="https://github.com/user-attachments/assets/6373d1ce-f4f6-4529-899a-3d535a513f4a" />

備註：

* 可以不用理會 Billing，因為 Google 提供免費 Free Tier 使用。
* Free Tier 多用時會有 rate limit 限制，建議如果一家幾口一起使用，多用幾個不同成員的 Google Accounts 分別申請多幾個 API Keys。
* 如想切換 Google Gemini 到其他 AI 供應端，可參考 https://github.com/eliranwong/biblematetc/tree/main/docs/backends_setup

## 第二步 - 安裝 python 

1. 開啓 [https://python.org](https://python.org) ，選擇 `Downloads` -> `macOS`，切勿直接下載 3.14 版本，BibleMate AI 目前只支援 python versions 3.9-3.12
<img width="1503" height="660" alt="Image" src="https://github.com/user-attachments/assets/81f0eb85-20ea-4480-8ff5-17c0d4dac0e6" />

2. 選擇 Download [macOS 64-bit universal2 installer](https://www.python.org/ftp/python/3.12.10/python-3.12.10-macos11.pkg) 。你也可以選用其他版本，但必須是在 3.9-3.12 這範圍內。

<img width="987" height="865" alt="Image" src="https://github.com/user-attachments/assets/b3c7bcbb-da7e-4590-8d74-cce13a269605" />

3. 下載後，在你個人電腦的 Downloads 文件夾裏找出新下載檔案，然後雙擊開啓，按指示安裝

<img width="732" height="556" alt="Image" src="https://github.com/user-attachments/assets/7bed2aea-a381-4fa3-b7b9-c1582b88e3e3" />

## 第三步 - 安裝 BibleMate AI 中文版

1. 開啟 `Terminal` app （`Applications` -> `Utilities` -> `Terminal`）

<img width="1032" height="576" alt="Image" src="https://github.com/user-attachments/assets/126afe61-758e-404d-9e9f-8dccd6e9936d" />

2. 開啟後，複製 Copy 下面七行指令，在 Terminal app 貼上 Paste，按 `Enter` 鍵執行

```
cd
python3 -m venv biblematetc
source biblematetc/bin/activate
pip install --upgrade pip "biblematetc[genai]"
echo "alias bmtc='$HOME/biblematetc/bin/bmtc'" >> .zprofile
echo "alias biblemate tc='$HOME/biblematetc/bin/biblematetc'" >> .zprofile
bmtc
```

3. 允許 Terminal app 連接網絡

<img width="372" height="360" alt="Image" src="https://github.com/user-attachments/assets/667f10d0-075c-478b-a2f5-717b7decd936" />

4. 輸入在第一步申請的 Google Gemini API Key。如果不想一個個字打進去，可以把 API Key 先複製 Copy，`然後按 Command+V` 貼上 Paste 這裏（請用你有效的 API Key 取代 xxxxxxxxxxx）：

<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/ee882eae-514f-4406-95cf-a40d1fe632ac" />

5. BibleMate AI 支援輪流使用數個 API Keys（用英文逗號 `,` 隔開多個 API Keys，但不要加空格）：

<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/6520bcbf-ee7d-4727-8c1d-2fb36b7e3a69" />

6. 按下 `OK` 確定後，需要重新啓動，在 Terminal App 上輸入 `biblematetc` 或者 `bmtc` 即可。

<img width="890" height="124" alt="Image" src="https://github.com/user-attachments/assets/92332717-0011-4504-8bbc-f0b38721e63f" />

## 備註

* 所有 API Keys 只會儲存在你的個人電腦上，儲存的檔案是 `~/agentmake/agentmake.env`。
* Terminal app，預設是白底黑字，預設的字體也很小。個人建議改用黑底白字，和增加字體大小。可以在 Terminal app 的 Settings 更改。

# 使用方法

1. 在 Terminal app 輸入 `biblematetc` 或者 `bmtc` 即可進入 BibleMate AI 中文版。
2. 輸入你的要求，然後按 `Ctrl+S` 確定，讓 BibleMate AI 執行你的要求。

<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/a2f84f01-e2e4-496e-9359-b8afd5dcc583" />

## 切換不同 AI 模式

BibleMate AI 支援三種 AI 模式 - 代理，搭檔，對話 - 供使用者按需要隨時切換：

* `代理`模式 - 全自動模式，AI 執行所有步驟
* `搭檔`模式 - 半自動操作模式，使用者參與檢閱及修改
* `對話`模式 - 簡單一問一答的對話模式

1. 輸入 `.mode` 開啟 AI 模式選單：

<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/47ecf9ed-fe07-4773-91f6-1cd9a8598d41" />

2. 選擇其中一個模式

<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/13a07479-1fd9-4cac-b379-c2c16a71525b" />

3. 切換後，輸入你的要求，然後按 `Ctrl+S` 來確定

<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/1514558a-5d8e-472e-b06f-2fb72ebb96dd" />

## 支援語義搜索 Semantic Searches [Optional]

你可以通過 BibleMate AI 搜索多項聖經資料，如聖經，原文字典，百科全書，聖經應許 ... 等，但需要兩個額外的設置：

1. 在你的電腦上安裝 Ollama （BibleMate AI 使用 Ollama 建立向量資料庫） ，下載可參考 https://ollama.com/download
2. 在 BibleMate AI 輸入要求 `.download`，按指示下載附加的資料庫。

<img width="866" height="629" alt="Image" src="https://github.com/user-attachments/assets/1e8aa6b2-4c47-4fe0-9e9d-7d5163f88ea4" />

## 在不使用 AI 功能下，直接提取聖經和相關資源

BibleMate AI 預設連接[英倫福音教會](ttps://bible.gospelchurch.uk)的聖經網站 https://bible.gospelchurch.uk/traditional.html ，使用者可以隨時直接提取有關聖經的研讀資料，而不需要通過 AI 功能。

BibleMate AI 大多的功能都能通過快速鍵開啓，其中五個組合正是爲了快速開啓聖經相關資料而設計的：

`Ctrl+F` 搜索聖經資料庫 [幫助記憶：F -> Find]

<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/a5005066-029f-432f-88a2-771dddd52f8f" />

`Ctrl+B` 開啓聖經選項 [幫助記憶：B -> Bible]

<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/2016b4cc-f370-4aa1-bcd9-8b8b30f8a727" />

`Ctrl+C` 開啓聖經註釋功能 [幫助記憶：C -> Commentary]

<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/9a175b0e-7385-4aaa-9f6e-00f57ae675fa" />

`Ctrl+V` 開啓單節查考功能 [幫助記憶：V -> Verse]

<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/2089542c-573d-47f7-ae57-4704295b9417" />

`Ctrl+X` 開啓經文串珠功能 [幫助記憶：X -> Cross-references]

<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/aa2e31fb-e89c-4af8-bd5e-53e631fc12ce" />

## 更多快速鍵

`Ctrl+Y` 開啓幫助諮詢

## 更多功能介紹

中文： https://github.com/eliranwong/biblematetc

英文： https://github.com/eliranwong/biblemate