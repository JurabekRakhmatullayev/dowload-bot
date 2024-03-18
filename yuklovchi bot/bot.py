import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.types import Message,CallbackQuery
from keyboard import inline_menu,about_us,contact_admin,dowloads,back_to,location,courses

 
TOKEN = "6399847517:AAGVofxBA9ZUAVRLcBg9sERc5KZ07P471KQ" #Token kiriting
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Assalomu alaykum. \nPastdagilardan birini tanlang",reply_markup=inline_menu)

@dp.callback_query(F.data=="courses")
async def lakatsiya(callback:CallbackQuery):
    await callback.message.edit_text(text="Bizning manzil",reply_markup=courses)

@dp.callback_query(F.data=="location")
async def lakatsiya(callback:CallbackQuery):
    await callback.message.edit_text(text="Bizning manzil",reply_markup=location)
    
@dp.callback_query(F.data=="about_us")
async def saytimiz(callback:CallbackQuery):
    await callback.message.edit_text(text="Bizning sayt",reply_markup=about_us)
    
@dp.callback_query(F.data=="contact_admin")
async def men(callback:CallbackQuery):
    await callback.message.edit_text(text="Admin",reply_markup=contact_admin)

@dp.callback_query(F.data=="yuklanmalar")
async def men(callback:CallbackQuery):
    await callback.message.edit_text(text="yuklanmalar",reply_markup=dowloads)

@dp.callback_query(F.data=="back")
async def men(callback:CallbackQuery):
    await callback.message.edit_text(text="quyidagilardan birini tanlang",reply_markup=back_to)

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
