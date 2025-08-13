
import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import { Sequelize } from 'sequelize';
import Wiadomosc from './models/message.js';

const app = express();
const port = 8080;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Konfiguracja połączenia z bazą danych MySQL za pomocą Sequelize
const sequelize = new Sequelize('interviewTask', 'German', 'interview123', {
  host: 'db',
  dialect: 'mysql',
  logging: false,
});

// Zdefiniowanie modelu
const MessageModel = Wiadomosc(sequelize);

// Funkcja do opóźniania operacji
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// Funkcja do ponawiania połączenia z bazą danych
const connectWithRetry = async (retries = 5, delayMs = 5000) => {
  try {
    await sequelize.authenticate();
    console.log('Połączenie z bazą danych zostało ustanowione pomyślnie.');
    console.log('Serwer gotowy.');
    return true;
  } catch (err) {
    if (retries > 0) {
      console.error(`Błąd połączenia z bazą danych. Pozostało ${retries} prób. Ponawiam za ${delayMs / 1000}s...`);
      await delay(delayMs);
      return connectWithRetry(retries - 1, delayMs);
    } else {
      console.error('Nie udało się połączyć z bazą danych po wielokrotnych próbach. Sprawdź konfigurację.', err);
      return false;
    }
  }
};

// Uruchamianie serwera po udanej próbie połączenia z bazą danych
(async () => {
  const isConnected = await connectWithRetry();
  if (isConnected) {

    // Endpointy API

    // 1. GET
    app.get('/api/wiadomosci', async (req, res) => {
      try {
        const wiadomosci = await MessageModel.findAll();
        res.json(wiadomosci);
      } catch (err) {
        console.error(err);
        res.status(500).json({ success: false, message: 'Nie udało się otrzymać wiadomości.' });
      }
    });

    // 2. POST
    app.post('/api/wiadomosci', async (req, res) => {
      try {
        const { content } = req.body;
        const nowaWiadomosc = await MessageModel.create({ content });
        res.json(nowaWiadomosc);
      } catch (err) {
        console.error(err);
        res.status(500).json({ success: false, message: 'Nie udało się dodać wiadomości.' });
      }
    });

    // 3. PUT
    app.put('/api/wiadomosci/:id', async (req, res) => {
      try {
        const { id } = req.params;
        const { content } = req.body;
        const wiadomosc = await MessageModel.findByPk(id);
        if (wiadomosc) {
          wiadomosc.content = content;
          await wiadomosc.save();
          res.json(wiadomosc);
        } else {
          res.status(404).json({ success: false, message: 'Wiadomość nie znaleziona.' });
        }
      } catch (err) {
        console.error(err);
        res.status(500).json({ success: false, message: 'Nie udało się zaktualizować wiadomości.' });
      }
    });

    // 4. DELETE
    app.delete('/api/wiadomosci/:id', async (req, res) => {
      try {
        const { id } = req.params;
        const wiadomosc = await MessageModel.findByPk(id);
        if (wiadomosc) {
          await wiadomosc.destroy();
          res.json({ success: true, message: 'Wiadomość usunięta.' });
        } else {
          res.status(404).json({ success: false, message: 'Wiadomość nie znaleziona.' });
        }
      } catch (err) {
        console.error(err);
        res.status(500).json({ success: false, message: 'Nie udało się usunąć wiadomości.' });
      }
    });

    // 5. LISTEN
    app.listen(port, () => {
      console.log(`Serwer backendowy działa na http://localhost:${port}`);
    });
  } else {
    console.error('Nie udało się połączyć z bazą danych. Serwer nie został uruchomiony.');
    process.exit(1);
  }
})();