def translate_into_traditional_chinese(event=None):
    custom_prompt = "請將以下內容翻譯成繁體中文。如果內容包含程式碼，請保持程式碼不變，只翻譯文字部分。請確保翻譯準確且自然流暢。"

    if custom_prompt is not None:
        buffer = event.app.current_buffer if event is not None else text_field.buffer
        selectedText = buffer.copy_selection().text
        content = selectedText if selectedText else buffer.text
        content = agentmake(get_augment_instruction(custom_prompt, content), system="auto" if ApplicationState.auto_agent else None, **AGENTMAKE_CONFIG)[-1].get("content", "").strip()
        # insert the improved prompt as a code block
        buffer.insert_text(format_assistant_content(content))
        # Repaint the application; get_app().invalidate() does not work here
        get_app().reset()