from django.core import validators
from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import Account






class FinancialOrganization(models.Model):
    organization = models.CharField(
        verbose_name='Название организации',
        max_length=200,
        null=False,
        blank=False,
    )
    chairman_directors = models.TextField(
        verbose_name='Председатель Совета директоров',
        max_length=200,
        null=False,
        blank=False,
    )
    chairman_board = models.TextField(
        verbose_name='Председатель Правления',
        max_length=200,
        null=False,
        blank=False,
    )
    board_directors = models.TextField(
        verbose_name='Совет директоров',
        max_length=1000,
        null=False,
        blank=False,
    )
    board_members = models.CharField(
        verbose_name='Члены правления',
        max_length=1000,
        null=False,
        blank=False,
    )
    cheif_accountant = models.CharField(
        verbose_name='Главный бухгалтер',
        max_length=200,
        null=False,
        blank=False,
    )
    bin = models.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                r'^[0-9]*$',
                'Only 0-9 are allowed.',
                'Invalid Number'
            ),
        ],
    )
    address = models.CharField(
        verbose_name='Адрес (город, улица, дом, квартира)',
        max_length=200,
        null=False,
        blank=False,
    )
    phone = PhoneNumberField(
        verbose_name='Телефон',
        null=False,
        blank=False
    )
    fax = PhoneNumberField(
        verbose_name='Факс',
        max_length=200,
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name='E-mail',
        validators=[validators.EmailValidator(message="Invalid Email")],
        blank=True
    )
    web_site = models.CharField(
        verbose_name='Web-сайт',
        max_length=200,
        null=False,
        blank=False
    )
    level_of_organization=models.CharField(
        verbose_name='Уровень организации',
        max_length=200,
        null=False,
        blank=False
    )
    custodian = models.TextField(
        verbose_name='Кастодиан',
        max_length=500,
        null=False,
        blank=False
    )
    broker_dealers = models.TextField(
        verbose_name='Брокеры-дилеры',
        max_length=1000,
        null=False,
        blank=False
    )
    org_logo = models.ImageField(
        null=False,
        blank=True,
        verbose_name='Фото организации',
    )
    responsible = models.ForeignKey(Account,
                               verbose_name=('Куратор'),
                               on_delete=models.CASCADE,
                               related_name='financial_organizations',
                               null=True, blank=True
                               )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )


    def __str__(self):
        return f'{self.organization}'





