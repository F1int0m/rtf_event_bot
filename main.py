from aiogram import Bot, Dispatcher, executor, types
import logging

API_TOKEN = 'token'
check_texts = ['text1', 'text2']

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def text_contains_any_handler(message: types.Message):
    log.info(f'Got {message.text=} from {message.from_user.username=}')
    if any(x in message.text for x in check_texts):
        await message.answer('きっと勝つ')
    else:
        await message.answer('Неверно')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
