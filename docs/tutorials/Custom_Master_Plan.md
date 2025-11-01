# 📝 自訂主要計畫

在某些情況下，您可能希望為複雜的任務指定一個包含多個工具的「自訂計畫」，而不是在全自動代理模式下自動生成「主要計畫」。

您可以使用自己的自訂「主要計畫」，而不是由 BibleMate AI 生成的計畫。為此，請在您的 BibleMate AI 提示中以「@@」開頭，後面跟著您自己的聖經學習主要計畫。

例如：

```
@@ 分析約翰福音 3:16，步驟如下：
1. 呼叫工具「retrieve_english_bible_verses」以獲取聖經文本，
2. 呼叫工具「retrieve_bible_cross_references」以獲取聖經串珠，
3. 呼叫工具「interpret_new_testament_verse」以進行解釋，以及
4. 呼叫工具「write_bible_theology」以解釋其神學。
```

觀看此影片：https://youtu.be/Lejq0sAx030

另一個例子：

```
@@ 撰寫申命記 6:4 的感人靈修，步驟如下：
1. 使用 @study_old_testament_themes 分析主題
2. 使用 @identify_bible_keywords 識別並解釋經文中的關鍵聖經詞彙
3. 使用 @write_bible_insights 撰寫靈修見解
4. 使用 @write_bible_applications 將經文與日常生活聯繫起來
5. 使用 @write_bible_devotion 撰寫感人靈修。
確保每個步驟都清晰明確，最終輸出連貫且鼓舞人心
```

觀看此影片：https://youtu.be/NYPyujFG09E

即使您在停用「代理」模式的情況下使用「聊天」模式，「@@」技巧也有效。
