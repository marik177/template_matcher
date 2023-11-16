import datetime

from app import db

template_names = ["MyForm", "OrderForm"]
template_fields = ["email", "phone", "date", "text"]

emails = [f"user_{i}@ya.ru" for i in range(1, 6)]
phones = [f"+7 00{i} 111 222 33" for i in range(1, 6)]
dates = [
    (datetime.datetime.today() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
    for i in range(5)
]
textes = ["Some text " + i * "TEST " for i in range(5)]


def make_fields(name):
    name = name[: name.find("Form")].lower()
    return [f"{name}_{field}" for field in template_fields]


def save_form(form):
    fields = make_fields(form)
    for user in zip(emails, phones, dates, textes):
        d = {"name": form}
        d.update((zip(fields, user)))
        db.insert(d)


def main():
    for form in template_names:
        save_form(form)


if __name__ == "__main__":
    main()
