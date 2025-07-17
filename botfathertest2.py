from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import aiohttp
import subprocess

bot = Bot(token="ТУТ ТОКЕН")
dp = Dispatcher()

SERVER = "тут айпи ваш/launch"
YOUTUBE_URL = "https://youtube.com"

@dp.message(Command("youtube"))
async def start_youtube(message: types.Message):
    subprocess.Popen(["start", YOUTUBE_URL], shell=True)
    await message.answer("YouTube запущен")

@dp.message(Command("firefox"))
async def firefox(message: types.Message):
    async with aiohttp.ClientSession() as session:
        await session.get(f"{SERVER}/firefox")
    await message.answer("🦊 Firefox запущен")

@dp.message(Command("vscode"))
async def vscode(message: types.Message):
    async with aiohttp.ClientSession() as session:
        await session.get(f"{SERVER}/vscode")
    await message.answer("💻 VS Code запущен")

@dp.message(Command("info"))
async def info(message: types.Message): 
    await message.answer("Основные команды /vscode /firefox /youtube")


if __name__ == '__main__':
    dp.run_polling(bot)