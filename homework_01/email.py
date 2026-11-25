import datetime

# 1. Создайте словарь email:
email = {
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "  lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon.\nRegards,\nTeam",
}

# 2. Добавьте дату отправки:
x = datetime.datetime.now()
send_date = x.strftime("%Y-%m-%d")
email["date"] = send_date

# 3. Нормализуйте e-mail адреса:
email["from"] = email["from"].strip().casefold()
email["to"] = email["to"].strip().lower()

# 4. Извлеките логин и домен отправителя:
login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]

# 5. Создайте сокращённую версию текста:
email["short_body"] = email["body"][:10] + "..."

# 6. Списки доменов:
personal_domains = list(
    {
        "gmail.com",
        "list.ru",
        "yahoo.com",
        "outlook.com",
        "hotmail.com",
        "icloud.com",
        "yandex.ru",
        "mail.ru",
        "list.ru",
        "bk.ru",
        "inbox.ru",
    }
)
corporate_domains = list(
    {
        "company.ru",
        "corporation.com",
        "university.edu",
        "organization.org",
        "company.ru",
        "business.net",
    }
)

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений:
checking_intersections = not set(personal_domains) & set(corporate_domains)

# 8. Проверьте «корпоративность» отправителя:
is_corporate = domain in corporate_domains

# 9. Соберите «чистый» текст сообщения:
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")

# 10. Сформируйте текст отправленного письма
email["sent_text"] = (
    f"Кому: {email['to']}, от {email['from']} "
    f"Тема: {email['subject']}, дата {email['date']} "
    f"{email['clean_body']}"
)

# 11. Рассчитайте количество страниц печати
pages = (len(email["sent_text"]) + 499) // 500

# 12. Проверьте пустоту темы и тела письма:
is_subject_empty = not email["subject"]
is_body_empty = not email["body"]

# 13. Создайте «маску» e-mail отправителя:
email["masked_from"] = login[:2] + "***@" + domain

# 14. Удалите из списка личных доменов:
personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")

# Результаты:
print("email:", email)
print(
    "login:",
    login,
)
print("domain:", domain)
print("checking_intersections:", checking_intersections)
print("is_corporate:", is_corporate)
print("pages:", pages)
print("is_subject_empty:", is_subject_empty)
print("is_body_empty:", is_body_empty)
print("personal_domains:", personal_domains)
