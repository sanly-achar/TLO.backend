from django.db import models




# Фотография для слайдера

class Slider(models.Model):

    image = models.ImageField(upload_to='slider', blank=True, null=True, verbose_name='Слайдер')
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name="Слоган")


    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

    def __str__(self):
        return self.title

# Категория


class Category(models.Model):

    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Имя")
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to='category', blank=True, null=True, verbose_name='Категория')


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name





# Новости

class News(models.Model):

    image = models.ImageField(upload_to='news', blank=True, null=True, verbose_name='Изображение')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Слоган")
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



    def __str__(self):
        return self.title



# Обратная связь

class ContactUs(models.Model):
    
    email = models.EmailField(max_length=50, verbose_name="Email")
    name = models.CharField(max_length=100, verbose_name="Name")
    phone = models.CharField(max_length=50, verbose_name="Phone")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at",)


    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'




# Продукт

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    sale = models.BooleanField(default=False, verbose_name='Скидка')
    new =  models.BooleanField(default=False, verbose_name='Новый')


    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя")
    title = models.CharField( max_length=255, blank=True, null=True, verbose_name="Слоган")
    link = models.FileField(upload_to="price_list", max_length=254, blank=True, null=True, verbose_name='Файл для скачки')
    main_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Главная изображение')
    second_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Второе изображение')
    three_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Третее изображение')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'



    def __str__(self):
        return self.name


# Заказы от продукта
class ProductContactUs(models.Model):

    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Продукт', blank=True, null=True)
    email = models.EmailField(max_length=50, verbose_name="Email")
    name = models.CharField(max_length=100, verbose_name="Name")
    phone = models.CharField(max_length=50, verbose_name="Phone")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at",)


    class Meta:
        verbose_name = 'Заказы от продукта'
        verbose_name_plural = 'Заказы от продукта'


# Главная страница

class MainPageImage(models.Model):

    image_1 = models.ImageField(upload_to='image', blank=True, null=True, verbose_name='Изображение главной страницы ')
    image_2 = models.ImageField(upload_to='image', blank=True, null=True, verbose_name='Изображение главной страницы ')
    image_3 = models.ImageField(upload_to='image', blank=True, null=True, verbose_name='Изображение главной страницы ')
    image_4 = models.ImageField(upload_to='image', blank=True, null=True, verbose_name='Изображение главной страницы ')
    image_5 = models.ImageField(upload_to='image', blank=True, null=True, verbose_name='Изображение главной страницы ')



    class Meta:
        verbose_name = 'Изображение главной страницы '
        verbose_name_plural = 'Изображение главной страницы '



# Дополнительная информация

class Info(models.Model):

    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Слоган")
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to='news', blank=True, null=True, verbose_name='Изображение')


    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительная информация'



    def __str__(self):
        return self.title




# Контакты 

class Contacts(models.Model):

    logo = models.ImageField(upload_to='news', blank=True, null=True, verbose_name='LOGO')

    map = models.TextField( blank=True, null=True, verbose_name="Расположение на карте")
    link = models.FileField(upload_to='path')
    phone = models.CharField( blank=True, null=True, max_length=50, verbose_name='Мобильный')
    email = models.EmailField( blank=True, null=True, verbose_name='Почта')
    email_2 = models.EmailField( blank=True, null=True, verbose_name='Почта')
    address = models.CharField( blank=True, null=True, max_length=255, verbose_name='Адрес')
    bank_name = models.CharField( blank=True, null=True, max_length=255, verbose_name='Банковские реквизиты')
    bank_recw_usd = models.CharField( blank=True, null=True, max_length=255, verbose_name='Расчетный счет USD')
    bank_recw_eur = models.CharField( blank=True, null=True, max_length=255, verbose_name='Расчетный счет EUR ')
    
 

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


# Информация о нас

class About(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Имя")
    image = models.ImageField(upload_to='about', blank=True, null=True, verbose_name='Изображение')
    mini_title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Мини-слоган")
    title = models.TextField(max_length=255, blank=True, null=True, verbose_name="Слоган")
    desc = models.TextField(blank=True, null=True, verbose_name="Описание")
    facebook = models.CharField(max_length=255, blank=True, null=True, verbose_name="Файсбоок")
    instagram = models.CharField(max_length=255, blank=True, null=True, verbose_name="Инстаграм")
    whatsapp =  models.CharField(max_length=255, blank=True, null=True, verbose_name="Востапп")
    gmail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Гоогл почта")
    mail = models.CharField(max_length=255, blank=True, null=True, verbose_name="Меил почта")
    yandex =  models.CharField(max_length=255, blank=True, null=True, verbose_name="Яндекс почта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    