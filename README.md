# Final-project
پروژه کارشناسی

نحوه اجراي پروژه:

1. پوشه اي كه پروژه در ان قرار دارد را باز ميكنيم و از بخش ادرس cmd را تايپ کرده و اينترر ميزنيم تا ترمينال يا محیط كنسول باز شود

2. بعد از باز شدن كنسول دستور
python manage.py makemigrations
را وارد میکنیم و اينتر را میزنیم

3. سپس دستور 
4python manage.py migrate 
را وارد میکنیم و اینتر را میزنیم.

4. سپس دستور
 python manage.py createsuperuser
را وارد میکنیم و اینتر را میزنیم.

در اینجا ما باید ادمین بسازیم .که اسم و پسورد و ایمیل ادمین را دریافت میکند
و در اخر هم اگر پسورد ساده باشد پیغام های لازم را میدهد و ..

5. سپس دستور اخر را اجرا میکنیم
python manage.py runserver --insecure



بعد از اجرا این دستور یک ادرس به ما میدهد که ان را در مرورگر سرچ میکنیم.

*برای دفعه اول لازم است پس از ان ادرس admin را هم اضافه کنیم
http://127.0.0.1:8000/admin


به صفحه ادمین جنگو میرود که ابتدا باید اسم و رمز بزنیم
سپس لازم است انجا اسم و فامیل ادمین سایت را وارد کنیم:
بر روی جدول College userss کلیک میکنیم 
سپس با کلیک بر روی گزینه ADD COLLEGE USERS یوزر ادمین را ایجاد میکنیم.
*باید دو فیلدis teacher ,is student را غیرفعال کنیم.


سپس با سرچ کردن ادرسی که بما داد و وارد شدن با ایدی و رمز ادمین که وارد کردیم وراد سایت میشویم.
برای دفعه های بعدی تنها لازم است دستور اخر را در مرورگر وارد کنید .



