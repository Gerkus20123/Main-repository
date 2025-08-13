# 🧩 Zadanie Rekrutacyjne – Aplikacja Wiadomości

## 🎯 Cel

Rozbudowa istniejącego projektu poprzez implementację formularza do dodawania wiadomości do bazy danych. Dodatkowo, wiadomości powinny być wyświetlane w tabeli z następującymi kolumnami: **ID**, **Wiadomość**, **Akcje**.

---

## ✅ Wymagania techniczne

- **Node.js v18.17.0+**
- **Docker v20.10.11+**
- **Sequelize + migracje (`sequelize-cli`)**
- **RTK Query (Redux Toolkit Query)**
- **ShadCN UI (komponenty UI)**

---

## 🧠 Zakres zadania

### 📝 Formularz dodawania wiadomości

- Formularz umożliwia wprowadzenie treści wiadomości i dodanie jej do bazy danych.
- Formularz musi posiadać walidację danych.

### 📄 Tabela wiadomości

- Tabela z kolumnami: **ID**, **Wiadomość**, **Akcje**.
- Kolumna **Akcje** zawiera:
  - 🔧 **Edytuj** – otwiera popup z formularzem do edycji wiadomości.
  - ❌ **Usuń** – usuwa wiadomość po potwierdzeniu.

### 🖥️ Backend

- Własna implementacja obsługi zapytań do bazy danych (dodawanie, edytowanie, usuwanie).
- **Zamień `sequelize.sync()` na migracje (`sequelize-cli`)**:
  - Model wiadomości musi być utworzony przez migrację.
  - W kodzie nie może być używany `sequelize.sync()`.
- **Dodaj seeder**:
  - Seeder dodający przynajmniej 3 przykładowe wiadomości.
  - Możliwość uruchomienia przez:
    ```bash
    npx sequelize-cli db:seed:all
    ```

### 🔌 RTK Query

- Komunikacja frontend ↔ backend musi być oparta w całości o RTK Query.

### 🎨 ShadCN UI

- UI musi korzystać z komponentów biblioteki **ShadCN**.
- Interfejs powinien być estetyczny, intuicyjny i spójny.

---

## 🚀 Uruchomienie projektu

1. Sklonuj repozytorium.
2. W katalogu głównym uruchom:

```bash
docker compose up
```

> Po uruchomieniu kontenery powinny:
>
> - automatycznie wykonać migracje,
> - umożliwić pracę z aplikacją bez ręcznej konfiguracji.

---

## 📦 Dystrybucja

1. Stwórz osobny branch `dev`.
2. Po zakończeniu zadania utwórz pull request `dev → main`.
3. Dodaj użytkownika `@BiznesportTech` jako **reviewera**.
4. Upewnij się, że `@BiznesportTech` ma dostęp do repozytorium:
   - `Settings → Collaborators → Invite a collaborator`.

---

## 🧪 Weryfikacja

Zadanie będzie oceniane na podstawie:

- Poprawności działania po `docker compose up`.
- Braku `sequelize.sync()` – tylko migracje.
- Poprawnie zaimplementowanych seederów.
- Czytelności i jakości kodu (frontend + backend).
- Poprawnej integracji RTK Query i ShadCN UI.
- Intuicyjności i estetyki interfejsu użytkownika.

---

## ✅ Checklista przed wysłaniem

- [ ] Formularz dodaje wiadomości do bazy.
- [ ] Edycja i usuwanie działają zgodnie z wymaganiami.
- [ ] Brak `sequelize.sync()` – użyte migracje.
- [ ] Seeder dodaje min. 3 wiadomości.
- [ ] Frontend korzysta z RTK Query.
- [ ] UI zbudowane z komponentów ShadCN.
- [ ] Projekt uruchamia się poprawnie przez `docker compose up`.
- [ ] Pull request z `dev` do `main` gotowy.
- [ ] `@BiznesportTech` dodany jako współpracownik i reviewer.

---

💡 Powodzenia! W razie pytań skontaktuj się z zespołem BiznesportTech.
