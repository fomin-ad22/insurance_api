# insurance_api
REST API project on FAST API  with insurance (cargo_type-rate) related methods (SQLModel DB connection).

Cервис предоставляет методы для расчета стоимости страхования в зависимости от груза и обьявленной цены. Также реализована возможность подключения к БД и хранения данных в ней (в текущем проекте SQLlite).

Основные классы БД:

• test_insurance=Insurance(date:"2020-12-20",cargo_type:"plastic",rate:0.04)

Основные JSON - структуры :

• test_tariff= {
    "2020-08-03":[
        {"cargo_type":"metall",
        "rate":"0.04"
        },
        {"cargo_type":"arhentum",
        "rate":"0.08"
        }
    ]}

• test_insurance_request={
    "cargo_type":"metall",
    "declared_value":123
}

Основные функции:

Тарифы:

• Добавление Тарифа: Добавляйте новые тарифы upload_tariff(test_tariffs) - Добавляет новый тариф в БД
• Расчет стоимости страхования: Рассчитывайте актуальную стоимость страхования calculate_insurance(test_insurance_request) - Возвращает актуальную стоимость страхования в зависимости от указанного cargo_type и его актуального значения rate

Как использовать сервис:

Для работы с сервисом вам необходимо из рабочей директории запустить API через терминал командой "uvicorn main:app".
Взаимодействие с сервисом осуществляется через отправку post и get запросов, с приложенными test_insurance_request и test_tariff в формате json (при отсутствии, БД автоматически создается во время 1 запуска)

Примеры:

• requests.post("http://127.0.0.1:8000/tariff/",json=test_tariff) - для загрузки данных о тарифах.

• requests.get("http://127.0.0.1:8000/insurance/",json=test_insurance_request) - для получения актуальных данных о стоимости страхования.

Как развернуть?

• Для импорта проекта через git, откройте git-bash и запустите "git clone https://github.com/fomin-ad22/insurance_api.git", либо перейдите по ссылке https://github.com/fomin-ad22/insurance_api.git и скопируйте файлы репозитория.
 
• Для компиляции проекта в docker image, в корне каталога содержится Dockerfile, из директории с файлом "docker build -t myimage . ". Для запуска контейнера "docker run --name myimagecont -d -p 8000:8000 myimage".

С вопросами и предложениями @fomin_ad22 tg
