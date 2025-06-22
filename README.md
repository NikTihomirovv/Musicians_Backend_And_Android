API:
    INDEX:
        Получить список пользователей
        GET: http://127.0.0.1:8000/ AllowAny

        Пример запроса:
            -

        Пример ответа:
            {
                "count": 3,
                "next": null,
                "previous": null,
                "results": [
                    {
                        "avatar": binary,
                        "first_name": str,
                        "last_name": str,
                        "instrument_1": str,
                        "instrument_2": str,
                        "instrument_3": str,
                        "purpose": str,
                        "city": str
                    },
                    {
                        "avatar": binary,
                        "first_name": str,
                        "last_name": str,
                        "instrument_1": str,
                        "instrument_2": str,
                        "instrument_3": str,
                        "purpose": str,
                        "city": str
                    },
                    {
                        "avatar": binary,
                        "first_name": str,
                        "last_name": str,
                        "instrument_1": str,
                        "instrument_2": str,
                        "instrument_3": str,
                        "purpose": str,
                        "city": str
                    }
                ]
            }

        Получить отфильтрованный список пользователей
        GET: http://127.0.0.1:8000/ AllowAny

        Пример запроса:
            {
                "city": "Лондон",
                "purpose": "Создание профессиональных связей",
                "instrument": "Гитара"
            }

        Пример ответа:
            {
                "count": 1,
                "next": null,
                "previous": null,
                "results": [
                    {
                        "avatar": binary,
                        "first_name": str,
                        "last_name": str,
                        "instrument_1": str,
                        "instrument_2": str,
                        "instrument_3": str,
                        "purpose": str,
                        "city": str
                    }
                ]
            }