'use client';

// importowanie Provider z react-redux oraz store z ./store (konfiguracja API i RTK Query)

import { Provider } from 'react-redux';
import { store } from './store';

export function Providers({ children }) {
  return (
    <Provider store={store}>
      {children}
    </Provider>
  );
}
