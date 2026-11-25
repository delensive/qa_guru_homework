import datetime


# 1. Нормализация email адресов
def normalize_addresses(value: str) -> str:
    return value.strip().lower()


# 2. Сокращённая версия тела письма
def add_short_body(email: dict) -> dict:
    email["short_body"] = email["body"][:10] + "..."
    return email


# 3. Очистка текста письма
def clean_body_text(body: str) -> str:
    return body.replace("\t", " ").replace("\n", " ")


# 4. Формирование итогового текста письма
def build_sent_text(email: dict) -> str:
    if "short_body" in email:
        body = email["short_body"]
    else:
        body = email["body"]

    email["clean_body"] = clean_body_text(body)
    return (
        f"Кому: {email['recipient']}, от {email['sender']}\n"
        f"Тема: {email['subject']}, дата {email['date']}\n"
        f"{email['clean_body']}"
    )


# 5. Проверка пустоты темы и тела
def check_empty_fields(subject: str, body: str) -> tuple[bool, bool]:
    is_subject_empty = not subject.strip()
    is_body_empty = not body.strip()
    return is_subject_empty, is_body_empty


# 6. Маска email отправителя
def mask_sender_email(login: str, domain: str) -> str:
    return login[:2] + "***@" + domain


# 7. Проверка корректности email
def get_correct_email(email_list: list[str]) -> list[str]:
    correct_emails = []

    for email in email_list:
        email = email.strip()
        if "@" in email and email.lower().endswith((".com", ".ru", ".net")):
            login, domain = email.rsplit("@", 1)
            if login and domain and not domain.startswith("."):
                correct_emails.append(email)

    return correct_emails


# 8. Создание словаря письма
def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    email = {
        "recipient": recipient,
        "sender": sender,
        "subject": subject,
        "body": body,
    }
    return email


# 9. Добавление даты отправки
def add_send_date(email: dict) -> dict:
    x = datetime.datetime.now()
    send_date = x.strftime("%Y-%m-%d")
    email["date"] = send_date
    return email


# 10. Получение логина и домена
def extract_login_domain(address: str) -> tuple[str, str]:
    login = address.split("@")[0]
    domain = address.split("@")[1]
    return login, domain


# 11. Отправка письма
def sender_email(
    recipient_list: list[str],
    subject: str,
    message: str,
    *,
    sender: str = "default@study.com",
) -> list[dict]:
    # Проверка списка получателей
    if not recipient_list:
        return []

    # Проверка email отправителя и получателей
    correct_sender = get_correct_email([sender])
    correct_recipients = get_correct_email(recipient_list)
    if not correct_sender or not correct_recipients:
        return []

    # Проверка темы и тела письма
    is_subject_empty, is_body_empty = check_empty_fields(subject, message)
    if is_subject_empty or is_body_empty:
        return []

    # Нормализация данных
    sender = normalize_addresses(sender)
    subject = clean_body_text(subject)
    message = clean_body_text(message)
    recipient_list = [
        normalize_addresses(recipient) for recipient in correct_recipients
    ]

    emails = []
    for recipient in recipient_list:
        # Исключение отправки самому себе
        if recipient == sender:
            continue

        # Создание письма и добавление даты
        email = create_email(sender, recipient, subject, message)
        email = add_send_date(email)

        # Маска отправителя и короткая версия тела
        login, domain = extract_login_domain(sender)
        email["masked_sender"] = mask_sender_email(login, domain)
        email = add_short_body(email)

        # Итоговый текст письма
        email["sent_text"] = build_sent_text(email)
        emails.append(email)

    return emails


# 12. Вывод готового списка писем
print(sender_email(["admin@company.ru"], "Hello!", "Привет, коллега!"))
