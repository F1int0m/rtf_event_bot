from aiogram import Bot, Dispatcher, executor, types
import logging

API_TOKEN = 'token'
check_texts = ['text1', 'text2']

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def text_contains_any_handler(message: types.Message):
    print(f'Got {message.text=} from {message.from_user.username=}')
    log.info(f'Got {message.text=} from {message.from_user.username=}')
    await message.answer('きっと勝つ')


for i in check_texts:
    dp.message_handler(text_contains=i)(text_contains_any_handler)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
