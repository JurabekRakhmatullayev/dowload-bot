
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_menu = InlineKeyboardMarkup(
    inline_keyboard= [

    [InlineKeyboardButton(text="Bizning kurslar",callback_data="courses"),
    InlineKeyboardButton(text="Bizning manzil",callback_data="location"),],

    [InlineKeyboardButton(text="Bizning haqimizda",callback_data="about_us"),],

    [InlineKeyboardButton(text="Admin ",callback_data="contact_admin")],
    [InlineKeyboardButton(text="Dowloads",callback_data="yuklanmalar")],

    ]
)
courses = InlineKeyboardMarkup(
    inline_keyboard= [

    [InlineKeyboardButton(text="Frontend",url="https://medium.com/@muhammadbobur99/front-end-nima-fc747f74f568"),
    InlineKeyboardButton(text="Backend",url="https://uzbekdevs.uz/wiki/backend"),],

    [InlineKeyboardButton(text="Online kurslar",url="https://www.youtube.com/@SIFATDEV"),],
    
    [InlineKeyboardButton(text="ortga",callback_data="back")],

    ]
)

location = InlineKeyboardMarkup(
    inline_keyboard= [
    [InlineKeyboardButton(text="Sifat edu",url="https://www.google.com/maps/@40.1028381,65.3730178,16z?entry=ttu")],
    [InlineKeyboardButton(text="ortga",callback_data="back")],
    ]
)

about_us = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text="Sifat EDU",url="https://sifatedu.uz/")],
        [InlineKeyboardButton(text="ortga",callback_data="back")],
    ]
)

contact_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Jurabekjon",url="https://t.me/Jur_bek_jon_123com")],
        [InlineKeyboardButton(text="ortga",callback_data="back")],
    ]
)

dowloads = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text="Tik_Tok",url="https://apps.microsoft.com/detail/9nh2gph4jzs4?hl=en-us&gl=US")],
        [InlineKeyboardButton(text="Instagram",url="https://instagram.softonic.ru/")],
        [InlineKeyboardButton(text="Youtube",url="https://www.dvdvideosoft.com/free-youtube-download-en5")],
        
     [InlineKeyboardButton(text="ortga",callback_data="back")],   
    ],
)

back_to = InlineKeyboardMarkup(
    inline_keyboard=[

    [InlineKeyboardButton(text="Bizning kurslar",callback_data="courses"),
    InlineKeyboardButton(text="Bizning manzil",callback_data="location"),],

    [InlineKeyboardButton(text="Bizning haqimizda",callback_data="about_us"),],

    [InlineKeyboardButton(text="Admin ",callback_data="contact_admin")],
    [InlineKeyboardButton(text="Dowloads",callback_data="yuklanmalar")],

    ]

)