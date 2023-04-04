#◉ Developer Source : @DEV_SAMIR ∆

#◉ Channel Source : @FTTUTY ∆

import os
import random
from asyncio import sleep

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

from sbb_b import sbb_b
from sbb_b.core.logger import logging

from ..Config import Config
from ..core.managers import edit_or_reply, edit_delete
from ..helpers import reply_id
from . import *
from . import mention

plugin_category = "العروض"
LOGS = logging.getLogger(__name__)

jjj = [
    "100% مو رمزيات غنبلهہ‏‏ 😱😂.",
    "90% مو رمزيات ضيم 😱😂👆",
    "80%  ٴ😱😂",
    "70%  ٴ😱😂",
    "60% براسهہ‏‏ 60 حظ 👌😂",
    "50% رمزيات هہ‏‏جين👍😂",
    "( 40% ) خوش رمزيات 👌😂",
    "30% ٴ😒😂",
    "20% ٴ😒😂",
    "10% ٴ😒😂",
    "0% ٴ😢😂",
]

photo = "https://t.me/GTTUTY/39"

async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_object = await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        if isinstance(user, int) or user.startswith("@"):
            user_obj = await event.client.get_entity(user)
            return user_obj
        try:
            user_object = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_object


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)
    )
    replied_user_profile_photos_count = "الرمزيات مامخلي بروفايل"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.id
    first_name = replied_user.first_name
    last_name = replied_user.last_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    yoy = random.choice(jjj)
    photo
    x = random.randrange(1, 9)
    if x == 1:
       username = "@{}".format(username) if username else ("لايوجد معرف")
       caption = f"<b>  ╮•🦦 الرمزيات ⇦ </b> {first_name} {last_name} \n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ </b>\n"
       caption += f"<b> • 🌚 | معـرفهہ‏‏  ⇦ </b> {username}\n"
       caption += f"<b> • 🌚 | ايـديهہ‏‏   ⇦ </b> <code>{user_id}</code>\n"
       caption += f"<b> • 🌚 | صـورهہ‏‏  ⇦ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> • 🌚 | نــوعهہ‏‏   ⇦  مطي زربهہ‏‏ 🦓 </b>\n"
       caption += f"<b> • 🌚 | نسبتـهہ‏‏  ⇦  {yoy} </b>\n\n\n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ "
       return photo, caption
    if x == 2:
       username = "@{}".format(username) if username else ("لايوجد معرف")
       caption = f"<b>  ╮•🦦 الرمزيات ⇦ </b> {first_name} {last_name} \n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ </b>\n"
       caption += f"<b> • 🌚 | معـرفهہ‏‏  ⇦ </b> {username}\n"
       caption += f"<b> • 🌚 | ايـديهہ‏‏   ⇦ </b> <code>{user_id}</code>\n"
       caption += f"<b> • 🌚 | صـورهہ‏‏  ⇦ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> • 🌚 | نــوعهہ‏‏   ⇦  جلب شوارع 🐕‍🦺 </b>\n"
       caption += f"<b> • 🌚 | نسبتـهہ‏‏  ⇦  {yoy} </b>\n\n\n"
       caption += f"<b> 𓆩  ╼•✬• 𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐄𝐌𝐎 ➪︎ @FTTUTY •✬•╾ "
       return photo, caption
    if x == 3:
       username = "@{}".format(username) if username else ("لايوجد معرف")
       caption = f"<b>  ╮•🦦 الرمزيات ⇦ </b> {first_name} {last_name} \n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ </b>\n"
       caption += f"<b> • 🌚 | معـرفهہ‏‏  ⇦ </b> {username}\n"
       caption += f"<b> • 🌚 | ايـديهہ‏‏   ⇦ </b> <code>{user_id}</code>\n"
       caption += f"<b> • 🌚 | صـورهہ‏‏  ⇦ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> • 🌚 | نــوعهہ‏‏   ⇦  قرد لزكـهہ‏‏ 🐒 </b>\n"
       caption += f"<b> • 🌚 | نسبتـهہ‏‏  ⇦  {yoy} </b>\n\n\n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ 𓆪  "
       return photo, caption
    if x == 4:
       username = "@{}".format(username) if username else ("لايوجد معرف")
       caption = f"<b>  ╮•🦦 الرمزيات ⇦ </b> {first_name} {last_name} \n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ </b>\n"
       caption += f"<b> • 🌚 | معـرفهہ‏‏  ⇦ </b> {username}\n"
       caption += f"<b> • 🌚 | ايـديهہ‏‏   ⇦ </b> <code>{user_id}</code>\n"
       caption += f"<b> • 🌚 | صـورهہ‏‏  ⇦ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> • 🌚 | نــوعهہ‏‏   ⇦  صخل محترم 🐐 </b>\n"
       caption += f"<b> • 🌚 | نسبتـهہ‏‏  ⇦  {yoy} </b>\n\n\n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯  "
       return photo, caption
    if x == 5:
       username = "@{}".format(username) if username else ("لايوجد معرف")
       caption = f"<b>  ╮•🦦 الرمزيات ⇦ </b> {first_name} {last_name} \n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ </b>\n"
       caption += f"<b> • 🌚 | معـرفهہ‏‏  ⇦ </b> {username}\n"
       caption += f"<b> • 🌚 | ايـديهہ‏‏   ⇦ </b> <code>{user_id}</code>\n"
       caption += f"<b> • 🌚 | صـورهہ‏‏  ⇦ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> • 🌚 | نــوعهہ‏‏   ⇦  طلي ابو البعرور الوصخ 🐑 </b>\n"
       caption += f"<b> • 🌚 | نسبتـهہ‏‏  ⇦  {yoy} </b>\n\n\n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ 𓆪  "
       return photo, caption
    if x == 6:
       username = "@{}".format(username) if username else ("لايوجد معرف")
       caption = f"<b>  ╮•🦦 الرمزيات ⇦ </b> {first_name} {last_name} \n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ </b>\n"
       caption += f"<b> • 🌚 | معـرفهہ‏‏  ⇦ </b> {username}\n"
       caption += f"<b> • 🌚 | ايـديهہ‏‏   ⇦ </b> <code>{user_id}</code>\n"
       caption += f"<b> • 🌚 | صـورهہ‏‏  ⇦ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> • 🌚 | نــوعهہ‏‏   ⇦  بزون ابوخالد 🐈 </b>\n"
       caption += f"<b> • 🌚 | نسبتـهہ‏‏  ⇦  {yoy} </b>\n\n\n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯  "
       return photo, caption
    if x == 7:
       username = "@{}".format(username) if username else ("لايوجد معرف")
       caption = f"<b>  ╮•🦦 الرمزيات ⇦ </b> {first_name} {last_name} \n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ </b>\n"
       caption += f"<b> • 🌚 | معـرفهہ‏‏  ⇦ </b> {username}\n"
       caption += f"<b> • 🌚 | ايـديهہ‏‏   ⇦ </b> <code>{user_id}</code>\n"
       caption += f"<b> • 🌚 | صـورهہ‏‏  ⇦ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> • 🌚 | نــوعهہ‏‏   ⇦  الزاحف ابو بريص 🦎 </b>\n"
       caption += f"<b> • 🌚 | نسبتـهہ‏‏  ⇦  {yoy} </b>\n\n\n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯  "
       return photo, caption
    if x == 8:
       username = "@{}".format(username) if username else ("لايوجد معرف")
       caption = f"<b>  ╮•🦦 الرمزيات ⇦ </b> {first_name} {last_name} \n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ </b>\n"
       caption += f"<b> • 🌚 | معـرفهہ‏‏  ⇦ </b> {username}\n"
       caption += f"<b> • 🌚 | ايـديهہ‏‏   ⇦ </b> <code>{user_id}</code>\n"
       caption += f"<b> • 🌚 | صـورهہ‏‏  ⇦ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> • 🌚 | نــوعهہ‏‏   ⇦  جريذي ابو المجاري 🐀 </b>\n"
       caption += f"<b> • 🌚 | نسبتـهہ‏‏  ⇦  {yoy} </b>\n\n\n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ 𓆪  "
       return photo, caption
    if x == 9:
       username = "@{}".format(username) if username else ("لايوجد معرف")
       caption = f"<b>  ╮•🦦 الرمزيات ⇦ </b> {first_name} {last_name} \n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯ </b>\n"
       caption += f"<b> • 🌚 | معـرفهہ‏‏  ⇦ </b> {username}\n"
       caption += f"<b> • 🌚 | ايـديهہ‏‏   ⇦ </b> <code>{user_id}</code>\n"
       caption += f"<b> • 🌚 | صـورهہ‏‏  ⇦ </b> {replied_user_profile_photos_count} </b>\n"
       caption += f"<b> • 🌚 | نــوعهہ‏‏   ⇦  هہ‏‏ايشهہ‏‏ 🐄 </b>\n"
       caption += f"<b> • 🌚 | نسبتـهہ‏‏  ⇦  {yoy} </b>\n\n\n"
       caption += f"<b> ⌯╼═══❬ ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ ❭═══╾⌯  "
       return photo, caption


@sbb_b.ar_cmd(pattern="رمزيات(?: |$)(.*)")
async def who(event):
    zed = await edit_or_reply(event, "⇆")
    zel_dev = (2095357462, 1346542270, 1885375980, 1721284724, 1951523146, 1243462298, 1037828349, 1985711199, 2028523456, 2045039090, 1764272868, 2067387667, 294317157, 2066568220, 1403932655, 1389046667, 444672531, 2055451976, 294317157, 2134101721, 1719023510, 1985225531, 2107283646, 2146086267, 1850533212, 5280339206)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(zed, "**- لـم استطـع العثــور ع الشخــص**")
    if replied_user.id in zel_dev:
       return await edit_or_reply(zed, "**- دي . . انـهہ‏‏ُ احـد المطـورين . . انتـهہ‏‏ الحيـوان ولك**")
    if replied_user.id == 925972505 or replied_user.id == 5680297831 or replied_user.id == 5680297831:
       return await edit_or_reply(zed, "**- دي . . انـهہ‏‏ُ المطـور . . انتـهہ‏‏ الحيـوان ولك**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        await zed.delete()
    except TypeError:
        await zed.edit(caption, parse_mode="html")
