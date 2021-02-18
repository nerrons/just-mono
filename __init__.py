import os

from aqt import mw
from aqt.qt import *
from anki.hooks import addHook

def get_key():
    conf = mw.addonManager.getConfig(__name__)
    return conf.get("hotkey", "") if conf else ""

def format_key(k):
    return QKeySequence(k).toString(QKeySequence.NativeText)

def wrap_mono(editor):
    editor.web.eval("wrap('<code>', '</code>')")

def setupEditorButtonsFilter(buttons, editor):
    key = get_key()
    b = editor.addButton(
            os.path.join(os.path.dirname(__file__), "justmono.png"),
            "justmono_button",
            wrap_mono,
            tip=f"Just Mono ({format_key(key)})",
            keys=key
        )
    buttons.append(b)
    return buttons

addHook("setupEditorButtons", setupEditorButtonsFilter)
