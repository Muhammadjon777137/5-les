from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from keyboard import *

BOT_TOKEN = "6562002464:AAHaLinBolbmHgIMU4sHw4ZJIDdKMv_W-Pg"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

evos_photo = "https://tashkent.hh.uz/employer-logo/4136381.jpeg"


@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    with open("Evos.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, reply_markup=main_menu())


@dp.message_handler(Text(equals="⬅️ Назад"))
async def start_bot(message: types.Message):
    with open("Evos.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, reply_markup=main_menu())


@dp.message_handler(Text(equals="❌ Отменить ❌"))
async def start_bot(message: types.Message):
    with open("Evos.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, reply_markup=main_menu())


@dp.message_handler(Text(equals="📍 Филиалы"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo,
                               reply_markup=filial_buttons(),
                               caption="""EVOS - крупнейшая фастфуд-компания в Узбекистане. В настоящее время у нас 49 точек продаж и широко диверсифицированное производство.

Сотрудники компании развиваются вместе, становясь большой семьей изо дня в день. У нас каждый день растет число наших сотрудников, сегодня у нас более пятнадцати тысяч человек. Присоединяйтесь к нашему сообществу, добро пожаловать в семью EVOS!""")


@dp.message_handler(Text(equals="🏢 О компании"))
async def start_bot(message: types.Message):
    with open("oila.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   reply_markup=main_menu(),
                                   caption="""EVOS ® сеть ресторанов быстрого обслуживания не стоит на месте, она развивается и растет вместе с вами и для вас! Мы расширяем географию и почти каждый месяц открываем новые филиалы.
Теперь в нашей сети по всему Узбекистану более 50 филиалов. Мы всегда ищем динамичных и активных людей, которые хотели бы стать частью нашей команды и уже готовы начать свою деятельность в EVOS ®.
EVOS ® - это надежный бренд. Работать в EVOS ® - это гарантия постоянного дохода и перспектив статуса.
Начните свою карьеру в EVOS ® уже сегодня!""")


# =================================================================================

@dp.message_handler(Text(equals="💼 Вакансии"))
async def start_bot(message: types.Message):
    await message.answer(text="Присоединяйтесь к команде EVOS!", reply_markup=ishorinlari_menu())
    await message.answer(text="📍 Выберите город:", reply_markup=ishorinlari_menu())


@dp.message_handler(Text(equals="Ташкент"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=lavozimlar_menu())


@dp.message_handler(Text(equals="⬅️ Назад"))
async def start_bot(message: types.Message):
    with open("Evos.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, reply_markup=Tumanlar_menu1())


@dp.message_handler(Text(equals="Универсальный  работник"))
async def start_bot(message: types.Message):
    with open("Universal xodim.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график (по желанию)

✔️ Приятный внешний вид

💰 Зарплата от 17228.96 (до вычета налогов) за час""", reply_markup=Tumanlar_menu1())
        await message.answer("В настоящее время вакансия открыта в одном из выбранных районов", reply_markup=Tumanlar_menu1())


# =================================================================================
@dp.message_handler(Text(equals="Мирзо Улугбек"))
async def start_bot(message: types.Message):
    await message.answer(text="📍 Выберите филиал, в котором хотите работать", reply_markup=Mirzo_Ulugbek_menu())


@dp.message_handler(Text(equals="Паркент"))
async def start_bot(message: types.Message):
    with open("Parkent.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, caption="Ташкент, ул. Паркент, 131", reply_markup=Bahodir_menu())
        latitude = 41.31533
        longitude = 69.326836
        await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
        await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="Максим Горький"))
async def start_bot(message: types.Message):
    with open("Maksim Gorkiy.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, caption="Ташкент, ул. Амир Темур, 42", reply_markup=Bahodir_menu())
        latitude = 41.325676
        longitude = 69.324199
        await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
        await message.answer(text="👤 Введите ваше полное имя?", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Корасу"))
async def start_bot(message: types.Message):
    await message.answer(text="Ташкент, Мирзо-Улугбекский район, микрорайон Корасу, 3-й квартал, 14Б",
                         reply_markup=Bahodir_menu())
    latitude = 41.334536
    longitude = 69.370294
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Экобазар торговый центр"))
async def start_bot(message: types.Message):
    await message.answer(text="Ташкент, улица Тимур Малик, дом 3", reply_markup=Bahodir_menu())
    latitude = 41.354116
    longitude = 69.353745
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Сельхоз"))
async def start_bot(message: types.Message):
    await message.answer(text="Ташкентская область, Кибрайский район, поселок Салар шахарча, Ташкентский халк йули",
                         reply_markup=Bahodir_menu())
    latitude = 41.358738
    longitude = 69.339848
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 ТТЗ"))
async def start_bot(message: types.Message):
    with open("TTZ.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, caption="Ташкент, Мирзо Улугбекский район, микрорайон Бешкапа",
                                   reply_markup=Bahodir_menu())
        latitude = 41.355777
        longitude = 69.376184
        await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
        await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="Яшнобод"))
async def start_bot(message: types.Message):
    await message.answer(text="📍 На каком филиале хотели бы работать?", reply_markup=Yashnobod_menu())


@dp.message_handler(Text(equals="📍 Лисунова 2"))
async def start_bot(message: types.Message):
    await message.answer(text="Ташкент, Авиасозлар, 9/3", reply_markup=Bahodir_menu())
    latitude = 41.290593
    longitude = 69.342983
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Лисунова"))
async def start_bot(message: types.Message):
    await message.answer(text="Авиасозлар, 3, строение 21", reply_markup=Bahodir_menu())
    latitude = 41.291738
    longitude = 69.340682
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="Яккасарай"))
async def start_bot(message: types.Message):
    await message.answer(text="📍 На каком филиале хотели бы работать?", reply_markup=Yakkasaroy_menu())


@dp.message_handler(Text(equals="📍 Шота Руставели"))
async def start_bot(message: types.Message):
    with open("Bahodir.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, caption="Шота Руставели, 36", reply_markup=Bahodir_menu())
        latitude = 41.289768
        longitude = 69.257899
        await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
        await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Мухимий"))
async def start_bot(message: types.Message):
    with open("Muqimiy.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, caption="Узбекистан, Ташкент, улица Мухимий, 7",
                                   reply_markup=Bahodir_menu())
        latitude = 41.280089
        longitude = 69.241588
        await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
        await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 'Next' торговый центр"))
async def start_bot(message: types.Message):
    await message.answer(text="Яккасарайский район, улица Бобура, дом 6",
                         reply_markup=Bahodir_menu())
    latitude = 41.297963
    longitude = 69.249409
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Театральный"))
async def start_bot(message: types.Message):
    await message.answer(text="Яккасарайский район, улица Бобура, дом 40А", reply_markup=Bahodir_menu())
    latitude = 41.28557
    longitude = 69.253178
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Южный"))
async def start_bot(message: types.Message):
    await message.answer(
        text="ТРЦ VegaCentre, ул. Шота Руставели 150 напротив Южного вокзала, 100121, Тоshkent по Zargarlik ko'chasi и Kichik Xalqa Yo'li",
        reply_markup=Bahodir_menu())
    latitude = 41.265792
    longitude = 69.163624
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Ism sharifingizni kiriting?", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="Uchtepa"))
async def start_bot(message: types.Message):
    await message.answer(text="📍 Qaysi filialda ishlashni istaysiz?", reply_markup=Uchtepa_menu())


@dp.message_handler(Text(equals="📍 Бешкайрагоч"))
async def start_bot(message: types.Message):
    await message.answer(text="Ташкент, улица Кукча Дарвоза, 622", reply_markup=Bahodir_menu())
    latitude = 41.310648
    longitude = 69.166093
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Фозилтепа"))
async def start_bot(message: types.Message):
    await message.answer(text="Учтепинский район, улица Фозил тепа, 25-дом, 12 Б-дом", reply_markup=Bahodir_menu())
    latitude = 41.283574
    longitude = 69.164991
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Лутфий"))
async def start_bot(message: types.Message):
    await message.answer(text="Чиланзарский массив, 12-квартал, 41", reply_markup=Bahodir_menu())
    latitude = 41.281629
    longitude = 69.181073
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="Сергели"))
async def start_bot(message: types.Message):
    await message.answer(text="📍 На каком филиале хотели бы работать?", reply_markup=Sergeli_menu())


@dp.message_handler(Text(equals="📍 Сергели"))
async def start_bot(message: types.Message):
    await message.answer(text="Ташкент, Сергелийский район, махалля Янги-Сергели, Йўналиш",
                         reply_markup=Bahodir_menu())
    latitude = 41.223002
    longitude = 69.221532
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Сергели Янги Хаёт"))
async def start_bot(message: types.Message):
    await message.answer(text="Ташкент, улица Мехригийо, дом 84", reply_markup=Bahodir_menu())
    latitude = 41.220129
    longitude = 69.201101
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Сергели Ярмарка"))
async def start_bot(message: types.Message):
    await message.answer(text="Ташкент, улица Янги Сергели", reply_markup=Bahodir_menu())
    latitude = 41.211752
    longitude = 69.230013
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="Чиланзар"))
async def start_bot(message: types.Message):
    await message.answer(text="📍 На каком филиале хотели бы работать?", reply_markup=Chilonzor_menu())


@dp.message_handler(Text(equals="📍 Чиланзар"))
async def start_bot(message: types.Message):
    with open("Chilonzor.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="Ташкент, Чиланзарский район, Чиланзарский массив, 10-квартал, 17-дом",
                                   reply_markup=Bahodir_menu())
        latitude = 41.279397
        longitude = 69.197984
        await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
        await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Катартал"))
async def start_bot(message: types.Message):
    await message.answer(text="Чиланзарский район, Чиланзарский массив, 8-дом, 21А 1-этаж",
                         reply_markup=Bahodir_menu())
    latitude = 41.291511
    longitude = 69.210684
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Алгоритм"))
async def start_bot(message: types.Message):
    await message.answer(text="Узбекистан, Ташкент, улица Сугалли ота", reply_markup=Bahodir_menu())
    latitude = 41.272314
    longitude = 69.160648
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Magic City"))
async def start_bot(message: types.Message):
    await message.answer(text="Magic City Park, Чиланзарский район, Олмазорский массив, 183а", reply_markup=Bahodir_menu())
    latitude = 41.303477
    longitude = 69.245445
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Катта-Кани"))
async def start_bot(message: types.Message):
    await message.answer(
        text="Чиланзарский район, 20-й квартал, улица Катта-Кани.",
        reply_markup=Bahodir_menu())
    latitude = 41.268826
    longitude = 69.172706
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="Миробод"))
async def start_bot(message: types.Message):
    await message.answer(text="📍 На каком филиале хотели бы работать?", reply_markup=Mirobod_menu())


@dp.message_handler(Text(equals="📍 Койлик"))
async def start_bot(message: types.Message):
    with open("Bahodir.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="Узбекистан, Ташкент, Мирободский район, махалля Парвона 3-отиш Сарбон",
                                   reply_markup=Bahodir_menu())
        latitude = 41.25294
        longitude = 69.321805
        await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
        await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Боровский"))
async def start_bot(message: types.Message):
    await message.answer(text="Ташкент, улица Яхъё Гуломов, дом 94", reply_markup=Bahodir_menu())
    latitude = 41.304766
    longitude = 69.284631
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Bahodir_menu())


# =================================================================================
@dp.message_handler(Text(equals="Колл-центр оператор"))
async def start_bot(message: types.Message):
    with open("Operator.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, caption="""📌 Возраст от 18 до 35 лет

🇷🇺/🇺🇿 Знание русского и узбекского языков

🕑 Полная занятость

👨‍💼/👩‍💼 Привлекательный внешний вид

🧑‍💻/👩‍💻 Наличие компьютера или ноутбука
Мы предлагаем:
- Официальное трудоустройство
- Питание, предоставляемое компанией
- Оплата труда с первого дня работы
- Почасовая оплата труда""", reply_markup=Operaror_menu())
        await message.answer(text="В настоящее время вакансии открыты в следующих районах. Выберите один из них", reply_markup=Operaror_menu())


@dp.message_handler(Text(equals="Чиланзар"))
async def start_bot(message: types.Message):
    await  message.answer(text="📍 На каком филиале хотели бы работать?", reply_markup=Operaror2_menu())


@dp.message_handler(Text(equals="Главный офис"))
async def start_bot(message: types.Message):
    with open("Bosh Ofis.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, caption="Улица Фуркат 175", reply_markup=Bahodir_menu())
        latitude = 41.302192
        longitude = 69.248867
        await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())


# =================================================================================
@dp.message_handler(Text(equals="Курьер"))
async def start_bot(message: types.Message):
    with open("Kuryer.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, caption="""📌 Возраст от 20 до 35 лет

🇷🇺/🇺🇿 Знание русского и узбекского языков

🕑 Гибкий график работы (по возможности)

👨‍💼/👩‍💼 Привлекательный внешний вид

🚘 Наличие личного транспорта

📍 Место оплаты труда и распределения грузов""", reply_markup=Kuryer_menu())
        await message.answer(text="В настоящее время вакансии открыты в следующих районах. Выберите один из них", reply_markup=Kuryer_menu())


@dp.message_handler(Text(equals="Олмазор"))
async def start_bot(message: types.Message):
    await message.answer(text="👤 Введите ваше полное имя", reply_markup=Olmazor_buttons())


@dp.message_handler(Text(equals="📍Орзу"))
async def start_bot(message: types.Message):
    with open("toshmi.jpg", "rb") as photo:
        latitude = 41.304766
        longitude = 69.284631
        await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
        await message.answer_photo(photo=photo, caption="""Узбекистан, Ташкент, улица Беруни""",
                                   reply_markup=Toshmi_buttons())
        await message.answer("👤 Введите ваше полное имя")

@dp.message_handler(Text(equals="📍Коракамыш 1/3"))
async def start_bot(message: types.Message):
    latitude = 41.304766
    longitude = 69.284631
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer("👤 Введите ваше полное имя")
    await message.answer(text="Олмазорский район, улица Сагбон, Кора-Камыш 1/3, ГСКБ",
                         reply_markup=Chorshugum_buttons())


@dp.message_handler(Text(equals="📍Охунбобоев"))
async def start_bot(message: types.Message):
    latitude = 41.304766
    longitude = 69.284631
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer("👤 Введите ваше полное имя")
    await message.answer(text="Улица Келес йўли, 166", reply_markup=Samarqand_buttons())


@dp.message_handler(Text(equals="📍Коракамыш 2/4"))
async def start_bot(message: types.Message):
    latitude = 41.304766
    longitude = 69.284631
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer("👤 Введите ваше полное имя")
    await message.answer(text="Ташкент, Олмазорский район, Бешкўргон массиви, 2-й квартал",
                         reply_markup=Navoiy_buttons())


@dp.message_handler(Text(equals="📍Эски шахар"))
async def start_bot(message: types.Message):
    latitude = 41.304766
    longitude = 69.284631
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer("👤 Введите ваше полное имя")
    await message.answer(
        text="Ташкентский ш., Олмазорский район, махалля Куёш, улица Фороби, 129 АТС Эски Шахар, 3-й этаж.",
        reply_markup=Beltepa_buttons())


@dp.message_handler(Text(equals="Шайхантаур"))
async def start_bot(message: types.Message):
    await message.answer(text="📍 На каком филиале хотели бы работать?", reply_markup=Shayxontahur_buttons())


@dp.message_handler(Text(equals="📍ТошМИ"))
async def start_bot(message: types.Message):
    with open("toshmi.jpg", "rb") as photo:
        latitude = 41.304766
        longitude = 69.284631
        await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
        await message.answer_photo(photo=photo, reply_markup=Toshmi_buttons())
        await message.answer("👤 Введите ваше полное имя")


@dp.message_handler(Text(equals="📍София"))
async def start_bot(message: types.Message):
    with open("sofiya.jpg", "rb") as photo:
        latitude = 41.304766
        longitude = 69.284631
        await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
        await message.answer_photo(photo=photo, caption="Улица Богировон, 29")
        await message.answer("👤 Введите ваше полное имя", reply_markup=Sofiya_buttons())


@dp.message_handler(Text(equals="📍Чоршу ГУМ"))
async def start_bot(message: types.Message):
    latitude = 41.304766
    longitude = 69.284631
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer("👤 Введите ваше полное имя")
    await message.answer(text="Старый ГУМ, Ташкент, улица Навоий шах, 21", reply_markup=Chorshugum_buttons())


@dp.message_handler(Text(equals="📍Самарканд дарвоза"))
async def start_bot(message: types.Message):
    latitude = 41.304766
    longitude = 69.284631
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer("👤 Введите ваше полное имя")
    await message.answer(text="Шайхантохурский район, улица Коратош, 5 А.", reply_markup=Samarqand_buttons())


@dp.message_handler(Text(equals="📍Навоий Кочаси"))
async def start_bot(message: types.Message):
    latitude = 41.304766
    longitude = 69.284631
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer("👤 Введите ваше полное имя")
    await message.answer(text="Улица Алишер Навоий, 27-дом", reply_markup=Navoiy_buttons())


@dp.message_handler(Text(equals="📍Белтепа"))
async def start_bot(message: types.Message):
    latitude = 41.304766
    longitude = 69.284631
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer("👤 Введите ваше полное имя")
    await message.answer(text="Улица Фароби, 37А", reply_markup=Beltepa_buttons())


@dp.message_handler(Text(equals="📍1-городская клиническая больница"))
async def start_bot(message: types.Message):
    latitude = 41.304766
    longitude = 69.284631
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer("👤 Введите ваше полное имя")
    await message.answer(text="Ташкент, Шайхантахурский район, массив Гулобод, улица Уйгур", reply_markup=Klinika_buttons())


@dp.message_handler(Text(equals="Меню"))
async def start_bot(message: types.Message):
    with open("menu.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   reply_markup=main_menu(),
                                   caption="<a href='https://evos.uz/'>Перейти на сайт Evos</a>",
                                   parse_mode="HTML")
        await message.answer(
            text="<a href='https://www.instagram.com/evosuzbekistan/'>Instagram</a> | <a href='https://t.me/evosdeliverybot'>Telegram</a> | <a href='https://www.facebook.com/evosuzbekistan/'>Facebook</a>",
            parse_mode="HTML", )


@dp.message_handler(Text(equals="Бектемир"))
async def start_bot(message: types.Message):
    await message.answer(text="📍 На каком филиале хотели бы работать?", reply_markup=Bektemir_menu())


@dp.message_handler(Text(equals="📍 <<Центр торговли Компас>>"))
async def start_bot(message: types.Message):
    await message.answer(text="г. Ташкент, Халка йули, 17-й квартал", reply_markup=Bahodir_menu())
    latitude = 41.239044
    longitude = 69.329295
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя?", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Водник"))
async def start_bot(message: types.Message):
    await message.answer(text="Улица Хусайн Бойкоро, 37А/1", reply_markup=Bahodir_menu())
    latitude = 41.254962
    longitude = 69.374671
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя?", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="📍 Бектемир"))
async def start_bot(message: types.Message):
    await message.answer(text="г. Ташкент, улица Янги Сергели", reply_markup=Bahodir_menu())
    latitude = 41.232693
    longitude = 69.335219
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Bahodir_menu())
    await message.answer(text="👤 Введите ваше полное имя?", reply_markup=Bahodir_menu())


@dp.message_handler(Text(equals="☕️ Показать ближайшие филиалы"))
async def start_bot(message: types.Message):
    await message.answer(text="Отправьте свое местоположение, чтобы найти ближайший филиал", reply_markup=yaqin_filial_menu())

@dp.message_handler(Text(equals="📍 Отправить геолокацию"))
async def start_bot(message: types.Message):
    await message.answer_location()

@dp.message_handler(Text(equals="📞 Контакты/Адрес"))
async def start_bot(message: types.Message):
    with open("Evos.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   reply_markup=main_menu(),
                                   caption="""Адрес: улица Фуркат, 175, вход 1, 
2-й этаж.
Ориентир: MAKRO THE TOWER

Контакт: +998 71 203 12 12""",)

        latitude = 41.302198
        longitude = 69.248871
        await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())

@dp.message_handler(Text(equals="🗣 Новости"))
async def start_bot(message: types.Message):
    await message.answer(text="""Новости компании
Акции
Новые филиалы
Новые торты и т.д.""")

@dp.message_handler(Text(equals="Андижан"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=Andijon_tumanlar_menu())

@dp.message_handler(Text(equals="Универсал  сотрудник"))
async def start_bot(message: types.Message):
    with open("Universal xodim.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график (при наличии)

✔️ Привлекательный внешний вид

💰 Заработная плата от 17228.96 (до уплаты налогов) в час""", reply_markup=Andijon_tumanlar_menu())
        await message.answer("Сейчас открыта вакансия в одном из районов, выберите один из них", reply_markup=Andijon_tumanlar_menu())

@dp.message_handler(Text(equals="📍 Озбегимский Торговый Центр"))
async def start_bot(message: types.Message):
    await message.answer(text="г. Андижан, улица Обод, 31")
    latitude = 40.786262
    longitude = 72.348605
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")




@dp.message_handler(Text(equals="📍 3-й микрорайон"))
async def start_bot(message: types.Message):
    await message.answer(text="г. Андижан, улица Лермонтова, 51")
    latitude = 40.749204
    longitude = 72.346543
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")


@dp.message_handler(Text(equals="📍 Торговый Центр Навруз"))
async def start_bot(message: types.Message):
    await message.answer(text="г. Андижан, улица Лермонтова, 51")
    latitude = 40.749204
    longitude = 72.346543
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")


@dp.message_handler(Text(equals="Карши"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=Qarshi_tumanlar_menu())


@dp.message_handler(Text(equals="Универсальный Сотрудник"))
async def start_bot(message: types.Message):
    with open("Universal xodim.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график работы (по возможности)

✔️ Привлекательный внешний вид

💰 Зарплата от 17 228,96 сум (до уплаты налогов) за один час""",
                                   reply_markup=Qarshi_tumanlar_menu())
        await message.answer("В настоящее время открыта вакансия в одном из районов. Пожалуйста, выберите интересующий вас район", reply_markup=Qarshi_tumanlar_menu())


@dp.message_handler(Text(equals="📍 Сардоба"))
async def start_bot(message: types.Message):
    await message.answer(text="Кашкадарьинская область, Карши, 5-й маленький район")
    latitude = 38.838436
    longitude = 65.787894
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")


@dp.message_handler(Text(equals="📍 Зархал"))
async def start_bot(message: types.Message):
    await message.answer(text="Улица Мустакиллик, здание Пахтазор МФЙ (Зархал)")
    latitude = 38.837743
    longitude = 65.796064
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")


@dp.message_handler(Text(equals="Коканд"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=Qoqon_tumanlar_menu())


@dp.message_handler(Text(equals="Универсальный сотрудник"))
async def start_bot(message: types.Message):
    with open("Universal xodim.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график работы (по возможности)

✔️ Привлекательный внешний вид

💰 Зарплата от 17 228,96 сум (до уплаты налогов) за один час""",
                                   reply_markup=Qoqon_tumanlar_menu())
        await message.answer("В настоящее время открыта вакансия в одном из районов. Пожалуйста, выберите интересующий вас район", reply_markup=Qoqon_tumanlar_menu())


@dp.message_handler(Text(equals="📍 Коканд"))
async def start_bot(message: types.Message):
    await message.answer(text="г. Коканд, улица Мавароннама, 13")
    latitude = 40.553521
    longitude = 70.924092
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")








@dp.message_handler(Text(equals="Наманган"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=Namangan_tumanlar_menu())

@dp.message_handler(Text(equals="Универсальный Сотрудник"))
async def start_bot(message: types.Message):
    with open("Universal xodim.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график работы (по возможности)

✔️ Привлекательный внешний вид

💰 Зарплата от 17 228,96 сум (до уплаты налогов) за один час""",
                                   reply_markup=Namangan_tumanlar_menu())
        await message.answer("В настоящее время открыта вакансия в одном из районов. Пожалуйста, выберите интересующий вас район", reply_markup=Namangan_tumanlar_menu())


@dp.message_handler(Text(equals="📍 Наманган"))
async def start_bot(message: types.Message):
    await message.answer(text="г. Наманган, улица Нодир Кориева, 3")
    latitude = 40.993418
    longitude = 71.667718
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")


@dp.message_handler(Text(equals="Ташкентская область"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=Toshkent_viloyat_tumanlar_menu())

@dp.message_handler(Text(equals="Универсальный Сотрудник"))
async def start_bot(message: types.Message):
    with open("Universal xodim.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график работы (по возможности)

✔️ Привлекательный внешний вид

💰 Зарплата от 17 228,96 сум (до уплаты налогов) за один час""",
                                   reply_markup=Toshkent_viloyat_tumanlar_menu())
        await message.answer("В настоящее время открыта вакансия в одном из районов. Пожалуйста, выберите интересующий вас район", reply_markup=Toshkent_viloyat_tumanlar_menu())


@dp.message_handler(Text(equals="📍 Чирчик городской бог"))
async def start_bot(message: types.Message):
    await message.answer(text="Ташкентская область, г. Чирчик, улица Истироҳат боғи")
    latitude = 41.477064
    longitude = 69.592933
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")


@dp.message_handler(Text(equals="📍 Контейнер"))
async def start_bot(message: types.Message):
    await message.answer(text="Ташкентская область, Бостонлинский район, (Хужакент МФЙ)")
    latitude = 41.622815
    longitude = 69.943048
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")


@dp.message_handler(Text(equals="📍 Янгиюль"))
async def start_bot(message: types.Message):
    await message.answer(text="г. Янгиюль, Файзли МФЙ, улицы Беруний и Тошкент Шох кўчалари чоррахаси")
    latitude = 41.123062
    longitude = 69.073915
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")


@dp.message_handler(Text(equals="📍 <<Троицкий>> Чирчик"))
async def start_bot(message: types.Message):
    await message.answer(text="г. Чирчик, ул. Навоий шох, рядом с рестораном Рохат")
    latitude = 41.436464
    longitude = 69.545743
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")


@dp.message_handler(Text(equals="📍 Бекабад"))
async def start_bot(message: types.Message):
    await message.answer(text="Бекабад, улица Нурли ёл МФЙ, улица Буюк Ипак ёли, 337-й дом.")
    latitude = 40.212555
    longitude = 69.263946
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")


@dp.message_handler(Text(equals="📍 Кибрай"))
async def start_bot(message: types.Message):
    await message.answer(text="массив Гафура Гуляма, улица Алишера Навоий, 23а дом")
    latitude = 41.388065
    longitude = 69.459036
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=main_menu())
    await message.answer(text="👤 Введите ваше полное имя?")









@dp.message_handler(Text(equals="Нукус"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=Unevirsal_Nukus())

@dp.message_handler(Text(equals="Универсальный   сотрудник"))
async def start_bot(message: types.Message):
    with open("Universal xodim.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график работы (по возможности)

✔️ Привлекательный внешний вид

💰 Зарплата от 17 228,96 сум (до уплаты налогов) за один час""",
                                   reply_markup=Unevirsal_Nukus())

@dp.message_handler(Text(equals="📍Контейнер - 2"))
async def start_bot(message: types.Message):
    await message.answer(text="📍 В каком филиале вы хотите работать?", reply_markup=Unevirsal_Nukus())
    await message.answer(text="125 А. Шамуратовой, Нукус, Узбекистан", reply_markup=Unevirsal_Nukus())
    await message.answer(text="👤 Введите ваше полное имя?", reply_markup=Otmena_Orqaga())

@dp.message_handler(Text(equals="Самарканд"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=Samarqand_Uneversal())

@dp.message_handler(Text(equals="Универсальный сотрудник"))
async def start_bot(message: types.Message):
    with open("Universal xodim.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график работы (по возможности)

✔️ Привлекательный внешний вид

💰 Зарплата от 17 228,96 сум (до уплаты налогов) за один час""",
                                   reply_markup=Samarqand_Uneversal())


@dp.message_handler(Text(equals="📍 Бульвар"))
async def start_bot(message: types.Message):
    await message.answer(text="г. Сaмарканд, ул. Орзу Махмудов, 13 дом.")
    latitude = 39.644287
    longitude = 66.956278
    await message.answer_location(latitude=latitude, longitude=longitude)

    await message.answer(text="👤 Введите ваше полное имя?", reply_markup=Otmena_Orqaga())

@dp.message_handler(Text(equals="📍 Фрунзе"))
async def start_bot(message: types.Message):
    await message.answer(text="г. Самарканд, ул. Амира Темура, 93а")
    latitude = 39.648085
    longitude = 66.939146
    await message.answer_location(latitude=latitude, longitude=longitude)

    await message.answer(text="👤 Введите ваше полное имя?", reply_markup=Otmena_Orqaga())



@dp.message_handler(Text(equals="Фергана"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=Fargona_menu())

@dp.message_handler(Text(equals="Универсальный сотрудник"))
async def start_bot(message: types.Message):
    with open("Universal xodim.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график работы (по возможности)

✔️ Привлекательный внешний вид

💰 Зарплата от 17 228,96 сум (до уплаты налогов) за один час""",
                                   reply_markup=Fargona_menu1())

@dp.message_handler(Text(equals="📍 Афсона"))
async def start_bot(message: types.Message):
    await message.answer(text="Фергана, улица Сайилгох, 29-й дом")
    latitude = 40.385523
    longitude = 71.784299
    await message.answer_location(latitude=latitude, longitude=longitude)

    await message.answer(text="👤 Введите ваше полное имя?", reply_markup=Otmena_Orqaga())

@dp.message_handler(Text(equals="Курьер"))
async def start_bot(message: types.Message):
    with open("Kuryer.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, caption="""📌 Возраст от 20 до 35 лет

🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график работы (по возможности)

👨‍💼/👩‍💼 Привлекательный внешний вид

🚘 Наличие личного транспорта обязательно

📍 Место работы и регистрация зарплаты""")
        await message.answer(text="В настоящее время вакансия открыта в одном из районов. Пожалуйста, выберите интересующий вас район", reply_markup=Otmena_Orqaga())

@dp.message_handler(Text(equals="Шахрисабз"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=Unevirsal_Shahrisabz())

@dp.message_handler(Text(equals="Универсальный сотрудник"))
async def start_bot(message: types.Message):
    with open("Universal xodim.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график работы (по возможности)

✔️ Привлекательный внешний вид

💰 Зарплата от 17 228,96 сум (до уплаты налогов) за один час""",
                                   reply_markup=Unevirsal_Shahrisabz())

@dp.message_handler(Text(equals="📍Шахрисабз"))
async def start_bot(message: types.Message):
    await message.answer(text="Шахрисабз, МФУ Тепарлик")
    latitude = 39.053831
    longitude = 66.834863
    await message.answer_location(latitude=latitude, longitude=longitude,)

    await message.answer(text="👤 Введите ваше полное имя?", reply_markup=Otmena_Orqaga())

@dp.message_handler(Text(equals="Хорезмская область"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Выберите интересующую вас должность", reply_markup=Xorazm_Unevirsal())

@dp.message_handler(Text(equals="Универсальный сотрудник"))
async def start_bot(message: types.Message):
    with open("Universal xodim.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график работы (по возможности)

✔️ Привлекательный внешний вид

💰 Зарплата от 17 228,96 сум (до уплаты налогов) за один час""",
                                   reply_markup=Xorazm_Unevirsal())

@dp.message_handler(Text(equals="📍Ургенч"))
async def start_bot(message: types.Message):
    await message.answer(text="Хорезмская область, город Ургенч, улица В.Фязова, 3")
    latitude = 41.560614
    longitude = 60.611802
    await message.answer_location(latitude=latitude, longitude=longitude,)

    await message.answer(text="👤 Введите ваше полное имя?", reply_markup=Otmena_Orqaga())

@dp.message_handler(Text(equals="Курьер"))
async def start_bot(message: types.Message):
    with open("Kuryer.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, caption="""📌 Возраст от 20 до 35 лет

🇷🇺/🇺🇿 Необходимо знание русского и узбекского языков

🕑 Гибкий график работы (по возможности)

👨‍💼/👩‍💼 Привлекательный внешний вид

🚘 Наличие личного транспорта обязательно

📍 Место работы и регистрация зарплаты""")
        await message.answer(text="В настоящее время вакансия открыта в одном из районов. Пожалуйста, выберите интересующий вас район", reply_markup=Otmena_Orqaga())


if __name__ == '__main__':
    executor.start_polling(dp)
