import time
import nonebot
from nonebot import on_keyword,on_command,on_startswith,on_notice,on_message
from nonebot.params import CommandArg,Arg,ArgPlainText
from nonebot.adapters.onebot.v11 import Message,GroupIncreaseNoticeEvent,Event
from nonebot.adapters.onebot.v11 import GroupMessageEvent,PrivateMessageEvent,MessageEvent
from nonebot.rule import to_me
from nonebot.permission import SUPERUSER
from nonebot import Bot
from nonebot.adapters.onebot.v11 import MessageSegment, PokeNotifyEvent,bot
import requests,json
from nonebot import require
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
import random
from nonebot import get_driver

read_group_list={254551403,456430003}
@scheduler.scheduled_job("cron", hour="23",misfire_grace_time=10)
async def hour1():
    message=MessageSegment.text("群提醒睡觉小丛雨，提醒你23点到了，再不睡觉就会被恶鬼捉走哦。什...什么，我才不会怕呢！(丛雨也要睡觉了哦）")
    for qq_group in read_group_list:
        await nonebot.get_bot().send_group_msg(group_id=qq_group, message=Message(message))

@scheduler.scheduled_job("cron", hour="8",misfire_grace_time=10)
async def hour1():
    message=MessageSegment.text("群提醒起床小丛雨，提醒你8点到了，再不起床，上课就迟到了。哼，我才不会等你哦，笨蛋主人")
    for qq_group in read_group_list:
        await nonebot.get_bot().send_group_msg(group_id=qq_group, message=Message(message))


word=on_command("丛雨丛雨")
cong_file=["file:///nb/data/voices/wife/1.mp3",
                 "file:///nb/data/voices/wife/2.mp3",
                 "file:///nb/data/voices/wife/3.mp3",
                 "file:///nb/data/voices/wife/4.mp3",
                 "file:///nb/data/voices/wife/5.mp3",
                 "file:///nb/data/voices/wife/6.mp3",
                 "file:///nb/data/voices/wife/7.mp3",
                  "file:///nb/data/voices/wife/8.mp3"]
@word.handle()
async def _s1():
    a=random.randint(0,7)
    cong=cong_file[a]
    await word.send(MessageSegment.record(cong))

word=on_keyword({"色色"},rule=to_me())

@word.handle()
async def _q2():
    await word.finish(MessageSegment.record("file:///nb/data/voices/sese.wav"))

word=on_keyword({"你是笨蛋"},rule=to_me())

@word.handle()
async def _(event:GroupMessageEvent):
    uid=event.user_id
    await word.finish(Message(f"[CQ:at,qq={uid}]你才是笨蛋! qwq"))



word=on_command(("摸头"),rule=to_me())

@word.handle()
async def s1(event:GroupMessageEvent):
    bot = nonebot.get_bot("2460683855")
    message=MessageSegment.image("file:///nb/data/images/miao.jpg")
    await bot.call_api("send_group_msg",**{"group_id":event.group_id,"message":message})

def _check(event: PokeNotifyEvent):
    return event.target_id==event.self_id

agree_list=[1371006609]
poko=on_notice(rule=_check)
@poko.handle()
async def _poko(event: PokeNotifyEvent):
    if(event.user_id in agree_list):
        await poko.finish((MessageSegment.record("file:///nb/data/voices/2.wav"))
)
    else:
      await poko.finish(MessageSegment.record("file:///nb/data/voices/smile.wav"))
#C:\SQL\qq\nb\houduan\data\images



point=on_command("来点萝莉")

@point.handle()
async def get_url():
    try:
        url = "https://api.lolicon.app/setu/v2"
        content = requests.post(url,timeout=15).text
        content = json.loads(content)
        img_url = content["data"][0]["urls"]["original"]
        await point.send(MessageSegment.image(img_url))
    except:
        await point.finish(MessageSegment.text("没有萝莉！"))


point=on_command("来点二次元")

@point.handle()
async def get_url():
        url = "https://img.xjh.me/random_img.php?return=302"
        c2 = requests.get(url).content
        await point.finish(MessageSegment.image(c2))

point=on_command("来点涩涩")

@point.handle()
async def get_url():
        x=3
        url = "https://iw233.cn/API/Random.php"
        c2 = requests.get(url).content
        with open("tmp/{}.jpg".format(x), "wb") as f:
            f.write(c2)
        await point.finish(MessageSegment.image(c2))


#https://acg.7585.net.cn/acg
#https://www.dmoe.cc/random.php
word=on_command("喜欢你",permission=SUPERUSER)
@word.handle()
async def _s():
      await word.finish(MessageSegment.record("file:///nb/data/voices/dasuki.wav"))

word=on_command("丛雨色色",permission=SUPERUSER)
@word.handle()
async def _se():
      await word.finish(MessageSegment.record("file:///nb/data/voices/h.wav"))


word=on_command("早安")
@word.handle()
async def zao():
    await word.finish(MessageSegment.record("file:///nb/data/voices/zaoan.wav"))


word=on_command("晚安")
@word.handle()
async def zao():
    await word.send("要乖乖睡觉哦")
    await word.finish(MessageSegment.record("file:///nb/data/voices/wanan.wav"))


word=on_command("好耶")
@word.handle()
async def sa():
    await  word.finish(MessageSegment.image("file:///nb/data/images/haoye.jpg"))

word=on_command("对不起")
@word.handle()
async def se():
    await  word.finish(MessageSegment.image("file:///nb/data/images/sorry.jpg"))

word = on_command("丛雨丛雨丛？")

@word.handle()
async def cong():
    await  word.finish(MessageSegment.image("file:///nb/data/images/cong.jpg"))

word=on_command("丛雨亲亲")
@word.handle()
async def _bak():
      await word.finish(MessageSegment.record(file=r"file:///nb/data/voices/bak.wav"))

point=on_command("来点动漫")

@point.handle()
async def get_url():
        x =random.randint(1,100)
        url = "http://api.mtyqx.cn/api/random.php"
        content1 = requests.post(url).content
        with open("tmp/{}.jpg".format(x), "wb") as f:
            f.write(content1)

        await point.finish(MessageSegment.image(content1))

point = on_command("舔狗日记")


@point.handle()
async def get():
    with open("./data/tiangou/tiangou.json", "r", encoding="utf-8") as f:
        txt = f.read()
    tx = json.loads(txt)
    i=random.randint(0,279)
    tt1 = tx["data"][i]
    await point.finish(MessageSegment.text(tt1))


word=on_command("丛雨帮助")
@word.handle()
async def _help():
      msg=MessageSegment.image("file:///nb/data/images/help.png")
      await word.finish(msg)

word = on_command("揉揉丛雨")
@word.handle()
async def _bak():
    await word.finish(MessageSegment.record("file:///nb/data/voices/b.wav"))

word = on_command("抱抱丛雨")

@word.handle()
async def _bak():
    await word.finish(MessageSegment.record("file:///nb/data/voices/baobao.wav"))


word=on_command("摸摸丛雨")
@word.handle()
async def se():
    await  word.finish(MessageSegment.image("file:///nb/data/images/momo.gif"))


word=on_command("爱莉")
@word.handle()
async def se():
    await  word.finish(MessageSegment.image("file:////nb/data/images/aili.jpg"))

word=on_command("别在这理发店")
@word.handle()
async def se():
    await  word.finish(MessageSegment.image("file:///nb/data/images/fadian.jpg"))

word=on_command("丛雨骂！")
@word.handle()
async def se():
    await  word.finish(MessageSegment.image("file:///nb/data/images/fabing.jpg"))

word=on_command("我生气了")
@word.handle()
async def se():
    await  word.finish(MessageSegment.image("file:///nb/data/images/s1.jpg"))


luck=on_command("今日运势")
@luck.handle()
async def luck1(args: Message = CommandArg()):
    msg = args.extract_plain_text().strip()
    if msg:
        star = msg

@luck.got("star",prompt="请输入你的星座哦")
async def handle_luck(event, star_name: str = ArgPlainText("star")):
    if star_name is None:
        await luck.send(MessageSegment.text("小丛雨不认识呢QWQ"))
    else:
        try:
            url = "https://v.api.aa1.cn/api/xingzuo/?msg=" + star_name
            c = requests.get(url, timeout=20).text
            c = json.loads(c)
            a1 = c["cfys"]
            a2 = c["ztys"]
            a3 = c["aqys"]
            a4 = c["ts"]
            d2 = "财运:"+a2+'\n'
            d1 = "整体运势:"+a1+'\n'
            d3 = "爱情运:"+a3+'\n'
            d4 = "提示："+a4
            d = '\n'+d1+d2+d3+d4
            await luck.send(MessageSegment.at(event.user_id)+MessageSegment.text(d))
        except:
            await luck.finish("小丛雨今天休息了哦~")



#https://api.7585.net.cn/luck/api.php?return=

#c=json.dumps(c,ensure_ascii=False)


word = on_command("发癫")

@word.handle()
async def _():
    await word.finish(MessageSegment.record("file:///nb/data/voices/dadian.wav"))


word = on_command("幼刀")

@word.handle()
async def _():
    await word.finish(MessageSegment.record("file:///nb/data/voices/youdao.mp3"))

word = on_command("睡觉了",permission=SUPERUSER)

@word.handle()
async def _():
    await word.finish(MessageSegment.record("file:///nb/data/voices/wanan.mp3"))

word = on_command("好累",rule=to_me())

@word.handle()
async def _():
    await word.finish(MessageSegment.record("file:///nb/data/voices/lei.mp3"))

word = on_command("平胸丛雨")

@word.handle()
async def _():
    await word.finish(MessageSegment.record("file:///nb/data/voices/xiong.mp3"))

word=on_command("肚肚饿饿")
@word.handle()
async def se():
    await  word.finish(MessageSegment.image("file:///nb/data/images/v50.jpg"))

def _ch(event:GroupMessageEvent):
    return event.group_id==615488207

tyfile=("file:///nb/data/images/tianyi1.jpg",
           "file:///nb/data/images/tianyi2.jpg",
            "file:///nb/data/images/tianyi3.gif",
            "file:///nb/data/images/tianyi4.jpg")
word=on_command("天一小天使",rule=_ch)
@word.handle()
async def _se():
    t=random.randint(0,3)
    m=str(tyfile[t])
    await word.send(MessageSegment.image(m))

word=on_command("不好评价")
@word.handle()
async def se():
    await word.finish(MessageSegment.image("file:///nb/data/images/liuhan.jpg"))

word=on_command("炫我嘴里")
@word.handle()
async def se():
    await word.finish(MessageSegment.image("file:///nb/data/images/a.jpg"))

word=on_command("丛雨?")
@word.handle()
async def se():
    await word.finish(MessageSegment.image("file:///nb/data/images/haoqi.jpg"))
#luk=on_keyword({"丛雨抽签","我要抽签！"})

luk=on_command("。抽签")
@luk.handle()
async def _luk(event):
    try:
     url="https://api.fanlisky.cn/api/qr-fortune/get/"
     m=str(event.user_id)
     url=url+m
     print(url)
     a=requests.get(url,timeout=50).text
     a = json.loads(a)
     a1=a["data"]["fortuneSummary"]
     a2=a["data"]["signText"]
     a3=a["data"]["luckyStar"]
     b=a1+a2
     d1="今日运势:"+a1+" "
     d3="幸运指数:"+a3+" "
     d2="评价为:"+a2+" "
     d=MessageSegment.at(event.user_id)+"\n"+MessageSegment.text(d1)+"\n"+MessageSegment.text(d3)+"\n"+MessageSegment.text(d2)
     await luk.send(Message(d))
    except:
        c=MessageSegment.text("不许抽签！")+MessageSegment.image("file:///nb/data/images/s1.jpg")
        await luk.finish(Message(c))

point = on_command("。setu")


@point.handle()
async def get_url(args=CommandArg()):
    msg = args.extract_plain_text().strip()

@point.got("msg",prompt="你的tag是？")
async def _msg(event,ms: str = ArgPlainText("msg")):
    try:
        url = "https://api.lolicon.app/setu/v2?tag="
        u = url + ms
        content = requests.post(u,timeout=15).text
        content = json.loads(content)
        c2 = content["data"][0]["urls"]["original"]
        c4=MessageSegment.at(event.user_id)+MessageSegment.image(c2)
        await point.send(Message(c4))
    except:
        await point.finish(MessageSegment.text("你的xp太怪了哦"))


word = on_keyword({"mua", "啾咪","亲亲"},rule=to_me())

@word.handle()
async def _():
      a=random.choice([
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

pom=on_keyword({"丛雨摸摸头","丛雨揉揉"})

@pom.handle()
async def _(event:GroupMessageEvent):
    if(event.user_id!=SUPERUSER):
       a=random.choice([
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
        "唔... 手...好温暖呢.....就像是......新出炉的蛋糕",
        "走开啦，咱喵说过，被摸头会长不高的啦~~~",
        ])
       await pom.finish(MessageSegment.text(a))
    else:
        a=random.choice([
            "你的手总是那么暖和呢~",
            "舒服w，蹭蹭~",
            "唔。。头发要乱啦",
            "唔... 手...好温暖呢.....就像是......新出炉的蛋糕",
            "呼噜呼噜～",
            "不可以总摸的哦，不然的话，会想那个的wwww",
            "欸，现在么..也不是不可以啦(小小声)",
            "呜姆呜姆~~~w（害羞，兴奋）主人喵~（侧过脑袋蹭蹭你的手",
            "不可以摸啦~其实咱已经...了QAQ会弄脏你的手的"])
        await pom.finish(MessageSegment.text(a))

word0 = on_keyword({"贴贴","丛雨贴贴"},rule=to_me())

@word0.handle()
async def _():
        a=random.choice([
        "贴什么贴.....只......只能......一下哦！",
        "贴...贴贴（靠近）",
        "蹭蹭…你以为咱会这么说吗！baka死宅快到一边去啦！",
        "你把脸凑这么近，咱会害羞的啦Σ>―(〃°ω°〃)♡→",
        "退远",
        "不可以贴"])
        await word0.finish(MessageSegment.text(a))

ne=on_keyword({"抱抱","丛雨抱","要抱抱"},rule=to_me())
@ne.handle()
async def _fu():
        a=random.choice([
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

se1=on_command("看看")
@se1.handle()
async def _(args=CommandArg()):
    a=args.extract_plain_text()
    a=str(a)
    if(a=="内裤" or a=="胖次"):
        b=random.choice(
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
    elif (a=="内衣"):
        c=random.choice([
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
    elif (a=="批" or a=="欧派"):
        d=random.choice( ["你在说什么呀，再这样，咱就不理你了！",
        "咱觉得有话就应该好好说..",
        "讨厌，别摸啦(///ω///)",
        "你个变态！把手拿开！",
        "啊～那…那里～不可以",
        "没有，走开！","大笨蛋——！"])
        await se1.finish(Message(d))

    elif(a=="你的" or a=="丛雨"):
        await se1.finish(Message("看什么呢你！"))

    else:
        await se1.finish()

ne=on_keyword({"咕咕","咕"})
@ne.handle()
async def _fu():
    a=random.choice([
        "咕咕咕是要被当成鸽子炖的哦(:з」∠)_",
        "咕咕咕",
        "咕咕咕是不好的行为呢_(:з」∠)_",
        "鸽德警告！",
        "☆ﾐ(o*･ω･)ﾉ 咕咕咕小鸽子是会被炖掉的",
        "当大家都以为你要鸽的时候，你鸽了，亦是一种不鸽",
        "这里有一只肥美的咕咕，让咱把它炖成美味的咕咕汤吧(੭•̀ω•́)੭"
    ])
    await ne.finish(Message(a))

suki=on_keyword({"suki","喜欢","好き"},rule=to_me())
@suki.handle()
async def ew():
    a=random.choice([
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

suki=on_keyword({"炸了","丛雨没了"})
@suki.handle()
async def ew():
    a=random.choice([
        "你才炸了！",
        "才没有呢",
        "咱好好的呀",
        "过分！"
    ])
    await suki.finish(Message(a))

ne=on_keyword({"来点色色","涩图"})
@ne.handle()
async def _fu():
    a=random.choice([
        "没有，有也不给",
        "天天色图色图的，今天就把你变成色图！",
        "咱没有色图",
        "哈？你的脑子一天都在想些什么呢，咱才没有这种东西啦。"
    ])
    await ne.finish(MessageSegment.text(a))

m=on_keyword({"喵喵","喵呜"})
@m.handle()
async def _():
     a=random.choice( [
        "诶~~小猫咪不要害怕呦，在姐姐怀里乖乖的，姐姐带你回去哦。",
        "不要这么卖萌啦~咱也不知道怎么办丫",
        "摸头⊙ω⊙",
        "汪汪汪！",
        "嗷~喵~",
        "喵~？喵呜~w"
    ])
     await m.finish(Message(a))

ae=on_command("awsl")
@ae.handle()
async def _():
    a=random.choice([
        "你别死啊！（抱住使劲晃）",
        "你别死啊！咱又要孤单一个人了QAQ",
        "啊！怎么又死了呀"
    ])
    await ae.finish(Message(a))

ae=on_command("rua")
@ae.handle()
async def _():
    a=random.choice([
        "略略略～（吐舌头）",
        "rua！",
        "mua~",
        "略略略",
        "mua～⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄",
        "摸了",
        "嘁，丢人（嫌弃脸）"
    ])
    await ae.finish(Message(a))

ae=on_keyword({"吃掉"})
@ae.handle()
async def _():
    a=random.choice( [
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

ae=on_command(("可爱"),rule=to_me())
@ae.handle()
async def _():
    a=random.choice([
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

ae2=on_keyword({"早上好","早早早","早呀","哦哈呦"})
@ae2.handle()
async def _():
    a=random.choice(["早喵~",
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


ae3=on_keyword({"炼铜","萝莉控"})
@ae3.handle()
async def _():
    b=random.choice([
         "炼铜有什么好玩的，和咱一起玩吧",
         "炼铜不如恋咱",
         "你也是个炼铜术士嘛？",
         "信不信咱把你按在水泥上摩擦？",
         "炼，都可以炼！",
         "大hentai！一巴掌拍飞！(╯‵□′)╯︵┻━┻",
         "锻炼什么的咱才不需要呢 （心虚地摸了摸自己的小肚子）",
         "把你的头按在地上摩擦",
         "你在盯着什么地方看！变态萝莉控！"])
    await ae3.finish(Message(b))

e=on_command("查询疫情")
@e.handle()
async def _(foo:Message=CommandArg()):
            a = str(foo).split(",")
            url="https://interface.sina.cn/news/ncp/data.d.json?mod=risk_level&areaname=" + str(f'{a[0]}|{a[1]}|')
            print(url)
            b = requests.get(url,
                             headers={
                                 "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"})
            b=b.json()
            if b["data"]["highNum"] != 0:
               c = ["!——查询的高风险地区————"]
               for i in range(len(b["data"]["high"])):
                   c.append(str(i + 1) + str(f'.{b["data"]["high"][i]["county"]}'))
               hn = b["data"]["highNum"]
               c= ''.join(c)
               s=MessageSegment.text(c)+MessageSegment.text("\n")+MessageSegment.text(f"高风险地区数：{hn}")

               await e.send(Message(s))

            else:

                    await e.send(Message(f"{a[0]}{a[1]}没有高风险哦"))


dfile=("file:////nb/data/voices/dinggong/1.wav",
           "file:////nb/data/voices/dinggong/2.wav",
            "file:////nb/data/voices/dinggong/3.wav",
            "file:////nb/data/voices/dinggong/4.wav",
        "file:////nb/data/voices/dinggong/5.wav",
       "file:////nb/data/voices/dinggong/6.wav")
d=on_command("钉宫",rule=to_me())
@d.handle()
async def _():
    a=random.randint(0,5)
    ad=dfile[a]
    ad=MessageSegment.record(ad)
    await d.send(ad)


word = on_keyword({"苦呀西", "可狠", "不甘心","库鲁西"})


@word.handle()
async def se():
    await word.finish(MessageSegment.image("file:///nb/data/images/kuyaxi.jpg"))

def _rule(event: Event):
    return isinstance(event, GroupIncreaseNoticeEvent)

join=on_notice(rule=_rule)
@join.handle()
async def group_increase_handle(event: GroupIncreaseNoticeEvent):
    m = MessageSegment.at(event.user_id)+MessageSegment.text('欢迎你哦！QWQ，想知道我的功能，请发送“丛雨帮助”吧！')
    await join.finish(Message(m))
    

point1 = on_command(".搜索色图")


@point1.handle()
async def get_url(args=CommandArg()):
    msg = args.extract_plain_text().strip()


@point1.got("msg",prompt="你的tag是？")
async def _msg1(event, msg: str = ArgPlainText("msg")):
    try:
        url = "http://a60.one:404/get/tags/"
        muo = url + msg
        con = requests.get(muo).text
        content = json.loads(con)
        c2 = content["data"]["imgs"][0]["url"]
        c4 = MessageSegment.at(event.user_id)+MessageSegment.image(c2)
        await point1.send(Message(c4))
    except:
        await point1.finish(MessageSegment.text("你的xp太怪了哦"))

word=on_keyword({"test"})

@word.handle()
async def _q2():
    await word.finish(MessageSegment.record("https://www.nekomiacg.top/voice/1.wav"))

za = ["file:///nb/data/images/zako/1.jpg",
      "file:///nb/data/images/zako/2.jpg",
      "file:///nb/data/images/zako/3.jpg",
      "file:///nb/data/images/zako/4.jpg",
      "file:///nb/data/images/zako/5.jpg",
      "file:///nb/data/images/zako/6.jpg"]
zav = ["file:///nb/data/voices/zako/1.wav",
       "file:///nb/data/voices/zako/2.wav",
       "file:///nb/data/voices/zako/3.wav",
       "file:///nb/data/voices/zako/4.wav"]
wordz = on_keyword({"雌小鬼", "杂鱼", "杂~鱼"})


@wordz.handle()
async def _():
    a = random.randint(1, 25)
    print(a)
    if a < 7:
        b = za[a-1]
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
        zc = c[a-7]
        await wordz.finish(MessageSegment.text(zc))
    else:
        d = zav[a-22]
        await wordz.finish(MessageSegment.record(d))

pointb = on_command(".发病")


@pointb.handle()
async def _(args=CommandArg()):
    a=args.extract_plain_text()
    target=str(a)
    with open("./data/ill/fadian.json", "r", encoding="UTF-8") as f:
        T = json.loads(f.read())["data"]
    if len(target) >= 15:
        await pointb.finish(Message("字数太长啦,谁名字这么长呢"))
    else:
        await pointb.finish(Message(random.choice(T).format(target=target)))



