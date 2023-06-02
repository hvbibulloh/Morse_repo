from aiogram.dispatcher.filters.state import StatesGroup, State


class ShifrState(StatesGroup):
    comment = State()


class Shifrochish(StatesGroup):
    comment = State()


class Admin(StatesGroup):
    comment = State()
