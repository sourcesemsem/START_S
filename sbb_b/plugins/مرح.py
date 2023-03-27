import random

from razan.strings.fun import *
from sbb_b import sbb_b
from sbb_b.core.managers import edit_or_reply
from sbb_b.helpers import get_user_from_event

from . import *


@sbb_b.ar_cmd(pattern="رفع بكلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بڪلبك 🖤 "
    )


@sbb_b.ar_cmd(pattern="رفع زوجي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعه زوجج روحوا خلفوا 🤤😂",
    )


@sbb_b.ar_cmd(pattern="رفع مطي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفـعه مطي هـنا "
    )


@sbb_b.ar_cmd(pattern="رفع مراتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه مـࢪاتك تعالي نخـلف 😹🤤",
    )


@sbb_b.ar_cmd(pattern="رفع كلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه كلب خليه يجي ينبح 😂🐶",
    )


@sbb_b.ar_cmd(pattern="كت(?: |$)(.*)")
async def mention(mention):
    reza = random.choice(kttwerz)
    await edit_or_reply(mention, f"**- {reza}**")


@sbb_b.ar_cmd(pattern="هينه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- يبن الوسخه ده مطور السورس 🤦🏻‍♂️ **")
    if user.id == 1694386561:
        return await edit_or_reply(mention, f"**- يبن الوسخه ده مطور السورس 🤦🏻‍♂️ **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- يبن الوسخه ده مطور السورس 🤦🏻‍♂️ **")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(hena)
    await edit_or_reply(mention, f"{sos} .")


@sbb_b.ar_cmd(pattern="نسبة الحب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rza = random.choice(roz)
    await edit_or_reply(
        mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {rza} 😔🖤"
    )


@sbb_b.ar_cmd(pattern="نسبة الانوثة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- ده مطور السورس ي زلمه وعلي راسك**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- ده مطور السورس ي زلمه وعلي راسك**")
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- ده مطور السورس ي زلمه وعلي راسك**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"- نسبة الانوثة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@sbb_b.ar_cmd(pattern="نسبة الغباء(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- والله ما فيه غيرك غبي علشان ده مطور السورس🤦🏻‍♂️😹**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- والله ما فيه غيرك غبي علشان ده مطور السورس🤦🏻‍♂️😹**")
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- والله ما فيه غيرك غبي علشان ده مطور السورس🤦🏻‍♂️😹**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"- نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@sbb_b.ar_cmd(pattern="رفع تاج(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه تاج 👑🔥"
    )


@sbb_b.ar_cmd(pattern="رفع قرد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه قرد واعطائه موزة 🐒🍌",
    )


@sbb_b.ar_cmd(pattern="اوصف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(osfroz)
    await edit_or_reply(mention, f"{rzona}")


@sbb_b.ar_cmd(pattern="شغله(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rezw = random.choice(rzwhat)
    await edit_or_reply(
        mention, f"- المستخدم [{muh}](tg://user?id={user.id}) شغله هو {rezw}"
    )


@sbb_b.ar_cmd(pattern="نسبة الرجولة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**100%**")
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**100%**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**100%**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(kz)
    await edit_or_reply(
        mention, f"- نسبة الرجولة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@sbb_b.ar_cmd(pattern="رفع بزون(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بزون 🐈"
    )


@sbb_b.ar_cmd(pattern="رفع زاحف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه زاحف 🐍💞"
    )


@sbb_b.on(admin_cmd(pattern="زواج(?:\s|$)([\s\S]*)"))
async def rzfun(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**⌔∮ عذرا هذا مطور السورس**")
    await edit_or_reply(mention, f"**نزوج وماتباوع على غيري 🥺💞 ܰ**")


@sbb_b.on(admin_cmd(pattern="طلاك(?:\s|$)([\s\S]*)"))
async def mention(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**⌔∮ عذرا هذا مطور السورس**")
    await edit_or_reply(mention, f"**طالق طالق بالعشرة 😹😭💕 ܰ**")

@sbb_b.on(admin_cmd(pattern="طلاق(?:\s|$)([\s\S]*)"))
async def mention(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**⌔∮ عذرا هذا مطور السورس **")
    await edit_or_reply(mention, f"**طالق طالق بالعشرة 😹😭💕 ܰ**")


@sbb_b.ar_cmd(pattern="تتجوزيني(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- عايز تتجوز المطور يهبل 😹 **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - الحقي يا [{tag}](tg://user?id={user.id}) \n\n- في واحد عايز يتجوزك 😱😹 ",
    )


@sbb_b.ar_cmd(pattern="رفع بقلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بقلبك 🖤 \n وبطل محن كلاب بق 🙄😹 "
    )


@sbb_b.ar_cmd(pattern="رفع ابني(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم رفعه ابنك ربيه كويس بق 😹 ",
    )


@sbb_b.ar_cmd(pattern="رفع بنتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم رفعه بنجاح ربيها علشان ناقصه تربيه😹 ",
    )


@sbb_b.ar_cmd(pattern="رفع مظه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم رفعه مظه محدش يعاكسها بق 😃",
    )


@sbb_b.ar_cmd(pattern="رفع مزه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم رفعه مزه محدش يعاكسها بق 😃 ",
    )


@sbb_b.ar_cmd(pattern="رفع خول(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم رفعه خول لما يسترجل نزلو 🥱 ",
    )


@sbb_b.ar_cmd(pattern="تنزيل كلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم تنزيله من قائمة الكلاب 😁 ",
    )


@sbb_b.ar_cmd(pattern="تنزيل خول(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم تنزيله من قائمة الخولات 👻 ",
    )


@sbb_b.ar_cmd(pattern="مسح زوجاتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f" تم مسح جميع زوجاتك 🤦🏻‍♂️💔"
    )


@sbb_b.ar_cmd(pattern="مسح الخولات(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f" تم مسح الخولات بنحاج 🤦🏻‍♂️😂"
    )


@sbb_b.ar_cmd(pattern="مسح الكلاب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f" تم مسح جميع الكلاب 🐕"
    )


@sbb_b.ar_cmd(pattern="رفع سيمب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم رفعه سيمب خلي الحريم تنفعو 😂😂 ",
    )


@sbb_b.ar_cmd(pattern="تنزيل سيمب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم تنزيله من قائمة السيمب 🤡 ",
    )


@sbb_b.ar_cmd(pattern="تنزيل بنتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم تنزيله من قائمة بناتك 💩\n\n- شوف واحده غيرهاا ينوبك ثواب 😹",
    )


@sbb_b.ar_cmd(pattern="تنزيل ابني(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم تنزيله من قائمة اولادك 💩\n\n- شوف واحد ولد غيره اتبناه 😂",
    )


@sbb_b.ar_cmd(pattern="تنزيل مظه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم تنزيله من قائمة المظظ 💩\n\n لانها بقت مقشفه 🙂😹",
    )


@sbb_b.ar_cmd(pattern="تنزيل مزه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم تنزيله من قائمة المزز 😪\n\n- لانها بقت واحده مقشفه 😅",
    )


@sbb_b.ar_cmd(pattern="رفع شاذ(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم رفعه شاذ لما يسترجل نزلو 🤡",
    )


@sbb_b.ar_cmd(pattern="تنزيل شاذ(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم تنزيله من قائمة الشواذ 🙀",
    )


@sbb_b.ar_cmd(pattern="مسح الشواذ(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f" تم مسح جميع الشواذ 👻"
    )


@sbb_b.ar_cmd(pattern="مسح المعرصين(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f" تم مسح جميع المعرصين 🤦🏻‍♂️💔"
    )


@sbb_b.ar_cmd(pattern="مسح المتحودين(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f" تم مسح جميع المتوحدين 🤣"
    )


@sbb_b.ar_cmd(pattern="مسح الحمير(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f" تم مسح جميع الحمير 🦓"
    )


@sbb_b.ar_cmd(pattern="مسح القلوب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f" تم مسح جميع القلوب 💔"
    )


@sbb_b.ar_cmd(pattern="تنزيل بقلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده في قلب الجميع 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده في قلب الجميع 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تم تنزيله من قلبك واصبحت مكسور القلب 🙂💔",
    )


@sbb_b.ar_cmd(pattern="رفع عرص(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه معرص بنجاح 😅",
    )


@sbb_b.ar_cmd(pattern="تنزيل عرص(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم تنزيله من المعرصين 🤣",
    )


@sbb_b.ar_cmd(pattern="رفع متوحد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه متوحد 🙂",
    )


@sbb_b.ar_cmd(pattern="تنزيل متوحد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم تنزيله من قائمة المتوحدين  🤦🏻‍♂️😃",
    )


@sbb_b.ar_cmd(pattern="رفع حمار(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه حمار شوفو حد يربكو 😹",
    )


@sbb_b.ar_cmd(pattern="تنزيل حمار(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم تنزيله من قائمة الحمير 😂 \n كده مش هنلاقي حد نركبو 🙀",
    )


@sbb_b.ar_cmd(pattern="رفع علق(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 6085251582:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" • العضو [{tag}](tg://user?id={user.id}) 🙀\n\n• تم رفعه علق بنجاح 👻\n\n• أما يبقا راجل ابقا أنزله 😹💔",
    )
