from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🏢 О компании"), KeyboardButton(text="📍 Филиалы"))
    rkm.row(KeyboardButton(text="💼 Вакансии"))
    rkm.row(KeyboardButton(text="Меню"), KeyboardButton(text="🗣 Новости"))
    rkm.row(KeyboardButton(text="📞 Контакты/Адрес"), KeyboardButton(text="🇺🇿/🇷🇺 Язык"))
    return rkm


def Operaror_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Бош Офис"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Operaror2_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Олмазор"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Kuryer_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Олмазор"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def filial_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="☕️ Показать ближайшие филиалы"))
    rkm.row(KeyboardButton(text="🏢 Главный офис"), KeyboardButton(text="Ташкент ш."))
    rkm.row(KeyboardButton(text="⬅️ Назад"), )
    return rkm

def ishorinlari_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Ташкент"), KeyboardButton(text="Андижан"))
    rkm.row(KeyboardButton(text="Карши"), KeyboardButton(text="Коканд"))
    rkm.row(KeyboardButton(text="Наманган"), KeyboardButton(text="Ташкентская область"))
    rkm.row(KeyboardButton(text="Нукус"), KeyboardButton(text="Самарканд"))
    rkm.row(KeyboardButton(text="Фергана"), KeyboardButton(text="Шахрисабз"))
    rkm.row(KeyboardButton(text="Хорезмская область"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def lavozimlar_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"), KeyboardButton(text="Оператор колл-центра"))
    rkm.row(KeyboardButton(text="Курьер"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Tumanlar_menu1():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Юнусабад"), KeyboardButton(text="Мирзо Улугбек"))
    rkm.row(KeyboardButton(text="Яшнабад"), KeyboardButton(text="Яккасарай"))
    rkm.row(KeyboardButton(text="Учтепа"), KeyboardButton(text="Сергели"))
    rkm.row(KeyboardButton(text="Чиланзар"), KeyboardButton(text="Миробод"))
    rkm.row(KeyboardButton(text="Шайхонтахур"), KeyboardButton(text="Олмазор"))
    rkm.row(KeyboardButton(text="Бектемир"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm



def Yunusobod_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Баходир"), KeyboardButton(text="📍 Олой Бозори"),
            KeyboardButton(text="📍 Юнусабад"))
    rkm.row(KeyboardButton(text="📍 Универсам"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Bahodir_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Mirzo_Ulugbek_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Паркент"), KeyboardButton(text="📍 Максим Горький"),
            KeyboardButton(text="📍 Корасу"))
    rkm.row(KeyboardButton(text="📍 Экобозор торговый центр"), KeyboardButton(text="📍 Сельхоз"),
            KeyboardButton(text="📍 Ташкентский текстильный завод"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Yashnobod_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Лисунова 2"), KeyboardButton(text="📍 Лисунова"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Yakkasaroy_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Шота Руставели"), KeyboardButton(text="📍 Мухаммад Мукумий"),
            KeyboardButton(text="📍 'Следующий' Торговый Центр"))
    rkm.row(KeyboardButton(text="📍 Театральный"), KeyboardButton(text="📍 Южный"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Uchtepa_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Бешкайрагач"), KeyboardButton(text="📍 Фозилтепа"),
            KeyboardButton(text="📍 Лутфий"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm



def Sergeli_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Сергели"), KeyboardButton(text="📍 Новая Жизнь Сергели"),
            KeyboardButton(text="📍 Ярмарка Сергели"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Chilonzor_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Чилонзор"), KeyboardButton(text="📍 Алгоритм"),
            KeyboardButton(text="📍 Магик Сити"))
    rkm.row(KeyboardButton(text="📍 Катта Кани"), KeyboardButton(text="📍 Катортол"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm



def Mirobod_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Куйлюк"), KeyboardButton(text="📍 Боровский"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm



def Toshkent_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm



def Shayxontahur_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍ТошМИ"), KeyboardButton(text="📍София"), KeyboardButton(text="📍Чорсу ГУМ"))
    rkm.row(KeyboardButton(text="📍Самарканд дарвоза"), KeyboardButton(text="📍Навоий кўчаси"),
            KeyboardButton(text="📍Белтепа"))
    rkm.row(KeyboardButton(text="📍1-городская клиническая больница"))
    rkm.row(KeyboardButton(text="⬅️ Назад"))
    return rkm


def Toshmi_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm



def Klinika_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm



def Sofiya_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Chorshugum_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Samarqand_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Navoiy_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Beltepa_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm



def Olmazor_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍Орзу"), KeyboardButton(text="📍Каракамыш 1/3"),
            KeyboardButton(text="📍Охунбобоев"))
    rkm.row(KeyboardButton(text="📍Каракамыш 2/4"), KeyboardButton(text="📍Старый город"))
    rkm.row(KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="❌ Отменить ❌"))
    return rkm



def Bektemir_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Торговый центр <<Компас>>"), KeyboardButton(text="📍 Водник"),
            KeyboardButton(text="📍 Бектемир"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def yaqin_filial_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Отправить местоположение", request_location=True))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def Andijon_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"),KeyboardButton(text="Курьер"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Andijon_tumanlar_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Узбегимский торговый центр"),KeyboardButton(text="📍 3-й микрорайон"),KeyboardButton(text="📍 Наврузский торговый центр"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Qarshi_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"),KeyboardButton(text="Курьер"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def Qarshi_tumanlar_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Сардоба"),KeyboardButton(text="📍 Зархал"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Qoqon_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"),KeyboardButton(text="Курьер"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def Qoqon_tumanlar_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Коканд"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Namangan_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"),KeyboardButton(text="Курьер"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def Namangan_tumanlar_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Наманган"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm


def Toshkent_viloyat_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"),KeyboardButton(text="Курьер"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def Toshkent_viloyat_tumanlar_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Чирчик городской округ"),KeyboardButton(text="📍 Контейнер"),KeyboardButton(text="📍 Янгиюль"))
    rkm.row(KeyboardButton(text="📍 <<Троицкий >> Чирчик"),KeyboardButton(text="📍 Бекабад"),KeyboardButton(text="📍 Кибрай"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm



def Nukus_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))

def Unevirsal_Nukus():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный   сотрудник"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def joylar_Nukus():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Контейнер - 2"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def Otmena_Orqaga():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def Samarqand_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный  Сотрудник"),KeyboardButton(text="Курьер") )
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def Samarqand_Uneversal():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Фрунзе"),KeyboardButton(text="📍 Бульвар") )
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def Fargona_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"),KeyboardButton(text="Курьер") )
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def Unevirsal_Fargona():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))



def Fargona_menu1():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍Афсона"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def Sharisabz_munu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Универсальный сотрудник"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))

def Unevirsal_Shahrisabz():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍Шахрисабз"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

def Xorazm_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Хорезмская область"), KeyboardButton(text="Курьер"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm
def Xorazm_Unevirsal():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍Ургенч"))
    rkm.row(KeyboardButton(text="❌ Отменить ❌"), KeyboardButton(text="⬅️ Назад"))
    return rkm

