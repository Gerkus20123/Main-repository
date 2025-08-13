// Główna aplikacja zarządzania wiadomościami

'use client';

// Importy hooków
import { useState } from 'react';
import {
  useGetWiadomosciQuery,
  useAddWiadomoscMutation,
  useUpdateWiadomoscMutation,
  useDeleteWiadomoscMutation,
} from './store';

// Importy komponentów interfejsa ShadCN UI
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
} from '@/components/ui/dialog';
import { Textarea } from '@/components/ui/textarea';
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';

// Zmenne co do funkcji aplikacji
export default function MessageClient() {
  const [newContent, setNewContent] = useState('');
  const [editingMessage, setEditingMessage] = useState(null);
  const [editedContent, setEditedContent] = useState('');

  const { data: messages, isLoading, isError } = useGetWiadomosciQuery();
  const [addWiadomosc] = useAddWiadomoscMutation();
  const [updateWiadomosc] = useUpdateWiadomoscMutation();
  const [deleteWiadomosc] = useDeleteWiadomoscMutation();

  const handleAddMessage = async (e) => {
    e.preventDefault();
    if (newContent) {
      await addWiadomosc({ content: newContent });
      setNewContent('');
    }
  };

  const handleDeleteMessage = async (id) => {
    await deleteWiadomosc(id);
  };

  const handleEditClick = (message) => {
    setEditingMessage(message);
    setEditedContent(message.content);
  };

  const handleSaveEdit = async () => {
    if (editingMessage && editedContent) {
      await updateWiadomosc({ id: editingMessage.id, content: editedContent });
      setEditingMessage(null);
      setEditedContent('');
    }
  };

  const handleCloseModal = () => {
    setEditingMessage(null);
    setEditedContent('');
  };


  // Komunikaty co do ładowania aplikacji oraz co do błedu

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen text-center text-lg text-gray-800">
        Wiadomości się ładują, proszę poczekać ...
      </div>
    );
  }


  if (isError) {
    return (
      <div className="flex items-center justify-center min-h-screen text-center text-red-500 text-lg">
        Wystąpił błąd podczas ładowania wiadomości.
      </div>
    );
  }

  // Aplikacja

  return (
    <div className="max-w-4xl mx-auto p-8">
      <Card>
        <CardHeader>
          <CardTitle className="text-4xl text-center">Panel Wiadomości</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleAddMessage} className="flex flex-col md:flex-row gap-4 mb-10">
            <Input
              type="text"
              value={newContent}
              onChange={(e) => setNewContent(e.target.value)}
              placeholder=" Proszę wpisać nową wiadomość..."
              className="flex-grow"
            />
            <Button type="submit">DODAJ</Button>
          </form>

          <div className="overflow-x-auto">
            <Table>

              <TableHeader>
                <TableRow>
                  <TableHead className="w-[100px] text-center text-red-500">ID</TableHead>
                  <TableHead className="text-center text-red-500" >Wiadomość</TableHead>
                  <TableHead className="text-center text-red-500">Akcje</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                {messages?.map((message) => (
                  <TableRow key={message.id}>
                    <TableCell className="font-medium text-center">{message.id}</TableCell>
                    <TableCell>{message.content}</TableCell>
                    <TableCell className="text-center">
                      <div className="flex items-center gap-4">
                        <Button variant="outline" onClick={() => handleEditClick(message)}>
                          EDYTUJ
                        </Button>
                        <Button variant="destructive" onClick={() => handleDeleteMessage(message.id)}>
                          USUŃ
                        </Button>
                      </div>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>

            </Table>
          </div>
        </CardContent>
      </Card>

      <Dialog open={!!editingMessage} onOpenChange={handleCloseModal}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle className="text-center">Edytuj Wiadomość</DialogTitle>
          </DialogHeader>
          <Textarea
            className="text-gray-500"
            value={editedContent}
            onChange={(e) => setEditedContent(e.target.value)}
            placeholder="Wpisz swoją wiadomość..."
            rows="5"
          />
          <DialogFooter className="sm:justify-end">

            <Button onClick={handleSaveEdit}>
              ZAPISZ
            </Button>

            <Button onClick={handleCloseModal} variant="outline">
              ANULUJ
            </Button>

          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  );
}
