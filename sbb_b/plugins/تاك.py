from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

from sbb_b import sbb_b

from ..core.managers import edit_delete, edit_or_reply

@sbb_b.on(admin_cmd(pattern="تاك 200(?: |$)(.*)"))
async def iq(sbb_b):
    mentions = sbb_b.text[8:]
    chat = await sbb_b.get_input_chat()
    async for x in sbb_b.client.iter_participants(chat, 200):
        mentions += f" \n◉  ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉"
    await sbb_b.client.send_message(sbb_b.chat_id, mentions)
    await sbb_b.delete()
@sbb_b.on(admin_cmd(pattern="تاك 150(?: |$)(.*)"))
async def iq(sbb_b):
    mentions = sbb_b.text[8:]
    chat = await sbb_b.get_input_chat()
    async for x in sbb_b.client.iter_participants(chat, 150):
        mentions += f" \n◉  ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await sbb_b.client.send_message(sbb_b.chat_id, mentions)
    await sbb_b.delete()
@sbb_b.on(admin_cmd(pattern="تاك 100(?: |$)(.*)"))
async def iq(sbb_b):
    mentions = sbb_b.text[8:]
    chat = await sbb_b.get_input_chat()
    async for x in sbb_b.client.iter_participants(chat, 100):
        mentions += f" \n◉  ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await sbb_b.client.send_message(sbb_b.chat_id, mentions)
    await sbb_b.delete()
@sbb_b.on(admin_cmd(pattern="تاك 50(?: |$)(.*)"))
async def iq(sbb_b):
    mentions = sbb_b.text[8:]
    chat = await sbb_b.get_input_chat()
    async for x in sbb_b.client.iter_participants(chat, 50):
        mentions += f" \n◉  ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await sbb_b.client.send_message(sbb_b.chat_id, mentions)
    await sbb_b.delete()
@sbb_b.on(admin_cmd(pattern="تاك 10(?: |$)(.*)"))
async def iq(sbb_b):
    mentions = sbb_b.text[8:]
    chat = await sbb_b.get_input_chat()
    async for x in sbb_b.client.iter_participants(chat, 10):
        mentions += f" \n◉  ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await sbb_b.client.send_message(sbb_b.chat_id, mentions)
    await sbb_b.delete()
@sbb_b.on(admin_cmd(pattern="طلاك(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    sbb_b = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await mention.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await edit_or_reply(mention, f"**᯽︙  انتِ طالق طالق طالق 🙎🏻‍♂️ من  :**{my_mention} .\n**᯽︙  لقد تم طلاقها بلثلاث وفسخ زواجكما الان الكل حر طليق ** ")
ownersayed_id = 5680297831
@sbb_b.on(events.NewMessage(outgoing=False, pattern='منصب؟'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownersayed_id :
        order = await event.reply('يب منصب ✓')
ownersayed1_id = 5680297831
@sbb_b.on(events.NewMessage(outgoing=False, pattern='منو فخر العرب؟'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownersayed1_id :
        order = await event.reply('انته فخر العرب مح ❤️')
