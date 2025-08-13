import { Inter } from "next/font/google";
import { Providers } from "./ReduxProvider";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Panel Wiadomości",
  description: "Aplikacja do zarządzania wiadomościami",
};


// Owijanie całej aplikacji, dostarczając kontekst Redux dla wszystkich komponentów potomnych - children.

export default function RootLayout({ children }) {
  return (
    <html lang="pl">
      <body className={`${inter.className} bg-gray-100 min-h-screen font-sans antialiased`}>
        <Providers>
          {children}
        </Providers>
      </body>
    </html>
  );
}
