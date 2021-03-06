import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("f!")
TOKEN = "token"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='Memes',
                description="Memes",
                brief="Memes",
                aliases=['dankmemes', 'memes', 'dank_memes'],
                pass_context=True)
async def memes(context):
    possible_responses = [
        'https://i.imgur.com/Zidrf3X.jpg',
        'https://i.imgur.com/TLuw0v7.jpg',
        'https://i.imgur.com/N6wmbF7.jpg',
        'https://i.imgur.com/vwcX28T.jpg',
        'https://i.imgur.com/kdW0Qhp.jpg',
        'https://i.imgur.com/g3xCrYX.jpg',
        'https://i.imgur.com/goHL8Uf.jpg',
        'https://i.imgur.com/iRBQzDg.jpg',
        'https://i.imgur.com/TxNKukD.jpg',
        'https://i.imgur.com/4HFzvyd.jpg',
        'https://i.imgur.com/PUQSd1p.jpg',
        'https://i.imgur.com/8xzoF7v.jpg',
        'https://i.imgur.com/m8nJngK.jpg',
        'https://i.imgur.com/0WuLg6z.jpg',
        'https://i.imgur.com/EPN90cd.jpg',
        'https://i.imgur.com/d4EGJ6I.jpg',
        'https://i.imgur.com/OBwk8WF.jpg',
        'https://i.imgur.com/YWjbAgo.jpg',
        'https://i.imgur.com/glfeRgj.jpg',
        'https://i.imgur.com/iV8yViE.jpg',
        'https://i.imgur.com/1fYVIqY.jpg',
        'https://i.imgur.com/xnSTAJ7.jpg',
        'https://i.imgur.com/MjPeN7C.jpg',
        'https://i.imgur.com/OcTwULk.jpg',
        'https://i.imgur.com/rFEPLu5.jpg',
        'https://i.imgur.com/GYMNgHq.jpg',
        'https://i.imgur.com/vzBcCoH.jpg',
        'https://i.imgur.com/gl4DAcK.jpg',
        'https://i.imgur.com/T75fX5V.jpg',
        'https://i.imgur.com/HPYCToX.jpg',
        'https://i.imgur.com/vhfLj5r.jpg',
        'https://i.imgur.com/kWVCMHW.jpg',
        'https://i.imgur.com/GDU0xEL.jpg',
        'https://i.imgur.com/RwDidsG.jpg',
        'https://i.imgur.com/JNU3TL5.jpg',
        'https://i.imgur.com/7fNpmjS.jpg',
        'https://i.imgur.com/aIin9pb.jpg',
        'https://i.imgur.com/uGDr0JI.jpg',
        'https://i.imgur.com/Ygw3xSb.jpg',
        'https://i.imgur.com/xzdDcKr.jpg',
        'https://i.imgur.com/ghSAeEs.jpg',
        'https://i.imgur.com/10VffJD.jpg',
        'https://i.imgur.com/7bpRo6T.jpg',
        'https://i.imgur.com/4tcgats.jpg',
        'https://i.imgur.com/zn3zv30.jpg',
        'https://i.imgur.com/gOAdBZA.jpg',
        'https://i.imgur.com/x3YFf0J.jpg',
        'https://i.imgur.com/zpbETA4.jpg',
        'https://i.imgur.com/QzgSWW0.jpg',
        'https://i.imgur.com/SbfXkv0.jpg',
        'https://i.imgur.com/qRPSE1O.jpg',
        'https://i.imgur.com/0MpWgNr.jpg',
        'https://i.imgur.com/tHCI6yU.jpg',
        'https://i.imgur.com/O8RQzE8.jpg',
        'https://i.imgur.com/Fg6ku1K.jpg',
        'https://i.imgur.com/yewdERV.jpg',
        'https://i.imgur.com/wdAfJWt.jpg',
        'https://i.imgur.com/UWNJXeJ.jpg',
        'https://i.imgur.com/tuJtabW.jpg',
        'https://i.imgur.com/yf3DbmC.jpg',
        'https://i.imgur.com/LyavqfF.jpg',
        'https://i.imgur.com/f2HEIfu.jpg',
        'https://i.imgur.com/ttDvz01.jpg',
        'https://i.imgur.com/QNWXaux.jpg',
        'https://i.imgur.com/8mdSMlH.jpg',
        'https://i.imgur.com/BtrzYPd.jpg',
        'https://i.imgur.com/PwKmauw.jpg',
        'https://i.imgur.com/jZng2sv.jpg',
        'https://i.imgur.com/MJ7yA8a.jpg',
        'https://i.imgur.com/xJFl8iy.jpg',
        'https://i.imgur.com/v2A3CIX.jpg',
        'https://i.imgur.com/cJouSqG.jpg',
        'https://i.imgur.com/0K8815R.jpg',
        'https://i.imgur.com/uHVUiTs.jpg',
        'https://i.imgur.com/3LduFci.jpg',
        'https://i.imgur.com/dAhoW8v.jpg',
        'https://i.imgur.com/2e9hwgG.jpg',
        'https://i.imgur.com/Ofnz1So.jpg',
        'https://i.imgur.com/0SDhjdd.jpg',
        'https://i.imgur.com/Ez07d9V.jpg',
        'https://i.imgur.com/h1YKQbL.jpg',
        'https://i.imgur.com/pTyuL2y.jpg',
        'https://i.imgur.com/zz7UD2K.jpg',
        'https://i.imgur.com/NefEjfa.jpg',
        'https://i.imgur.com/jMmLVn6.jpg',
        'https://i.imgur.com/lUBdIcY.jpg',
        'https://i.imgur.com/RSXYngk.jpg',
        'https://i.imgur.com/2fa6fro.jpg',
        'https://i.imgur.com/oPqv08w.jpg',
        'https://i.imgur.com/a0V5JYX.jpg',
        'https://i.imgur.com/QpfnBLf.jpg',
        'https://i.imgur.com/v7Q6uju.jpg',
        'https://i.imgur.com/iuzyat4.jpg',
        'https://i.imgur.com/bohDhsu.jpg',
        'https://i.imgur.com/hqCFBlp.jpg',
        'https://i.imgur.com/zWxMR8V.jpg',
        'https://i.imgur.com/EPJyzZP.jpg',
        'https://i.imgur.com/zWOZyNJ.jpg',
        'https://i.imgur.com/J8pjCoF.jpg',
        'https://i.imgur.com/Vuj51b7.jpg',
        'https://i.imgur.com/2ZYQddA.jpg',
        'https://i.imgur.com/DhbGq0P.jpg',
        'https://i.imgur.com/hWpweDz.jpg',
        'https://i.imgur.com/VycSwlU.jpg',
        'https://i.imgur.com/auvCmex.jpg',
        'https://i.imgur.com/FCsWuaG.jpg',
        'https://i.imgur.com/nhWgXi7.jpg',
        'https://i.imgur.com/51JA75S.jpg',
        'https://i.imgur.com/QDA1lCT.jpg',
        'https://i.imgur.com/Yr1bzaP.jpg',
        'https://i.imgur.com/BQR2z68.jpg',
        'https://i.imgur.com/Kv07te5.jpg',
        'https://i.imgur.com/G1ecWTZ.jpg',
        'https://i.imgur.com/eF9sTv2.jpg',
        'https://i.imgur.com/jr56PlS.jpg',
        'https://i.imgur.com/1ycpkGc.jpg',
        'https://i.imgur.com/hygCO9w.jpg',
        'https://i.imgur.com/rijj0Rw.jpg',
        'https://i.imgur.com/gjddLfE.jpg',
        'https://i.imgur.com/AzoCYbH.jpg',
        'https://i.imgur.com/OzQEetJ.jpg',
        'https://i.imgur.com/Wkd0vvQ.jpg',
        'https://i.imgur.com/x3VqbfP.jpg',
        'https://i.imgur.com/zA2jA1o.jpg',
        'https://i.imgur.com/iwnPNrC.jpg',
        'https://i.imgur.com/SKNlxKM.jpg',
        'https://i.imgur.com/pORbkf5.jpg',
        'https://i.imgur.com/vBAHJBA.jpg',
        'https://i.imgur.com/JeXiYbZ.jpg',
        'https://i.imgur.com/wwQLiKE.jpg',
        'https://i.imgur.com/dyiRtW1.jpg',
        'https://i.imgur.com/YN6GQHl.jpg',
        'https://i.imgur.com/tH8kqhI.jpg',
        'https://i.imgur.com/2fkqiuP.jpg',
        'https://i.imgur.com/aqROeL9.jpg',
        'https://i.imgur.com/lPmnajS.jpg',
        'https://i.imgur.com/yPF8Zon.jpg',
        'https://i.imgur.com/Gq1JDk9.jpg',
        'https://i.imgur.com/HsVq1rC.jpg',
        'https://i.imgur.com/2hagiqz.jpg',
        'https://i.imgur.com/6OtstWo.jpg',
        'https://i.imgur.com/VkcZ490.jpg',
        'https://i.imgur.com/Z5nik9I.jpg',
        'https://i.imgur.com/SUgyltJ.jpg',
        'https://i.imgur.com/XYZDtQd.jpg',
        'https://i.imgur.com/NkFUtBT.jpg',
        'https://i.imgur.com/SGSs86E.jpg',
        'https://i.imgur.com/ZLhS6Kw.jpg',
        'https://i.imgur.com/3kwOAi0.jpg',
        'https://i.imgur.com/Y4CQq24.jpg',
        'https://i.imgur.com/UPGfP5Z.jpg',
        'https://i.imgur.com/7HXrRC7.jpg',
        'https://i.imgur.com/zhqjsHa.jpg',
        'https://i.imgur.com/pPZwZBQ.jpg',
        'https://i.imgur.com/AYvy0BI.jpg',
        'https://i.imgur.com/1Js7it6.jpg',
        'https://i.imgur.com/wSZw9iG.jpg',
        'https://i.imgur.com/aKIThMb.jpg',
        'https://i.imgur.com/d81sMoz.jpg',
        'https://i.imgur.com/tno0ccb.jpg',
        'https://i.imgur.com/1nx7iPK.jpg',
        'https://i.imgur.com/8I97eYc.jpg',
        'https://i.imgur.com/AFsHv3n.jpg',
        'https://i.imgur.com/ZjOGCWl.jpg',
        'https://i.imgur.com/E8Q3PKv.jpg',
        
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

print ('Memes Module Activated')

client.run(TOKEN)
