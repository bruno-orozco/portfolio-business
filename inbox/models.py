from django.db import models
from django.forms import ValidationError


class message(models.Model):
    """ Model for the contact form """

    def validate_name(value):
        """ Validator so that you write your full name correctly """

        an_integer = value
        a_string = str(an_integer)
        length = len(a_string)

        if length < 3:
            raise ValidationError(('The name is very short. Enter your full name, please.'))

    contact_full_name = models.CharField(max_length=255, validators=[validate_name])

    def validate_length(value):
        """ Validator so that you write your full phonenumbre correctly """

        an_integer = value
        a_string = str(an_integer)
        length = len(a_string)

        if length > 10:
            raise ValidationError(('This phone number is greater than ten numbers. Enter only 10 numbers.'))
        elif length < 10:
            raise ValidationError(('This phone number is less than 10 numbers. Enter only 10 numbers.'))

    phone_number = models.PositiveBigIntegerField(validators=[validate_length])

    email = models.EmailField(blank=True, null=True)

    def validate_message(value):
        """ Validator so that you write your full phonenumbre correctly """

        an_integer = value
        a_string = str(an_integer)
        length = len(a_string)

        if length < 5:
            raise ValidationError(('The message is very short. Give a little more detail about the reason for your message.'))

    message = models.TextField(validators=[validate_message])

    date = models.DateField(auto_now=True)

    def __str__(self):
        """ return full name """

        return self.contact_full_name

    class Meta:
        """ Return names to model message """

        db_table = 'message'
        managed = True
        verbose_name = 'message'
        verbose_name_plural = 'messages'