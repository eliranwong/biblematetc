from biblematetc import config, DIALOGS
from agentmake.plugins.uba.lib.BibleBooks import BibleBooks
from agentmake.plugins.uba.lib.BibleParser import BibleVerseParser
import re

BIBLE_SEARCH_SCOPES = [
    "search",
    "genesis",
    "exodus",
    "leviticus",
    "numbers",
    "deuteronomy",
    "joshua",
    "judges",
    "ruth",
    "samuel1",
    "samuel2",
    "kings1",
    "kings2",
    "chronicles1",
    "chronicles2",
    "ezra",
    "nehemiah",
    "esther",
    "job",
    "psalms",
    "proverbs",
    "ecclesiastes",
    "songs",
    "isaiah",
    "jeremiah",
    "lamentations",
    "ezekiel",
    "daniel",
    "hosea",
    "joel",
    "amos",
    "obadiah",
    "jonah",
    "micah",
    "nahum",
    "habakkuk",
    "zephaniah",
    "haggai",
    "zechariah",
    "malachi",
    "matthew",
    "mark",
    "luke",
    "john",
    "acts",
    "romans",
    "corinthians1",
    "corinthians2",
    "galatians",
    "ephesians",
    "philippians",
    "colossians",
    "thessalonians1",
    "thessalonians2",
    "timothy1",
    "timothy2",
    "titus",
    "philemon",
    "hebrews",
    "james",
    "peter1",
    "peter2",
    "john1",
    "john2",
    "john3",
    "jude",
    "revelation",
]

# shared dialogs

async def get_multiple_bibles(options, descriptions):
    select = await DIALOGS.getMultipleSelection(
        default_values=config.last_multi_bible_selection,
        options=options,
        descriptions=descriptions,
        title="聖經版本",
        text="請選擇聖經版本："
    )
    if select:
        config.last_multi_bible_selection = select
        return select
    return []

async def get_reference(verse_reference=True, exhaustiveReferences=False):
    abbr = BibleBooks.abbrev["tc"]
    input_suggestions = []
    for book in range(1,67):
        input_suggestions += list(abbr[str(book)])
    result = await DIALOGS.getInputDialog(title="聖經經文", text="請輸入經文參考，例`約翰福音 3:16`", default=config.last_bible_reference, suggestions=input_suggestions)
    if result:
        parser = BibleVerseParser(True, language="tc")
        result = parser.extractExhaustiveReferencesReadable(result) if exhaustiveReferences else parser.extractAllReferencesReadable(result)
        if result and not verse_reference:
            result = re.sub(r":[\-0-9]+?;", ";", f"{result};")[:-1]
    if result:
        config.last_bible_reference = result
        return result
    if not result:
        abbr = BibleBooks.abbrev["tc"]
        book = await DIALOGS.getValidOptions(
            default=str(config.last_book),
            options=[str(book) for book in range(1,67)],
            descriptions=[abbr[str(book)][-1] for book in range(1,67)],
            title="書卷",
            text="請選擇書卷："
        )
        if not book:
            return ""
        config.last_book = book = int(book)
        chapter = await DIALOGS.getValidOptions(
            default=str(config.last_chapter),
            options=[str(chapter) for chapter in range(1,BibleBooks.chapters[int(book)]+1)],
            title="章數",
            text="請選擇章數："
        )
        if not chapter:
            return ""
        config.last_chapter = chapter = int(chapter)
        if verse_reference:
            verse = await DIALOGS.getValidOptions(
                default=str(config.last_verse),
                options=[str(verse) for verse in range(1,BibleBooks.verses[int(book)][int(chapter)]+1)],
                title="節數",
                text="請選擇節數："
            )
            if not verse:
                return ""
            config.last_verse = verse = int(verse)
            return f"{abbr[str(book)][0]} {chapter}:{verse}"
        return f"{abbr[str(book)][0]} {chapter}"

# dialogs for content retrieval

async def uba_search_bible(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="搜索聖經",
        text="請選擇聖經版本："
    )
    if not select:
        return ""
    abbr = BibleBooks.abbrev["eng"]
    book = await DIALOGS.getValidOptions(
        default=str(config.last_book),
        options=["0"]+[str(book) for book in range(1,67)],
        descriptions=["ALL"]+[abbr[str(book)][-1] for book in range(1,67)],
        title="選擇書卷",
        text="選擇所有書卷或特定書卷進行搜索："
    )
    if not book:
        return ""
    template = BIBLE_SEARCH_SCOPES[int(book)]
    result = await DIALOGS.getInputDialog(title="搜索", text="請輸入搜索關鍵字：")
    if not result:
        return ""
    return f"//{template}/{select}/{result}" if result else ""

async def uba_bible(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="聖經",
        text="請選擇聖經版本："
    )
    if not select:
        return ""
    result = await get_reference()
    return f"//bible/{select}/{result}" if result else ""

async def uba_ref(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="經文串珠參考",
        text="請選擇聖經版本："
    )
    if not select:
        return ""
    result = await get_reference()
    return f"//xref/{select}/{result}" if result else ""

async def uba_treasury(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="Treasury of Scripture Knowledge",
        text="請選擇聖經版本："
    )
    if not select:
        return ""
    result = await get_reference()
    return f"//treasury/{select}/{result}" if result else ""

async def uba_chapter(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="聖經",
        text="請選擇聖經版本："
    )
    if not select:
        return ""
    result = await get_reference(verse_reference=False)
    return f"//chapter/{select}/{result}" if result else ""

async def uba_compare(options, descriptions):
    select = await get_multiple_bibles(options, descriptions)
    if not select:
        return ""
    else:
        select = "_".join(select)
    result = await get_reference()
    return f"//uba/COMPARE:::{select}:::{result}" if result else ""

async def uba_compare_chapter(options, descriptions):
    select = await get_multiple_bibles(options, descriptions)
    if not select:
        return ""
    else:
        select = "_".join(select)
    result = await get_reference(verse_reference=False)
    return f"//uba/COMPARECHAPTER:::{select}:::{result}" if result else ""

async def uba_commentary(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_commentary,
        options=options,
        descriptions=descriptions,
        title="聖經註釋書",
        text="請選擇註釋書："
    )
    if not select:
        return ""
    result = await get_reference()
    return f"//commentary/{select}/{result}" if result else ""

async def uba_aicommentary():
    result = await get_reference()
    return f"//aicommentary/{result}" if result else ""

async def uba_index():
    result = await get_reference()
    return f"//index/{result}" if result else ""

async def uba_translation():
    result = await get_reference()
    return f"//translation/{result}" if result else ""

async def uba_discourse():
    result = await get_reference()
    return f"//discourse/{result}" if result else ""

async def uba_morphology():
    result = await get_reference()
    return f"//morphology/{result}" if result else ""

async def uba_dictionary():
    result = await DIALOGS.getInputDialog(title="Search Dictionary", text="請輸入搜索項目：")
    return f"//dictionary/{result.strip()}" if result and result.strip() else ""

async def uba_parallel(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="搜索聖經平行經文",
        text="請選擇聖經版本："
    )
    if not select:
        return ""
    result = await DIALOGS.getInputDialog(title="Search Bible Parallels", text="請輸入搜索項目：")
    return f"//parallel/{select}/{result.strip()}" if result and result.strip() else ""

async def uba_promise(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="搜索聖經應許",
        text="請選擇聖經版本："
    )
    if not select:
        return ""
    result = await DIALOGS.getInputDialog(title="搜索聖經應許", text="請輸入搜索項目：")
    return f"//promise/{select}/{result.strip()}" if result and result.strip() else ""

async def uba_topic():
    result = await DIALOGS.getInputDialog(title="搜索聖經主題", text="請輸入搜索項目：")
    return f"//topic/{result.strip()}" if result and result.strip() else ""

async def uba_name():
    result = await DIALOGS.getInputDialog(title="搜索聖經名字", text="請輸入搜索項目：")
    return f"//name/{result.strip()}" if result and result.strip() else ""

async def uba_character():
    result = await DIALOGS.getInputDialog(title="搜索聖經人物", text="請輸入搜索項目：")
    return f"//character/{result.strip()}" if result and result.strip() else ""

async def uba_location():
    result = await DIALOGS.getInputDialog(title="搜索聖經地點", text="請輸入搜索項目：")
    return f"//location/{result.strip()}" if result and result.strip() else ""

async def uba_encyclopedia(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_encyclopedia,
        options=options,
        descriptions=descriptions,
        title="百科全書",
        text="請選擇百科全書："
    )
    if not select:
        return ""
    result = await DIALOGS.getInputDialog(title=f"搜索百科全書 - {select}", text="請輸入搜索項目：")
    return f"//encyclopedia/{select}/{result.strip()}" if result and result.strip() else ""

async def uba_lexicon(options):
    select = await DIALOGS.getValidOptions(
        default=config.default_lexicon,
        options=options,
        title="原文字典",
        text="請選擇原文字典："
    )
    if not select:
        return ""
    result = await DIALOGS.getInputDialog(title=f"搜索原文字典 - {select}", text="請輸入搜索項目：")
    return f"//lexicon/{select}/{result.strip()}" if result and result.strip() else ""

# Configure default modules

async def uba_default_bible(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_bible,
        options=options,
        descriptions=descriptions,
        title="預設聖經版本",
        text="請選擇預設的聖經版本："
    )
    return select if select else ""

async def uba_default_commentary(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_commentary,
        options=options,
        descriptions=descriptions,
        title="預設聖經註釋書",
        text="請選擇預設的聖經註釋書："
    )
    return select if select else ""

async def uba_default_encyclopedia(options, descriptions):
    select = await DIALOGS.getValidOptions(
        default=config.default_encyclopedia,
        options=options,
        descriptions=descriptions,
        title="預設百科全書",
        text="請選擇預設的百科全書："
    )
    return select if select else ""

async def uba_default_lexicon(options):
    select = await DIALOGS.getValidOptions(
        default=config.default_lexicon,
        options=options,
        title="預設原文字典",
        text="請選擇預設的原文字典："
    )
    return select if select else ""