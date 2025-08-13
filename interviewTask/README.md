
------------------------------------------------------- OPIS -----------------------------------------------------------------

To jest aplikacja webowa typu CRUD (Create, Read, Update, Delete) do zarządzania wiadomościami przez użytkownika za pomocą formularza. Formularz posiada funkcjionalność taką jak dodawanie, edytiwanie oraz usuwanie wiadomości. Kolumna "ID" reprezentuje ID wiadomości w bazie danych (na razie nie zaimplementowane jest numer wiadomości bo chyba tak było by wygodnie dla użytkownika niż po prostu ID), kolumna "Wiadomości" reprezentuje tekst przekazany przez użytkownika do bazy danych, kolumna "Akcje" reprezentuje narzędzia do zarządzania wiadomościami tj. edytuj i usuń. 

Podjąłem się wyzwania stworzenia tej aplikacji, mimo braku wcześniejszego doświadczenia z technologiami Next.js, Node.js, Sequelize, RTK, ShadCN UI oraz pracy z Docker desktop. Korzystałem z dostępnych narzędzi i dokumentacji, aby zrozumieć, jak te technologie działają i jak rozwiązać pojawiające się problemy. Aby przyspieszyć proces i zbudować namacalny projekt, użyłem narzędzi AI do wygenerowania początkowych fragmentów kodu. Następnie zajełem się analizowaniem, modyfikowaniem i dostosowywaniem tego kodu, co pozwoliło mi dogłębnie zrozumieć działanie obu technologii.

Projekt ma obecnie znany problem z migracją i seedingiem bazy danych, który występuje po stronie połączenia z MySQL w kontenerze Docker. Błąd 'Access Denied' sugeruje problem z uprawnieniami użytkownika bazy danych. Pomimo dogłębnej analizy konfiguracji (plików config.cjs, docker-compose.yml, phpmyadmin) i prób ręcznego przypisania uprawnień, problem nie został rozwiązany. Proces ten znacząco pogłębił moją wiedzę na temat konfiguracji środowisk Docker i zarządzania uprawnieniami baz danych, co z pewnością wykorzystam w przyszłych projektach."

Jeśli aplikacja się od razu nie ładuje i widać komunikat - "Wiadomości się ładują, proszę poczekać ..." to należy kliknąć na "Refresh" w przeglądarce.

--------------------------------------------- CO ZOSTAŁÓ ZREALIZOWANE --------------------------------------------------------

----------------------------------------------------- Krótko -----------------------------------------------------------------

I. Architektura i technologie

BACKEND: Node.js z frameworkiem Express.js i Object-Relational Mapper(ORM) Sequelize dla bazy danych MySQL.

FRONTEND: Next.js z RTK Query do zarządzania stanem i komunikacji z API. Komponenty UI oparte na ShadCN UI.

Środowisko deweloperskie: Docker, aby łatwo uruchomić aplikację z MySQL i phpMyAdmin.

II. Zaimplementowane funkcjonalności

BACKEND: Pełny zestaw endpointów API (REST) dla operacji CRUD.

FRONTEND: Interfejs użytkownika z formularzem do dodawania i edytowania wiadomości oraz tabelą do wyświetlania i zarządzania nimi.


----------------------------------------------------- Szczegółowo ------------------------------------------------------------

I. BACKEND

1. backend/app.js zawiera konfiguracje połączenia z bazą danych MySQL za pomocą Sequelize, model, funkcje do ponawiania połączenia z bazą danych na wypadek błędów dostępu, Endpointy API (GET, POST, PUT, DELETE a także LISTEN).
2. backend/models/index.js zawiera model sequelize
3. backend/models/message.js zawiera model "Wiadomosc"
4. backend/config/config.cjs zawiera dane użytkownika i sposób połączenia 
5. backend/config/config.js zawiera dane użytkownika i sposób połączenia 
6. backend/seeder/20250812142721-demo-wiadomosci..cjs stworzony plik seeder poprzez komendę npx sequelize-cli db:seed --seed 20250812142721-demo-wiadomosci.cjs
7. Obrazy backend-api, mysql oraz phpadmin w kontainerze interviewTask w Docker-desktop uruchumiają się poprzez docker-compose up w PS C:\Users\"user_name"\Desktop\interviewTask\backend>

II. FRONTEND

1. frontend/app/MessageClient.js zaimplementowana aplikacja:
    a. zaimportowane hooki, 
    b. komponenty interfejsu ShadCN UI, 
    c. zmenne co do funkcji aplikacji, 
    d. komunikaty co do ładowania aplikacji wraz z potencjalnym błędem jeśli się nie załaduje, 
    e. sama aplikacja (postać tabeli z trzemia kolumnami ID, Wiadomość oraz akcje gdzie są przyciski do zarządzania aplikacją). Wiadomość jest wprowadzana w postaci textarea po kliknęciu na "Dodaj".

2. frontend/app/page.js importowanie aplikacji z MessageClient.js do page.js
3. frontend/app/layout.js poprzez ten plik jest dostarczony komponent Redux do wszystkich potomnych komponentów (powiązany jest z ReduxProvider.js oraz store.js co tworzy współną komunikację dla Redux Toolkit Query)
4. frontend/app/ReduxProvider.js konfiguracja API i RTK Query
5. frontend/app/store.js główny plik z konfiguracją API oraz RTK Query oraz ekport hooków RTK Query
6. frontend/app/globals.css style co do interfejsu ShadCN UI
7. frontend/components/ui komponenty co do interfejsu ShadCN UI (button, input, textarea, table, dialog, card).
8. frontend się uruchumia w PS C:\Users\"User_name"\Desktop\interviewTask\frontend> za pomocą komendy npm run dev (używałem Visual Studio Code gdzie uruchumiałem frontend)
