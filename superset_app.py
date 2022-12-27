import streamlit as st
from streamlit_option_menu import option_menu
import os


#-------------
IMG_PATH = "imgs/"

# demography_table = pd.read_excel('Демография 2015-2018 рус.xlsx')  

with st.sidebar:
    chosen_menu = option_menu(
        menu_title = None, # "Разделы:",
        options = ["1. Задача и актуальность", "2. Об Apache Superset", "3. Вход и регистрация в Superset", "4. Создание графиков", "5. Оформление дашборда", "6. Самостоятельная работа"],
        menu_icon = ["list"],
        icons = ["lightning-charge", "infinity", "box-arrow-in-right", "graph-up", "grid-1x2", "person-workspace"],  # берём название из https://icons.getbootstrap.com/   
        default_index = 0,
        styles = {
        "container": {"padding": "0!important", "background-color": "#f0f2f6", "text-align": "center"}, 
        "icon": {"color": "#323440", "font-size": "25px", "text-align": "center"},  # , "margin":"80px"
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        # "nav-link-selected": {"background-color": "green", "font-size": "15px"},
                },
        orientation='vertical'
    )

if chosen_menu =="1. Задача и актуальность":
    ##---------------------Header---------------------
    st.markdown('''<h1 style='text-align: center'>
                <span style='color: #484848;'>Построение интерактивного дашборда с помощью</span>
                <span style='color: #1FA7C9;'>Apache Superset</span>
                </h1>
                ''', unsafe_allow_html=True)        
    st.write("""
    Лабораторная работа **"Построение интерактивного дашборда с помощью Apache Superset"** поможет изучить основы создания и анализа связанных интерактивных графиков 
    на примере данных о демографической ситуации в России за 2015-2018 года.""")
    st.markdown('''<h2 style='text-align: center; color: black;'
            >Актуальность тематики</h2>''', 
            unsafe_allow_html=True)
    st.write(''' \n##### **Кому будет полезна эта лабораторная работа и почему?**
    \n* **Студентам направления аналитики и консалтинга:**
    \nтак как дашборды - это широко распространённый инструмент графического анализа данных и умение с ними работать входит в обязательный стек компетенций данного направления.
    \n* **Студентам факультетов менеджмента и управления:**
    \nинтерактивная визуальная аналитика позволяет быстрее понять структуру объекта управления и принимать более эффективные решения.
    \n* **Студентам-дизайнерам:**
    \nвы посмотрите примеры динамичной визуализации больших данных для клиента.
    \n* **Студентам профиля "социология" и "история":**
    \nпотому что данная работа выполнена на официальных статистических данных субъектов Российской Федерации.
    \n* **Студентам других специальностей:**
    \nдля общего понимания современных технологий в области пересечения анализа данных и их понятной интерпретации для любого пользователя.
    ''')
    st.write('''\n##### **А если у меня другой профиль?**
    \nВо-первых, всегда полезно знать о современных технологиях, которые применяются во множестве профессиональных областей. Во-вторых, в ходе выполнения работы вы ознакомитесь с примером решения широко распространенной бизнес-задачи.
    А для того, чтобы разработать и внедрить в деятельность организации такое решение, требуется вовлечение в команду специалистов разного уровня и разных ролей: как IT-специальностей, так и других профилей.
    ''')
    with st.expander('Роли в проекте для специалистов различных сфер:'):
        st.write('''
        \n 1. Проанализировать текущее состояние бизнес-процессов, оценить риски и участвовать в промежуточных результатах могли бы:
        \n\t * Аналитик-международник (международный аналитик)
        \n\t * Политолог, политический аналитик
        \n\t * Политтехнолог
        \n\t * Менеджер по связям с общественностью (PR)
        \n\t * Финансовый менеджер
        \n\t * GR-менеджер
        \n\t * Руководитель по цифровой трансформации (CDO – Chief Digital Officer)
        \n\t * Development manager (менеджер по развитию)
        \n\t * Digital-стратег

        \n 2. Управлять проектом, организовывать и развивать его могут:
        \n\t * Директор по данным, Chief Data Officer (CDO)
        \n\t * Менеджер проекта
        ''')

    with st.expander('Роли в проекте для IT-специалистов:'):
        st.write('''
        \n 1. Собрать, подготовить и обработать данные для проекта могли бы:
        \n\t * Аналитик данных (Data Analyst)
        \n\t * Data Mining Specialist: специалист по интеллектуальной обработке данных
        \n\t * Data Scientist: учёный по данным, исследователь данных
        \n\t * Big Data Analyst: специалист по анализу больших данных

        \n 2. Разработать серверную инфраструктуру, размещение данных и всей схемы решения, обеспечить безопасность на техническом уровне, обеспечить доступ пользователей к проекту могли бы:
        \n\t * DevOps (на данный момент нет в учебном процессе РАНХиГС)
        \n\t * MLOps (на данный момент нет в учебном процессе РАНХиГС)

        ''')

    st.markdown('''<h2 style='text-align: center; color: black;'
                >Цель и задачи:</h2>''', 
                unsafe_allow_html=True)
    st.write("""     
    \n**Цель данной лабораторной работы** - ознакомить пользователя с возможностями Apache Superset, научить оформлять и работать с интерактивными дашбордами.  
    \n**Задачи:**
    \n**1)** ознакомиться с платформой Apache Superset, как инструментом визуализации данных;
    \n**2)** самостоятельно построить дашборд по датасету демографической ситуации в Российской Федерации за 2015-2018 года; 
    \n**3)** произвести анализ графиков и сделать по ним выводы.

    \n*Разработано сотрудниками ЛИА РАНХиГС.*
    """)
    #-------------------------Pipeline description-------------------------
    st.markdown('''<h2 style='text-align: center; color: black;'
                >Пайплайн лабораторной работы:</h2>''', unsafe_allow_html=True)
    st.image(os.path.join(IMG_PATH, 'superset_pipeline.png'), use_column_width='auto')

    pipeline_bar = st.expander("Этапы работы:")    
    pipeline_bar.markdown(
        """
        \n *(зелёным обозначены этапы, работа с которыми доступна студенту, красным - этапы, доступные для корректировки сотрудникам ЛИА)*
        \n**1. Блок теории:**
        \nинформация о дашбордах, их видах и применении для бизнес-задач. 
        \n**2. Регистрация на платформе:**
        \nвход и регистрация на Apache Superset.
        \n**3. Создание графиков:**
        \nсамостоятельно построить несколько наиболее распространённых графиков на демографических данных субъектов Российской Федерации...
        \n**4. Оформление дашборда:**
        \n...и собрать их графики в единый дашборд, добавив фильтры.
        \n**5. Самостоятельная работа:**
        \nпроанализировать получившийся дашборд, выполнить задания и ответить на вопросы.
        \n*Используемые технологии:*
        \n * библиотека [Pandas](https://pandas.pydata.org/docs/user_guide/index.html)
        \n * библиотека [Streamlit](https://docs.streamlit.io/library/get-started)
        \n * платформа интерактивных дашбордов [Apache Superset](https://superset.apache.org/)
        """)

elif chosen_menu == "2. Об Apache Superset": 
    st.markdown('''<h2 style='text-align: center; color: #000000;'>
                О дашбордах и их использовании
                </h2>''', unsafe_allow_html=True)

    st.markdown(
        """
        \n ##### **_Что такое дашборд?_**
        \n**Дашборд** — это современный формат сбора и визуального представления массивов данных. Это аналитическая панель с понятным интерфейсом для интерактивного взаимодействия с огромным количеством постоянно 
        изменяющихся показателей. С помощью этих метрик можно выявить и проанализировать тренды и изменения. Алгоритмы и средства аналитики обрабатывают данные, сравнивают цифры и выдают пользователю индивидуально настроенные графики. 
        
        \nМы сталкиваемся с дашбордами каждый день. Приборная панель в автомобиле, графики активности в приложении фитнес-браслета, [«Яндекс.Метрика»](https://metrika.yandex.ru/list?) — 
        всё это дашборды.

        \n ##### **_Цели построения дашбордов:_**

        \n1.Сделать визуализацию результатов анализа данных простой и наглядной.
        \n2.Получать оперативные сводки и наблюдать динамику бизнес-процессов.
        \n3.Выстраивать иерархию данных и быстро проводить сравнение. 
        \n4.Выделить ключевые для компании показатели и всегда держать их под контролем. 


        \n ##### **_Типы дашбордов:_**
        \nСуществуют три основных вида дашбордов, но они могут сочетаться друг с другом:
        \n1. **Операционный** — отображает изменения данных в бизнесе. Примеры дашбордов для бизнеса — графики Яндекс Метрики, с помощью которых можно посмотреть, как менялась посещаемость сайта и что на неё влияло. 
        Ведь за какой период смотреть график, пользователь выбирает сам.
        \n2. **Аналитический** — помогает исследовать тенденции и делать выводы. Обычно их создают для конкретного бизнес-подразделения. Аналитики работают с ними, чтобы зафиксировать отклонения показателей и отследить 
        причины. Пример — разработка дашборда об изменении числа пользователей конкретного продукта за неделю. С его помощью можно увидеть средний чек, долю клиентов и процент товарооборота по каждому из конкурентов.
        \n3. **Стратегический** — нужен, чтобы составить представление о ситуации в целом или об отдельных показателях, выявляет проблемы и помогает их исправлять. Например, создание дашборда о лояльности персонала поможет 
        понять степень лояльности сотрудников и отследить её изменения среди разных групп.
        \nИсточники: [1](https://practicum.yandex.ru/blog/chto-takoe-dashbord/), [2](https://www.calltouch.ru/blog/dashbord-chto-eto-takoe-dlya-chego-nuzhen-dashboard-i-kak-ego-ispolzovat/), [3](https://kokoc.com/blog/dashboard/).
        """)    

    st.markdown('''<h2 style='text-align: center; color: #000000;'>
            Что такое<img src="https://miro.medium.com/max/1200/0*UiDRbGh8K4M5Rs7R.png" width="220">?     
            ''', unsafe_allow_html=True)
    col1, col2 = st.columns([1,1])
    col1.write("""
        **Superset** — это открытое программное обеспечение для исследования и визуализации данных.
        \n**Superset позволяет:**
        \n * исследовать данные, используя графическую визуализацию;
        \n * аккумулировать информацию из данных с помощью интерактивных информационных панелей (дашбордов);
        \n * подключать базы данных для работы с "большими данными".

        \n __Плюсы Superset:__
        \n * быстрота обработки данных;
        \n * легкость создания дашбордов;
        \n * интерактивность;
        \n * интуитивно понятный набор функций и возможностей;
        \n * множество опций визуализации данных.
        
        """)
    col2.image(os.path.join(IMG_PATH, 'visualization_types_in_apache_superset.png'), caption = 'Виды графиков в Superset', use_column_width='auto')

elif chosen_menu == "3. Вход и регистрация в Superset":        
    st.markdown('''<h2 style='text-align: center; color: #000000;'>
                Регистрация на платформе
                </h2>''', unsafe_allow_html=True)
    st.write('''
        1. Перейдите по [ссылке](http://ccrii1.ranepa.ru:27364/login/).
        2. Введите логин и пароль в соответствующие поля, как указано на рисунке нижее:
        ''')
    st.image(os.path.join(IMG_PATH, 'superset_login.png'))
    st.write('''
        3. Нажмите **"SIGN IN"**.''')

elif chosen_menu == "4. Создание графиков": 
    st.markdown('''<h2 style='text-align: center; color: #000000;'>
                Перейдём к созданию графиков
                </h2>''', unsafe_allow_html=True)

    st.markdown('''<h3 style='text-align: left; color: #000000;'>
                1. Просмотр табличных данных:
                </h3>''', unsafe_allow_html=True)
    st.image(os.path.join(IMG_PATH, 'table_chart_1.png'), caption = 'Вывод табличных данных в Superset', use_column_width='auto')
    with st.expander('Как вывести таблицу с данным в Superset?'):
        st.write('''
        1. Зайдите во вкладку **"Charts"**, выберите **"+ CHART"**, как показано на рисунке ниже:
        ''')
        st.image(os.path.join(IMG_PATH, 'new_chart.png'))
        st.write('''
        2. Выберите нужный **датасет** ("Демография РФ по годам (2015-2018)"), нужный **вид графика** и нажмите **"CREATE NEW CHART"**:
        ''')
        st.image(os.path.join(IMG_PATH, 'table_chart_2.png'))
        st.write('''
        3. Правильно заполните все **поля**, включите **все колонки таблицы** в поле **"COLUMNS"**, как показано на рисунке ниже, и **сохраните** график в ваш дашборд:
        ''')
        st.image(os.path.join(IMG_PATH, 'table_chart_3.png'))


    st.markdown('''<h3 style='text-align: left; color: #000000;'>
                2. График "Big Number":
                </h3>''', unsafe_allow_html=True)
    st.image(os.path.join(IMG_PATH, 'big_number_1.png'), caption = 'Вид графика "Big Number"', use_column_width='auto')
    with st.expander('Как сформировать "Big Number" в Superset?'):
        st.write('''
        1. Зайдите во вкладку **"Charts"**, выберите **"+ CHART"**, как показано на рисунке ниже:
        ''')
        st.image(os.path.join(IMG_PATH, 'new_chart.png'))
        st.write('''
        2. Выберите нужный **датасет** ("Демография РФ по годам (2015-2018)"), нужный **вид графика** и нажмите **"CREATE NEW CHART"**:
        ''')
        st.image(os.path.join(IMG_PATH, 'big_number_2.png'))
        st.write('''
        3. Правильно заполните все **поля**, как показано на рисунке ниже, и **сохраните** график в ваш дашборд:
        ''')
        st.image(os.path.join(IMG_PATH, 'big_number_3.png'))

    st.markdown('''<h3 style='text-align: left; color: #000000;'>
                3. График "Pie Chart":
                </h3>''', unsafe_allow_html=True)
    st.image(os.path.join(IMG_PATH, 'pie_chart_1.png'), caption = 'Вид графика "Pie Chart"', use_column_width='auto')
    with st.expander('Как сформировать "Pie Chart" в Superset?'):
        st.write('''
        1. Зайдите во вкладку **"Charts"**, выберите **"+ CHART"**, как показано на рисунке ниже:
        ''')
        st.image(os.path.join(IMG_PATH, 'new_chart.png'))
        st.write('''
        2. Выберите нужный **датасет** ("Демография РФ по годам (2015-2018)"), нужный **вид графика** и нажмите **"CREATE NEW CHART"**:
        ''')
        st.image(os.path.join(IMG_PATH, 'pie_chart_2.png'))

        st.write('''
        3. Правильно заполните все **поля**, как показано на рисунке ниже, и **сохраните** график в ваш дашборд:
        ''')
        st.image(os.path.join(IMG_PATH, 'pie_chart_3.png'))
        st.write('''_Обратите внимание:_
        \nЕсли выбрать значения фильтров, как указано ниже, мы сможем оставить на графике только нужные регионы:''')
        col1,col2 = st.columns([1,1])
        # col1
        col1.image(os.path.join(IMG_PATH, 'pie_chart_filters_1.png'), caption = 'Не включаем в Pie Chart общие данные по Российской Федерации', use_column_width='auto')
        col2.image(os.path.join(IMG_PATH, 'pie_chart_filters_2.png'), caption = 'Включаем в Pie Chart только данные по округам Российской Федерации', use_column_width='auto')
        st.write('Попробуйте сделать график со следующими фильтрами через "CUSTOM SQL" запрос:')
        col1,col2 = st.columns([1,1])
        col1.write('а). Включаем в данные только области Российской Федерации')
        col1.write('б). Включаем в данные только города федерального значения')
        col2.code("\nТерритория LIKE '%область%'")
        col2.code("\nТерритория LIKE '%город %'")

    st.markdown('''<h3 style='text-align: left; color: #000000;'>
                4. График "Bar Chart":
                </h3>''', unsafe_allow_html=True)
    st.image(os.path.join(IMG_PATH, 'bar_chart_1.png'), caption = 'Вид графика "Bar Chart"', use_column_width='auto')
    with st.expander('Как построить "Bar Chart" в Superset?'):
        st.write('''
        1. Зайдите во вкладку **"Charts"**, выберите **"+ CHART"**, как показано на рисунке ниже:
        ''')
        st.image(os.path.join(IMG_PATH, 'new_chart.png'))
        st.write('''
        2. Выберите нужный **датасет** ("Демография РФ по годам (2015-2018)"), нужный **вид графика** и нажмите **"CREATE NEW CHART"**:
        ''')
        st.image(os.path.join(IMG_PATH, 'bar_chart_2.png'))
        st.write('''
        3. Правильно заполните все **поля**, как показано на рисунке ниже, и **сохраните** график в ваш дашборд:
        ''')
        st.image(os.path.join(IMG_PATH, 'bar_chart_3.png'))
    
    st.markdown('''<h3 style='text-align: left; color: #000000;'>
                5. График "Time-series Line Chart":
                </h3>''', unsafe_allow_html=True)
    st.image(os.path.join(IMG_PATH, 'time_series_linechart_1.png'), caption = 'Вид графика "Time-series Line Chart"', use_column_width='auto')
    with st.expander('Как сформировать "Time-series Line Chart" в Superset?'):
        st.write('''
        1. Зайдите во вкладку **"Charts"**, выберите **"+ CHART"**, как показано на рисунке ниже:
        ''')
        st.image(os.path.join(IMG_PATH, 'new_chart.png'))
        st.write('''
        2. Выберите нужный **датасет** ("Демография РФ по годам (2015-2018)"), нужный **вид графика** и нажмите **"CREATE NEW CHART"**:
        ''')
        st.image(os.path.join(IMG_PATH, 'time_series_linechart_2.png'))
        st.write('''
        3. Правильно заполните все **поля**, как показано на рисунке ниже, и **сохраните** график в ваш дашборд:
        ''')
        st.image(os.path.join(IMG_PATH, 'time_series_linechart_3.png'))
        st.write('*Попробуйте построить и другие графики:*')
        col1,col2 = st.columns([1,1])
        col1.write('')
        col1.write('а). График миграционного прироста/убыли по городам федерального значения')
        col1.write('')
        col1.write('б). График младенческой смертности (на 1000 живых родившихся детей) по федеральным округам')
        col2.code("AVG(Миграц прирост/убыль)\nТерритория LIKE '%город %'")
        col2.code("AVG(Млад смертн/1000 родившихся жив)\nТерритория LIKE '%округ%'")
        

    

elif chosen_menu == "5. Оформление дашборда": 
    st.markdown('''<h2 style='text-align: center; color: #000000;'>
                Оформение дашборда
                </h2>''', unsafe_allow_html=True)
    st.write('''
        1. Зайдите во вкладку **"Dashboards"**, выберите **"+ DASHBOARD"**, как показано на рисунке ниже:
        ''')
    st.image(os.path.join(IMG_PATH, 'new_dashboard_1.png'), use_column_width='auto')
    st.write('''
        2. С помощью фильтров найдите созданные вами графики (по названию графика, используемому датасету, дате или типу графика) и перетащите их на поле дашборда. Укажите название дашборда и нажмите **"SAVE"**:
        ''')
    st.image(os.path.join(IMG_PATH, 'new_dashboard_2.png'), use_column_width='auto')
    st.write('''
        3. Теперь ваш дашборд появился в списке всех дашбордов. Его можно открывать и редактировать, изменяя положение, размер, количество графиков, добавляя надписи и рисунки:
        ''')
    st.image(os.path.join(IMG_PATH, 'new_dashboard_3.png'), use_column_width='auto')
    st.write('''
        4. Чтобы использовать возможности интерактивного изменения графиков в дашборде, добавьте фильтры и укажите, на какие графики они будут влиять. После этого сохраните изменения:
        ''')
    col1, col2 = st.columns([1,1])
    col1.image(os.path.join(IMG_PATH, 'add_filters_1.png'), caption = 'Добавление нового фильтра', use_column_width='auto')
    col2.image(os.path.join(IMG_PATH, 'add_filters_2.png'), caption = 'Фильтр может влиять на все графики дашборда или только определённые', use_column_width='auto')


    

elif chosen_menu == "6. Самостоятельная работа": 
    st.markdown('''<h2 style='text-align: center; color: #000000;'>
                Самостоятельная работа
                </h2>''', unsafe_allow_html=True)
    st.write("""
    В этом стримлите вам нужно, воспользовавшись платфформой Superset, провести исследование данных, собранных с сайта Avito.
    
    """)
    st.markdown('''<h3 style='text-align: left; color: #000000;'>
                Информация о датасете:
                </h3>''', unsafe_allow_html=True)
    st.markdown('''<h3 style='text-align: left; color: #000000;'>
                Подготовка к выполнению задания
                </h3>''', unsafe_allow_html=True)
    st.write("""
    Для того, чтобы выполнить задание, перейдите по [ссылке](http://ccrii1.ranepa.ru:27364/superset/dashboard/avito-cats-dashboard/).
    \nВам откроется уже подготовленный дашборд, со всеми необходимыми типами визуализации. В левом углу расположенна вкладка с фильтрами, взаимодейстуя с которой 
    вы можете выбирать необходимые числовые или категориальные параметры, основываясь на задании.
    """)
    st.image(os.path.join(IMG_PATH, 'filters.png'), caption = 'Расположение фильтров в дашборде', use_column_width='auto')
    st.write("*Для некоторых заданий вам также потребуется переходить непосредственно в график для создания SQL-запроса*")
    st.write("""
    Прежде, чем перейти к выполнению задания, давайте сделаем краткий экскурс в SQL запросы. Допустим, нам нужно расчитать, среднее значение цены всех автомобилей
    марки LADA. Наиболее удобным для подобной визуализации будет график 'Big number'. Давайте выберем любой график и перейдём к нему.
    """)
    st.image(os.path.join(IMG_PATH, 'big_number_avito.png'), caption = '', use_column_width='auto')
    st.write("""
    Нажимаем на наименование графика и попадаем в его собственные параметры. Здесь нам нужно в левом углу экрана нажать на три вертикальные точки, и выбрать вариант
    "Открыть в лаборатории SQL"
    """)
    st.image(os.path.join(IMG_PATH, 'sql_avito.png'), caption = '', use_column_width='auto')
    st.write("""
    В открывшемся окне нас интересует дополнение SQL-запроса для нашей базы данных. Поскольку нам интересны модели марки Lada, то нам необходимо добавить строку
    `WHERE Название LIKE '%LADA%'`, символы '`%`' означают, что SQL выдаст все значения, которые как начинаются, так и заканчиваются на указанный набор символов.
    Нажимаем на "Выполнить всё".
    \nТеперь давайте создадим визуализацию получившейся выборки. Для этого нажмем клавишу 'Create chart'
    """)
    st.image(os.path.join(IMG_PATH, 'sql_where_avito.png'), caption = '', use_column_width='auto')
    st.write("""
    Теперь мы создали график типа "Таблица" из отфильтрованных нами данных. Чтобы построить график "Big number". Просто изменим типа графика с таблицы на 'Big number.
    """)
    st.image(os.path.join(IMG_PATH, 'avito_table.png'), caption = '', use_column_width='auto')
    st.write("""
    Помимо визуализации, мы также можем узнать некоторую необходимую нам информацию, пользуясь исключительно SQL-запросами. Для более полного ознакомления с возможностями
    SQL вы можете воспользоваться другим стримлитом лаборатории РАНХиГС. [ссылка]()
    """)
    st.markdown('''<h3 style='text-align: left; color: #000000;'>
                Выполните следующие задания:
                </h3>''', unsafe_allow_html=True)
    with st.form('Ответьте на все вопросы, чтобы успешно завершить лабораторную работу'):

        st.markdown('**Вопрос 1:** Какой объем двигателя будет самым распространенным для машин с типом коробки "Вариатор" и типом привода "Полный"?')
        question_1_right_1 = st.checkbox("2.0 л")
        question_1_wrong_2 = st.checkbox("2.5 л")
        question_1_wrong_3 = st.checkbox("1.6 л")
        question_1_wrong_4 = st.checkbox("1.3 л")

        st.markdown('**Вопрос 2:** ')

        st.markdown('**Вопрос 3:** Давайте попробуем посмотреть, какова средняя цена всех машин марки `Mercedes` по всей России?')
        question_3_wrong_1 = st.checkbox("200K")
        question_3_right_2 = st.checkbox("2.8M")
        question_3_wrong_3 = st.checkbox("16M")
        question_3_wrong_4 = st.checkbox("500k") 

        if st.form_submit_button('Закончить тест и посмотреть результаты'):
        # if (question_1_right_2 and question_2_right_2 and question_4_right_2 and question_5_right_3)==True and answers == False:
            # st.markdown('''<h3 style='text-align: left; color: green;'
            # >Тест сдан! Теперь преступайте к выполнению второй части лабортаной работы.</h3>''', 
            # unsafe_allow_html=True) 
        # else:
            # st.markdown('''<h3 style='text-align: left; color: red;'
            # >Тест не сдан! Где-то была допущена ошибка.</h3>''', 
            # unsafe_allow_html=True)
            st.write('test')
