### 設定虛擬環境

例如：

```
cd
python3 -m venv biblematetc
source biblematetc/bin/activate
pip install --upgrade pip biblematetc
export PATH=$PATH:$HOME/biblematetc/bin
echo "export PATH=$PATH:$HOME/biblematetc/bin" >> ~/.bashrc
biblematetc
```

### Vertex AI 整合支援

由於某些裝置上可能存在相容性問題，因此 `google-genai` 函式庫會作為單獨的安裝提供。

若要將 Vertex AI 與 BibleMate AI 搭配使用，請安裝必要的函式庫：

> pip install --upgrade "biblematetc[genai]"

### 升級

再次執行：

> pip install --upgrade biblematetc

### 開發者適用

> pip install -e .
