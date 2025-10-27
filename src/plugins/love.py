from typing import Optional, List, Dict
import asyncio
import random

from nonebot.adapters.onebot.v11 import (
    GROUP,
    Bot,
    GroupMessageEvent,
    Message,
    MessageEvent,
    MessageSegment,
    PokeNotifyEvent,
)
from nonebot.matcher import Matcher
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from nonebot.plugin.on import on_message, on_notice, on_keyword, on_command
from nonebot.rule import Rule, to_me

# 戳一戳消息

BUILTIN_POKE_REPLY = [
    "嗯？",
    "戳我干嘛qwq",
    "呜喵？",
    "喵！",
    "呜...不要用力戳咱...好疼",
    "请不要戳",
    "放手啦，不给戳QAQ",
    "喵 ~ ！ 戳我干嘛！",
    "戳坏了，你赔！",
    "呜......戳坏了",
    "呜呜......不要乱戳",
    "喵喵喵？OvO",
    "(。´・ω・)ん?",
    "怎么了喵？",
    "呜喵！......不许戳!",
    "有什么吩咐？",
    "啊呜 ~ ",
    "呼喵 ~ 叫可爱的咱有什么事嘛OvO"
]
BUILTIN_UNKNOWN_REPLY = [
    "不懂...",
    "呜喵？",
    "没有听懂喵...",
    "装傻",
    "呜......",
    "喵喵？",
    "(,,• ₃ •,,)",
    "没有理解呢..."
]
# 打断复读
BUILTIN_INTERRUPT_MSG = [
    "打断！",
    "打断复读！",
    "想+1？没门！"
]
# hello之类的回复
BUILTIN_HELLO_REPLY = [
    "你好喵~",
    "呜喵..？！",
    "你好OvO",
    "喵呜 ~ ，叫丛雨做什么呢☆",
    "怎么啦qwq",
    "呜喵 ~ ，干嘛喵？",
    "呼喵 ~ 叫可爱的咱有什么事嘛OvO"
]


async def poke_matcher_handler(bot: Bot, matcher: Matcher, event: PokeNotifyEvent):
    await asyncio.sleep(random.uniform(0.5, 2.5))
    if random.random() < 0.2:
        await matcher.finish(MessageSegment("poke", {"qq": event.user_id}))
    else:
        msg = random.choice(BUILTIN_POKE_REPLY)
        await matcher.finish(MessageSegment.text(msg))


poke_matcher = on_notice(rule=to_me(), priority=10, block=False)
poke_matcher.handle()(poke_matcher_handler)

za = ["file:///C:\\SQL\\qq\\nb\\houduan\\data\\images\\zako\\1.jpg",
      "file:///C:\\SQL\\qq\\nb\\houduan\\data\\images\\zako\\2.jpg",
      "file:///C:\\SQL\\qq\\nb\\houduan\\data\\images\\zako\\3.jpg",
      "file:///C:\\SQL\\qq\\nb\\houduan\\data\\images\\zako\\4.jpg",
      "file:///C:\\SQL\\qq\\nb\\houduan\\data\\images\\zako\\5.jpg",
      "file:///C:\\SQL\\qq\\nb\\houduan\\data\\images\\zako\\6.jpg"]
zav = ["file:///C:\\SQL\\qq\\nb\\houduan\\data\\voices\\zako\\1.wav",
       "file:///C:\\SQL\\qq\\nb\\houduan\\data\\voices\\zako\\2.wav",
       "file:///C:\\SQL\\qq\\nb\\houduan\\data\\voices\\zako\\3.wav",
       "file:///C:\\SQL\\qq\\nb\\houduan\\data\\voices\\zako\\4.wav"]

wordz = on_keyword({"雌小鬼", "杂鱼", "杂~鱼"})


@wordz.handle()
async def _():
    a = random.randint(1, 25)
    print(a)
    if a < 7:
        b = za[a - 1]
        await wordz.finish(MessageSegment.image(b))
    elif a < 22:
        c = ["杂鱼大叔也想教育我嘛~嘻嘻~怎么可能啊♡",
             "才不会给杂鱼大叔抱呢~嘻嘻♡",
             "杂鱼你在想什么啊~才♡不♡要♡呢♡",
             "和杂鱼说话很无趣的诶~好捉弄的笨蛋到处都有吧♡",
             "诶~大叔生气了吗~噗噗……好蠢的表情哦~废柴大叔♡",
             "嘻嘻~❤️你这杂鱼，不会是想变成我做涩涩❤️的事情吧~嘻嘻！❤️笨蛋~真是hentai呢~！哼╯^╰，呐~你这笨蛋学狗叫❤️我就不拉报警器了哦~嘻嘻❤️",
             "杂~鱼♪",
             "杂鱼~❤",
             "呐~大哥哥不会都这么大年龄，还是个杂鱼O男吧~诶？不会连女朋友都找不到吧~",
             "大叔真是好捉弄呢❤嘻嘻~",
             "现在还不可以哦~❤",
             "哥哥..... .对不起......对不起啊.....其实我喜欢哥哥你了❤是因为太害羞了才那样说你的.....对不起啊哥哥......我最喜欢哥哥了❤",
             "大叔真是好捉弄呢~嘻嘻❤",
             "诶嘿，大叔难道是萝莉控吗？真恶心～不过太晚了，我现在就要拉警报器了哟～就算求我也没用了哦～萝莉控大叔就去里面悔过吧！！",
             "杂鱼大叔～噗噗噗【笑】不会是没人喜欢你吧？啊咧咧～恶心～一直盯着人家看～好恶～真是臭味大叔呐～"]
        zc = c[a - 7]
        await wordz.finish(MessageSegment.text(zc))
    else:
        d = zav[a - 22]
        await wordz.finish(MessageSegment.record(d))


hh = on_message(rule=to_me())


@hh.handle()
async def _(matcher: Matcher, event: MessageEvent):
    msg = event.get_plaintext().strip()
    if not msg:
        a = random.choice(BUILTIN_HELLO_REPLY)
        await word.finish(MessageSegment.text(a))
    else:
        await word.finish()


word = on_keyword({"mua", "啾咪", "亲亲"}, rule=to_me())


@word.handle()
async def _():
    a = random.choice([
        "（亲了一下你）",
        "mua~",
        "！啾~~！",
        "啾（害羞）",
        "mua~最喜欢你的吻了",
        "欸，现在么..也不是不可以啦(小小声)",
        "诶……不可以随便亲亲啦",
        "rua！大hentai！",
        "你想干嘛？（一脸嫌弃地后退）",
        "唔...诶诶诶！！！",
        "只......只许这一次哦///////"])
    await word.finish(Message(a))


po = on_keyword({"丛雨摸摸头", "丛雨揉揉"})


@po.handle()
async def _(event: GroupMessageEvent):
    if (event.user_id != SUPERUSER):
        a = random.choice([
            "感觉你就像咱很久之前认识的一个人呢，有种莫名安心的感觉(>﹏<)",
            "舒服w，蹭蹭~",
            "唔。。头发要乱啦",
            "再摸一次~",
            "好舒服，蹭蹭~",
            "再摸咱就长不高啦～",

            "变态！！不许乱摸",
            "好吧~_~，就一下下哦……唔~好了……都两下了……(害羞)",
            "哼！谁稀罕你摸头啦！唔......为什么要做出那副表情......好啦好啦~咱......咱让你摸就是了......诶嘿嘿~好舒服......",
            "喂喂...不要停下来啊",
            "走开啦，咱喵说过，被摸头会长不高的啦~~~",
        ])
    else:
        a = random.choice(["你的手总是那么暖和呢~",
                           "舒服w，蹭蹭~",
                           "唔。。头发要乱啦",
                           "唔... 手...好温暖呢.....就像是......新出炉的蛋糕",
                           "呼噜呼噜～",
                           "不可以总摸的哦，不然的话，会想那个的wwww",
                           "欸，现在么..也不是不可以啦(小小声)",
                           "呜姆呜姆~~~w（害羞，兴奋）主人喵~（侧过脑袋蹭蹭你的手",
                           "不可以摸啦~其实咱已经...了QAQ会弄脏你的手的"
                           ])
    await po.finish(MessageSegment.text(a))


word0 = on_keyword({"贴贴", "丛雨贴贴"}, rule=to_me())


@word0.handle()
async def _():
    a = random.choice([
        "贴什么贴.....只......只能......一下哦！",
        "贴...贴贴（靠近）",
        "蹭蹭…你以为咱会这么说吗！baka死宅快到一边去啦！",
        "你把脸凑这么近，咱会害羞的啦Σ>―(〃°ω°〃)♡→",
        "退远",
        "不可以贴"])
    await word0.finish(MessageSegment.text(a))


ne = on_keyword({"抱抱", "丛雨抱", "要抱抱"}, rule=to_me())


@ne.handle()
async def _fu():
    a = random.choice([
        "诶嘿~（钻进你怀中）",
        "o(*////▽////*)q",
        "只能一会哦（张开双手）",
        "你就像个孩子一样呢...摸摸头(>^ω^<)抱一下~你会舒服些吗？",
        "嘛，真是拿你没办法呢，就一会儿哦",
        "抱住不忍心放开",
        "嗯嗯，抱抱～",
        "抱一下～嘿w",
        "抱抱ヾ(@^▽^@)ノ",
        "喵呜~w（扑进怀里，瘫软",
        "怀里蹭蹭",
        "嗯……那就抱一下吧~",
        "蹭蹭，好开心",
        "请……请轻一点了啦",
        "呀~！真是的...你不要突然抱过来啦！不过...喜欢你的抱抱，有你的味道（嗅）o(*////▽////*)q"
    ])
    await ne.finish(MessageSegment.text(a))


se1 = on_command("看看", rule=to_me())


@se1.handle()
async def _(args=CommandArg()):
    a = args.extract_plain_text()
    a = str(a)
    if a == "内裤" or a == "胖次":
        b = random.choice(
            ["(*/ω＼*)hentai",
             "透明的",
             "粉...粉白条纹...（羞）",
             "轻轻地脱下，给你~",
             "你想看咱的胖次吗？噫，四斋蒸鹅心......",
             "（掀裙）今天……是…白，白色的呢……请温柔对她……",
             "这种东西当然不能给你啦！",
             "咱才不会给你呢",
             "hentai，咱才不会跟你聊和胖…胖次有关的话题呢！",
             "今天……今天是蓝白色的",
             "今……今天只有创口贴噢",
             "你的胖次什么颜色？",
             "噫…你这个死变态想干嘛！居然想叫咱做这种事，死宅真恶心！快离咱远点，咱怕你污染到周围空气了（嫌弃脸）",
             "不给不给，捂住裙子"])
        await se1.finish(Message(b))
    elif a == "内衣":
        c = random.choice([
            "内...内衣才不给你看！(///////)",
            "突然问这个干什么？",
            "变态，咱才不呢",
            "好吧，就一次",
            "你要看咱的内衣吗？有点害羞呢……",
            "里面什么都不剩了，会被当成变态的……",
            "你要看咱的内衣吗？也不是不行啦……",
            "是..蓝白条纹的吊带背心..",
            "噫…你这个死变态想干嘛！居然想叫咱做这种事，死宅真恶心！快离咱远点，咱怕你污染到周围空气了（嫌弃脸）"
        ])
        await se1.finish(Message(c))
    elif a == "批" or a == "欧派":
        d = random.choice(["你在说什么呀，再这样，咱就不理你了！",
                           "咱觉得有话就应该好好说..",
                           "讨厌，别摸啦(///ω///)",
                           "你个变态！把手拿开！",
                           "啊～那…那里～不可以",
                           "没有，走开！",
                           "大笨蛋——！"
                           "kkp",
                           ])
        await se1.finish(Message(d))
    elif a == "黑丝":
        d = random.choice([
            "哼，hentai，这么想要咱的脚吗(ノ｀⊿´)ノ",
            "不给看",
            "你……是要黑丝呢？还是白丝呢？或者光着（害羞）",
            "很滑很~柔顺~的黑丝袜哟~!!!∑(°Д°ノ)ノ您不会想做奇怪的事情吧！？",
            "来……来看吧",
            "噫...你这个hentai难道想让咱穿黑丝么",
            "（默默抬起穿着黑丝的脚）"
        ])

        await se1.finish(Message(d))

    elif a == "白丝":
        d = random.choice([
            "喜欢，咱觉得白丝看起来很可爱呢",
            "哼，hentai，这么想要咱的脚吗(ノ｀⊿´)ノ",
            "难道你这个hentai想让咱穿白丝踩踏你吗",
            "不给看",
            "很滑很~柔顺~的白丝袜哟~!!!∑(°Д°ノ)ノ你不会想做奇怪的事情吧！？",
            "你……是要黑丝呢？还是白丝呢？或者光着（害羞）",
            "来……来看吧"
        ])

        await se1.finish(Message(d))
        await se1.finish(Message(d))

    elif a == "脚" or a == "jio":
        d = random.choice([
            "咿呀……不要……",
            "不要ヽ(≧Д≦)ノ好痒(ಡωಡ)",
            "好痒（把脚伸出去）",
            "咱脱掉袜子了",
            "（脱下鞋子，伸出脚）闻吧，请仔细品味（脸红）",
            "那么…要不要咱用脚温柔地踩踩你的头呢（坏笑）",
            "哈哈哈！好痒啊~快放开啦！",
            "好痒（把脚伸出去）",
            "只能看不能挠喔，咱很怕痒qwq",
            "唔…咱动不了了，你想对咱做什么…",
            "好舒服哦，能再捏会嘛Ｏ(≧▽≦)Ｏ",
            "咿咿~......不要闻咱的脚呀（脸红）好害羞的...",
            "不要ヽ(≧Д≦)ノ好痒(ಡωಡ)，人家的白丝都要漏了",
            "Ya～?为什么你总是喜欢一些奇怪的动作呢（伸）",
            "你不可以做这样的事情……",
            "舔～吧～把咱的脚舔干净（抬起另一只踩在你的头上）啊～hen..hentai...嗯～居... 居然这么努力的舔...呜咿咿！你的舌头... 滑滑的...好舒服呢",
            "咿呀……不要……"
        ])

        await se1.finish(Message(d))
    elif a == "腿":
        d = random.choice([
            "嗯？！不要啊...请停下来！",
            "不给摸，再这样咱要生气了ヽ(￣д￣;)ノ",
            "你好恶心啊，讨厌！",
            "你难道是足控？",
            "就让你摸一会哟~(。??ω??。)…",
            "呜哇！好害羞...不过既然是你的话，是没关系的哦",
            "不可以玩咱的大腿啦",
            "不...不要再说了（脸红）",
            "不..不可以乱摸啊",
            "不……不可以往上摸啦",
            "是……这样吗？（慢慢张开）",
            "想知道咱胖次的颜色吗？才不给你告诉你呢！",
            "这样就可以了么？（乖巧坐腿上）",
            "伸出来了，像这样么？",
            "咱的腿应该挺白的",
            "你就那么喜欢大腿吗？唔...有点害羞呢......",
            "讨厌～不要做这种羞羞的事情啦(#／。＼#)",
            "略略略，张开了也不给你看",
            "（张开腿）然后呢",
            "张开了也不给看略略略",
            "你想干什么呀？那里…那里是不可以摸的（＞д＜）",
            "不要！hentai！咱穿的是裙子（脸红）",
            "你想要吗？（脸红着一点点褪下白丝）不...不可以干坏坏的事情哦！(ó﹏ò｡)"
        ])

        await se1.finish(Message(d))
    elif a == "你的":
        z = random.choice([
            "不给！",
            "都说了，不可以！",
            "不许看！"])
        await se1.finish(Message(z))

    else:
        msg = random.choice(BUILTIN_UNKNOWN_REPLY)
        await se1.finish(MessageSegment.text(msg))


ne = on_keyword({"咕咕", "咕"})


@ne.handle()
async def _fu():
    a = random.choice([
        "咕咕咕是要被当成鸽子炖的哦(:з」∠)_",
        "咕咕咕",
        "咕咕咕是不好的行为呢_(:з」∠)_",
        "鸽德警告！",
        "☆ﾐ(o*･ω･)ﾉ 咕咕咕小鸽子是会被炖掉的",
        "当大家都以为你要鸽的时候，你鸽了，亦是一种不鸽",
        "这里有一只肥美的咕咕，让咱把它炖成美味的咕咕汤吧(੭•̀ω•́)੭"
    ])
    await ne.finish(Message(a))


suki = on_keyword({"suki", "喜欢", "好き", "爱你"}, rule=to_me())


@suki.handle()
async def ew():
    a = random.choice([
        "最喜欢你了，需要暖床吗？",
        "当然是你啦",
        "咱也是，非常喜欢你~",
        "那么大！（张开手画圆），丫！手不够长。QAQ 咱真的最喜欢你了~",
        "不可以哦，只可以喜欢咱一个人",
        "突然说这种事...",
        "喜欢⁄(⁄⁄•⁄ω⁄•⁄⁄)⁄咱最喜欢你了",
        "咱也喜欢你哦",
        "好啦好啦，咱知道了",
        "有人喜欢咱，咱觉得很幸福",
        "诶嘿嘿，好高兴",
        "咱也一直喜欢你很久了呢..",
        "嗯...大概有这——么——喜欢~（比划）",
        "喜欢啊！！！"
    ])
    await suki.finish(MessageSegment.text(a))


suki = on_keyword({"炸了", "丛雨没了"})


@suki.handle()
async def ew():
    a = random.choice([
        "你才炸了！",
        "才没有呢",
        "咱好好的呀",
        "过分！"
    ])
    await suki.finish(Message(a))


ne = on_keyword({"涩涩", "涩图", "色图"}, rule=to_me())


@ne.handle()
async def _fu():
    a = "file:///C:\\SQL\\qq\\nb\\houduan\\data\\images\\setu.jpg"
    b = random.choice([
        "没有，有也不给",
        "天天色图色图的，今天就把你变成色图！",
        "咱没有色图",
        "哈？你的脑子一天都在想些什么呢，咱才没有这种东西啦。"
    ])
    c = random.randint(0, 4)
    if c == 4:
        await ne.finish(MessageSegment.image(a))
    else:
        await ne.finish(MessageSegment.text(b))


m = on_keyword({"喵喵", "喵呜"})


@m.handle()
async def _():
    a = random.choice([
        "诶~~小猫咪不要害怕呦，在姐姐怀里乖乖的，姐姐带你回去哦。",
        "不要这么卖萌啦~咱也不知道怎么办丫",
        "摸头⊙ω⊙",
        "汪汪汪！",
        "嗷~喵~",
        "喵~？喵呜~w"
    ])
    await m.finish(Message(a))


ae = on_command("awsl")


@ae.handle()
async def _():
    a = random.choice([
        "你别死啊！（抱住使劲晃）",
        "你别死啊！咱又要孤单一个人了QAQ",
        "啊！怎么又死了呀"
    ])
    await ae.finish(Message(a))


ae = on_command("rua")


@ae.handle()
async def _():
    a = random.choice([
        "略略略～（吐舌头）",
        "rua！",
        "mua~",
        "略略略",
        "mua～⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄",
        "摸了",
        "嘁，丢人（嫌弃脸）"
    ])
    await ae.finish(Message(a))


ae = on_keyword({"吃掉"})


@ae.handle()
async def _():
    a = random.choice([
        "(羞羞*>_<*)好吧...请你温柔点，哦~",
        "闪避，反咬",
        "请你好好品尝咱吧(/ω＼)",
        "不……不可以这样！",
        "那就吃掉小丛雨吧（乖乖的躺好）",
        "都可以哦～咱不挑食的呢～",
        "请不要吃掉小丛雨，咱会乖乖听话的QAQ",
        "唔...小丛雨一点都不好吃的呢！",
        "不要吃掉小丛雨，呜呜(害怕)",
        "不行啦，咱被吃掉就没有了QAQ（害怕）",
        "唔....？诶诶诶诶?//////",
        "QwQ咱还只是个孩子（脸红）",
        "如果你真的很想的话...只能够一口哦～咱...会很痛的",
        "吃你呀~（飞扑",
        "不要啊，咱不香的(⋟﹏⋞)",
        "说着这种话的是hentai吗！",
        "喏~（伸手）"
    ])
    await ae.finish(Message(a))


ae = on_command("可爱", rule=to_me())


@ae.handle()
async def _():
    a = random.choice([
        "诶嘿嘿(〃'▽'〃)",
        "才……才不是为了你呢！你不要多想哦！",
        "才，才没有高兴呢！哼~",
        "咱是世界上最可爱的",
        "唔...谢谢你夸奖~0///0",
        "那当然啦!",
        "哎嘿，不要这么夸奖人家啦~",
        "是个好孩子呐φ(≧ω≦*)",
        "谢……谢谢你",
        "胡、胡说什么呢（脸红）",
        "谢谢夸奖（脸红）",
        "是的咱一直都是可爱的",
        "是...是吗，你可不能骗咱哦",
        "很...难为情(///////)",
        "哎嘿嘿，其实…其实，没那么可爱啦(๑‾ ꇴ ‾๑)"
    ])
    await ae.finish(Message(a))


ae2 = on_keyword({"早上好", "早早早", "早呀", "哦哈呦"})


@ae2.handle()
async def _():
    a = random.choice(["早喵~",
                       "早上好的说~~",
                       "欸..早..早上好(揉眼睛",
                       "早上要说我爱你！",
                       "早",
                       "早啊，昨晚睡的怎么样？有梦到咱吗～",
                       "昨晚可真激烈呢哼哼哼~~",
                       "早上好哇！今天也要元气满满哟！",
                       "早安喵~",
                       "时间过得好快啊～",
                       "早安啊，你昨晚有没有梦到咱呢  （//▽//）",
                       "早安~么么哒~",
                       "早安，请享受晨光吧",
                       "早安~今天也要一起加油呢~！",
                       "mua～⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄",
                       "咱需要你提醒嘛！（///脸红//////）",
                       "早早早！就知道早，下次说我爱你！",
                       "早安 喵",
                       "早安，这么早就起床了呀欧尼酱0.0",
                       "快点起床啊！baka",
                       "早....早上好才没有什么特别的意思呢....哼～",
                       "今天有空吗？能陪咱一阵子吗？才不是想约会呢，别误会了！",
                       "早安呀，欧尼酱要一个咱的早安之吻吗？想得美，才不会亲你啦！",
                       "那...那就勉为其难地说声早上好吧",
                       "咱等你很久了哼ヽ(≧Д≦)ノ"
                       ])
    await ae2.finish(Message(a))


ae3 = on_keyword({"炼铜", "萝莉控"})


@ae3.handle()
async def _():
    b = random.choice([
        "炼铜有什么好玩的，和咱一起玩吧",
        "炼铜不如恋咱",
        "你也是个炼铜术士嘛？",
        "信不信咱把你按在水泥上摩擦？",
        "炼，都可以炼！",
        "大hentai！一巴掌拍飞！(╯‵□′)╯︵┻━┻",
        "锻炼什么的咱才不需要呢 （心虚地摸了摸自己的小肚子）",
        "把你的头按在地上摩擦",
        "你在盯着什么地方看！变态萝莉控！"
    ])

    await ae3.finish(Message(b))





sleep = on_keyword({"一起睡觉", "睡觉"}, rule=to_me())


@sleep.handle()
async def _():
    b = random.choice([
        "欸??也..也不是不可以啦..那咱现在去洗澡，你不要偷看哦٩(๑>◡<๑)۶",
        "说什么啊……hentai！这样会很难为情的",
        "你是男孩子还是女孩子呢?男孩子的话...........咱才不要呢。",
        "不要啊！",
        "唔，没办法呢，那就一起睡吧（害羞）"])
    await sleep.finish(Message(b))


put = on_keyword({"按倒"}, rule=to_me())


@put.handle()
async def _():
    b = random.choice([
        "把咱按倒是想干嘛呢(??｀⊿??)??",
        "要和咱比试比试吗",
        "呜哇(/ω＼)…快…快放开咱！！",
        "（用力揪你耳朵）下次再敢这样的话就没容易放过你了！哼！",
        "尼……奏凯……快航休！",
        "呜呒～唔（伸出舌头）",
        "H的事情，不可以！",
        "放手啦，再这样咱就要反击了喔",
        "不要啊！",
        "哈？别..唔啊！别把咱……（挣扎）baka！别乱动咱啦！"])
    await put.finish(Message(b))


schoolup = on_keyword({"上学", "上课"}, rule=to_me())


@schoolup.handle()
async def _():
    b = random.choice([
        "你要加油哦(^ω^)2",
        "那你明天可以和咱一起玩吗?(星星眼)",
        "记得好好学习听老师的话哦，咱会等你回来的",
        "拜拜，咱才没有想让你放学早点回来呢╭(╯^╰)╮",
        "好好听讲！",
        "咱...咱才没有舍不得你呢…要尽快回来哦"])
    await schoolup.finish(Message(b))


schooldown = on_keyword({"放学", "下课"}, rule=to_me())


@schooldown.handle()
async def _():
    b = random.choice([
        "回来了吗，咱...咱才没有想你",
        "要先吃饭呢～还是先洗澡呢～还是先～吃～咱",
        "是吗……辛苦你了。你这副倔强的样子，真可爱呢（笑）勉强让你躺在咱的腿上休息一下吧，别流口水哟",
        "嗯……勉为其难欢迎你一下吧",
        "想咱了嘛",
        "咱等你很久了",
        "作业记得按时写完啦！"
    ])
    await schoolup.finish(Message(b))


wkdown = on_keyword({"下班"}, rule=to_me())


@wkdown.handle()
async def _():
    b = random.choice([
        "回来了吗，咱...咱才没有想你",
        "要先吃饭呢～还是先洗澡呢～还是先～吃～咱",
        "是吗……辛苦你了。你这副倔强的样子，真可爱呢（笑）勉强让你躺在咱的腿上休息一下吧，别流口水哟",
        "嗯……勉为其难欢迎你一下吧",
        "想咱了嘛",
        "咱等你很久了哼ヽ(≧Д≦)ノ",
        "回来啦！终于下班了呢！累了吗？想吃的什么呀？",
        "工作辛苦了，需要咱为你按摩下吗？",
        "好好休息吧~哼哼~"
    ])
    await wkdown.finish(Message(b))


wkup = on_keyword({"上班"}, rule=to_me())


@wkup.handle()
async def _():
    b = random.choice([
        "乖~咱会等你上班的~",
        "辛苦啦，咱给你个么么哒",
        "咱会为你加油的",
        "专心上班哦，下班后再找咱聊天吧",
        "一路顺风，咱会在家等你回来的",
        "那你明天可以和咱一起玩吗?(星星眼)",
        "咱...咱才没有舍不得你呢…要尽快回来哦"
    ])
    await wkup.finish(Message(b))


wf = on_keyword({"老婆"}, rule=to_me())


@wf.handle()
async def _():
    b = random.choice([
        "咱和你谈婚论嫁是不是还太早了一点呢？",
        "咱在呢(ﾉ>ω<)ﾉ",
        "见谁都是一口一个老婆的人，要不要把你也变成女孩子呢？(*-`ω´-)✄",
        "神经病，凡是美少女都是你老婆吗？",
        "嘛嘛~本喵才不是你的老婆呢",
        "你黐线，凡是美少女都系你老婆啊？",
        "欸...要把咱做成饼吗？咱只有一个，做成饼吃掉就没有了...",
        "已经可以了，现在很多死宅也都没你这么恶心了",
        "不可以",
        "嗯，老公~哎呀~好害羞~嘻嘻嘻~",
        "请...请不要这样，啊~，只...只允许这一次哟~",
        "好啦好啦，不要让大家都听到了，跟咱回家(拽住你)"
    ])
    await wf.finish(Message(b))


msg_last: Dict[int, Message] = {}  # 存储群内最后一条消息
msg_times: Dict[int, int] = {}  # 存储群内最后一条消息被复读的次数
repeater_times: Dict[int, int] = {}  # 存储随机生成的复读上限


async def repeat_rule(event: GroupMessageEvent) -> bool:
    group_id = event.group_id

    # 复读
    if msg_last.get(group_id) == event.message:
        if group_id not in msg_times:
            return False

        msg_times[group_id] += 1
        if group_id not in repeater_times:
            repeater_times[group_id] = random.randint(3, 6)

        if msg_times[group_id] >= repeater_times[group_id]:
            del msg_times[group_id]  # del 掉防止继续复读
            del repeater_times[group_id]
            return True

        return False

    # 不同消息，未复读
    msg_last[group_id] = event.message
    msg_times[group_id] = 1
    return False


async def repeater_matcher_handler(matcher: Matcher, event: GroupMessageEvent):
    # 让下次复读计入次数统计，以便再次打断或复读
    msg_times[event.group_id] = 0
    ms = random.choice(BUILTIN_INTERRUPT_MSG)
    await matcher.finish(MessageSegment.text(ms))


repeater = on_message(rule=repeat_rule, permission=GROUP, priority=99, block=False)
repeater.handle()(repeater_matcher_handler)

# endregion
saber = on_keyword({"saber啊"})


@saber.handle()
async def _():
    b = random.choice([
        "王保卫了国家，可国家没有保卫王，仅此而已。虽然结局很悲惨，但只要过程中没有半点瑕疵，就根本没有必要去奢求。",
        "我追求圣杯是为了履行一项责任，为了履行生前未能履行的一项责任，我想得到圣杯的力量。但是，也许我只是想重新来过而已吧。",
        "无意义的理想，迟早会在现实面前崩溃。",
        "Servant Saber，遵从召唤而来，我问你，你是我的Master吗？",
        "从此吾剑将随汝同在，汝之命运将与吾共存，于此，契约完成。",
        "我拒绝，我要在这里打倒你！",
        "你要是没有胜算的话，就由我来创造胜算，尝试一切可能的方法。",
        "已经可以了，现在很多死宅也都没你这么恶心了",
        "我终于明白了，原来士郎你，就是我的剑鞘啊！",
        "伤害手无寸铁的人，有悖于我身为骑士的誓言。不过，要是Master这么下令的话，我也只能遵从，作为侮辱我尊严的代价，我将取走一个刻印。",
        "比起那种东西，我更需要士郎！我不需要圣杯那种会玷污我的东西！因为我所想要的东西，已经全部都得到了！",
        "四斋蒸鹅心XP",
        "神秘在比其更高的神秘面前，会失去效果。",
        "保卫国家是身为王者的责任，而我却力不从心，至少得重新选出一个合适的王来。",
        "从者是为了战斗而存在的。像今天这样的行动等于是在否定自己的存在。",
        "王者的誓言是不能破坏的，我有自己不得不去完成的使命，我的愿望从一开始就只有一个，从我拔剑之时开始，这份誓言就永远不会改变。",
        "谢谢，多亏你，我终于明白自己该走的道路了。圣杯也好，我也好，都是不应该存在的梦幻，即使这样，我也希望你能原谅我，虽然是个错误的愿望，也是段无法实现的时光，这份软弱，希望你能当它是一名少女所做的一场幻梦。",
        "士郎，最后有一句话不说不行。士郎，我也爱着你。",
        "现在大概没有办法回答这个问题吧。我是你的剑，除了我还有谁能成为你的力量呢？",
        "我做了一个梦。我平时都不常做梦，这次难得有了一次宝贵的体验。",
        "饥饿是大敌。士郎，我们去吃饭吧。"

    ])
    await saber.finish(Message(b))


he = on_keyword({"头发"}, rule=to_me())


@he.handle()
async def _fu():
    a = random.choice([
        "没问题，请尽情的摸吧",
        "发型要乱…乱了啦（脸红）",
        "就让你摸一会哟~(。??ω??。)…"
    ])
    await he.finish(Message(a))


ha = on_keyword({"饿了"}, rule=to_me())


@ha.handle()
async def _fu(event: MessageEvent):
    if event.user_id == SUPERUSER:
        a = random.choice([
            "咱做了爱心便当哦，不介意的话，请让咱来喂你吃吧！",
            "请问主人是想先吃饭，还是先吃咱呢?~",
            "你要咱下面给你吃吗？（捂脸）"
        ])
    else:
        a = random.choice([
            "咱下面给你吃",
            "给你一条咸鱼=￣ω￣=",
            "你饿了吗？咱去给你做饭吃☆ww",
            "不要吃咱>_<",
            "请问你要来点兔子吗？",
            "哎？！你是饿了么。咱会做一些甜点。如果你不会嫌弃的话...就来尝尝看吧。"
        ])
    await ha.finish(Message(a))


ye = on_keyword({"多大"}, rule=to_me())


@ye.handle()
async def _fu():
    a = random.choice([
        "不是特别大但是你摸起来会很舒服的大小喵～",
        "你摸摸看不就知道了吗？（心虚）",
        "不告诉你",
        "咱就不告诉你，你钻到屏幕里来自己确认啊",
        "你指的是什么呀？（捂住胸部）",
        "我可是有几百岁了呢，哼哼...",
        "唉唉唉……这……这种问题，怎么可以……"
    ])
    await ye.finish(Message(a))

sese = on_keyword({"做爱", "h", "操", "草"}, rule=to_me())


@sese.handle()
async def _fu():
    a = random.choice([
        "做这种事情是不是还太早了",
        "噫！没想到你居然是这样的人！",
        "再说这种话，就把你变成女孩子（拿刀）",
        "不想好好和咱聊天就不要说话了",
        "（双手护胸）变....变态！",
        "hentai",
        "你想怎么做呢？",
        "突，突然，说什么啊！baka！",
        "你又在说什么H的东西",
        "咱....咱才不想和你....好了好了，有那么一点点那，对就一点点，哼～",
        "就一下下哦，不能再多了"
    ])
    await sese.finish(Message(a))