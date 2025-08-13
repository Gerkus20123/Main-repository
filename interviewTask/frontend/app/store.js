// frontend/src/lib/store.js
import { configureStore } from '@reduxjs/toolkit';
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

// Konfiguracja API z RTK Query
const messagesApi = createApi({
  reducerPath: 'messagesApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:8082/api/wiadomosci' }),
  tagTypes: ['Message'],
  endpoints: (builder) => ({
    getWiadomosci: builder.query({
      query: () => '',
      providesTags: ['Message'],
    }),
    addWiadomosc: builder.mutation({
      query: ({ content }) => ({
        url: '',
        method: 'POST',
        body: { content },
      }),
      invalidatesTags: ['Message'],
    }),
    updateWiadomosc: builder.mutation({
      query: ({ id, content }) => ({
        url: `/${id}`,
        method: 'PUT',
        body: { content },
      }),
      invalidatesTags: ['Message'],
    }),
    deleteWiadomosc: builder.mutation({
      query: (id) => ({
        url: `/${id}`,
        method: 'DELETE',
      }),
      invalidatesTags: ['Message'],
    }),
  }),
});

// Eksportujemy hooki wygenerowane przez RTK Query
export const {
  useGetWiadomosciQuery,
  useAddWiadomoscMutation,
  useUpdateWiadomoscMutation,
  useDeleteWiadomoscMutation,
} = messagesApi;

// Konfiguracja i eksport Redux
export const store = configureStore({
  reducer: {
    [messagesApi.reducerPath]: messagesApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(messagesApi.middleware),
});