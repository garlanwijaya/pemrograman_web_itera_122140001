/* eslint-disable react-refresh/only-export-components */
// src/context/BookContext.jsx
import { createContext, useState } from "react";
import PropTypes from "prop-types";
import useLocalStorage from "../hooks/useLocalStorage,js"; // Import hook

export const BookContext = createContext();

export const BookProvider = ({ children }) => {
  // Gunakan hook useLocalStorage di sini
  const [books, setBooks] = useLocalStorage("books", []);
  const [filterStatus, setFilterStatus] = useState("all");
  const [searchTerm, setSearchTerm] = useState("");

  const addBook = (book) => {
    setBooks((prevBooks) => [...prevBooks, { id: Date.now(), ...book }]);
  };

  const deleteBook = (id) => {
    setBooks((prevBooks) => prevBooks.filter((book) => book.id !== id));
  };

  const updateBook = (updatedBook) => {
    setBooks((prevBooks) =>
      prevBooks.map((book) => (book.id === updatedBook.id ? updatedBook : book))
    );
  };

  return (
    <BookContext.Provider
      value={{
        books,
        filterStatus,
        searchTerm,
        setFilterStatus,
        setSearchTerm,
        addBook,
        deleteBook,
        updateBook,
      }}
    >
      {children}
    </BookContext.Provider>
  );
};

BookProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

export default BookContext;
