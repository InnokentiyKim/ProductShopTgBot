from .config import KEYBOARD, VERSION, AUTHOR


trading_store = """
<b> Добро пожаловать в приложение GroceryStore!!!</b>
Данное приложение рвзработано и может использоваться торговыми представителями
и коммерческими организациями осуществляющих оптово-розничную торговлю.

С помощью приложения GroceryStore можно без труда принять заказ от клиента,
сформировать заказ в удобном виде и адресовать его кладовщику для дальнейшего
комплектования.
"""

settings = """
<b> Общее руководство:</b>
<i> Навигация:</i>
-<b>({}) - </b><i>назад</i>
-<b>({}) - </b><i>вперед</i>
-<b>({}) - </b><i>увеличить</i>
-<b>({}) - </b><i>уменьшить</i>
-<b>({}) - </b><i>следующий</i>
-<b>({}) - </b><i>предыдущий</i>

<i>Специальные кнопки:</i>
-<b>({}) - </b><i>удалить</i>
-<b>({}) - </b><i>заказ</i>
-<b>({}) - </b><i>оформить заказ</i>

<i>Общая информация:</i>
-<b>версия программы - </b><i>({})</i>
-<b>разработчик - </b><i>({})</i>

<b>{}Иннокентий Ким</b><i>({})</i>
""".format(
    KEYBOARD['<<'],
    KEYBOARD['>>'],
    KEYBOARD['UP'],
    KEYBOARD['DOWN'],
    KEYBOARD['NEXT_STEP'],
    KEYBOARD['BACK_STEP'],
    KEYBOARD['X'],
    KEYBOARD['ORDER'],
    KEYBOARD['APPLY'],
    VERSION,
    AUTHOR,
    KEYBOARD['COPY']
)

product_order = """
Выбранный товар:

{}
{}
Стоимость: {} руб
Добавлен в заказ!!!
На складе осталось {} ед.
"""

order = """
<i>Название:</i> <b>{}</b>
<i>Описание:</i> <b>{}</b>
<i>Стоимость:</i> <b>{} руб за 1 ед.</b>
<i>Количество позиций:</i> <b>{} ед.</b>
"""

order_number = """
<b>Позиция в заказе № </b> <i>{}</i>
"""

no_orders = """
<b>Заказ отсутствует!!!</b>
"""

apply = """
<b>Ваш заказ оформлен!!!</b>
<i>Общая стоимость заказа:</i> <b>{} руб</b>
<i>Общее количество позиций:</i> <b>{} ед.</b>
<b>ЗАКАЗ ПРИНЯТ И КОМПЛЕКТУЕТСЯ!!!</b>
"""

MESSAGES = {
    'trading_store': trading_store,
    'product_order': product_order,
    'order': order,
    'order_number': order_number,
    'no_orders': no_orders,
    'apply': apply,
    'settings': settings
}