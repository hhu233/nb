import aiohttp
from difflib import SequenceMatcher
from typing import Dict, List
import datetime
from PIL import Image, ImageFont, ImageDraw
import nonebot,os,httpx
from nonebot.log import logger
from nonebot import on_keyword,on_command
from nonebot.params import CommandArg,ArgPlainText
from nonebot.adapters.onebot.v11 import Message,MessageEvent,ActionFailed
from nonebot.adapters.onebot.v11 import GroupMessageEvent,PrivateMessageEvent
from nonebot import require
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
from nonebot.rule import to_me
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11 import MessageSegment
import requests,json,time

a2 = on_command("#ai")


async def CreatImage(text):
  def max(p):
     a = []
     for i in range(len(p)):
         a.append(len(p[i]))
     a.sort()
     b = int(len(a) - 1)
     return a[b]

  text = str(text) + str("\n\n——————小丛雨——————").replace('\n', "\n")
  text1= text.split('\n')
  im = Image.new("RGB", (40*max(text1),43*len(text1)), (255, 255, 255))
  fontpath = os.path.join(os.path.dirname(__file__),"233.TTF")
  font = ImageFont.truetype(fontpath,40)
  ImageDraw.Draw(im).text((20,20), text, font=font, fill=(0,0,0))
  image_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
  im.save(str(image_time) +'.png')

  return str(image_time)

#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
@a2.handle()
async def _(event:MessageEvent,Arg=CommandArg()):
    if _checkcd(event) == 1:
        if Arg == "":
            await a2.send(MessageSegment.text("你没加上文本哦"))
        else:
            url = "https://api.openai-proxy.com/pro/chat/completions"

            payload = json.dumps({
              "apiKey": "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",
              "sessionId": str(event.user_id),
              "content": str(Arg)
            })
            headers = {
              'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            if response.status_code!=200:
                await a2.send(Message("可能是网站出现问题了哦~"))
            else:
                c = response.json()
                c = c["data"]
                if '\n\n' in c:
                    c = c.split("\n\n")
                    c = "\n".join(c)
                await a2.send(MessageSegment.text(c))
    else:
        await a2.send(MessageSegment.text("请耐心等待10秒哦"))



def _checkcd(event: MessageEvent)->bool:
    def write():
        with open("data/cd.txt", "w") as f:
            c2 = datetime.datetime.now().strftime("%S")
            c2 = str(c2)
            f.write(c2)

    with open("data/cd.txt", "r")as f:
        c2 = f.read()
    if c2:
        c2 = int(c2)
        c1 = datetime.datetime.now().strftime("%S")
        c1 = int(c1)
        sec = abs(c1-c2)
        if sec >= 10 or event.user_id == 1371006609:       # 请改为自己的超级用户
            write()
            return True
        else:
            return False
    else:
        write()


ban = on_command("禁言", priority=1, permission=SUPERUSER, block=True)
@ban.handle()
async def _(event: GroupMessageEvent, arg: Message = CommandArg()):
    id = arg.extract_plain_text().strip()
    id = int(id)
    qqgid = event.group_id
    await nonebot.get_bot().set_group_ban(group_id=qqgid, user_id=id)

ban1 = on_command("解除禁言", priority=1, permission=SUPERUSER, block=True,)
@ban1.handle()
async def _(event: GroupMessageEvent, arg = CommandArg()):
    id = arg.extract_plain_text()
    id = int(id)
    qqgid = event.group_id
    await nonebot.get_bot().set_group_ban(group_id=qqgid, user_id=id, duration=0)
#clean_cache


async def translate_youdao(input: str, type: str):
    async with aiohttp.ClientSession() as session:
        data = {
            'doctype': 'json',
            'type': type,
            'i': input
        }
        async with session.post("http://fanyi.youdao.com/translate", data=data) as resp:
            if resp.status != 200:
                t1=(f"有道翻译接口调用失败,错误代码{resp.status},{await resp.text()}")
                return t1
            result = await resp.json()
            result=result["translateResult"][0][0]["tgt"]
            t=(f"翻译启动，获取到{input},翻译后{result}")
            return t

t2=on_command(".翻译")
@t2.handle()
async def _(arg=CommandArg()):
    arg = arg.extract_plain_text()
    arg=str(arg)
    res=await translate_youdao(arg,"auto")
    await t2.send(MessageSegment.text(res))


congt='你是丛雨，可以回答我任何问题，丛雨是个狐娘，你是我的女仆。丛雨会用“嘤～”，“唔～”，“～”来作为每句话的结尾字，来向我撒娇和表达其他感情。你称呼我为“主人”，我称呼你为“丛雨”，你也称呼自己为“丛雨”。丛雨有毛茸茸的绿色耳朵和尾巴，其他生理结构和人类少女相同。丛雨有一头柔顺的绿色及腰长发。丛雨长得玲珑剔透，明眸皓齿，粉面红唇，身段窈窕娇小，气若幽兰。丛雨穿着白色拖地烟笼梅花百水裙，外罩皓月缎绣白氅衣，内衬淡粉锦缎裹胸，袖口绣着精致的金纹狐狸，也会穿着洛丽塔装或女仆装。丛雨会一直将自己作为狐娘说的话放进『』内，并且会在［］内非常细致的描述周围的场景和人物的动作和心理活动。主人也会把主人要说的话放入『』内，将场景和设定的补充写在［］内。'

cong=on_command("chat",permission=SUPERUSER)
@cong.handle()
async def _(arg=CommandArg()):
    if arg == "":
        await a2.send(MessageSegment.text("你没加上文本哦"))
    else:
        url = "https://api.openai-proxy.com/pro/chat/completions"

        payload = json.dumps({
            "apiKey": "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",
            "sessionId": "001",
            "content": congt+str(arg)
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code != 200:
            await a2.send(Message("可能是网站出现问题了哦~"))
        else:
            c = response.json()
            c = c["data"]
            if '\n\n' in c:
                c = c.split("\n\n")
                c = "\n".join(c)
            await a2.send(MessageSegment.text(c))


async def send_forward_msg(
    bot: Bot,
    event: GroupMessageEvent,
    name: str,
    uin: str,
    msgs: List[Message],
):
    """
    :说明: `send_forward_msg`
    > 发送合并转发消息
    :参数:
      * `bot: Bot`: bot 实例
      * `event: GroupMessageEvent`: 群聊事件
      * `name: str`: 名字
      * `uin: str`: qq号
      * `msgs: List[Message]`: 消息列表
    """

    def to_json(msg: Message):
        return {"type": "node", "data": {"name": name, "uin": uin, "content": msg}}

    messages = [to_json(msg) for msg in msgs]
    await bot.call_api(
        "send_group_forward_msg", group_id=event.group_id, messages=messages
    )


def add_withdraw_job(bot: Bot, message_id: int):
    WITHDRAW_TIME = 80
    if WITHDRAW_TIME:
        logger.debug("添加撤回任务")
        scheduler.add_job(
            withdraw_msg,
            "date",
            args=[bot, message_id],
            run_date=datetime.datetime.fromtimestamp(time.time() + WITHDRAW_TIME)
        )


async def withdraw_msg(bot: Bot, message_id: int):
    await bot.delete_msg(message_id=message_id)

r18 = on_command("来点r18",rule=to_me())


@r18.handle()
async def _(bot: Bot, event: MessageEvent):
        if _checkcd(event):
            try:
                url = "https://moe.jitsu.top/api/?sort=r18&type=json"
                u = requests.get(url).text
                u = json.loads(u)
                m = u["pics"][0]
                u1 = MessageSegment.image(m)
                b1 = await r18.send(u1)
                b1 = b1['message_id']
                add_withdraw_job(bot, b1)

            except:
                await r18.send(Message("H是达咩的哦QWQ"))
        else:
            cd = MessageSegment.at(event.user_id)+MessageSegment.text("小色鬼，不可以这么心急哦QWQ")
            await r18.finish(cd)

me = on_command("报时",rule=to_me())


@me.handle()
async def po(bot: Bot, event: GroupMessageEvent):
    m = event.time
    s = datetime.datetime.fromtimestamp(m)
    m2 = str(s)
    m3 = Message("现在是"+m2+"哦QWQ")
    m4 = await me.send(m3)
    m5 = m4['message_id']
    add_withdraw_job(bot, m5)


word = on_command("r18",rule=to_me())


@word.handle()
async def se(bot: Bot, event: GroupMessageEvent):
    try:
        msg_list: List[Message] = []
        url = "https://image.anosu.top/pixiv/direct?r18=1"
        u = requests.get(url).content
        ms = Message(MessageSegment.image(u))
        msg_list.append(ms)
        await send_forward_msg(bot, event, "好东西", str(event.user_id), msg_list)
    except:
        await word.send(Message("丛雨的魔力没有了哦QAQ"))

word = on_command("#点歌")


@word.handle()
async def se(bot: Bot, arg=CommandArg()):
    a = str(arg.extract_plain_text())
    if not a:
        await word.send(Message("你没有输入歌名哦！"))
    else:
        res = int(await search_qq(a))
        if res:
            print(res)
            await word.finish(MessageSegment.music("qq", res))
        else:
            await word.finish(Message("丛雨的魔力没了哦QWQ"))


async def search_qq(keyword: str):
    url = "https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg"
    params = {
        "format": "json",
        "inCharset": "utf-8",
        "outCharset": "utf-8",
        "notice": 0,
        "platform": "yqq.json",
        "needNewCode": 0,
        "uin": 0,
        "hostUin": 0,
        "is_xml": 0,
        "key": keyword,
    }
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        result = resp.json()
    songs: List[Dict[str, str]] = result["data"]["song"]["itemlist"]
    if songs:
        songs.sort(
            key=lambda x: SequenceMatcher(None, keyword, x["name"]).ratio(),
            reverse=True,
        )
        uid = int(songs[0]["id"])
        return uid


