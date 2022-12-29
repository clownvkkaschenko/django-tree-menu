from django.db import models


class Menu(models.Model):
    menu_name = models.CharField('Меню', max_length=50)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.menu_name


class MenuItem(models.Model):
    item_name = models.CharField('Пункт меню', max_length=50)
    item_url = models.SlugField('URL пункта-меню', max_length=50, unique=True)
    main_menu = models.ForeignKey(
        Menu, verbose_name='Главное меню', on_delete=models.CASCADE
    )
    parent_item = models.ForeignKey(
        to='self', verbose_name='Пункт родительского меню',
        blank=True, null=True, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.item_name
