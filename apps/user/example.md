import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_user, smtp_password):
    # Создаем объект сообщения
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Добавляем тело сообщения
    msg.attach(MIMEText(message, 'plain'))

    # Устанавливаем соединение с SMTP сервером
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Включаем защищенное соединение
    server.login(smtp_user, smtp_password)  # Логинимся на сервер
    text = msg.as_string()  # Конвертируем сообщение в строку
    server.sendmail(from_email, to_email, text)  # Отправляем письмо
    server.quit()  # Закрываем соединение

# Параметры для отправки письма
```python
from_email = 'your_email@example.com'
to_email = 'recipient_email@example.com'
subject = 'Ежедневный отчет'
message = 'Здесь ваш ежедневный отчет...'
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_user = 'your_email@example.com'
smtp_password = 'your_password'

# Отправляем письмо
send_email(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_user, smtp_password)
```
