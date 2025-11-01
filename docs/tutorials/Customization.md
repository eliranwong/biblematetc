# 🛠️ 自訂

BibleMate AI 具有高度可自訂性。進階使用者可以修改現有工具、建立新工具，甚至透過自訂系統提示來改變 AI 代理的行為。

自訂檔案放置在 AgentMake 使用者目錄中的 `biblemate` 子目錄中（在 Linux/macOS 上通常是 `~/.agentmake/biblemate`，在 Windows 上是 `%USERPROFILE%\.agentmake\biblemate`）。

## 主要設定檔

主要設定儲存在以下檔案中：

`~/.agentmake/biblemate/biblematetc.config` (在 Linux/macOS 上)

`%USERPROFILE%\.agentmake\biblemate\biblematetc.config` (在 Windows 上)

您可以手動編輯此檔案以更改某些設定。

例如，您可以透過更改此檔案中 `color_agent_mode` 和 `color_partner_mode` 的值來自訂代理和夥伴模式的邊框顏色。

## 常用提示和計畫

您可以儲存、搜尋、開啟或刪除常用提示和計畫。

例如：

* 輸入提示並使用 `Ctrl+W` 儲存提示。
* 在提示前加上 `@@` 並使用 `Ctrl+W` 儲存提示。
* 使用 `Esc+W` 刪除已儲存的提示/計畫。
* 使用 `Ctrl+L` 開啟提示/計畫。
* 使用 `Esc+L` 搜尋提示/計畫。

## 覆寫系統提示

代理的核心邏輯由系統提示（markdown 檔案）引導。您可以透過將自己的版本放置在 `~/.agentmake/systems/biblematetc/` 中來覆寫它們。

可自訂的系統提示檔案是：`supervisor.md`、`tool_instruction.md` 和 `tool_selection.md`。您可以將它們從套件安裝資料夾中的 `biblematetc/systems` 目錄複製到您的使用者目錄並根據需要進行修改。

## 新增或修改工具和計畫

您可以透過建立自訂的 `bible_study_mcp.py` 檔案來新增自己的工具和內建計畫（提示）。

1. 首先，找到 `biblematetc` 套件安裝目錄中的內建 `bible_study_mcp.py` 檔案。
2. 將此檔案複製到您的使用者自訂目錄 `~/.agentmake/biblematetc/bible_study_mcp.py`。
3. 現在您可以編輯此檔案，使用 `fastmcp` 語法新增或修改工具和提示。BibleMate AI 將自動載入您的自訂檔案而不是內建檔案。

## 使用 http 作為傳輸而不是 stdio

BibleMate 使用 `stdio` 作為與 BibleMate MCP 伺服器互動的預設傳輸。您可以改用 `http`。

在一個執行緒中運行：

> biblematemcp

在另一個執行緒中運行：

> biblemate -mcp biblemate

## 使用本地聖經資料

閱讀 [此處](https://github.com/eliranwong/biblematetc/issues/15#issuecomment-3314130281) 以獲取更多詳細資訊。

## 使用自訂 MCP 伺服器

您可以透過 CLI 選項 `mcp` 使用自訂 MCP 伺服器，例如：

> biblemate -mcp http://127.0.0.1:33333/mcp

## 託管或運行 BibleMate MCP 伺服器

使用預設埠 `33333`：

> biblematemcp

預設埠可以在設定檔 `config.py` 中編輯。

要暫時覆寫預設埠，例如：

> biblematemcp -p 33334
