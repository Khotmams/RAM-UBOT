# Gausah kesini ngentot!!
# NGEDIT CMD YG BENER KONTOL!!!


from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum dulu biar sopan yekan...!! ")


@register(outgoing=True, pattern='^.gdl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Ga Dlu dah, Makasi,, bhahaah!!")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumsalam WR.WB, thx udh ucapin salam nih ngab :v...")


@register(outgoing=True, pattern='^.gj(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Gajelas suu!")


@register(outgoing=True, pattern='^.yb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**iya bang...**")


@register(outgoing=True, pattern='^.m(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MEKINYA ANAK INIIIII....**")


@register(outgoing=True, pattern='^.k(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Apalo Khintil...**")


@register(outgoing=True, pattern='^.gjb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAJELAS IBAB....**")


@register(outgoing=True, pattern='^.bjt(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ETDAH BUJETT....**")


@register(outgoing=True, pattern='^.mls(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**gush dh gw gi mls HAHA!!!**")


@register(outgoing=True, pattern='^.ange1(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ANGEEEE!!! Pake N gapake tot bhaha**")


@register(outgoing=True, pattern='^.ay(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Sayang..!!**")


@register(outgoing=True, pattern='^.pc(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**PC bntr, PENTING!!**")


@register(outgoing=True, pattern='^.br(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Buruann asw..!!!**")


@register(outgoing=True, pattern='^.eh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Eh dasar asu...!**")


@register(outgoing=True, pattern='^.ucp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Lu siapa si ASW!!!!**")


@register(outgoing=True, pattern='^.hey(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Hey, JELEK GA KAYA GUA GANTENG YEKAN..😂**")


@register(outgoing=True, pattern='^.loh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GC SAMPAH KAYA GINI, BUBARIN AJA PLIS!!🤣**")

CMD_HELP.update({
    "salam3":
    ".p\
\nUsage:\
\n\n.l\
\nUsage:\
\n\n.gdl\
\nUsage:\
\n\n.gj\
\nUsage:\
\n\n.gjb\
\nUsage:\
\n\n.yb\
\nUsage:\
\n\n.bjt\
\nUsage:"
})

CMD_HELP.update({
    "salam4":
    ".mls\
\nUsage:\
\n\n.ay\
\nUsage:\
\n\n.pc\
\nUsage:\
\n\n.eh\
\nUsage:\
\n\n.br\
\nUsage:\
\n\n.ange1\
\nUsage:\
\n\n.hey\
\nUsage:\
\n\n.loh\
\nUsage:\
\n\n.ucp\
\nUsage:\
\n\n.m\
\nUsage:\
\n\n.k\
\nUsage:"
})
