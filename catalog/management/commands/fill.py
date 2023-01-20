from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Products = [
            {'name_product': 'apple', 'title': 'Я́блоко — сочный плод яблони, который употребляется в пищу в свежем и запеченном виде, служит сырьём в кулинарии и для приготовления напитков. Наибольшее распространение получила яблоня домашняя, реже выращивают яблоню сливолистную. Размер красных, зелёных или жёлтых шаровидных плодов 5—13 см в диаметре. Происходит из Центральной Азии, где до сих пор произрастает дикорастущий предок яблони домашней — яблоня Сиверса[1]. На сегодняшний день существует множество сортов этого вида яблони, произрастающих в различных климатических условиях. По времени созревания отличают летние, осенние и зимние сорта, более поздние сорта отличаются хорошей стойкостью.', 'category_id' : 1 ,'image': 'apple.jpg','price': '3',
             'date_create': '2021-12-31 15:25:00+01',
             'date_update': '2021-12-31 15:25:00+01'},
            {'name_product': 'bananas', 'title': 'Бана́н — название съедобных плодов культивируемых растений рода Банан (Musa); обычно под таковыми понимают Musa acuminata и Musa × paradisiaca, а также Musa balbisiana, Musa fehi[en], Musa troglodytarum[en] и ряд других. Также бананами могут называть плоды Ensete ventricosum[en] (строго говоря, являющегося представителем другого рода семейства Банановые)[1][2]. С ботанической точки зрения банан является ягодой[3], многосеменной и толстокожей. У культурных форм часто отсутствуют семена, ненужные при вегетативном размножении. Плоды имеют длину 6—30 см и диаметр 2—5 см. Соплодия могут состоять из 300 плодов и иметь массу до 50—60 кг[4].Бананы — одна из древнейших пищевых культур, а для тропических стран важнейшее пищевое растение и главная статья экспорта. Спелые бананы широко употребляются в пищу по всему миру, их используют при приготовлении большого количества блюд. Помимо употребления в свежем виде, в кухне некоторых народов бананы могут зажариваться или вариться как в очищенном, так и в неочищенном виде[1][5]. Их также сушат, консервируют, используют для приготовления банановой муки, мармелада, сиропов, вин. Бананы применяются также в качестве корма для скота. Запах бананов определяют изовалерианово-изоамиловый и уксусно-изоамиловый эфиры[5]. Выращиваются в тропических и субтропических районах с жарким влажным климатом. Существует большое число сортов съедобных видов банана[1].Размер, цвет и форма могут значительно различаться в зависимости от вида или сорта, но чаще всего они имеют продолговатую цилиндрическую или трёхгранную форму, выпрямленную либо закруглённую. Длина плода варьирует в пределах от 3 до 40 см, толщина — от 2 до 8 см. Цвет кожицы может быть жёлтым, зелёным, красным или даже серебристым. Мякоть белая, кремовая, жёлтая или оранжевая. В незрелом состоянии она твёрдая и клейкая, но по мере созревания становится мягкой и сочной[6].Во многих странах бананы являются одним из основных источников питания — например, только в Эквадоре годовое потребление этого продукта составляет 73,8 кг на одного человека (для сравнения, в России этот показатель равен 7,29 кг). Существенную долю потребления бананы также составляют в Бурунди (189,4 кг), Самоа (85,0 кг), Коморских Островах (77,8 кг) и на Филиппинах (40,6 кг)[7].', 'image': 'bananas.jpg', 'category_id': 1, 'price': '5',
             'date_create': '2021-12-31 15:25:00+01',
             'date_update': '2021-12-31 15:25:00+01'},
        ]
        Categories = [
            {'category_name': 'fruits', 'title': 'useful, very tasty'},
            {'category_name': 'vegetables', 'title': 'useful but not tasty'},
            {'category_name': 'milk', 'title': 'white, fat'},
        ]

        products_list = []
        categories_list = []

        for item in Categories:
            categories_list.append(Category(**item))

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_list)

        for item in Products:
            products_list.append(Product(**item))
        Product.objects.all().delete()
        Product.objects.bulk_create(products_list)

