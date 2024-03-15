import telebot
from telebot import types
import time
import os
import email
from email.message import EmailMessage
from datetime import datetime
import random
import sys
import time

bot = telebot.TeleBot('ID_BOT')

user_answers = {}
chat_states = {}
ID_manager = 'tg_id_menedger'

@bot.message_handler(commands=['start'])
def start_button(message):
  bot.send_message(message.chat.id, f'Добрый день, <b>{message.from_user.first_name}</b>!\nУказывая свои данные, Вы соглашаетесь с политикой конфиденциальности.\nДля работы с ботом используйте кнопку "Меню"... \U0001F447',\
                     parse_mode = 'html')
#-------------------------------------------------------------------------------

@bot.message_handler(commands=['about_company'])
def about_company_button(message):
  bot.send_message(message.chat.id, 'Менеджер Доставки 8 лет помогает компаниям в организации международной перевозки грузов на импорт и экспорт.\n\nМы упростили взаимодействие с транспортной компанией. Работа с нами осуществляется в режиме одного менеджера. Он разработает маршрут, поможет заполнить необходимые документы и проведет доставку от начала до конца.\n\nВаш Менеджер Доставки владеет иностранными языками. Он поможет в общении с поставщиком и согласует выгодные условия для отгрузки.\n\nНаш сервис подойдет опытным компаниям и только начинающим свою международную деятельность.')
#-------------------------------------------------------------------------------

@bot.message_handler(commands=['web_site'])
def web_site_button(message):
  bot.send_message(message.chat.id, 'https://deliverymanager.biz/ru/')
#-------------------------------------------------------------------------------
@bot.message_handler(commands=['consultation'])
def consultation_button(message):
  user_id = message.from_user.id
  user_answers[user_id] = {}
  bot.send_message(message.chat.id, 'Укажите название компании или Ваше имя, а также Ваш телефон и email')
  bot.register_next_step_handler(message, get_name)

def get_name(message):
  user_id = message.from_user.id
  if message.text == '/web_site':
    web_site_button(message)
  elif message.text == '/about_company':
    about_company_button(message)
  elif message.text == '/services':
    services_button(message)
  elif message.text == '/cost_calculation':
    cost_calculation_button(message)
  else:
    user_answers[user_id]['contacts'] = message.text
    bot.send_message(message.chat.id, 'Какой у Вас вопрос?')
    bot.register_next_step_handler(message, comment_is)

def comment_is(message):
  now = datetime.now()
  random_number = random.randint(0, 99)
  user_id = message.from_user.id
  if message.text == '/web_site':
    web_site_button(message)
  elif message.text == '/about_company':
    about_company_button(message)
  elif message.text == '/services':
    services_button(message)
  elif message.text == '/cost_calculation':
    cost_calculation_button(message)
  else:
    user_answers[user_id]['comments'] = message.text
    bot.send_message(ID_manager, f"Запрос_звонка_{now.strftime('%Y-%m-%d')}_{random_number}\n" f"Контакты клиента: {user_answers[user_id]['contacts']}\n" f"Комментарии к заказу: {user_answers[user_id]['comments']}\n" f"Ник клиента в Telegram - https://t.me/{message.from_user.username}\n")
    del user_answers[user_id]
    bot.send_message(message.chat.id, 'Спасибо за обращение в нашу компанию! Менеджер свяжется с Вами в ближайшее время!\nДля продолжения работы с ботом воспользуйтесь кнопкой "Меню".')
#-------------------------------------------------------------------------------

@bot.message_handler(commands=['services'])
def services_button(message):
  keyboard_1 = types.InlineKeyboardMarkup()
  bot1 = types.InlineKeyboardButton('Авиаперевозки', callback_data='air_transportation_service')
  keyboard_1.add(bot1)
  bot2 = types.InlineKeyboardButton('Автомобильные перевозки', callback_data='avto_transportation_service')
  keyboard_1.add(bot2)
  bot3 = types.InlineKeyboardButton('Морские перевозки', callback_data='sea_transportation_service')
  keyboard_1.add(bot3)
  bot4 = types.InlineKeyboardButton('Железнодорожные перевозки', callback_data='railway_transportation_service')
  keyboard_1.add(bot4)
  bot5 = types.InlineKeyboardButton('Страхование груза', callback_data='cargo_insurance')
  keyboard_1.add(bot5)
  bot6 = types.InlineKeyboardButton('Таможенное оформление', callback_data='customs_clearance')
  keyboard_1.add(bot6)
  bot7 = types.InlineKeyboardButton('Вывоз груза с таможни', callback_data='cargo_removal_from_customs')
  keyboard_1.add(bot7)
  bot8 = types.InlineKeyboardButton('Оплата сборов СВХ', callback_data='payment_of_fees_SVH')
  keyboard_1.add(bot8)
  bot9 = types.InlineKeyboardButton('Организация погрузки, разгрузки', callback_data='organization_of_loading')
  keyboard_1.add(bot9)
  bot10 = types.InlineKeyboardButton('Перевозка опасного груза', callback_data='dangerous_cargo')
  keyboard_1.add(bot10)
  bot11 = types.InlineKeyboardButton('Общение с иностранным поставщиком', callback_data='supplier_communication')
  keyboard_1.add(bot11)
  bot.send_message(message.chat.id, 'Какая услуга Вас интересует?', reply_markup=keyboard_1)
#-------------------------------------------------------------------------------

@bot.message_handler(commands=['cost_calculation'])
def cost_calculation_button(message):
  keyboard_2 = types.InlineKeyboardMarkup()
  bot12 = types.InlineKeyboardButton('Авиаперевозки', callback_data='cost_air_transportation_service')
  keyboard_2.add(bot12)
  bot13 = types.InlineKeyboardButton('Автомобильные перевозки', callback_data='cost_avto_transportation_service')
  keyboard_2.add(bot13)
  bot14 = types.InlineKeyboardButton('Морские перевозки', callback_data='cost_sea_transportation_service')
  keyboard_2.add(bot14)
  bot15 = types.InlineKeyboardButton('Железнодорожные перевозки', callback_data='cost_railway_transportation_service')
  keyboard_2.add(bot15)
  bot16 = types.InlineKeyboardButton('Страхование груза', callback_data='cost_cargo_insurance')
  keyboard_2.add(bot16)
  bot17 = types.InlineKeyboardButton('Таможенное оформление', callback_data='cost_customs_clearance')
  keyboard_2.add(bot17)
  bot18 = types.InlineKeyboardButton('Вывоз груза с таможни', callback_data='cost_cargo_removal_from_customs')
  keyboard_2.add(bot18)
  bot19 = types.InlineKeyboardButton('Оплата сборов СВХ', callback_data='cost_payment_of_fees_SVH')
  keyboard_2.add(bot19)
  bot20 = types.InlineKeyboardButton('Организация погрузки, разгрузки', callback_data='cost_organization_of_loading')
  keyboard_2.add(bot20)
  bot21 = types.InlineKeyboardButton('Перевозка опасного груза', callback_data='cost_dangerous_cargo')
  keyboard_2.add(bot21)
  bot22 = types.InlineKeyboardButton('Общение с иностранным поставщиком', callback_data='cost_supplier_communication')
  keyboard_2.add(bot22)
  bot.send_message(message.chat.id, 'Какая услуга Вас интересует?', reply_markup=keyboard_2)
#-------------------------------------------------------------------------------

@bot.callback_query_handler(func=lambda call: call.data == 'air_transportation_service')
def callback_inline_01(call):
  keyboard_3 = types.InlineKeyboardMarkup()
  bot23 = types.InlineKeyboardButton('Расчет стоимости', callback_data='cost_air_transportation_service')
  keyboard_3.add(bot23)
  bot.send_message(call.message.chat.id, '<b>Подробнее об услуге Авиаперевозка</b>\n\nВоздушные перевозки позволяют доставлять грузы в максимально короткие сроки.\nМы работаем с большим количеством авиакомпаний и сможем подобрать подходящий маршрут для любого груза.\nРаботаем с прямыми и транзитными рейсами, с пассажирскими и грузовыми самолетами.\n\n<b>Преимущества авиаперевозок</b>\n\n• Большое количество рейсов\n• Высокий уровень безопасности\n• Быстрое прохождение таможенных процедур\n• Перевозка очень мелких грузов',\
                      parse_mode = 'html', reply_markup=keyboard_3)

@bot.callback_query_handler(func=lambda call: call.data == 'avto_transportation_service')
def callback_inline_02(call):
  keyboard_4 = types.InlineKeyboardMarkup()
  bot24 = types.InlineKeyboardButton('Расчет стоимости', callback_data='cost_avto_transportation_service')
  keyboard_4.add(bot24)
  bot.send_message(call.message.chat.id, '<b>Подробнее об услуге</b>\n\nАвтоперевозки позволяют перевезти груз быстро и по доступной цене.\nМы организуем международные автомобильные грузоперевозки двумя способами:\n• отдельная машина разной грузоподъемности (от 1,5 до 20 тонн);\n• сборные грузы для перевозки небольших грузов.\n\n<b>Преимущества автоперевозок</b>\n\n• Подходит для всех типов грузов\n• Соотношение цены и скорости\n• Гибкость при выборе СВХ размещения\n• Возможность оформления "с колес"',\
                      parse_mode = 'html', reply_markup=keyboard_4)

@bot.callback_query_handler(func=lambda call: call.data == 'sea_transportation_service')
def callback_inline_03(call):
  keyboard_5 = types.InlineKeyboardMarkup()
  bot25 = types.InlineKeyboardButton('Расчет стоимости', callback_data='cost_sea_transportation_service')
  keyboard_5.add(bot25)
  bot.send_message(call.message.chat.id, '<b>Подробнее об услуге</b>\n\nОрганизуем морские перевозки коммерческих грузов на импорт и экспорт.\nКонтейнерные перевозки - один из самых экономичных видов перевозки. Мы организуем перевозки отдельным контейнером разного размера 20DC, 40DC, 40HQ, и типа: закрытые, открытые (OPEN TOP) и REF контейнеры с температурным режимом.\n\n<b>Преимущества морских перевозок</b>\n\n• Морской борт универсален для приема груза любого типа\n• Высокая грузоподъемность и вместительность контейнера\n• Низкие тарифы\n• Минимальный риск повреждения товаров в пути',\
                      parse_mode = 'html', reply_markup=keyboard_5)

@bot.callback_query_handler(func=lambda call: call.data == 'railway_transportation_service')
def callback_inline_04(call):
  keyboard_6 = types.InlineKeyboardMarkup()
  bot26 = types.InlineKeyboardButton('Расчет стоимости', callback_data='cost_railway_transportation_service')
  keyboard_6.add(bot26)
  bot.send_message(call.message.chat.id, '<b>Подробнее об услуге</b>\n\nДанный тип перевозки подходит для крупногабаритных грузов и позволяет перевозить тяжелые грузы. Мы подберем варианты перевозки в контейнере, вагоне или на платформе.\nМы организуем отправку по железной дороге в составе сборных контейнеров. Этот вариант перевозки может оказаться дешевле и быстрее альтернативных морских логистических путей.\n\n<b>Преимущества ЖД перевозок</b>\n\n• Высокая грузоподъемность подвижного состава\n• Безопасная перевозка хрупких товаров\n• Выгодная доставка насыпных и наливных грузов\n• Возможности для перевозки негабаритного груза',\
                      parse_mode = 'html', reply_markup=keyboard_6)

@bot.callback_query_handler(func=lambda call: call.data == 'cargo_insurance')
def callback_inline_05(call):
  keyboard_7 = types.InlineKeyboardMarkup()
  bot27 = types.InlineKeyboardButton('Расчет стоимости', callback_data='cost_cargo_insurance')
  keyboard_7.add(bot27)
  bot.send_message(call.message.chat.id, '<b>Подробнее об услуге</b>\n\nМы бережно доставляем ваши грузы и строго соблюдаем сроки. Но бывают внешние обстоятельства, которые невозможно предугадать. Чтобы избежать потенциальных рисков, мы предлагаем оформить услуги страхования. Мы установили низкую стоимость услуги и готовы оформить страховой полис на любой груз. Груз страхуется на всем маршруте перевозки, а страховой полис покрывает все возможные риски и гарантирует быстрые выплаты.\n\nМы бережно доставляем ваши грузы и строго соблюдаем сроки. Но бывают внешние обстоятельства, которые невозможно предугадать. Чтобы избежать потенциальных рисков, мы предлагаем оформить услуги страхования. Мы установили низкую стоимость услуги и готовы оформить страховой полис на любой груз. Груз страхуется на всем маршруте перевозки, а страховой полис покрывает все возможные риски и гарантирует быстрые выплаты.',\
                      parse_mode = 'html', reply_markup=keyboard_7)

@bot.callback_query_handler(func=lambda call: call.data == 'customs_clearance')
def callback_inline_06(call):
  keyboard_8 = types.InlineKeyboardMarkup()
  bot28 = types.InlineKeyboardButton('Расчет стоимости', callback_data='cost_customs_clearance')
  keyboard_8.add(bot28)
  bot.send_message(call.message.chat.id, '<b>Подробнее об услуге</b>\n\nТаможенное оформление грузов - важный этап в процессе перемещения товаров через границу. Таможенное оформление грузов включает в себя следующие процедуры: - подача декларации - проверка документов - оценка товарных стоимостей - уплата пошлин и налогов - приграничный контроль - освобождение груза.\n\nНаша компания предоставляет услуги таможенного оформления. Мы проверяем правильность заполнения документов и их наличия, кроме того, предлагаем проверенных брокеров. Уже более 8 лет помогаем фирмам в организации международных перевозок, работаем на импорт, и экспорт.',\
                      parse_mode = 'html', reply_markup=keyboard_8)

@bot.callback_query_handler(func=lambda call: call.data == 'cargo_removal_from_customs')
def callback_inline_07(call):
  keyboard_9 = types.InlineKeyboardMarkup()
  bot29 = types.InlineKeyboardButton('Расчет стоимости', callback_data='cost_cargo_removal_from_customs')
  keyboard_9.add(bot29)
  bot.send_message(call.message.chat.id, '<b>Подробнее об услуге</b>\n\nПосле выпуска таможенной декларации остается только забрать груз и доставить его по адресу. Но этот процесс часто вызывает много проблем. Мы позаботились о финальной части доставки. Ваш Менеджер Доставки заранее проверит зарегистрирована ли на СВХ (склад временного хранения) доверенность. Мы подготовим доверенности и вышлем вместе с инструкциями по их подписанию с помощью электронной подписи. Проверим наличие денег на счету для оплаты услуг СВХ, назначим водителя и оформим необходимые пропуска.\n\nВывоз груза с СВХ занимает много времени и требует внимания. Мы вывозим много грузов одновременно. Поэтому наши процессы отлажены, а стоимость таких услуг невысокая.',\
                      parse_mode = 'html', reply_markup=keyboard_9)

@bot.callback_query_handler(func=lambda call: call.data == 'payment_of_fees_SVH')
def callback_inline_08(call):
  keyboard_10 = types.InlineKeyboardMarkup()
  bot30 = types.InlineKeyboardButton('Расчет стоимости', callback_data='cost_payment_of_fees_SVH')
  keyboard_10.add(bot30)
  bot.send_message(call.message.chat.id, '<b>Подробнее об услуге</b>\n\nТаможенные склады временного хранения (СВХ) осуществляют терминальную обработку и хранение груза во время его таможенного оформления. Склад взимает сбор за работу по официальному прейскуранту терминала. Оплатить счет необходимо до вывоза товара с СВХ, но на дату вывоза. Мы оплачиваем сборы СВХ под свой контракт, чтобы деньги пришли на таможенный счет вовремя.\n\nКаждый день простоя увеличивает расходы на хранение. Мы берем на себя расчеты за въезд на территорию, погрузо-разгрузочные работы, хранение товара на СВХ. Вы экономите время и деньги. Рекомендуем заказывать услугу вместе с услугой вывоза груза с СВХ и доставкой до двери по всей стране.',\
                      parse_mode = 'html', reply_markup=keyboard_10)

@bot.callback_query_handler(func=lambda call: call.data == 'organization_of_loading')
def callback_inline_09(call):
  keyboard_11 = types.InlineKeyboardMarkup()
  bot31 = types.InlineKeyboardButton('Расчет стоимости', callback_data='cost_organization_of_loading')
  keyboard_11.add(bot31)
  bot.send_message(call.message.chat.id, '<b>Подробнее об услуге</b>\n\nОрганизация погрузочно-разгрузочных работ - важная составляющая в логистической цепи доставки грузов. Это процесс переноса товаров между различными транспортными средствами, складами или местами назначения. Правильная организация погрузочно-разгрузочных работ способствует эффективной и безопасной доставке, сокращению времени и стоимости перевозки.\nПервый шаг в организации таких работ - это подробное планирование. Необходимо определить количество грузов, их характеристики и особенности:\n• вес;\n• размеры;\n• количество;\n• условия хранения.\nЭто поможет определить необходимое оборудование и ресурсы для выполнения работ.\n\nВажный аспект организации - выбор подходящих средств для проведения процедуры.\nНаша компания предлагает спец. технику для осуществления процесса в зависимости от веса и габаритов товара. Мы даем рекомендации по упаковке и подготовке груза к перевозке.',\
                      parse_mode = 'html', reply_markup=keyboard_11)

@bot.callback_query_handler(func=lambda call: call.data == 'dangerous_cargo')
def callback_inline_10(call):
  keyboard_12 = types.InlineKeyboardMarkup()
  bot32 = types.InlineKeyboardButton('Расчет стоимости', callback_data='cost_dangerous_cargo')
  keyboard_12.add(bot32)
  bot.send_message(call.message.chat.id, '<b>Подробнее об услуге</b>\n\nПеревозка опасных грузов - максимально ответственная процедура, что требует строгого соблюдения правил и норм безопасности. Товары представляют угрозу для окружающей среды, людей и имущества, поэтому их транспортировка должна быть тщательно организована и контролируема.\nКак правило, речь идет о веществах, материалах или предметах, которые могут создавать опасность для окружающего пространства и людей. Это:\n• химические вещества;\n• яды;\n• взрывчатые вещества;\n• радиоактивные материалы;\n• газы;\n• органические и биологические вещества;\n• оружие или легковоспламеняющиеся материалы.\n\nМы проконсультируем, как перевезти такой товар, дадим подробные советы по оформлению паспорта безопасности и будем сопровождать процесс от начала до конца, на всех этапах.',\
                      parse_mode = 'html', reply_markup=keyboard_12)

@bot.callback_query_handler(func=lambda call: call.data == 'supplier_communication')
def callback_inline_11(call):
  keyboard_13 = types.InlineKeyboardMarkup()
  bot33 = types.InlineKeyboardButton('Расчет стоимости', callback_data='cost_supplier_communication')
  keyboard_13.add(bot33)
  bot.send_message(call.message.chat.id, '<b>Подробнее об услуге</b>\n\nУслуга общения с поставщиком предоставляется бесплатно и дополняет сервис компании Менеджер Доставки. Наши логисты находятся по всему миру и владеют разными иностранными языками.\n\nМы возьмем на себя общение, согласуем выгодные и комфортные условия поставки, поторопим поставщика, чтобы успеть отгрузить товар в нужные даты. Возьмем на себя рутинную работу и освободим Ваше время для более важных дел.',\
                      parse_mode = 'html', reply_markup=keyboard_13)
#-------------------------------------------------------------------------------

@bot.callback_query_handler(func=lambda call: call.data == 'cost_air_transportation_service')
def callback_inline_21(call):
  chat_states[call.message.chat.id] = {'state': 'cost_air_transportation_service', 'questions_asked': 0}
  bot.send_message(call.message.chat.id, text = 'Укажите адреса отправки и доставки')

@bot.callback_query_handler(func=lambda call: call.data == 'cost_avto_transportation_service')
def callback_inline_22(call):
  chat_states[call.message.chat.id] = {'state': 'cost_avto_transportation_service', 'questions_asked': 0}
  bot.send_message(call.message.chat.id, text = 'Укажите адреса отправки и доставки')

@bot.callback_query_handler(func=lambda call: call.data == 'cost_sea_transportation_service')
def callback_inline_23(call):
  chat_states[call.message.chat.id] = {'state': 'cost_sea_transportation_service', 'questions_asked': 0}
  bot.send_message(call.message.chat.id, text = 'Укажите адреса отправки и доставки')

@bot.callback_query_handler(func=lambda call: call.data == 'cost_railway_transportation_service')
def callback_inline_24(call):
  chat_states[call.message.chat.id] = {'state': 'cost_railway_transportation_service', 'questions_asked': 0}
  bot.send_message(call.message.chat.id, text = 'Укажите адреса отправки и доставки')

@bot.callback_query_handler(func=lambda call: call.data == 'cost_cargo_insurance')
def callback_inline_25(call):
  chat_states[call.message.chat.id] = {'state': 'cost_cargo_insurance', 'questions_asked': 0}
  bot.send_message(call.message.chat.id, text = 'Укажите название компании или Ваше имя, а также Ваш телефон и email')

@bot.callback_query_handler(func=lambda call: call.data == 'cost_customs_clearance')
def callback_inline_26(call):
  chat_states[call.message.chat.id] = {'state': 'cost_customs_clearance', 'questions_asked': 0}
  bot.send_message(call.message.chat.id, text = 'Укажите название компании или Ваше имя, а также Ваш телефон и email')

@bot.callback_query_handler(func=lambda call: call.data == 'cost_cargo_removal_from_customs')
def callback_inline_27(call):
  chat_states[call.message.chat.id] = {'state': 'cost_cargo_removal_from_customs', 'questions_asked': 0}
  bot.send_message(call.message.chat.id, text = 'Укажите название компании или Ваше имя, а также Ваш телефон и email')

@bot.callback_query_handler(func=lambda call: call.data == 'cost_payment_of_fees_SVH')
def callback_inline_28(call):
  chat_states[call.message.chat.id] = {'state': 'cost_payment_of_fees_SVH', 'questions_asked': 0}
  bot.send_message(call.message.chat.id, text = 'Укажите название компании или Ваше имя, а также Ваш телефон и email')

@bot.callback_query_handler(func=lambda call: call.data == 'cost_organization_of_loading')
def callback_inline_29(call):
  chat_states[call.message.chat.id] = {'state': 'cost_organization_of_loading', 'questions_asked': 0}
  bot.send_message(call.message.chat.id, text = 'Укажите название компании или Ваше имя, а также Ваш телефон и email')

@bot.callback_query_handler(func=lambda call: call.data == 'cost_dangerous_cargo')
def callback_inline_30(call):
  chat_states[call.message.chat.id] = {'state': 'cost_dangerous_cargo', 'questions_asked': 0}
  bot.send_message(call.message.chat.id, text = 'Укажите название компании или Ваше имя, а также Ваш телефон и email')

@bot.callback_query_handler(func=lambda call: call.data == 'cost_supplier_communication')
def callback_inline_31(call):
  chat_states[call.message.chat.id] = {'state': 'cost_supplier_communication', 'questions_asked': 0}
  bot.send_message(call.message.chat.id, text = 'Укажите название компании или Ваше имя, а также Ваш телефон и email')
#-------------------------------------------------------------------------------

@bot.message_handler(func=lambda message: True)
def handle_text(message):
  if chat_states:
    if chat_states[message.chat.id]:
      state = chat_states.get(message.chat.id, {}).get('state')

      if state == 'cost_air_transportation_service':
        questions_asked = chat_states[message.chat.id]['questions_asked']

        if questions_asked == 0:
          user_id = message.from_user.id
          user_answers[user_id] = {}
          now = datetime.now()
          random_number = random.randint(0, 99)
          user_answers[user_id]['heading'] = f"Заявка_авиаперевозка_{now.strftime('%Y-%m-%d')}_{random_number}"
          user_answers[user_id]['from_to'] = message.text
          bot.send_message(message.chat.id, 'Укажите вес, габариты и объем груза')
          chat_states[message.chat.id]['questions_asked'] += 1

        elif questions_asked == 1:
          user_id = message.from_user.id
          user_answers[user_id]['wsv'] = message.text
          bot.send_message(message.chat.id, 'Укажите название компании или Ваше имя, а также Ваш телефон и email')
          chat_states[message.chat.id]['questions_asked'] += 1

        elif questions_asked == 2:
          user_id = message.from_user.id
          user_answers[user_id]['contacts'] = message.text
          bot.send_message(message.chat.id, 'Хотите что-то добавить к заявке?')
          chat_states[message.chat.id]['questions_asked'] += 1

        elif questions_asked == 3:
          user_id = message.from_user.id
          user_answers[user_id]['comments'] = message.text
          bot.send_message(ID_manager, f"{user_answers[user_id]['heading']}\n" f"Адрес отправки и доставки: {user_answers[user_id]['from_to']}\n" f"Параметры груза: {user_answers[user_id]['wsv']}\n" f"Контакты клиента: {user_answers[user_id]['contacts']}\n" f"Комментарии к заказу: {user_answers[user_id]['comments']}\n" f"Ник клиента в Telegram - https://t.me/{message.from_user.username}\n")
          del user_answers[user_id]
          bot.send_message(message.chat.id, 'Спасибо за обращение в нашу компанию! Менеджер свяжется с Вами в ближайшее время!\nДля продолжения работы с ботом воспользуйтесь кнопкой "Меню".')
          chat_states[message.chat.id] = None

      if state == 'cost_avto_transportation_service':
        questions_asked = chat_states[message.chat.id]['questions_asked']
        if questions_asked == 0:
          user_id = message.from_user.id
          user_answers[user_id] = {}
          now = datetime.now()
          random_number = random.randint(0, 99)
          user_answers[user_id]['heading'] = f"Заявка_автоперевозка_{now.strftime('%Y-%m-%d')}_{random_number}"
          user_answers[user_id]['from_to'] = message.text
          bot.send_message(message.chat.id, 'Укажите вес, габариты и объем груза')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 1:
          user_id = message.from_user.id
          user_answers[user_id]['wsv'] = message.text
          bot.send_message(message.chat.id, 'Укажите название компании или Ваше имя, а также Ваш телефон и email')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 2:
          user_id = message.from_user.id
          user_answers[user_id]['contacts'] = message.text
          bot.send_message(message.chat.id, 'Хотите что-то добавить к заявке?')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 3:
          user_id = message.from_user.id
          user_answers[user_id]['comments'] = message.text
          bot.send_message(ID_manager, f"{user_answers[user_id]['heading']}\n" f"Адрес отправки и доставки: {user_answers[user_id]['from_to']}\n" f"Параметры груза: {user_answers[user_id]['wsv']}\n" f"Контакты клиента: {user_answers[user_id]['contacts']}\n" f"Комментарии к заказу: {user_answers[user_id]['comments']}\n" f"Ник клиента в Telegram - https://t.me/{message.from_user.username}\n")
          del user_answers[user_id]
          bot.send_message(message.chat.id, 'Спасибо за обращение в нашу компанию! Менеджер свяжется с Вами в ближайшее время!\nДля продолжения работы с ботом воспользуйтесь кнопкой "Меню".')
          chat_states[message.chat.id] = None

      if state == 'cost_sea_transportation_service':
        questions_asked = chat_states[message.chat.id]['questions_asked']
        if questions_asked == 0:
          user_id = message.from_user.id
          user_answers[user_id] = {}
          now = datetime.now()
          random_number = random.randint(0, 99)
          user_answers[user_id]['heading'] = f"Заявка_морская_перевозка_{now.strftime('%Y-%m-%d')}_{random_number}"
          user_answers[user_id]['from_to'] = message.text
          bot.send_message(message.chat.id, 'Укажите вес, габариты и объем груза')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 1:
          user_id = message.from_user.id
          user_answers[user_id]['wsv'] = message.text
          bot.send_message(message.chat.id, 'Укажите название компании или Ваше имя, а также Ваш телефон и email')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 2:
          user_id = message.from_user.id
          user_answers[user_id]['contacts'] = message.text
          bot.send_message(message.chat.id, 'Хотите что-то добавить к заявке?')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 3:
          user_id = message.from_user.id
          user_answers[user_id]['comments'] = message.text
          bot.send_message(ID_manager, f"{user_answers[user_id]['heading']}\n" f"Адрес отправки и доставки: {user_answers[user_id]['from_to']}\n" f"Параметры груза: {user_answers[user_id]['wsv']}\n" f"Контакты клиента: {user_answers[user_id]['contacts']}\n" f"Комментарии к заказу: {user_answers[user_id]['comments']}\n" f"Ник клиента в Telegram - https://t.me/{message.from_user.username}\n")
          del user_answers[user_id]
          bot.send_message(message.chat.id, 'Спасибо за обращение в нашу компанию! Менеджер свяжется с Вами в ближайшее время!\nДля продолжения работы с ботом воспользуйтесь кнопкой "Меню".')
          chat_states[message.chat.id] = None

      if state == 'cost_railway_transportation_service':
        questions_asked = chat_states[message.chat.id]['questions_asked']
        if questions_asked == 0:
          user_id = message.from_user.id
          user_answers[user_id] = {}
          now = datetime.now()
          random_number = random.randint(0, 99)
          user_answers[user_id]['heading'] = f"Заявка_ЖД_перевозка_{now.strftime('%Y-%m-%d')}_{random_number}"
          user_answers[user_id]['from_to'] = message.text
          bot.send_message(message.chat.id, 'Укажите вес, габариты и объем груза')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 1:
          user_id = message.from_user.id
          user_answers[user_id]['wsv'] = message.text
          bot.send_message(message.chat.id, 'Укажите название компании или Ваше имя, а также Ваш телефон и email')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 2:
          user_id = message.from_user.id
          user_answers[user_id]['contacts'] = message.text
          bot.send_message(message.chat.id, 'Хотите что-то добавить к заявке?')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 3:
          user_id = message.from_user.id
          user_answers[user_id]['comments'] = message.text
          bot.send_message(ID_manager, f"{user_answers[user_id]['heading']}\n" f"Адрес отправки и доставки: {user_answers[user_id]['from_to']}\n" f"Параметры груза: {user_answers[user_id]['wsv']}\n" f"Контакты клиента: {user_answers[user_id]['contacts']}\n" f"Комментарии к заказу: {user_answers[user_id]['comments']}\n" f"Ник клиента в Telegram - https://t.me/{message.from_user.username}\n")
          del user_answers[user_id]
          bot.send_message(message.chat.id, 'Спасибо за обращение в нашу компанию! Менеджер свяжется с Вами в ближайшее время!\nДля продолжения работы с ботом воспользуйтесь кнопкой "Меню".')
          chat_states[message.chat.id] = None

      if state == 'cost_cargo_insurance':
        questions_asked = chat_states[message.chat.id]['questions_asked']
        if questions_asked == 0:
          user_id = message.from_user.id
          user_answers[user_id] = {}
          now = datetime.now()
          random_number = random.randint(0, 99)
          user_answers[user_id]['heading'] = f"Заявка_страхование_{now.strftime('%Y-%m-%d')}_{random_number}"
          user_answers[user_id]['contacts'] = message.text
          bot.send_message(message.chat.id, 'Укажите Ваши комментарии')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 1:
          user_id = message.from_user.id
          user_answers[user_id]['comments'] = message.text
          bot.send_message(ID_manager, f"{user_answers[user_id]['heading']}\n" f"Контакты клиента: {user_answers[user_id]['contacts']}\n" f"Комментарии к заказу: {user_answers[user_id]['comments']}\n" f"Ник клиента в Telegram - https://t.me/{message.from_user.username}\n")
          del user_answers[user_id]
          bot.send_message(message.chat.id, 'Спасибо за обращение в нашу компанию! Менеджер свяжется с Вами в ближайшее время!\nДля продолжения работы с ботом воспользуйтесь кнопкой "Меню".')
          chat_states[message.chat.id] = None

      if state == 'cost_customs_clearance':
        questions_asked = chat_states[message.chat.id]['questions_asked']
        if questions_asked == 0:
          user_id = message.from_user.id
          user_answers[user_id] = {}
          now = datetime.now()
          random_number = random.randint(0, 99)
          user_answers[user_id]['heading'] = f"Заявка_таможенное_оформление_{now.strftime('%Y-%m-%d')}_{random_number}"
          user_answers[user_id]['contacts'] = message.text
          bot.send_message(message.chat.id, 'Укажите Ваши комментарии')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 1:
          user_id = message.from_user.id
          user_answers[user_id]['comments'] = message.text
          bot.send_message(ID_manager, f"{user_answers[user_id]['heading']}\n" f"Контакты клиента: {user_answers[user_id]['contacts']}\n" f"Комментарии к заказу: {user_answers[user_id]['comments']}\n" f"Ник клиента в Telegram - https://t.me/{message.from_user.username}\n")
          del user_answers[user_id]
          bot.send_message(message.chat.id, 'Спасибо за обращение в нашу компанию! Менеджер свяжется с Вами в ближайшее время!\nДля продолжения работы с ботом воспользуйтесь кнопкой "Меню".')
          chat_states[message.chat.id] = None

      if state == 'cost_cargo_removal_from_customs':
        questions_asked = chat_states[message.chat.id]['questions_asked']
        if questions_asked == 0:
          user_id = message.from_user.id
          user_answers[user_id] = {}
          now = datetime.now()
          random_number = random.randint(0, 99)
          user_answers[user_id]['heading'] = f"Заявка_вывоз_с_таможни_{now.strftime('%Y-%m-%d')}_{random_number}"
          user_answers[user_id]['contacts'] = message.text
          bot.send_message(message.chat.id, 'Укажите Ваши комментарии')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 1:
          user_id = message.from_user.id
          user_answers[user_id]['comments'] = message.text
          bot.send_message(ID_manager, f"{user_answers[user_id]['heading']}\n" f"Контакты клиента: {user_answers[user_id]['contacts']}\n" f"Комментарии к заказу: {user_answers[user_id]['comments']}\n" f"Ник клиента в Telegram - https://t.me/{message.from_user.username}\n")
          del user_answers[user_id]
          bot.send_message(message.chat.id, 'Спасибо за обращение в нашу компанию! Менеджер свяжется с Вами в ближайшее время!\nДля продолжения работы с ботом воспользуйтесь кнопкой "Меню".')
          chat_states[message.chat.id] = None

      if state == 'cost_payment_of_fees_SVH':
        questions_asked = chat_states[message.chat.id]['questions_asked']
        if questions_asked == 0:
          user_id = message.from_user.id
          user_answers[user_id] = {}
          now = datetime.now()
          random_number = random.randint(0, 99)
          user_answers[user_id]['heading'] = f"Заявка_оплата_сборов_СВХ_{now.strftime('%Y-%m-%d')}_{random_number}"
          user_answers[user_id]['contacts'] = message.text
          bot.send_message(message.chat.id, 'Укажите Ваши комментарии')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 1:
          user_id = message.from_user.id
          user_answers[user_id]['comments'] = message.text
          bot.send_message(ID_manager, f"{user_answers[user_id]['heading']}\n" f"Контакты клиента: {user_answers[user_id]['contacts']}\n" f"Комментарии к заказу: {user_answers[user_id]['comments']}\n" f"Ник клиента в Telegram - https://t.me/{message.from_user.username}\n")
          del user_answers[user_id]
          bot.send_message(message.chat.id, 'Спасибо за обращение в нашу компанию! Менеджер свяжется с Вами в ближайшее время!\nДля продолжения работы с ботом воспользуйтесь кнопкой "Меню".')
          chat_states[message.chat.id] = None

      if state == 'cost_organization_of_loading':
        questions_asked = chat_states[message.chat.id]['questions_asked']
        if questions_asked == 0:
          user_id = message.from_user.id
          user_answers[user_id] = {}
          now = datetime.now()
          random_number = random.randint(0, 99)
          user_answers[user_id]['heading'] = f"Заявка_услуги_погрузки/разгрузки_{now.strftime('%Y-%m-%d')}_{random_number}"
          user_answers[user_id]['contacts'] = message.text
          bot.send_message(message.chat.id, 'Укажите Ваши комментарии')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 1:
          user_id = message.from_user.id
          user_answers[user_id]['comments'] = message.text
          bot.send_message(ID_manager, f"{user_answers[user_id]['heading']}\n" f"Контакты клиента: {user_answers[user_id]['contacts']}\n" f"Комментарии к заказу: {user_answers[user_id]['comments']}\n" f"Ник клиента в Telegram - https://t.me/{message.from_user.username}\n")
          del user_answers[user_id]
          bot.send_message(message.chat.id, 'Спасибо за обращение в нашу компанию! Менеджер свяжется с Вами в ближайшее время!\nДля продолжения работы с ботом воспользуйтесь кнопкой "Меню".')
          chat_states[message.chat.id] = None

      if state == 'cost_dangerous_cargo':
        questions_asked = chat_states[message.chat.id]['questions_asked']
        if questions_asked == 0:
          user_id = message.from_user.id
          user_answers[user_id] = {}
          now = datetime.now()
          random_number = random.randint(0, 99)
          user_answers[user_id]['heading'] = f"Заявка_перевозка_опасного_груза_{now.strftime('%Y-%m-%d')}_{random_number}"
          user_answers[user_id]['contacts'] = message.text
          bot.send_message(message.chat.id, 'Укажите Ваши комментарии')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 1:
          user_id = message.from_user.id
          user_answers[user_id]['comments'] = message.text
          bot.send_message(ID_manager, f"{user_answers[user_id]['heading']}\n" f"Контакты клиента: {user_answers[user_id]['contacts']}\n" f"Комментарии к заказу: {user_answers[user_id]['comments']}\n" f"Ник клиента в Telegram - https://t.me/{message.from_user.username}\n")
          del user_answers[user_id]
          bot.send_message(message.chat.id, 'Спасибо за обращение в нашу компанию! Менеджер свяжется с Вами в ближайшее время!\nДля продолжения работы с ботом воспользуйтесь кнопкой "Меню".')
          chat_states[message.chat.id] = None

      if state == 'cost_supplier_communication':
        questions_asked = chat_states[message.chat.id]['questions_asked']
        if questions_asked == 0:
          user_id = message.from_user.id
          user_answers[user_id] = {}
          now = datetime.now()
          random_number = random.randint(0, 99)
          user_answers[user_id]['heading'] = f"Заявка_обсуждение_отгрузки_с_поставщиком_{now.strftime('%Y-%m-%d')}_{random_number}"
          user_answers[user_id]['contacts'] = message.text
          bot.send_message(message.chat.id, 'Укажите Ваши комментарии')
          chat_states[message.chat.id]['questions_asked'] += 1

        if questions_asked == 1:
          user_id = message.from_user.id
          user_answers[user_id]['comments'] = message.text
          bot.send_message(ID_manager, f"{user_answers[user_id]['heading']}\n" f"Контакты клиента: {user_answers[user_id]['contacts']}\n" f"Комментарии к заказу: {user_answers[user_id]['comments']}\n" f"Ник клиента в Telegram - https://t.me/{message.from_user.username}\n")
          del user_answers[user_id]
          bot.send_message(message.chat.id, 'Спасибо за обращение в нашу компанию! Менеджер свяжется с Вами в ближайшее время!\nДля продолжения работы с ботом воспользуйтесь кнопкой "Меню".')
          chat_states[message.chat.id] = None

    else:
      bot.send_message(message.chat.id, 'Для работы с ботом воспользуйтесь кнопкой "Меню", пожалуйста.')

  else:
    bot.send_message(message.chat.id, 'Для работы с ботом воспользуйтесь кнопкой "Меню", пожалуйста.')

if __name__ == "__main__":
    bot.polling(none_stop=True)